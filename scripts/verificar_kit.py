"""Checagem opcional do mantenedor, sem dependências e sem alterar arquivos.

Confere distribuição; não mede adesão do agente, segurança ou economia.
"""

import argparse
import re
import sys
from pathlib import Path


COPIAS = {
    **{f"templates/{nome}.template.md": f"{nome}.md"
       for nome in ("AGENTS", "CLAUDE", "BRIEF", "SPEC", "PLAN")},
    "docs/validacao-proporcional.md": ".pacto/validacao.md",
}
VERSAO = re.compile(r"<!-- Kit PACTO: (\d{4}\.\d{2}\.\d{2}\.\d+) -->")
SECOES = (
    "Escolher a prova", "Corrigir bugs", "Dados e edição parcial",
    "Entrega e publicação", "Artefato visual", "Operação conjunta", "Comunicação",
)


def ler(caminho, erros):
    try:
        return caminho.read_bytes().decode("utf-8-sig")
    except (OSError, UnicodeError) as exc:
        erros.append(f"{caminho}: ausente, ilegível ou não UTF-8 ({type(exc).__name__})")
        return ""


def verificar_instalacao(pasta):
    erros = []
    agentes = ler(pasta / "AGENTS.md", erros)
    if not VERSAO.search(agentes):
        erros.append("AGENTS.md sem identidade de versão do kit")
    if "`.pacto/validacao.md`" not in agentes:
        erros.append("AGENTS.md não encaminha à política local")
    politica = ler(pasta / ".pacto/validacao.md", erros)
    for secao in SECOES:
        if f"## {secao}\n" not in politica.replace("\r\n", "\n"):
            erros.append(f"Política sem seção: {secao}")
    claude = pasta / "CLAUDE.md"
    if claude.exists() and "@AGENTS.md" not in ler(claude, erros):
        erros.append("CLAUDE.md não encaminha ao AGENTS.md")
    return erros


def verificar_fontes(raiz):
    kit = raiz / "kit-pacto/PARA-COPIAR-NA-RAIZ"
    erros = verificar_instalacao(kit)
    for origem, destino in COPIAS.items():
        fonte, copia = raiz / origem, kit / destino
        ler(fonte, erros)
        ler(copia, erros)
        if fonte.is_file() and copia.is_file() and fonte.read_bytes() != copia.read_bytes():
            erros.append(f"Cópia diferente da fonte: {destino}")
    fonte_agentes = ler(raiz / "templates/AGENTS.template.md", erros)
    versao = VERSAO.search(fonte_agentes)
    if versao:
        for arquivo in ("README.md", "kit-pacto/LEIA-PRIMEIRO.md"):
            if f"`{versao.group(1)}`" not in ler(raiz / arquivo, erros):
                erros.append(f"Versão não identificada em {arquivo}")
    return erros


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instalacao", type=Path, help="Conferir somente um kit local isolado/adaptado")
    args = parser.parse_args()
    erros = (verificar_instalacao(args.instalacao.resolve()) if args.instalacao
             else verificar_fontes(Path(__file__).resolve().parents[1]))
    if erros:
        print("FALHOU:\n- " + "\n- ".join(dict.fromkeys(erros)))
        return 1
    print("OK: kit local disponível, versão e UTF-8 conferidos."
          if args.instalacao else "OK: seis cópias idênticas, versão, caminho local e UTF-8 conferidos.")
    print("Esta checagem não comprova adesão do agente nem economia.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
