"""Provas determinísticas da distribuição e da integridade documental."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "scripts"))
import distribuir_pacto as distribuir
import verificar_kit as verificar
import instalar_pacto as instalar


class PacotePactoTest(unittest.TestCase):
    def test_instalacao_atual_exige_as_politicas_que_o_agents_referencia(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            instalar.aplicar(raiz, "continuidade", "instalar")
            self.assertEqual(verificar.verificar_instalacao(raiz, True), [])
            (raiz / ".pacto/operacao.md").unlink()
            self.assertTrue(any("operacao.md" in e for e in verificar.verificar_instalacao(raiz, True)))

    def copiar_distribuicao(self, raiz):
        arquivos = {"prompts/operacionais.md", *distribuir.COPIAS}
        for destinos in distribuir.COPIAS.values(): arquivos.update(destinos)
        for destinos in distribuir.PROMPTS.values(): arquivos.update(p for p, _, _ in destinos)
        for rel in arquivos:
            alvo = raiz / rel; alvo.parent.mkdir(parents=True, exist_ok=True)
            alvo.write_bytes((RAIZ / rel).read_bytes())

    def test_divergencia_de_prompt_reprova_e_aplicacao_repara_sem_tocar_entorno(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); self.copiar_distribuicao(raiz)
            pagina = raiz / "guia-visual/index.html"
            original = pagina.read_bytes()
            atual = pagina.read_text(encoding="utf-8")
            # Corrompe somente um prompt; demais cartões e HTML devem sobreviver.
            inicio = atual.index('<pre id="prompt-5">') + len('<pre id="prompt-5">')
            fim = atual.index('</pre>', inicio)
            pagina.write_text(atual[:inicio] + 'Pare sempre após qualquer checkpoint.' + atual[fim:], encoding="utf-8")
            with mock.patch.object(distribuir, "RAIZ", raiz):
                erros = distribuir.conferir(False)
                self.assertTrue(any("prompt-5" in e for e in erros))
                self.assertEqual(distribuir.conferir(True), [])
                self.assertEqual(distribuir.conferir(False), [])
            self.assertEqual(pagina.read_text(encoding="utf-8"), original.decode("utf-8").replace("\r\n", "\n"))

    def test_aplicar_escape_html_sem_alterar_texto_do_prompt(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); self.copiar_distribuicao(raiz)
            fonte = raiz / "prompts/operacionais.md"
            texto = fonte.read_text(encoding="utf-8").replace("Execute o escopo", "Se a < b & c > d, execute o escopo")
            fonte.write_text(texto, encoding="utf-8")
            with mock.patch.object(distribuir, "RAIZ", raiz):
                self.assertEqual(distribuir.conferir(True), [])
                self.assertEqual(distribuir.conferir(False), [])
            pagina = (raiz / "guia-visual/index.html").read_text(encoding="utf-8")
            self.assertIn("Se a &lt; b &amp; c &gt; d", pagina)
            markdown = (raiz / "kit-pacto/LEIA-PRIMEIRO.md").read_text(encoding="utf-8")
            self.assertIn("Se a < b & c > d", markdown)

    def test_marcador_ausente_nao_permite_reescrever_destino(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); self.copiar_distribuicao(raiz)
            guia = raiz / "docs/guia-projeto-do-zero.md"
            guia.write_text("Conteúdo local sem marcadores", encoding="utf-8")
            with mock.patch.object(distribuir, "RAIZ", raiz):
                self.assertTrue(any("marcador" in e for e in distribuir.conferir(True)))
            self.assertEqual(guia.read_text(encoding="utf-8"), "Conteúdo local sem marcadores")

    def test_copia_de_pacote_alterada_reprova(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); self.copiar_distribuicao(raiz)
            (raiz / "plugin-pacto/scripts/pacto_estado.py").write_text("# cópia incorreta", encoding="utf-8")
            with mock.patch.object(distribuir, "RAIZ", raiz):
                self.assertTrue(any("cópia diferente" in e for e in distribuir.conferir(False)))

    def test_verificador_detecta_referencias_e_estrutura_do_guia(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            md = raiz / "leia.md"; md.write_text("[Alvo](alvo.md)\n\n```text\n[Exemplo](nao-e-link.md)\n```", encoding="utf-8")
            alvo = raiz / "alvo.md"; alvo.write_text("# Alvo", encoding="utf-8")
            html = raiz / "guia.html"
            html.write_text('<meta charset="utf-8"><a href="#p">Ir</a><pre id="p">Texto</pre><button data-copy="p">Copiar</button>', encoding="utf-8")
            self.assertEqual(verificar.verificar_documentos(raiz), [])
            alvo.unlink()
            html.write_text('<meta charset="utf-8"><a href="#ausente">Ir</a><pre id="p"></pre><pre id="p"></pre><button data-copy="inexistente">Copiar</button>', encoding="utf-8")
            erros = verificar.verificar_documentos(raiz)
            self.assertTrue(any("alvo.md" in e for e in erros))
            self.assertTrue(any("ID HTML duplicado" in e for e in erros))
            self.assertTrue(any("âncora HTML ausente" in e for e in erros))
            self.assertTrue(any("botão de cópia" in e for e in erros))

    def test_utf8_sintaxe_e_json_invalidos_reprovam(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "texto.md").write_bytes(b"inv\xe1lido")
            (raiz / "config.json").write_text("{inválido", encoding="utf-8")
            (raiz / "script.py").write_text("def sem_corpo(", encoding="utf-8")
            erros = verificar.verificar_documentos(raiz)
            for trecho in ("UTF-8", "JSON inválido", "Python inválido"):
                self.assertTrue(any(trecho in e for e in erros), (trecho, erros))


if __name__ == "__main__": unittest.main()
