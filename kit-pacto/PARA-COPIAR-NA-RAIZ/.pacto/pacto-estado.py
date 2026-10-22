"""Estado curto e versionado dos trabalhos PACTO em um projeto.

Sem dependências. O arquivo fica em .pacto/estado.json e guarda somente o
estado vigente de cada trabalho, não a transcrição do chat.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


FORMATO = 1
SITUACOES = {"ativo", "pausado", "aguardando-usuario", "concluido"}


def agora():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def caminho_estado(raiz: Path) -> Path:
    return raiz / ".pacto" / "estado.json"


def vazio():
    return {"formato": FORMATO, "revisao": 0, "atualizado_em": None, "trabalhos": []}


def ler(raiz: Path):
    arquivo = caminho_estado(raiz)
    if not arquivo.exists():
        return vazio()
    try:
        dados = json.loads(arquivo.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as erro:
        raise ValueError(f"estado ilegível: {arquivo} ({erro})") from erro
    if dados.get("formato") != FORMATO or not isinstance(dados.get("trabalhos"), list):
        raise ValueError("estado incompatível; preserve o arquivo e atualize pelo migrador compatível")
    return dados


@contextmanager
def trava(arquivo: Path):
    caminho = arquivo.with_suffix(arquivo.suffix + ".lock")
    try:
        descritor = os.open(caminho, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as erro:
        raise ValueError("estado ocupado por outra atualização; releia e tente novamente") from erro
    try:
        yield
    finally:
        os.close(descritor)
        try:
            caminho.unlink()
        except FileNotFoundError:
            pass


def gravar(raiz: Path, dados, esperada: int | None):
    arquivo = caminho_estado(raiz)
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    with trava(arquivo):
        atual = ler(raiz)
        if esperada is not None and atual["revisao"] != esperada:
            raise ValueError(f"conflito: revisão atual {atual['revisao']}, esperada {esperada}")
        dados["revisao"] = atual["revisao"] + 1
        dados["atualizado_em"] = agora()
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=arquivo.parent, delete=False, suffix=".tmp") as temp:
            json.dump(dados, temp, ensure_ascii=False, indent=2)
            temp.write("\n")
            temporario = Path(temp.name)
        os.replace(temporario, arquivo)
    return dados


def localizar(dados, identificador: str):
    for trabalho in dados["trabalhos"]:
        if trabalho["id"] == identificador:
            return trabalho
    raise ValueError(f"trabalho inexistente: {identificador}")


def imprimir(dados, somente_ativos=False):
    trabalhos = [t for t in dados["trabalhos"] if not somente_ativos or t["situacao"] != "concluido"]
    print(json.dumps({"revisao": dados["revisao"], "trabalhos": trabalhos}, ensure_ascii=False, indent=2))


def contexto(dados):
    pendentes = [t for t in dados["trabalhos"] if t["situacao"] != "concluido"]
    if not pendentes:
        print("PACTO: sem trabalho persistido em aberto.")
        return
    linhas = [f"PACTO: revisão do estado {dados['revisao']}. Trabalhos em aberto:"]
    for t in pendentes:
        linhas.append(f"- [{t['id']}] {t['situacao']}: {t['titulo']}. Próximo passo: {t['proximo_passo']}")
        if t.get("bloqueio"):
            linhas.append(f"  Bloqueio: {t['bloqueio']}")
    print("\n".join(linhas))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raiz", type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest="comando", required=True)
    sub.add_parser("listar").add_argument("--abertos", action="store_true")
    sub.add_parser("contexto")
    iniciar = sub.add_parser("iniciar")
    iniciar.add_argument("--titulo", required=True)
    iniciar.add_argument("--objetivo", required=True)
    iniciar.add_argument("--proximo-passo", required=True)
    iniciar.add_argument("--situacao", choices=sorted(SITUACOES), default="ativo")
    atualizar = sub.add_parser("atualizar")
    atualizar.add_argument("id")
    atualizar.add_argument("--objetivo")
    atualizar.add_argument("--situacao", choices=sorted(SITUACOES))
    atualizar.add_argument("--decisao")
    atualizar.add_argument("--resultado")
    atualizar.add_argument("--tentativa-descartada")
    atualizar.add_argument("--bloqueio")
    atualizar.add_argument("--proximo-passo")
    atualizar.add_argument("--referencia", action="append")
    for comando in (iniciar, atualizar):
        comando.add_argument("--esperada-revisao", type=int)
    args = parser.parse_args()
    raiz = args.raiz.resolve()
    try:
        dados = ler(raiz)
        if args.comando == "listar":
            imprimir(dados, args.abertos)
            return
        if args.comando == "contexto":
            contexto(dados)
            return
        if args.comando == "iniciar":
            trabalho = {
                "id": uuid4().hex[:8], "titulo": args.titulo, "objetivo": args.objetivo,
                "situacao": args.situacao, "decisoes": [], "ultimo_resultado": None,
                "tentativas_descartadas": [], "bloqueio": None, "proximo_passo": args.proximo_passo,
                "referencias": [], "atualizado_em": agora(),
            }
            dados["trabalhos"].append(trabalho)
            dados = gravar(raiz, dados, args.esperada_revisao)
            print(json.dumps({"id": trabalho["id"], "revisao": dados["revisao"]}, ensure_ascii=False))
            return
        trabalho = localizar(dados, args.id)
        for campo in ("objetivo", "situacao", "bloqueio", "proximo_passo"):
            valor = getattr(args, campo)
            if valor is not None:
                trabalho[campo] = valor
        if args.decisao:
            trabalho["decisoes"].append(args.decisao)
        if args.resultado:
            trabalho["ultimo_resultado"] = args.resultado
        if args.tentativa_descartada:
            trabalho["tentativas_descartadas"].append(args.tentativa_descartada)
        if args.referencia:
            trabalho["referencias"] = list(dict.fromkeys([*trabalho["referencias"], *args.referencia]))
        trabalho["atualizado_em"] = agora()
        dados = gravar(raiz, dados, args.esperada_revisao)
        print(json.dumps({"id": trabalho["id"], "revisao": dados["revisao"]}, ensure_ascii=False))
    except ValueError as erro:
        print(f"FALHOU: {erro}", file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
