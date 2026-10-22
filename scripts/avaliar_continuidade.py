"""Prepara uma bancada limitada; não chama IA sem executor explícito e autorização."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
PADRAO = RAIZ / "tests" / "cenarios_continuidade.json"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cenarios", type=Path, default=PADRAO)
    parser.add_argument("--executar-ia", action="store_true")
    parser.add_argument("--confirmar-orcamento", action="store_true")
    args = parser.parse_args()
    cenarios = json.loads(args.cenarios.read_text(encoding="utf-8"))
    plano = {"cenarios": len(cenarios), "variantes": 2, "execucoes_maximas": len(cenarios) * 2, "turnos_maximos_por_execucao": 8, "saida_maxima_por_execucao": 6000, "saida_maxima_agregada": len(cenarios) * 2 * 6000, "chamadas_ia_realizadas": 0}
    if args.executar_ia:
        if not args.confirmar_orcamento:
            print(json.dumps({**plano, "estado": "bloqueada", "motivo": "--executar-ia exige --confirmar-orcamento e um executor configurado; este script não possui executor embutido."}, ensure_ascii=False, indent=2)); return 2
        print(json.dumps({**plano, "estado": "bloqueada", "motivo": "executor externo não implementado para evitar consumo ou cobrança implícitos."}, ensure_ascii=False, indent=2)); return 2
    print(json.dumps({**plano, "estado": "preparada", "nota": "Nenhuma IA foi chamada. Compare baseline 01d0d03 e candidato em sessões equivalentes antes de registrar ganho."}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__": raise SystemExit(main())
