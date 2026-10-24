import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
ESTADO = RAIZ / "scripts" / "pacto_estado.py"


class EvidenciasPactoTest(unittest.TestCase):
    def executar(self, pasta, *args):
        return subprocess.run([sys.executable, str(ESTADO), "--raiz", str(pasta), *args], text=True, encoding="utf-8", capture_output=True, check=False, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1"})

    def criar(self, pasta):
        r = self.executar(pasta, "iniciar", "--titulo", "Provar", "--objetivo", "Cobrir", "--proximo-passo", "Testar", "--esperada-revisao", "0")
        self.assertEqual(r.returncode, 0, r.stderr); return json.loads(r.stdout)["id"]

    def test_prova_vence_so_quando_arquivo_declarado_muda(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); trabalho = self.criar(pasta)
            (pasta / "alvo.txt").write_text("um", encoding="utf-8"); (pasta / "outro.txt").write_text("x", encoding="utf-8")
            (pasta / ".pacto" / "verificacoes.json").write_text(json.dumps({"verificacoes": [{"id": "ok", "argv": [sys.executable, "-c", "print('ok')"], "arquivos": ["alvo.txt"]}]}), encoding="utf-8")
            prova = self.executar(pasta, "provar", trabalho, "--verificacao", "ok", "--esperada-revisao", "1")
            self.assertEqual(prova.returncode, 0, prova.stderr)
            (pasta / "outro.txt").write_text("mudou", encoding="utf-8")
            vigente = json.loads(self.executar(pasta, "verificar", trabalho).stdout)
            self.assertFalse(vigente["evidencias"][0]["vencida"])
            (pasta / "alvo.txt").write_text("mudou", encoding="utf-8")
            vencida = json.loads(self.executar(pasta, "verificar", trabalho).stdout)
            self.assertTrue(vencida["evidencias"][0]["vencida"])

    def test_publicacao_divergente_nao_vira_sucesso(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); trabalho = self.criar(pasta)
            registro = self.executar(pasta, "registrar-publicacao", trabalho, "--esperado-ambiente", "producao", "--observado-ambiente", "homologacao", "--esperada-revisao-publicada", "abc", "--observada-revisao-publicada", "abc", "--fonte", "consulta", "--esperada-revisao", "1")
            self.assertEqual(registro.returncode, 0, registro.stderr)
            resultado = json.loads(self.executar(pasta, "verificar", trabalho).stdout)
            self.assertTrue(resultado["publicacao_divergente"])

    def test_cli_mostra_falha_da_prova_e_preserva_o_registro(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); trabalho = self.criar(pasta)
            (pasta / ".pacto/verificacoes.json").write_text(json.dumps({"verificacoes": [{"id": "falha", "argv": [sys.executable, "-c", "raise SystemExit(7)"], "criterio": "Comando deve passar"}]}), encoding="utf-8")
            r = self.executar(pasta, "provar", trabalho, "--verificacao", "falha", "--esperada-revisao", "1")
            self.assertEqual(r.returncode, 1, r.stderr)
            saida = json.loads(r.stdout)
            self.assertEqual(saida["revisao"], 2)
            self.assertEqual(saida["evidencias"][0]["resultado"], "falhou")
            self.assertEqual(saida["evidencias"][0]["codigo_saida"], 7)
            armazenado = json.loads(self.executar(pasta, "mostrar", trabalho).stdout)
            self.assertEqual(armazenado["evidencias"][0]["resultado"], "falhou")

    def test_d09_cli_nao_confirma_publicacao_incompleta_ou_manual(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); trabalho = self.criar(pasta)
            base = ["registrar-publicacao", trabalho, "--esperado-ambiente", "producao", "--observado-ambiente", "producao", "--esperada-revisao-publicada", "abc123", "--fonte", "informação manual"]
            r = self.executar(pasta, *base, "--esperada-revisao", "1")
            self.assertEqual(r.returncode, 0, r.stderr)
            pendente = json.loads(self.executar(pasta, "verificar", trabalho).stdout)
            self.assertEqual(pendente["publicacao_situacao"], "pendente")
            self.assertFalse(pendente["publicacao_confirmada_automaticamente"])
            self.assertEqual(pendente["situacao"], "ativo")
            r = self.executar(pasta, *base, "--observada-revisao-publicada", "abc123", "--esperada-revisao", "2")
            self.assertEqual(r.returncode, 0, r.stderr)
            informada = json.loads(self.executar(pasta, "verificar", trabalho).stdout)
            self.assertEqual(informada["publicacao_situacao"], "informada")
            self.assertFalse(informada["publicacao_confirmada_automaticamente"])


if __name__ == "__main__": unittest.main()
