"""Hook somente de leitura: insere o resumo PACTO na sessão atual."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main():
    try:
        evento = json.load(sys.stdin)
        raiz = Path(evento["cwd"])
        arquivo = raiz / ".pacto" / "estado.json"
        if not arquivo.is_file():
            return
        dados = json.loads(arquivo.read_text(encoding="utf-8"))
        abertos = [t for t in dados.get("trabalhos", []) if t.get("situacao") != "concluido"]
        if not abertos:
            return
        linhas = [f"PACTO: estado local revisão {dados.get('revisao', '?')}. Não reabra decisões sem motivo concreto."]
        for t in abertos[:3]:
            linhas.append(f"[{t.get('id')}] {t.get('situacao')}: {t.get('titulo')}. Próximo: {t.get('proximo_passo')}")
        saida = {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n".join(linhas)}}
        print(json.dumps(saida, ensure_ascii=False))
    except (OSError, ValueError, KeyError, json.JSONDecodeError):
        return


if __name__ == "__main__":
    main()
