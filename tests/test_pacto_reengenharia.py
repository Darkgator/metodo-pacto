"""Regressões das fronteiras reproduzidas na revisão arquitetural."""

import json
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path
from types import SimpleNamespace

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "scripts"))
import instalar_pacto as instalador
import pacto_estado as estado
import verificar_kit as kit


def trabalho():
    return estado._novo_trabalho(SimpleNamespace(titulo="Caso sintético", objetivo="Preservar a regra", situacao="ativo", proximo_passo="PRÓXIMO_PASSO_ESSENCIAL"))


class ReengenhariaPactoTest(unittest.TestCase):
    def test_d01_contratos_opcionais_e_remocao_preservadora(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            instalador.aplicar(raiz, "continuidade", "instalar")
            self.assertFalse((raiz / "BRIEF.md").exists())
            self.assertFalse((raiz / "SPEC.md").exists())
            contratos = ("BRIEF", "SPEC", "PLAN", "INVARIANTES")
            instalador.aplicar(raiz, "continuidade", "instalar", contratos)
            antes = {p: (raiz / p).read_bytes() for p in instalador.PROJETO}
            removidos, _ = instalador.remover(raiz)
            self.assertIn(".pacto/pacto-estado.py", removidos)
            self.assertEqual(antes, {p: (raiz / p).read_bytes() for p in antes})

    def test_d01_manifesto_antigo_nao_da_posse_dos_contratos(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            for nome in ("AGENTS.md", "CLAUDE.md", "BRIEF.md", "SPEC.md", "PLAN.md", "INVARIANTES.md"):
                (raiz / nome).write_text("Contrato preservado", encoding="utf-8")
            (raiz / ".pacto").mkdir()
            meta = {p.name: {"hash": instalador.sha(p)} for p in raiz.glob("*.md")}
            (raiz / ".pacto/instalacao.json").write_text(json.dumps({"arquivos": meta}), encoding="utf-8")
            removidos, preservados = instalador.remover(raiz)
            self.assertEqual(removidos, [])
            self.assertEqual(set(preservados), set(meta))

    def test_d02_adota_suporte_sem_sobrescrever_instrucoes(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "AGENTS.md").write_text("Instruções aprovadas do projeto", encoding="utf-8")
            acoes = instalador.aplicar(raiz, "continuidade", "instalar")
            self.assertEqual((raiz / "AGENTS.md").read_text(encoding="utf-8"), "Instruções aprovadas do projeto")
            self.assertTrue((raiz / ".pacto/validacao.md").exists())
            self.assertEqual(instalador.integracao_pendente(acoes), ["AGENTS.md"])

    def test_d03_atualizar_preserva_estado_usado(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            instalador.aplicar(raiz, "continuidade", "instalar")
            estado.mutar(raiz, 0, lambda dados: dados["trabalhos"].append(trabalho()))
            antes = (raiz / ".pacto/estado.json").read_bytes()
            instalador.aplicar(raiz, "continuidade", "atualizar")
            self.assertEqual((raiz / ".pacto/estado.json").read_bytes(), antes)

    def test_suporte_adaptado_continua_protegido(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            instalador.aplicar(raiz, "continuidade", "instalar")
            politica = raiz / ".pacto/validacao.md"
            politica.write_text("Política local", encoding="utf-8")
            with self.assertRaises(ValueError):
                instalador.aplicar(raiz, "continuidade", "atualizar")
            self.assertEqual(politica.read_text(encoding="utf-8"), "Política local")

    def test_falha_ao_gravar_manifesto_preserva_projeto_e_desfaz_criacoes(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            agentes = raiz / "AGENTS.md"
            agentes.write_text("Instruções locais intactas", encoding="utf-8")
            gravar = instalador.gravar
            def falhar_manifesto(caminho, conteudo):
                if caminho.name == "instalacao.json":
                    raise OSError("falha simulada de gravação")
                return gravar(caminho, conteudo)
            with mock.patch.object(instalador, "gravar", side_effect=falhar_manifesto):
                with self.assertRaises(OSError):
                    instalador.aplicar(raiz, "continuidade", "instalar", ("SPEC",))
            self.assertEqual(agentes.read_text(encoding="utf-8"), "Instruções locais intactas")
            self.assertEqual([p.relative_to(raiz).as_posix() for p in raiz.rglob("*") if p.is_file()], ["AGENTS.md"])

    def test_d04_kit_e_runtime_rejeitam_o_mesmo_estado(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            instalador.aplicar(raiz, "continuidade", "instalar")
            (raiz / ".pacto/estado.json").write_text(json.dumps({"formato": 2, "revisao": "inválida", "trabalhos": "inválido"}), encoding="utf-8")
            self.assertTrue(any("revisao" in erro for erro in kit.verificar_instalacao(raiz, True)))
            with self.assertRaises(estado.ErroPacto):
                estado.ler(raiz)

    def test_schema_recusa_tipos_invalidos_sem_excecao_interna(self):
        for campo in ("situacao", "resultado", "sessao"):
            with self.subTest(campo=campo):
                dados = estado.vazio(); t = trabalho(); dados["trabalhos"].append(t)
                if campo == "situacao": t["situacao"] = []
                if campo == "resultado": t["evidencias"] = [{"id": "invalida", "registrado_em": estado.agora(), "resultado": []}]
                if campo == "sessao": dados["sessoes"] = {"s1": []}
                with self.assertRaises(estado.ErroPacto):
                    estado.validar(dados)

    def test_d05_resumo_longo_preserva_acao_bloqueio_e_teto(self):
        t = trabalho()
        t["id"] = "i" * 64
        t["titulo"] = "T" * 160
        t["objetivo"] = "O" * 1000
        t["proximo_passo"] = "AÇÃO_" + "P" * 995
        t["bloqueio"] = "BLOQUEIO_" + "B" * 991
        t["decisoes"] = [{"id": f"d{i}", "texto": "D" * 1000, "substitui": None, "fonte": "SPEC.md", "registrado_em": estado.agora()} for i in range(5)]
        dados = estado.vazio(); dados["trabalhos"].append(t); estado.validar(dados)
        resumo = estado.resumo(t)
        self.assertLessEqual(len(resumo), estado.LIMITE_CONTEXTO)
        self.assertIn(t["proximo_passo"], resumo)
        self.assertIn(t["bloqueio"], resumo)
        self.assertIn("Resumo cortado", resumo)

    def test_d06_entrada_ausente_nao_executa_nem_aprova(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); t = trabalho()
            estado.registrar_prova(raiz, t, {"id": "ausente", "argv": [sys.executable, "-c", "from pathlib import Path; Path('executou').touch()"], "arquivos": ["nao-existe.txt"], "criterio": "Entrada obrigatória disponível"})
            prova = t["evidencias"][-1]
            self.assertEqual(prova["resultado"], "inconclusiva")
            self.assertIsNone(prova["codigo_saida"])
            self.assertTrue(estado.evidencia_vencida(raiz, prova))
            self.assertFalse((raiz / "executou").exists())

    def test_d07_entrada_alterada_durante_teste_fica_inconclusiva(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); t = trabalho()
            (raiz / "entrada.txt").write_text("ANTES", encoding="utf-8")
            estado.registrar_prova(raiz, t, {"id": "mutavel", "argv": [sys.executable, "-c", "from pathlib import Path; Path('entrada.txt').write_text('DEPOIS')"], "arquivos": ["entrada.txt"], "criterio": "Entrada examinada preservada"})
            prova = t["evidencias"][-1]
            self.assertEqual(prova["resultado"], "inconclusiva")
            self.assertTrue(estado.evidencia_vencida(raiz, prova))

    def test_saida_declarada_pode_ser_produzida_e_vence_se_mudar(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); t = trabalho()
            estado.registrar_prova(raiz, t, {"id": "saida", "argv": [sys.executable, "-c", "from pathlib import Path; p=Path('saida.txt'); p.write_text('ok'); assert p.read_text() == 'ok'"], "saidas": ["saida.txt"], "criterio": "Saída contém ok"})
            prova = t["evidencias"][-1]
            self.assertEqual(prova["resultado"], "passou")
            self.assertFalse(estado.evidencia_vencida(raiz, prova))
            (raiz / "saida.txt").write_text("errado", encoding="utf-8")
            self.assertTrue(estado.evidencia_vencida(raiz, prova))

    def test_saida_obrigatoria_ausente_reprova(self):
        with tempfile.TemporaryDirectory() as d:
            t = trabalho()
            estado.registrar_prova(Path(d), t, {"id": "sem-saida", "argv": [sys.executable, "-c", "pass"], "saidas": ["saida.txt"], "criterio": "Produzir arquivo"})
            self.assertEqual(t["evidencias"][-1]["resultado"], "falhou")

    def test_d08_stdout_e_stderr_nao_viram_memoria(self):
        with tempfile.TemporaryDirectory() as d:
            t = trabalho()
            estado.registrar_prova(Path(d), t, {"id": "canario", "argv": [sys.executable, "-c", "import sys; print('CREDENCIAL_FICTICIA_PACTO_123'); print('OUTRO_CANARIO_FICTICIO', file=sys.stderr)"]})
            serializado = json.dumps(t)
            self.assertNotIn("CREDENCIAL_FICTICIA_PACTO_123", serializado)
            self.assertNotIn("OUTRO_CANARIO_FICTICIO", serializado)
            self.assertEqual(t["evidencias"][-1]["resultado"], "executada")

    def test_ausencia_explicita_e_legado_sem_proveniencia(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); t = trabalho()
            estado.registrar_prova(raiz, t, {"id": "ausencia", "argv": [sys.executable, "-c", "from pathlib import Path; assert not Path('ausente.txt').exists()"], "ausentes": ["ausente.txt"], "criterio": "Arquivo permanece ausente"})
            prova = t["evidencias"][-1]
            self.assertEqual(prova["resultado"], "passou")
            self.assertFalse(estado.evidencia_vencida(raiz, prova))
            (raiz / "ausente.txt").touch()
            self.assertTrue(estado.evidencia_vencida(raiz, prova))
            self.assertTrue(estado.evidencia_vencida(raiz, {"resultado": "aprovada", "arquivos": {}}))

    def test_d09_publicacao_manual_distingue_pendencia_e_divergencia(self):
        pub = {"esperado": {"ambiente": "producao", "revisao": "abc123"}, "observado": {"ambiente": "producao", "revisao": None, "fonte": "informação manual"}, "divergente": False}
        self.assertEqual(estado.situacao_publicacao(pub), "pendente")
        pub["observado"]["revisao"] = "abc123"
        self.assertEqual(estado.situacao_publicacao(pub), "informada")
        pub["observado"]["ambiente"] = "homologacao"
        self.assertEqual(estado.situacao_publicacao(pub), "divergente")

    def test_verificacao_recusa_caminho_externo_e_papeis_ambiguos(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            with self.assertRaises(estado.ErroPacto):
                estado.registrar_prova(raiz, trabalho(), {"id": "escape", "argv": [sys.executable, "-c", "pass"], "saidas": ["../fora.txt"]})
            with self.assertRaises(estado.ErroPacto):
                estado.registrar_prova(raiz, trabalho(), {"id": "ambiguo", "argv": [sys.executable, "-c", "pass"], "arquivos": ["mesmo.txt"], "saidas": ["./mesmo.txt"]})


if __name__ == "__main__":
    unittest.main()
