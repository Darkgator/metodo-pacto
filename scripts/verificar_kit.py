"""Verifica fontes, distribuição e uma instalação PACTO sem modificá-las."""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from distribuir_pacto import COPIAS, RAIZ, conferir
from pacto_estado import ErroPacto, ler
from instalar_pacto import VERSAO


class Guia(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.copias, self.pres = [], [], [], set()
        self.utf8 = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
            if tag == "pre": self.pres.add(a["id"])
        if a.get("href"): self.links.append(a["href"])
        if a.get("src"): self.links.append(a["src"])
        if a.get("data-copy"): self.copias.append(a["data-copy"])
        if tag == "meta" and a.get("charset", "").lower() == "utf-8": self.utf8 = True


def conferir_link(raiz: Path, arquivo: Path, destino: str) -> str | None:
    url = urlsplit(destino.strip("<>"))
    if url.scheme or url.netloc or not url.path:
        return None  # Sem rede; âncoras HTML são verificadas no próprio guia.
    caminho = (arquivo.parent / unquote(url.path)).resolve()
    if not caminho.is_relative_to(raiz.resolve()) or not caminho.exists():
        return f"{arquivo.relative_to(raiz)}: referência local ausente ou externa à raiz: {destino}"
    return None


def verificar_documentos(raiz: Path) -> list[str]:
    erros = []
    extensoes = {".md", ".py", ".json", ".html", ".yml", ".yaml", ".txt"}
    ignorar = {".git", "__pycache__", ".venv", "node_modules", ".pytest_cache"}
    for caminho in sorted(raiz.rglob("*")):
        if not caminho.is_file() or caminho.suffix not in extensoes or ignorar.intersection(caminho.relative_to(raiz).parts):
            continue
        conteudo = texto(caminho, erros)
        if caminho.suffix == ".py":
            try: ast.parse(conteudo, filename=str(caminho))
            except SyntaxError: erros.append(f"{caminho.relative_to(raiz)}: Python inválido")
        elif caminho.suffix == ".json":
            try: json.loads(conteudo)
            except json.JSONDecodeError: erros.append(f"{caminho.relative_to(raiz)}: JSON inválido")
        elif caminho.suffix == ".md":
            # Exemplos em código não são referências navegáveis do documento.
            visivel = re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$", "", conteudo)
            visivel = re.sub(r"`[^`\n]*`", "", visivel)
            destinos = re.findall(r"\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", visivel)
            for destino in destinos:
                erro = conferir_link(raiz, caminho, destino)
                if erro: erros.append(erro)
        elif caminho.suffix == ".html":
            guia = Guia(); guia.feed(conteudo)
            if not guia.utf8: erros.append(f"{caminho.relative_to(raiz)}: charset UTF-8 ausente")
            if any(n > 1 for n in Counter(guia.ids).values()): erros.append(f"{caminho.relative_to(raiz)}: ID HTML duplicado")
            if set(guia.copias) - guia.pres: erros.append(f"{caminho.relative_to(raiz)}: botão de cópia sem prompt correspondente")
            for destino in guia.links:
                if destino.startswith("#"):
                    if destino[1:] and unquote(destino[1:]) not in guia.ids:
                        erros.append(f"{caminho.relative_to(raiz)}: âncora HTML ausente: {destino}")
                else:
                    erro = conferir_link(raiz, caminho, destino)
                    if erro: erros.append(erro)
    return erros


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
    if "`.pacto/operacao.md`" in agentes:
        operacao = texto(pasta / ".pacto/operacao.md", erros)
        if "## Segurança e licença" not in operacao: erros.append("Política de operação incompleta")
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
        erros = conferir(False) + verificar_documentos(RAIZ)
        if f"Kit PACTO: {VERSAO}" not in texto(RAIZ / "templates/AGENTS.template.md", erros):
            erros.append("Versão do instalador diverge do modelo AGENTS")
        plugin = RAIZ / "plugin-pacto" / "plugin.json"
        try:
            dados = json.loads(plugin.read_text(encoding="utf-8"))
            if not str(dados.get("version", "")): erros.append("plugin sem versão")
            if not (RAIZ / "plugin-pacto" / "skills" / "pacto" / "references" / "continuidade.md").is_file(): erros.append("referência da skill ausente")
        except (OSError, UnicodeError, json.JSONDecodeError): erros.append("plugin.json inválido")
    if erros:
        print("FALHOU:\n- " + "\n- ".join(dict.fromkeys(erros))); return 1
    quantidade = sum(len(destinos) for destinos in COPIAS.values())
    print(f"OK: {quantidade} cópias, prompts, UTF-8, sintaxe e referências locais conferidos." if not args.instalacao else "OK: instalação PACTO coerente.")
    print("Esta checagem não comprova adesão do agente, confiança de hook ou economia.")
    return 0


if __name__ == "__main__": raise SystemExit(main())
