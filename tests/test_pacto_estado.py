import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
ESTADO = RAIZ / "scripts" / "pacto_estado.py"
HOOK = RAIZ / "plugin-pacto" / "scripts" / "pacto_hook.py"


class EstadoPactoTest(unittest.TestCase):
    def executar(self, pasta, *argumentos):
        ambiente = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1"}
        return subprocess.run([sys.executable, str(ESTADO), "--raiz", str(pasta), *argumentos], text=True, encoding="utf-8", capture_output=True, check=False, env=ambiente)

    def iniciar(self, pasta, titulo="Corrigir acesso"):
        retorno = self.executar(pasta, "iniciar", "--titulo", titulo, "--objetivo", "Corrigir rota", "--proximo-passo", "Reproduzir", "--esperada-revisao", "0")
        self.assertEqual(retorno.returncode, 0, retorno.stderr)
        return json.loads(retorno.stdout)["id"]

    def test_mutacao_sem_revisao_e_leitura_ausente_sem_efeito(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio)
            leitura = self.executar(pasta, "contexto")
            self.assertEqual(leitura.returncode, 0)
            self.assertFalse((pasta / ".pacto").exists())
            sem_revisao = self.executar(pasta, "iniciar", "--titulo", "A", "--objetivo", "B", "--proximo-passo", "C")
            self.assertNotEqual(sem_revisao.returncode, 0)
            self.assertFalse((pasta / ".pacto").exists())

    def test_d01_leitura_antiga_nao_sobrescreve(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); identificador = self.iniciar(pasta)
            primeira = self.executar(pasta, "atualizar", identificador, "--resultado", "A", "--esperada-revisao", "1")
            antiga = self.executar(pasta, "atualizar", identificador, "--resultado", "B", "--esperada-revisao", "1")
            self.assertEqual(primeira.returncode, 0, primeira.stderr)
            self.assertEqual(antiga.returncode, 3, antiga.stderr)
            estado = json.loads((pasta / ".pacto" / "estado.json").read_text(encoding="utf-8"))
            self.assertEqual(estado["trabalhos"][0]["ultimo_resultado"], "A")

    def test_processos_simultaneos_retornam_sucesso_ou_conflito(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); identificador = self.iniciar(pasta)
            ambiente = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1"}
            base = [sys.executable, str(ESTADO), "--raiz", str(pasta), "atualizar", identificador, "--esperada-revisao", "1"]
            primeiro = subprocess.Popen([*base, "--resultado", "A"], text=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=ambiente)
            segundo = subprocess.Popen([*base, "--resultado", "B"], text=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=ambiente)
            _, erro_um = primeiro.communicate(timeout=10); _, erro_dois = segundo.communicate(timeout=10)
            self.assertEqual(sorted([primeiro.returncode, segundo.returncode]), [0, 3], (primeiro.returncode, erro_um, segundo.returncode, erro_dois))
            estado = json.loads((pasta / ".pacto" / "estado.json").read_text(encoding="utf-8"))
            self.assertEqual(estado["revisao"], 2)

    def test_d02_subpasta_resolve_raiz_e_hook(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); identificador = self.iniciar(pasta, "Raiz correta")
            (pasta / "src").mkdir()
            evento = json.dumps({"cwd": str(pasta / "src"), "session_id": "sessao_1"})
            hook = subprocess.run([sys.executable, str(HOOK)], input=evento, text=True, encoding="utf-8", capture_output=True, check=False)
            self.assertEqual(hook.returncode, 0, hook.stderr)
            self.assertIn(identificador, hook.stdout)
            self.assertIn("Raiz correta", hook.stdout)

    def test_hook_comando_com_caminho_de_espaco_e_acento(self):
        with tempfile.TemporaryDirectory(prefix="pacto espaço ç ") as diretorio:
            pasta = Path(diretorio); self.iniciar(pasta, "Acentuação")
            (pasta / "sub pasta").mkdir()
            hook = subprocess.run([sys.executable, str(HOOK)], input=json.dumps({"cwd": str(pasta / "sub pasta")}), text=True, encoding="utf-8", capture_output=True, check=False, env={**os.environ, "PYTHONUTF8": "1"})
            self.assertEqual(hook.returncode, 0, hook.stderr); self.assertIn("Acentuação", hook.stdout)

    def test_migracao_preserva_dados_e_formato_futuro_nao_grava(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); (pasta / ".pacto").mkdir()
            antigo = {"formato": 1, "revisao": 4, "atualizado_em": "2026-10-22T12:00:00Z", "trabalhos": [{"id": "legado", "titulo": "Legado", "objetivo": "Migrar", "situacao": "ativo", "decisoes": ["Manter API"], "ultimo_resultado": None, "tentativas_descartadas": ["Troca simples"], "bloqueio": None, "proximo_passo": "Migrar", "referencias": [], "atualizado_em": "2026-10-22T12:00:00Z"}]}
            arquivo = pasta / ".pacto" / "estado.json"; arquivo.write_text(json.dumps(antigo), encoding="utf-8")
            migrado = self.executar(pasta, "migrar", "--esperada-revisao", "4")
            self.assertEqual(migrado.returncode, 0, migrado.stderr)
            novo = json.loads(arquivo.read_text(encoding="utf-8"))
            self.assertEqual(novo["formato"], 2); self.assertEqual(novo["trabalhos"][0]["id"], "legado"); self.assertEqual(novo["trabalhos"][0]["decisoes"][0]["texto"], "Manter API")
            novo["formato"] = 99; antes = json.dumps(novo, ensure_ascii=False); arquivo.write_text(antes, encoding="utf-8")
            futuro = self.executar(pasta, "atualizar", "legado", "--resultado", "não pode", "--esperada-revisao", "5")
            self.assertEqual(futuro.returncode, 2)
            self.assertEqual(arquivo.read_text(encoding="utf-8"), antes)

    def test_sessoes_decisao_substituida_e_retorno(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); um = self.iniciar(pasta, "Um")
            dois_retorno = self.executar(pasta, "iniciar", "--titulo", "Dois", "--objetivo", "Alternar", "--proximo-passo", "Executar", "--esperada-revisao", "1")
            dois = json.loads(dois_retorno.stdout)["id"]
            a = self.executar(pasta, "associar", um, "--sessao", "s1", "--esperada-revisao", "2")
            self.assertEqual(a.returncode, 0, a.stderr)
            d1 = self.executar(pasta, "atualizar", um, "--decisao", "Primeira", "--fonte-decisao", "SPEC.md", "--esperada-revisao", "3")
            decisao = json.loads(self.executar(pasta, "mostrar", um).stdout)["decisoes"][0]["id"]
            d2 = self.executar(pasta, "atualizar", um, "--decisao", "Segunda", "--substitui-decisao", decisao, "--esperada-revisao", "4")
            troca = self.executar(pasta, "alternar", dois, "--sessao", "s1", "--esperada-revisao", "5")
            self.assertEqual(d1.returncode, 0); self.assertEqual(d2.returncode, 0); self.assertEqual(troca.returncode, 0, troca.stderr)
            contexto = self.executar(pasta, "contexto", "--sessao", "s1")
            self.assertIn("Dois", contexto.stdout)
            estado = json.loads((pasta / ".pacto" / "estado.json").read_text(encoding="utf-8"))
            self.assertEqual(estado["trabalhos"][0]["situacao"], "pausado")

    def test_schema_rejeita_ids_duplicados_sem_traceback(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio); self.iniciar(pasta)
            arquivo = pasta / ".pacto" / "estado.json"; dados = json.loads(arquivo.read_text(encoding="utf-8")); dados["trabalhos"].append(dict(dados["trabalhos"][0])); arquivo.write_text(json.dumps(dados), encoding="utf-8")
            retorno = self.executar(pasta, "listar")
            self.assertEqual(retorno.returncode, 2); self.assertIn("duplicado", retorno.stderr); self.assertNotIn("Traceback", retorno.stderr)

    def test_contexto_limite_e_ambiguidade(self):
        with tempfile.TemporaryDirectory() as diretorio:
            pasta = Path(diretorio)
            for numero in range(7):
                retorno = self.executar(pasta, "iniciar", "--titulo", f"T{numero}", "--objetivo", "O", "--proximo-passo", "P", "--esperada-revisao", str(numero))
                self.assertEqual(retorno.returncode, 0, retorno.stderr)
            contexto = self.executar(pasta, "contexto")
            self.assertIn("mais 2", contexto.stdout); self.assertLessEqual(len(contexto.stdout), 4000)


if __name__ == "__main__":
    unittest.main()
