"""Verifica fontes, distribuição e uma instalação PACTO sem modificá-las."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from distribuir_pacto import COPIAS, RAIZ, conferir
from pacto_estado import ErroPacto, ler


def texto(caminho: Path, erros: list[str]) -> str:
    try: return caminho.read_bytes().decode("utf-8-sig")
    except (OSError, UnicodeError) as erro:
        erros.append(f"{caminho}: ausente, ilegível ou não UTF-8 ({type(erro).__name__})"); return ""


def verificar_instalacao(pasta: Path, continuidade: bool) -> list[str]:
    erros = []
    agentes = texto(pasta / "AGENTS.md", erros)
    if "Kit PACTO:" not in agentes: erros.append("AGENTS.md sem identidade de versão do kit")
    if "`.pacto/validacao.md`" not in agentes: erros.append("AGENTS.md não encaminha à política local")
    politica = texto(pasta / ".pacto" / "validacao.md", erros)
    if "## Escolher a prova" not in politica: erros.append("Política local incompleta")
    claude = pasta / "CLAUDE.md"
    if claude.exists() and "@AGENTS.md" not in texto(claude, erros): erros.append("CLAUDE.md não encaminha ao AGENTS.md")
    estado = pasta / ".pacto" / "estado.json"; comando = pasta / ".pacto" / "pacto-estado.py"
    if continuidade:
        if not estado.is_file(): erros.append("Continuidade solicitada sem estado PACTO")
        else:
            try:
                ler(pasta)
            except ErroPacto as erro: erros.append(f"Estado PACTO inválido: {erro}")
        if not comando.is_file(): erros.append("Continuidade solicitada sem comando de estado")
    return erros


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instalacao", type=Path)
    parser.add_argument("--continuidade", action="store_true")
    args = parser.parse_args()
    if args.instalacao:
        erros = verificar_instalacao(args.instalacao.resolve(), args.continuidade)
    else:
        erros = conferir(False)
        plugin = RAIZ / "plugin-pacto" / "plugin.json"
        try:
            dados = json.loads(plugin.read_text(encoding="utf-8"))
            if not str(dados.get("version", "")): erros.append("plugin sem versão")
            if not (RAIZ / "plugin-pacto" / "skills" / "pacto" / "references" / "continuidade.md").is_file(): erros.append("referência da skill ausente")
        except (OSError, json.JSONDecodeError): erros.append("plugin.json inválido")
    if erros:
        print("FALHOU:\n- " + "\n- ".join(dict.fromkeys(erros))); return 1
    quantidade = sum(len(destinos) for destinos in COPIAS.values())
    print(f"OK: {quantidade} cópias distribuídas e UTF-8 conferidos." if not args.instalacao else "OK: instalação PACTO coerente.")
    print("Esta checagem não comprova adesão do agente, confiança de hook ou economia.")
    return 0


if __name__ == "__main__": raise SystemExit(main())
