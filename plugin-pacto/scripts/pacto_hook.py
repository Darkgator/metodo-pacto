"""Adaptador de SessionStart: leitura local, sem escrita nem chamada de modelo."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from pacto_estado import ErroPacto, contexto, ler, localizar_raiz


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        evento = json.load(sys.stdin)
        cwd = evento.get("cwd")
        if not isinstance(cwd, str):
            return 0
        raiz = localizar_raiz(Path(cwd))
        if raiz is None:
            return 0
        try:
            dados = ler(raiz, aceitar_v1=True)
        except ErroPacto:
            saida = "PACTO: cobertura de continuidade indisponível; estado local inválido ou incompatível."
        else:
            saida = contexto(dados, evento.get("session_id"))
            if saida == "PACTO: sem trabalho persistido em aberto.":
                return 0
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": saida[:4000]}}, ensure_ascii=False))
    except (OSError, ValueError, KeyError, json.JSONDecodeError):
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
