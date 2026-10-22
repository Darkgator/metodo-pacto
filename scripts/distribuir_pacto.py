"""Distribui as fontes canônicas do PACTO para o plugin e o kit, de forma determinística."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
KIT = RAIZ / "kit-pacto" / "PARA-COPIAR-NA-RAIZ"
COPIAS = {
    "scripts/pacto_estado.py": ["plugin-pacto/scripts/pacto_estado.py", "kit-pacto/PARA-COPIAR-NA-RAIZ/.pacto/pacto-estado.py"],
    "templates/ESTADO.template.json": ["kit-pacto/PARA-COPIAR-NA-RAIZ/.pacto/estado.json"],
    **{f"templates/{nome}.template.md": [f"kit-pacto/PARA-COPIAR-NA-RAIZ/{nome}.md"] for nome in ("AGENTS", "CLAUDE", "BRIEF", "SPEC", "PLAN", "INVARIANTES")},
    "docs/validacao-proporcional.md": ["kit-pacto/PARA-COPIAR-NA-RAIZ/.pacto/validacao.md"],
}


def conferir(aplicar: bool = False) -> list[str]:
    erros = []
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
