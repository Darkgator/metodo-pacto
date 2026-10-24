"""Instala suporte PACTO preservando contratos, instruções e estado do projeto."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
VERSAO = "2026.10.24.1"
DOCUMENTOS = {
    "AGENTS.md": "templates/AGENTS.template.md",
    "CLAUDE.md": "templates/CLAUDE.template.md",
    ".pacto/validacao.md": "docs/validacao-proporcional.md",
}
CONTRATOS = {f"{n}.md": f"templates/{n}.template.md" for n in ("BRIEF", "SPEC", "PLAN", "INVARIANTES")}
CONTINUIDADE = {
    ".pacto/pacto-estado.py": "scripts/pacto_estado.py",
    ".pacto/estado.json": "templates/ESTADO.template.json",
}
PACOTE = {".pacto/validacao.md", ".pacto/pacto-estado.py"}
PROJETO = {"AGENTS.md", "CLAUDE.md", ".pacto/estado.json", *CONTRATOS}


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
    if not dentro(destino, arquivo):
        raise ValueError("manifesto aponta para fora do projeto")
    if not arquivo.exists():
        return None
    try:
        dados = json.loads(arquivo.read_text(encoding="utf-8"))
        if not isinstance(dados, dict) or not isinstance(dados.get("arquivos"), dict):
            raise ValueError("manifesto de instalação inválido")
        if any(not isinstance(m, dict) for m in dados["arquivos"].values()):
            raise ValueError("manifesto de instalação inválido")
        return dados
    except (OSError, UnicodeError, json.JSONDecodeError) as erro:
        raise ValueError("manifesto de instalação inválido") from erro


def fontes(perfil: str, contratos=()) -> dict[str, Path]:
    itens = dict(DOCUMENTOS)
    if perfil == "continuidade":
        itens.update(CONTINUIDADE)
    for nome in contratos:
        rel = f"{nome}.md"
        if rel not in CONTRATOS:
            raise ValueError(f"contrato desconhecido: {nome}")
        itens[rel] = CONTRATOS[rel]
    return {destino: RAIZ / origem for destino, origem in itens.items()}


def planejar(destino: Path, perfil: str, modo: str, contratos=()):
    destino = destino.resolve()
    if not destino.is_dir():
        raise ValueError(f"destino inválido: {destino}")
    geridos = (ler_manifesto(destino) or {}).get("arquivos", {})
    acoes, conflitos = [], []
    for rel, origem in fontes(perfil, contratos).items():
        alvo = destino / rel
        if not dentro(destino, alvo):
            conflitos.append(f"recusa: {rel} aponta para fora do projeto")
        elif not alvo.exists():
            acoes.append(("criar", alvo, origem))
        elif rel in PROJETO:
            acoes.append(("preservar-projeto", alvo, origem))
        elif sha(alvo) == sha(origem):
            acoes.append(("manter", alvo, origem))
        elif rel not in geridos:
            conflitos.append(f"preservar não gerido: {rel}")
        elif geridos[rel].get("hash") != sha(alvo):
            conflitos.append(f"conflito local: {rel}")
        else:
            acoes.append(("manter" if modo == "instalar" else "atualizar", alvo, origem))
    return acoes, conflitos


def gravar(arquivo: Path, conteudo: bytes):
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    temporario = None
    try:
        with tempfile.NamedTemporaryFile(dir=arquivo.parent, delete=False) as f:
            temporario = Path(f.name)
            f.write(conteudo)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporario, arquivo)
    finally:
        if temporario is not None:
            temporario.unlink(missing_ok=True)


def aplicar(destino: Path, perfil: str, modo: str, contratos=()):
    destino = destino.resolve()
    acoes, conflitos = planejar(destino, perfil, modo, contratos)
    if conflitos:
        raise ValueError("; ".join(conflitos))
    anterior = ler_manifesto(destino) or {"arquivos": {}}
    alterados = []
    try:
        for acao, alvo, origem in acoes:
            if acao not in {"criar", "atualizar"}:
                continue
            backup = alvo.read_bytes() if alvo.exists() else None
            gravar(alvo, origem.read_bytes())
            alterados.append((alvo, backup))
        arquivos = dict(anterior["arquivos"])
        for _, alvo, _ in acoes:
            rel = alvo.relative_to(destino).as_posix()
            if alvo.exists():
                arquivos[rel] = {"hash": sha(alvo), "propriedade": "projeto" if rel in PROJETO else "pacote"}
        dados = {"formato": 2, "versao": VERSAO, "perfil": perfil, "arquivos": arquivos}
        gravar(manifesto(destino), (json.dumps(dados, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    except OSError:
        for alvo, backup in reversed(alterados):
            if backup is None:
                alvo.unlink(missing_ok=True)
            else:
                gravar(alvo, backup)
        raise
    return acoes


def remover(destino: Path):
    destino = destino.resolve()
    dados = ler_manifesto(destino)
    if not dados:
        raise ValueError("não há manifesto PACTO para remover")
    preservados, removidos = [], []
    for rel, meta in dados["arquivos"].items():
        alvo = destino / rel
        # Mesmo manifestos antigos não concedem propriedade sobre contratos.
        if rel not in PACOTE or not dentro(destino, alvo):
            preservados.append(rel)
        elif not alvo.is_file() or sha(alvo) != meta.get("hash"):
            preservados.append(rel)
        else:
            alvo.unlink()
            removidos.append(rel)
    return removidos, preservados


def integracao_pendente(acoes) -> list[str]:
    return [alvo.name for acao, alvo, origem in acoes
            if acao == "preservar-projeto" and alvo.name in {"AGENTS.md", "CLAUDE.md"}
            and alvo.read_bytes() != origem.read_bytes()]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destino", required=True, type=Path)
    parser.add_argument("--perfil", choices=("documental", "continuidade"), default="documental")
    parser.add_argument("--contrato", dest="contratos", action="append", choices=("BRIEF", "SPEC", "PLAN", "INVARIANTES"), default=[])
    sub = parser.add_subparsers(dest="comando", required=True)
    sub.add_parser("planejar")
    sub.add_parser("diagnosticar")
    for nome in ("instalar", "atualizar", "remover"):
        sub.add_parser(nome).add_argument("--aplicar", action="store_true")
    args = parser.parse_args()
    try:
        destino = args.destino.resolve()
        if args.comando == "diagnosticar":
            dado = ler_manifesto(destino)
            print(json.dumps({"presente": bool(dado), "politica_presente": (destino / ".pacto/validacao.md").is_file(),
                              "runtime_presente": (destino / ".pacto/pacto-estado.py").is_file(),
                              "skill_instalada_por_este_comando": False, "reconhecido_pelo_host": None,
                              "confianca_pendente": None, "evento_observado": None}, ensure_ascii=False))
            return 0
        if args.comando == "planejar":
            acoes, conflitos = planejar(destino, args.perfil, "atualizar", args.contratos)
            print(json.dumps({"acoes": [{"acao": a, "arquivo": p.relative_to(destino).as_posix()} for a, p, _ in acoes],
                              "conflitos": conflitos, "integracao_pendente": integracao_pendente(acoes)}, ensure_ascii=False))
            return 1 if conflitos else 0
        if not args.aplicar:
            raise ValueError("operação mutável exige --aplicar")
        if args.comando == "remover":
            removidos, preservados = remover(destino)
            print(json.dumps({"removidos": removidos, "preservados": preservados}, ensure_ascii=False))
            return 0
        acoes = aplicar(destino, args.perfil, args.comando, args.contratos)
        print(json.dumps({"acoes": [a for a, _, _ in acoes], "integracao_pendente": integracao_pendente(acoes),
                          "skill_instalada_por_este_comando": False}, ensure_ascii=False))
        return 0
    except (ValueError, OSError) as erro:
        print(f"FALHOU: {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
