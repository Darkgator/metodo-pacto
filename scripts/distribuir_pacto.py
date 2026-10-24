"""Distribui as fontes canônicas do PACTO para o plugin e o kit, de forma determinística."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
KIT = RAIZ / "kit-pacto" / "PARA-COPIAR-NA-RAIZ"
COPIAS = {
    "guia-visual/index.html": ["guia-visual/index-v2-claude.html"],
    "scripts/pacto_estado.py": ["plugin-pacto/scripts/pacto_estado.py", "kit-pacto/PARA-COPIAR-NA-RAIZ/.pacto/pacto-estado.py"],
    "templates/ESTADO.template.json": ["kit-pacto/PARA-COPIAR-NA-RAIZ/.pacto/estado.json"],
    **{f"templates/{nome}.template.md": [f"kit-pacto/PARA-COPIAR-NA-RAIZ/{nome}.md"] for nome in ("AGENTS", "CLAUDE", "BRIEF", "SPEC", "PLAN", "INVARIANTES")},
    "docs/validacao-proporcional.md": ["kit-pacto/PARA-COPIAR-NA-RAIZ/.pacto/validacao.md"],
    "docs/operacao.md": ["kit-pacto/PARA-COPIAR-NA-RAIZ/.pacto/operacao.md"],
}

PROMPTS = {
    "globais": [("guia-visual/index.html", "prompt-global", "html")],
    "executar": [("docs/guia-projeto-do-zero.md", "executar", "md"), ("kit-pacto/LEIA-PRIMEIRO.md", "executar", "md"), ("guia-visual/index.html", "prompt-5", "html"), ("guia-visual/index.html", "prompt-7a", "html")],
    "revisar": [("docs/guia-projeto-do-zero.md", "revisar", "md"), ("guia-visual/index.html", "prompt-6", "html")],
    "fechar": [("guia-visual/index.html", "prompt-7b", "html")],
}


def conferir_prompts(aplicar: bool = False) -> list[str]:
    erros = []
    try:
        fonte = (RAIZ / "prompts/operacionais.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ["fonte dos prompts ausente ou não UTF-8"]
    for nome, destinos in PROMPTS.items():
        blocos = re.findall(r"^## " + re.escape(nome) + r"\n\n```text\n(.*?)\n```", fonte, re.M | re.S)
        if len(blocos) != 1:
            erros.append(f"prompt {nome}: esperado um único bloco canônico")
            continue
        for rel, identificador, tipo in destinos:
            caminho = RAIZ / rel
            try:
                atual = caminho.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                erros.append(f"destino do prompt ausente ou não UTF-8: {rel}")
                continue
            if tipo == "html":
                padrao = r'(<pre id="' + re.escape(identificador) + r'">)(.*?)(</pre>)'
                conteudo = html.escape(blocos[0], quote=False)
            else:
                padrao = r"(<!-- pacto:" + identificador + r" -->\n```text\n)(.*?)(\n```\n<!-- /pacto:" + identificador + r" -->)"
                conteudo = blocos[0]
            if len(re.findall(padrao, atual, re.S)) != 1:
                erros.append(f"destino {rel}: marcador único ausente para {identificador}")
                continue
            esperado = re.sub(padrao, lambda m: m[1] + conteudo + m[3], atual, flags=re.S)
            if esperado != atual:
                if aplicar:
                    caminho.write_text(esperado, encoding="utf-8")
                else:
                    erros.append(f"prompt divergente: {rel}#{identificador}")
    return erros


def conferir(aplicar: bool = False) -> list[str]:
    erros = conferir_prompts(aplicar)
    for origem_rel, destinos in COPIAS.items():
        origem = RAIZ / origem_rel
        if not origem.is_file():
            erros.append(f"fonte ausente: {origem_rel}")
            continue
        conteudo = origem.read_bytes()
        for destino_rel in destinos:
            destino = RAIZ / destino_rel
            if destino.is_file() and destino.read_bytes() == conteudo:
                continue
            if aplicar:
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_bytes(conteudo)
            else:
                erros.append(f"cópia diferente da fonte: {destino_rel}")
    return erros


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--conferir", action="store_true")
    grupo.add_argument("--aplicar", action="store_true")
    args = parser.parse_args()
    erros = conferir(args.aplicar)
    if erros:
        print("FALHOU:\n- " + "\n- ".join(erros))
        return 1
    print("OK: distribuição atualizada." if args.aplicar else "OK: distribuição idêntica às fontes canônicas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
