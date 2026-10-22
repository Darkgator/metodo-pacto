import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
INSTALADOR = RAIZ / "scripts" / "instalar_pacto.py"


class InstalacaoPactoTest(unittest.TestCase):
    def rodar(self, destino, *argumentos):
        return subprocess.run([sys.executable, str(INSTALADOR), "--destino", str(destino), *argumentos], text=True, encoding="utf-8", capture_output=True, check=False, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1"})

    def test_previa_nao_escreve_e_instalacao_repetida(self):
        with tempfile.TemporaryDirectory() as diretorio:
            destino = Path(diretorio)
            previa = self.rodar(destino, "--perfil", "continuidade", "planejar")
            self.assertEqual(previa.returncode, 0, previa.stderr); self.assertFalse((destino / "AGENTS.md").exists())
            instalado = self.rodar(destino, "--perfil", "continuidade", "instalar", "--aplicar")
            self.assertEqual(instalado.returncode, 0, instalado.stderr); self.assertTrue((destino / ".pacto" / "estado.json").is_file())
            repetido = self.rodar(destino, "--perfil", "continuidade", "instalar", "--aplicar")
            self.assertEqual(repetido.returncode, 0, repetido.stderr)

    def test_preserva_alteracao_local_e_estado_na_remocao(self):
        with tempfile.TemporaryDirectory() as diretorio:
            destino = Path(diretorio)
            self.assertEqual(self.rodar(destino, "--perfil", "continuidade", "instalar", "--aplicar").returncode, 0)
            agentes = destino / "AGENTS.md"; agentes.write_text("adaptação local", encoding="utf-8")
            conflito = self.rodar(destino, "--perfil", "continuidade", "atualizar", "--aplicar")
            self.assertEqual(conflito.returncode, 2); self.assertEqual(agentes.read_text(encoding="utf-8"), "adaptação local")
            # Reinstalação limpa em outro destino para exercer remoção segura.
            outro = destino / "outro"; outro.mkdir()
            self.assertEqual(self.rodar(outro, "--perfil", "continuidade", "instalar", "--aplicar").returncode, 0)
            remover = self.rodar(outro, "remover", "--aplicar")
            self.assertEqual(remover.returncode, 0, remover.stderr)
            self.assertTrue((outro / ".pacto" / "estado.json").exists())


if __name__ == "__main__": unittest.main()
