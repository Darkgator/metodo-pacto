import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
ESTADO = RAIZ / "scripts" / "pacto_estado.py"
HOOK = RAIZ / "plugin-pacto" / "scripts" / "pacto_hook.py"
VERIFICADOR = RAIZ / "scripts" / "verificar_kit.py"


class EstadoPactoTest(unittest.TestCase):
    def executar(self, pasta, *argumentos):
        return subprocess.run(
            [sys.executable, str(ESTADO), "--raiz", str(pasta), *argumentos],
            text=True, capture_output=True, check=False,
        )

    def test_ciclo_e_contexto(self):
        with tempfile.TemporaryDirectory() as temporario:
            pasta = Path(temporario)
            criado = self.executar(pasta, "iniciar", "--titulo", "Corrigir acesso", "--objetivo", "Corrigir rota", "--proximo-passo", "Reproduzir")
            self.assertEqual(criado.returncode, 0, criado.stderr)
            retorno = json.loads(criado.stdout)
            atualizado = self.executar(pasta, "atualizar", retorno["id"], "--decisao", "Preservar RBAC", "--resultado", "Bug reproduzido", "--tentativa-descartada", "Troca de rótulo não altera permissão", "--referencia", "SPEC.md")
            self.assertEqual(atualizado.returncode, 0, atualizado.stderr)
            contexto = self.executar(pasta, "contexto")
            self.assertIn("Corrigir acesso", contexto.stdout)
            dados = json.loads((pasta / ".pacto" / "estado.json").read_text(encoding="utf-8"))
            self.assertEqual(dados["revisao"], 2)
            self.assertEqual(dados["trabalhos"][0]["decisoes"], ["Preservar RBAC"])

    def test_rejeita_revisao_concorrente(self):
        with tempfile.TemporaryDirectory() as temporario:
            pasta = Path(temporario)
            criado = self.executar(pasta, "iniciar", "--titulo", "A", "--objetivo", "B", "--proximo-passo", "C")
            trabalho = json.loads(criado.stdout)["id"]
            conflito = self.executar(pasta, "atualizar", trabalho, "--proximo-passo", "D", "--esperada-revisao", "0")
            self.assertEqual(conflito.returncode, 2)
            self.assertIn("conflito", conflito.stderr)

    def test_rejeita_escrita_enquanto_estado_esta_travado(self):
        with tempfile.TemporaryDirectory() as temporario:
            pasta = Path(temporario)
            criado = self.executar(pasta, "iniciar", "--titulo", "A", "--objetivo", "B", "--proximo-passo", "C")
            trabalho = json.loads(criado.stdout)["id"]
            trava = pasta / ".pacto" / "estado.json.lock"
            trava.write_text("ocupado", encoding="utf-8")
            ocupado = self.executar(pasta, "atualizar", trabalho, "--proximo-passo", "D")
            self.assertEqual(ocupado.returncode, 2)
            self.assertIn("ocupado", ocupado.stderr)

    def test_hook_so_ve_trabalhos_abertos(self):
        with tempfile.TemporaryDirectory() as temporario:
            pasta = Path(temporario)
            criado = self.executar(pasta, "iniciar", "--titulo", "Publicar", "--objetivo", "Produção", "--proximo-passo", "Conferir ambiente")
            trabalho = json.loads(criado.stdout)["id"]
            evento = json.dumps({"cwd": str(pasta), "hook_event_name": "SessionStart"})
            hook = subprocess.run([sys.executable, str(HOOK)], input=evento, text=True, capture_output=True, check=False)
            self.assertEqual(hook.returncode, 0, hook.stderr)
            self.assertIn("Publicar", hook.stdout)
            fechado = self.executar(pasta, "atualizar", trabalho, "--situacao", "concluido")
            self.assertEqual(fechado.returncode, 0, fechado.stderr)
            hook = subprocess.run([sys.executable, str(HOOK)], input=evento, text=True, capture_output=True, check=False)
            self.assertEqual(hook.stdout, "")

    def test_kit_rejeita_estado_corrompido(self):
        with tempfile.TemporaryDirectory() as temporario:
            destino = Path(temporario) / "kit"
            shutil.copytree(RAIZ / "kit-pacto" / "PARA-COPIAR-NA-RAIZ", destino)
            (destino / ".pacto" / "estado.json").write_text("{", encoding="utf-8")
            resultado = subprocess.run(
                [sys.executable, str(VERIFICADOR), "--instalacao", str(destino)],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(resultado.returncode, 1)
            self.assertIn("Estado PACTO", resultado.stdout)
            self.assertIn("JSON", resultado.stdout)


if __name__ == "__main__":
    unittest.main()
