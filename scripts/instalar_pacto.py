"""Instala o kit PACTO em um projeto sem sobrescrever adaptações locais."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
VERSAO = "2026.10.22.3"
DOCUMENTOS = {
    "AGENTS.md": "templates/AGENTS.template.md",
    "CLAUDE.md": "templates/CLAUDE.template.md",
    "BRIEF.md": "templates/BRIEF.template.md",
    "SPEC.md": "templates/SPEC.template.md",
    "PLAN.md": "templates/PLAN.template.md",
    "INVARIANTES.md": "templates/INVARIANTES.template.md",
    ".pacto/validacao.md": "docs/validacao-proporcional.md",
}
CONTINUIDADE = {
    ".pacto/pacto-estado.py": "scripts/pacto_estado.py",
    ".pacto/estado.json": "templates/ESTADO.template.json",
}


def sha(caminho: Path) -> str:
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def dentro(raiz: Path, caminho: Path) -> bool:
    try:
        caminho.resolve(strict=False).relative_to(raiz.resolve())
        return True
    except ValueError:
        return False


def manifesto(destino: Path) -> Path:
    return destino / ".pacto" / "instalacao.json"


def ler_manifesto(destino: Path) -> dict | None:
    arquivo = manifesto(destino)
    if not arquivo.exists(): return None
    try: return json.loads(arquivo.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError): raise ValueError("manifesto de instalação inválido")


def fontes(perfil: str) -> dict[str, Path]:
    itens = dict(DOCUMENTOS)
    if perfil == "continuidade": itens.update(CONTINUIDADE)
    return {destino: RAIZ / origem for destino, origem in itens.items()}


def planejar(destino: Path, perfil: str, modo: str) -> tuple[list[tuple[str, Path, Path | None]], list[str]]:
    destino = destino.resolve()
    if not destino.is_dir(): raise ValueError(f"destino inválido: {destino}")
    atual = ler_manifesto(destino) or {"arquivos": {}}
    geridos = atual.get("arquivos", {})
    acoes, conflitos = [], []
    for rel, origem in fontes(perfil).items():
        alvo = destino / rel
        if not dentro(destino, alvo): conflitos.append(f"recusa: {rel} aponta para fora do projeto"); continue
        novo_hash = sha(origem)
        if not alvo.exists(): acoes.append(("criar", alvo, origem)); continue
        atual_hash = sha(alvo)
        if atual_hash == novo_hash: acoes.append(("manter", alvo, origem)); continue
        if rel not in geridos: conflitos.append(f"preservar não gerido: {rel}"); continue
        if geridos[rel].get("hash") != atual_hash: conflitos.append(f"conflito local: {rel}"); continue
        if modo == "instalar": acoes.append(("manter", alvo, origem))
        else: acoes.append(("atualizar", alvo, origem))
    return acoes, conflitos


def aplicar(destino: Path, perfil: str, modo: str):
    acoes, conflitos = planejar(destino, perfil, modo)
    if conflitos: raise ValueError("; ".join(conflitos))
    escritos = []
    try:
        for acao, alvo, origem in acoes:
            if acao not in {"criar", "atualizar"}: continue
            alvo.parent.mkdir(parents=True, exist_ok=True)
            anterior = alvo.read_bytes() if alvo.exists() else None
            alvo.write_bytes(origem.read_bytes()); escritos.append((alvo, anterior))
        dados = {"versao": VERSAO, "perfil": perfil, "arquivos": {}}
        for _, alvo, origem in acoes:
            if alvo.exists(): dados[alvo.relative_to(destino).as_posix()] = sha(alvo)
        # Armazenar hashes em uma chave estável; o laço acima não usa caminhos como contrato.
        dados["arquivos"] = {alvo.relative_to(destino).as_posix(): {"hash": sha(alvo)} for _, alvo, _ in acoes if alvo.exists()}
        arq = manifesto(destino); arq.parent.mkdir(parents=True, exist_ok=True); arq.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except OSError:
        for alvo, anterior in reversed(escritos):
            if anterior is None:
                try: alvo.unlink()
                except OSError: pass
            elif alvo.exists(): alvo.write_bytes(anterior)
        raise
    return acoes


def remover(destino: Path):
    dados = ler_manifesto(destino)
    if not dados: raise ValueError("não há manifesto PACTO para remover")
    preservados, removidos = [], []
    for rel, meta in dados.get("arquivos", {}).items():
        alvo = destino / rel
        if not dentro(destino, alvo): preservados.append(f"recusa: {rel}"); continue
        if not alvo.exists() or sha(alvo) != meta.get("hash"):
            preservados.append(rel); continue
        # Estado e evidências são dados do projeto, nunca são removidos por este comando.
        if rel == ".pacto/estado.json": preservados.append(rel); continue
        alvo.unlink(); removidos.append(rel)
    return removidos, preservados


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destino", required=True, type=Path)
    parser.add_argument("--perfil", choices=("documental", "continuidade"), default="documental")
    sub = parser.add_subparsers(dest="comando", required=True)
    sub.add_parser("planejar"); sub.add_parser("diagnosticar")
    for nome in ("instalar", "atualizar", "remover"): sub.add_parser(nome).add_argument("--aplicar", action="store_true")
    args = parser.parse_args()
    try:
        destino = args.destino.resolve()
        if args.comando == "diagnosticar":
            dado = ler_manifesto(destino)
            print(json.dumps({"presente": bool(dado), "configurado": bool(dado), "reconhecido_pelo_host": False, "confianca_pendente": False, "evento_observado": False, "indisponivel": False}, ensure_ascii=False)); return 0
        if args.comando == "planejar":
            acoes, conflitos = planejar(destino, args.perfil, "atualizar")
            print(json.dumps({"acoes": [a for a, _, _ in acoes], "conflitos": conflitos}, ensure_ascii=False)); return 1 if conflitos else 0
        if not args.aplicar: raise ValueError("operação mutável exige --aplicar")
        if args.comando == "remover":
            removidos, preservados = remover(destino); print(json.dumps({"removidos": removidos, "preservados": preservados}, ensure_ascii=False)); return 0
        acoes = aplicar(destino, args.perfil, args.comando); print(json.dumps({"acoes": [a for a, _, _ in acoes]}, ensure_ascii=False)); return 0
    except ValueError as erro:
        print(f"FALHOU: {erro}", file=sys.stderr); return 2


if __name__ == "__main__": raise SystemExit(main())
