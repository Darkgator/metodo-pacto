"""Estado local, concorrente e limitado dos trabalhos PACTO.

O arquivo ``.pacto/estado.json`` é uma ajuda de continuidade, não uma
transcrição, autorização ou mecanismo de implantação. Todas as mutações usam
comparação de revisão dentro de uma trava do sistema operacional.
"""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

FORMATO = 2
LIMITE_ESTADO = 256 * 1024
LIMITE_CONTEXTO = 4000
SITUACOES = {"ativo", "pausado", "aguardando-usuario", "concluido"}
ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")


class ErroPacto(Exception):
    codigo = 2


class Conflito(ErroPacto):
    codigo = 3



class Ocupado(ErroPacto):
    codigo = 4


class ErroIO(ErroPacto):
    codigo = 5


def agora() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def vazio() -> dict:
    return {"formato": FORMATO, "revisao": 0, "atualizado_em": None, "trabalhos": [], "sessoes": {}}


def caminho_estado(raiz: Path) -> Path:
    return raiz / ".pacto" / "estado.json"


def _dentro(raiz: Path, caminho: Path) -> bool:
    try:
        caminho.resolve(strict=False).relative_to(raiz.resolve())
        return True
    except ValueError:
        return False


def validar_raiz(raiz: Path, criar: bool = False) -> Path:
    raiz = raiz.expanduser().resolve(strict=False)
    if not raiz.exists() or not raiz.is_dir():
        raise ErroPacto(f"raiz inválida: {raiz}")
    if criar and not _dentro(raiz, caminho_estado(raiz)):
        raise ErroPacto("recusa: .pacto aponta para fora da raiz do projeto")
    return raiz


def localizar_raiz(inicio: Path) -> Path | None:
    """Encontra a instalação mais próxima sem cruzar a fronteira Git."""
    atual = inicio.expanduser().resolve()
    while True:
        if (atual / ".pacto" / "estado.json").is_file():
            return atual
        if (atual / ".git").exists():
            return None
        if atual.parent == atual:
            return None
        atual = atual.parent


def resolver_raiz(valor: Path | None, mutacao: bool = False) -> Path | None:
    if valor is not None:
        return validar_raiz(valor, criar=mutacao)
    raiz = localizar_raiz(Path.cwd())
    if raiz is None and mutacao:
        raise ErroPacto("estado ausente: informe --raiz para iniciar ou migrar um projeto")
    return raiz


def _tipo_texto(valor, caminho: str, obrigatorio: bool = False, limite: int = 1000, nulo: bool = True):
    if valor is None and nulo:
        return
    if not isinstance(valor, str) or (obrigatorio and not valor.strip()) or len(valor) > limite:
        regra = "texto não vazio" if obrigatorio else "texto ou null"
        raise ErroPacto(f"{caminho}: esperado {regra} com até {limite} caracteres")


def _id(valor, caminho: str):
    if not isinstance(valor, str) or not ID_RE.fullmatch(valor):
        raise ErroPacto(f"{caminho}: identificador inválido")


def _instante(valor, caminho: str, nulo: bool = False):
    if valor is None and nulo:
        return
    if not isinstance(valor, str) or not valor.endswith("Z"):
        raise ErroPacto(f"{caminho}: instante UTC inválido")
    try:
        datetime.fromisoformat(valor[:-1] + "+00:00")
    except ValueError as erro:
        raise ErroPacto(f"{caminho}: instante UTC inválido") from erro


def _validar_trabalho(t: dict, indice: int):
    p = f"trabalhos[{indice}]"
    if not isinstance(t, dict):
        raise ErroPacto(f"{p}: esperado objeto")
    _id(t.get("id"), f"{p}.id")
    _tipo_texto(t.get("titulo"), f"{p}.titulo", True, 160, False)
    _tipo_texto(t.get("objetivo"), f"{p}.objetivo", True, 1000, False)
    if not isinstance(t.get("situacao"), str) or t["situacao"] not in SITUACOES:
        raise ErroPacto(f"{p}.situacao: situação inválida")
    _tipo_texto(t.get("proximo_passo"), f"{p}.proximo_passo", True, 1000, False)
    for campo in ("bloqueio", "ultimo_resultado"):
        _tipo_texto(t.get(campo), f"{p}.{campo}", False, 1000)
    _instante(t.get("atualizado_em"), f"{p}.atualizado_em")
    for campo in ("decisoes", "tentativas_descartadas", "referencias", "evidencias"):
        if not isinstance(t.get(campo), list):
            raise ErroPacto(f"{p}.{campo}: esperado lista")
    ids = set()
    for j, decisao in enumerate(t["decisoes"]):
        q = f"{p}.decisoes[{j}]"
        if not isinstance(decisao, dict):
            raise ErroPacto(f"{q}: esperado objeto")
        _id(decisao.get("id"), f"{q}.id")
        if decisao["id"] in ids:
            raise ErroPacto(f"{q}.id: decisão duplicada")
        ids.add(decisao["id"])
        _tipo_texto(decisao.get("texto"), f"{q}.texto", True, 1000, False)
        if decisao.get("substitui") is not None:
            _id(decisao["substitui"], f"{q}.substitui")
            if decisao["substitui"] not in ids:
                raise ErroPacto(f"{q}.substitui: decisão anterior inexistente")
        _tipo_texto(decisao.get("fonte"), f"{q}.fonte", False, 1000)
        _instante(decisao.get("registrado_em"), f"{q}.registrado_em")
    ids = set()
    for j, tentativa in enumerate(t["tentativas_descartadas"]):
        q = f"{p}.tentativas_descartadas[{j}]"
        if not isinstance(tentativa, dict):
            raise ErroPacto(f"{q}: esperado objeto")
        _id(tentativa.get("id"), f"{q}.id")
        if tentativa["id"] in ids:
            raise ErroPacto(f"{q}.id: tentativa duplicada")
        ids.add(tentativa["id"])
        _tipo_texto(tentativa.get("hipotese"), f"{q}.hipotese", True, 1000, False)
        _tipo_texto(tentativa.get("resultado"), f"{q}.resultado", True, 1000, False)
        _instante(tentativa.get("registrado_em"), f"{q}.registrado_em")
    for j, ref in enumerate(t["referencias"]):
        _tipo_texto(ref, f"{p}.referencias[{j}]", True, 1000, False)
    for j, evidencia in enumerate(t["evidencias"]):
        q = f"{p}.evidencias[{j}]"
        if not isinstance(evidencia, dict):
            raise ErroPacto(f"{q}: esperado objeto")
        _id(evidencia.get("id"), f"{q}.id")
        _instante(evidencia.get("registrado_em"), f"{q}.registrado_em")
        if not isinstance(evidencia.get("resultado"), str) or evidencia["resultado"] not in {"aprovada", "executada", "passou", "falhou", "inconclusiva", "nao_executada"}:
            raise ErroPacto(f"{q}.resultado: inválido")
        for campo in ("arquivos", "saidas"):
            hashes = evidencia.get(campo, {})
            if not isinstance(hashes, dict) or any(not isinstance(k, str) or (v is not None and (not isinstance(v, str) or not re.fullmatch(r"[0-9a-f]{64}", v))) for k, v in hashes.items()):
                raise ErroPacto(f"{q}.{campo}: hashes inválidos")
        ausentes = evidencia.get("ausentes", [])
        if not isinstance(ausentes, list) or not all(isinstance(x, str) for x in ausentes):
            raise ErroPacto(f"{q}.ausentes: esperado lista de caminhos")
    pub = t.get("publicacao")
    if pub is not None:
        if not isinstance(pub, dict):
            raise ErroPacto(f"{p}.publicacao: esperado objeto ou null")
        for campo in ("esperado", "observado"):
            parte = pub.get(campo, {})
            if not isinstance(parte, dict):
                raise ErroPacto(f"{p}.publicacao.{campo}: esperado objeto")
            for chave in ("ambiente", "revisao", "fonte"):
                _tipo_texto(parte.get(chave), f"{p}.publicacao.{campo}.{chave}")


def validar(dados: dict, aceitar_v1: bool = False):
    if not isinstance(dados, dict):
        raise ErroPacto("raiz: esperado objeto JSON")
    formato = dados.get("formato")
    if formato == 1 and aceitar_v1:
        if not isinstance(dados.get("trabalhos"), list):
            raise ErroPacto("trabalhos: esperado lista")
        return
    if formato != FORMATO:
        raise ErroPacto("formato: incompatível; preserve o arquivo e use migrador compatível")
    revisao = dados.get("revisao")
    if isinstance(revisao, bool) or not isinstance(revisao, int) or revisao < 0:
        raise ErroPacto("revisao: esperado inteiro não negativo")
    _instante(dados.get("atualizado_em"), "atualizado_em", True)
    if not isinstance(dados.get("trabalhos"), list):
        raise ErroPacto("trabalhos: esperado lista")
    if not isinstance(dados.get("sessoes"), dict):
        raise ErroPacto("sessoes: esperado objeto")
    ids = set()
    for i, t in enumerate(dados["trabalhos"]):
        _validar_trabalho(t, i)
        if t["id"] in ids:
            raise ErroPacto(f"trabalhos[{i}].id: trabalho duplicado")
        ids.add(t["id"])
    for sessao, trabalho in dados["sessoes"].items():
        _id(sessao, f"sessoes.{sessao}")
        _id(trabalho, f"sessoes.{sessao}.trabalho")
        if trabalho not in ids:
            raise ErroPacto(f"sessoes.{sessao}: trabalho inexistente")
    bruto = json.dumps(dados, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    if len(bruto) > LIMITE_ESTADO:
        raise ErroPacto(f"estado excede o limite de {LIMITE_ESTADO} bytes; mova detalhes para referências")


def ler(raiz: Path, aceitar_v1: bool = True) -> dict:
    arquivo = caminho_estado(raiz)
    if not arquivo.exists():
        return vazio()
    if not _dentro(raiz, arquivo):
        raise ErroPacto("recusa: estado aponta para fora da raiz do projeto")
    try:
        # No Windows, os.replace pode manter uma janela curtíssima de acesso
        # negado para outro processo. Releia o arquivo, nunca um snapshot.
        for tentativa in range(100):
            try:
                tamanho = arquivo.stat().st_size
                bruto = arquivo.read_text(encoding="utf-8")
                break
            except PermissionError:
                if tentativa == 99:
                    raise
                time.sleep(0.03)
        if tamanho > LIMITE_ESTADO:
            raise ErroPacto(f"estado excede o limite de {LIMITE_ESTADO} bytes")
        dados = json.loads(bruto)
    except ErroPacto:
        raise
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as erro:
        raise ErroPacto(f"estado ilegível: {arquivo} ({erro})") from erro
    validar(dados, aceitar_v1=aceitar_v1)
    return dados


@contextmanager
def trava(raiz: Path, timeout: float = 3.0):
    pasta = raiz / ".pacto"
    if pasta.exists() and not _dentro(raiz, pasta):
        raise ErroPacto("recusa: .pacto aponta para fora da raiz do projeto")
    pasta.mkdir(parents=True, exist_ok=True)
    arquivo = pasta / "estado.lock"
    try:
        handle = open(arquivo, "a+b")
    except OSError as erro:
        raise ErroIO(f"não foi possível abrir trava: {erro}") from erro
    mutex = None
    try:
        prazo = time.monotonic() + timeout
        if os.name == "nt":
            # locking() por byte não bloqueou consistentemente entre processos
            # neste runtime Windows. O mutex nomeado é uma primitiva do SO e
            # cobre a seção crítica inteira; estado.lock continua persistente.
            nome = "Local\\PACTO-" + hashlib.sha256(str(raiz).encode("utf-8")).hexdigest()
            mutex = ctypes.windll.kernel32.CreateMutexW(None, False, nome)
            if not mutex:
                raise ErroIO("não foi possível criar mutex de estado")
            resultado = ctypes.windll.kernel32.WaitForSingleObject(mutex, int(timeout * 1000))
            if resultado not in (0, 0x80):
                raise Ocupado("estado ocupado por outra atualização; releia e reconcilie")
            yield
            return
        while True:
            try:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except (BlockingIOError, OSError):
                if time.monotonic() >= prazo:
                    raise Ocupado("estado ocupado por outra atualização; releia e reconcilie")
                time.sleep(0.03)
        yield
    finally:
        try:
            if os.name == "nt" and mutex:
                ctypes.windll.kernel32.ReleaseMutex(mutex)
                ctypes.windll.kernel32.CloseHandle(mutex)
            elif os.name != "nt":
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        except OSError:
            pass
        handle.close()


def _escrever(arquivo: Path, dados: dict):
    temporario = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=arquivo.parent, delete=False, suffix=".tmp") as temp:
            json.dump(dados, temp, ensure_ascii=False, indent=2)
            temp.write("\n"); temp.flush(); os.fsync(temp.fileno())
            temporario = Path(temp.name)
        for tentativa in range(100):
            try:
                os.replace(temporario, arquivo)
                temporario = None
                break
            except PermissionError:
                if tentativa == 99:
                    raise
                time.sleep(0.03)
    except OSError as erro:
        raise ErroIO(f"não foi possível gravar estado: {erro}") from erro
    finally:
        if temporario is not None:
            try: temporario.unlink()
            except OSError: pass


def mutar(raiz: Path, esperada: int | None, operacao):
    if esperada is None or isinstance(esperada, bool) or esperada < 0:
        raise ErroPacto("--esperada-revisao é obrigatório e deve ser inteiro não negativo")
    with trava(raiz):
        dados = ler(raiz, aceitar_v1=False)
        if dados["revisao"] != esperada:
            raise Conflito(f"conflito: revisão atual {dados['revisao']}, esperada {esperada}")
        resultado = operacao(dados)
        validar(dados); dados["revisao"] += 1; dados["atualizado_em"] = agora(); validar(dados)
        _escrever(caminho_estado(raiz), dados)
        return dados, resultado


def localizar(dados: dict, identificador: str) -> dict:
    for trabalho in dados["trabalhos"]:
        if trabalho["id"] == identificador: return trabalho
    raise ErroPacto(f"trabalho inexistente: {identificador}")


def _novo_trabalho(args) -> dict:
    instante = agora()
    return {"id": uuid4().hex, "titulo": args.titulo, "objetivo": args.objetivo, "situacao": args.situacao, "proximo_passo": args.proximo_passo, "bloqueio": None, "ultimo_resultado": None, "decisoes": [], "tentativas_descartadas": [], "referencias": [], "evidencias": [], "publicacao": None, "atualizado_em": instante}


def migrar_v1(dados: dict) -> dict:
    if dados.get("formato") != 1: return dados
    convertido = {"formato": FORMATO, "revisao": dados.get("revisao", 0), "atualizado_em": dados.get("atualizado_em"), "trabalhos": [], "sessoes": {}}
    for anterior in dados["trabalhos"]:
        t = dict(anterior); instante = t.get("atualizado_em") or agora()
        t.setdefault("id", uuid4().hex); t.setdefault("titulo", "Trabalho sem título"); t.setdefault("objetivo", "Definir objetivo"); t.setdefault("situacao", "ativo"); t.setdefault("proximo_passo", "Definir próximo passo"); t.setdefault("bloqueio", None); t.setdefault("ultimo_resultado", None)
        t["decisoes"] = [{"id": uuid4().hex, "texto": x, "substitui": None, "fonte": None, "registrado_em": instante} if isinstance(x, str) else x for x in t.get("decisoes", [])]
        t["tentativas_descartadas"] = [{"id": uuid4().hex, "hipotese": x, "resultado": "Descartada", "registrado_em": instante} if isinstance(x, str) else x for x in t.get("tentativas_descartadas", [])]
        t.setdefault("referencias", []); t.setdefault("evidencias", []); t.setdefault("publicacao", None); t["atualizado_em"] = instante
        convertido["trabalhos"].append(t)
    return convertido


def decisoes_vigentes(trabalho: dict) -> list[dict]:
    substituidas = {d["substitui"] for d in trabalho["decisoes"] if d.get("substitui")}
    return [d for d in trabalho["decisoes"] if d["id"] not in substituidas]


def resumo(trabalho: dict) -> str:
    # Campos necessários à retomada vêm antes de histórico e detalhes.
    linhas = [f"PACTO [{trabalho['id']}] {trabalho['situacao']}: {trabalho['titulo']}", f"Próximo passo: {trabalho['proximo_passo']}"]
    if trabalho.get("bloqueio"): linhas.append(f"Bloqueio: {trabalho['bloqueio']}")
    linhas.append(f"Objetivo: {trabalho['objetivo']}")
    if trabalho.get("ultimo_resultado"): linhas.append(f"Último resultado: {trabalho['ultimo_resultado']}")
    vigentes = decisoes_vigentes(trabalho)
    if vigentes: linhas.append("Decisões vigentes: " + "; ".join(d["texto"] for d in vigentes))
    if trabalho["tentativas_descartadas"]:
        t = trabalho["tentativas_descartadas"][-1]; linhas.append(f"Tentativa descartada: {t['hipotese']} ({t['resultado']})")
    if trabalho["referencias"]: linhas.append("Referências: " + ", ".join(trabalho["referencias"]))
    texto = "\n".join(linhas)
    aviso = "\n[Resumo cortado; use mostrar " + trabalho["id"] + ".]"
    return texto if len(texto) <= LIMITE_CONTEXTO else texto[:LIMITE_CONTEXTO - len(aviso)].rstrip() + aviso


def contexto(dados: dict, sessao: str | None = None) -> str:
    if dados.get("formato") == 1: return "PACTO: estado no formato 1; migre explicitamente antes de registrar alterações."
    if sessao and sessao in dados["sessoes"]: return resumo(localizar(dados, dados["sessoes"][sessao]))
    abertos = [t for t in dados["trabalhos"] if t["situacao"] != "concluido"]
    if not abertos: return "PACTO: sem trabalho persistido em aberto."
    linhas = ["PACTO: escolha explicitamente o trabalho para esta sessão:"] + [f"- [{t['id']}] {t['situacao']}: {t['titulo']}" for t in abertos[:5]]
    if len(abertos) > 5: linhas.append(f"- e mais {len(abertos) - 5} trabalho(s); use listar ou mostrar ID.")
    return "\n".join(linhas)


def _sha256(caminho: Path) -> str | None:
    if not caminho.is_file(): return None
    h = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(65536), b""): h.update(bloco)
    return h.hexdigest()


def carregar_verificacoes(arquivo: Path) -> dict:
    try: bruto = json.loads(arquivo.read_text(encoding="utf-8"))
    except FileNotFoundError as erro: raise ErroPacto("configuração de verificações ausente") from erro
    except (OSError, UnicodeError, json.JSONDecodeError) as erro: raise ErroPacto(f"configuração de verificações inválida: {erro}") from erro
    itens = bruto.get("verificacoes") if isinstance(bruto, dict) else bruto
    if not isinstance(itens, list): raise ErroPacto("verificacoes: esperado lista")
    resultado = {}
    for item in itens:
        validar_verificacao(item)
        if item["id"] in resultado: raise ErroPacto(f"verificação duplicada: {item['id']}")
        resultado[item["id"]] = item
    return resultado


def validar_verificacao(item: dict):
    if not isinstance(item, dict) or not isinstance(item.get("argv"), list) or not item["argv"] or not all(isinstance(x, str) and x for x in item["argv"]):
        raise ErroPacto("verificação: id e argv de texto são obrigatórios")
    _id(item.get("id"), "verificação.id")
    timeout = item.get("timeout", 30)
    if isinstance(timeout, bool) or not isinstance(timeout, int) or timeout <= 0:
        raise ErroPacto("verificação.timeout: esperado inteiro positivo")
    _tipo_texto(item.get("criterio"), "verificação.criterio", True)
    caminhos = []
    for campo in ("arquivos", "saidas", "ausentes"):
        valores = item.get(campo, [])
        if not isinstance(valores, list) or not all(isinstance(x, str) and x.strip() for x in valores):
            raise ErroPacto(f"verificação.{campo}: esperado lista de caminhos")
        caminhos.extend(valores)
    normalizados = [os.path.normcase(os.path.normpath(p)) for p in caminhos]
    if len(normalizados) != len(set(normalizados)):
        raise ErroPacto("verificação: caminho duplicado ou com papéis incompatíveis")


def caminho_prova(raiz: Path, relativo: str) -> Path:
    caminho = raiz / relativo
    if Path(relativo).is_absolute() or not _dentro(raiz, caminho):
        raise ErroPacto("verificação: caminho deve permanecer dentro do projeto")
    return caminho


def registrar_prova(raiz: Path, trabalho: dict, item: dict):
    validar_verificacao(item)
    entradas = {p: _sha256(caminho_prova(raiz, p)) for p in item.get("arquivos", [])}
    ausentes = item.get("ausentes", [])
    for p in [*item.get("saidas", []), *ausentes]: caminho_prova(raiz, p)
    codigo = None
    if any(h is None for h in entradas.values()):
        estado, mensagem = "inconclusiva", "entrada obrigatória ausente; comando não executado"
    elif any(caminho_prova(raiz, p).exists() for p in ausentes):
        estado, mensagem = "falhou", "ausência esperada não observada; comando não executado"
    else:
        try:
            # Saída arbitrária não vira memória nem precisa caber em RAM.
            retorno = subprocess.run(item["argv"], cwd=raiz, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=item.get("timeout", 30), check=False)
            codigo = retorno.returncode
            estado = "falhou" if codigo else ("passou" if item.get("criterio") else "executada")
            mensagem = f"retorno {codigo}; " + ("verificação configurada" if item.get("criterio") else "suficiência não declarada")
            if any(_sha256(caminho_prova(raiz, p)) != h for p, h in entradas.items()):
                estado, mensagem = "inconclusiva", "entrada mudou durante a execução"
            elif not codigo and any(not caminho_prova(raiz, p).is_file() for p in item.get("saidas", [])):
                estado, mensagem = "falhou", "saída obrigatória ausente"
            elif not codigo and any(caminho_prova(raiz, p).exists() for p in ausentes):
                estado, mensagem = "falhou", "ausência esperada não preservada"
        except FileNotFoundError: estado, mensagem = "nao_executada", "comando não encontrado"
        except subprocess.TimeoutExpired: estado, mensagem = "falhou", "tempo limite excedido"
        except OSError: estado, mensagem = "nao_executada", "comando indisponível"
    trabalho["evidencias"].append({"formato": 2, "id": item["id"], "tipo": "automatizada", "registrado_em": agora(), "resultado": estado, "codigo_saida": codigo, "criterio": item.get("criterio"), "resumo": mensagem, "arquivos": entradas, "saidas": {p: _sha256(caminho_prova(raiz, p)) for p in item.get("saidas", [])}, "ausentes": ausentes})


def evidencia_vencida(raiz: Path, evidencia: dict) -> bool:
    # Registros antigos são preservados, mas não ganham proveniência retroativa.
    if evidencia.get("formato") != 2: return True
    hashes = {**evidencia.get("arquivos", {}), **evidencia.get("saidas", {})}
    return any(h is None or _sha256(caminho_prova(raiz, p)) != h for p, h in hashes.items()) or any(caminho_prova(raiz, p).exists() for p in evidencia.get("ausentes", []))


def situacao_publicacao(publicacao: dict | None) -> str:
    if not publicacao: return "nao_registrada"
    esperado, observado = publicacao.get("esperado", {}), publicacao.get("observado", {})
    for campo in ("ambiente", "revisao"):
        if esperado.get(campo) and observado.get(campo) and esperado[campo] != observado[campo]:
            return "divergente"
    if not esperado.get("ambiente") or not observado.get("ambiente") or not observado.get("fonte"):
        return "pendente"
    if esperado.get("revisao") and not observado.get("revisao"):
        return "pendente"
    # Este comando recebe observações manuais, não consulta o ambiente remoto.
    return "informada"


def _emitir(valor, json_saida: bool = False):
    if json_saida or not isinstance(valor, str): print(json.dumps(valor, ensure_ascii=False, indent=2))
    else: print(valor)


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("--raiz", type=Path); p.add_argument("--json", action="store_true", dest="json_saida"); sub = p.add_subparsers(dest="comando", required=True)
    x = sub.add_parser("listar"); x.add_argument("--abertos", action="store_true")
    x = sub.add_parser("mostrar"); x.add_argument("id")
    x = sub.add_parser("contexto"); x.add_argument("--sessao")
    sub.add_parser("diagnosticar")
    x = sub.add_parser("iniciar"); x.add_argument("--titulo", required=True); x.add_argument("--objetivo", required=True); x.add_argument("--proximo-passo", required=True); x.add_argument("--situacao", choices=sorted(SITUACOES), default="ativo"); x.add_argument("--esperada-revisao", required=True, type=int)
    x = sub.add_parser("atualizar"); x.add_argument("id"); x.add_argument("--objetivo"); x.add_argument("--situacao", choices=sorted(SITUACOES)); x.add_argument("--decisao"); x.add_argument("--fonte-decisao"); x.add_argument("--substitui-decisao"); x.add_argument("--resultado"); x.add_argument("--tentativa-descartada"); x.add_argument("--resultado-tentativa", default="Descartada"); x.add_argument("--bloqueio"); x.add_argument("--limpar-bloqueio", action="store_true"); x.add_argument("--proximo-passo"); x.add_argument("--referencia", action="append"); x.add_argument("--esperada-revisao", required=True, type=int)
    for nome in ("associar", "alternar"):
        x = sub.add_parser(nome); x.add_argument("id"); x.add_argument("--sessao", required=True); x.add_argument("--reabrir", action="store_true"); x.add_argument("--esperada-revisao", required=True, type=int)
    x = sub.add_parser("migrar"); x.add_argument("--esperada-revisao", required=True, type=int)
    x = sub.add_parser("verificar"); x.add_argument("id")
    x = sub.add_parser("provar"); x.add_argument("id"); x.add_argument("--config", type=Path); x.add_argument("--verificacao", action="append", required=True); x.add_argument("--esperada-revisao", required=True, type=int)
    x = sub.add_parser("registrar-publicacao"); x.add_argument("id"); x.add_argument("--esperado-ambiente", required=True); x.add_argument("--observado-ambiente", required=True); x.add_argument("--esperada-revisao-publicada"); x.add_argument("--observada-revisao-publicada"); x.add_argument("--fonte", required=True); x.add_argument("--esperada-revisao", required=True, type=int)
    return p


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
    args = _parser().parse_args(); mutacoes = {"iniciar", "atualizar", "associar", "alternar", "migrar", "provar", "registrar-publicacao"}
    try:
        raiz = resolver_raiz(args.raiz, args.comando in mutacoes)
        if raiz is None: _emitir("PACTO: estado local ausente.", args.json_saida); return 0
        if args.comando == "migrar":
            with trava(raiz):
                antigo = ler(raiz, aceitar_v1=True)
                if antigo.get("formato") == FORMATO: _emitir({"migrado": False, "revisao": antigo["revisao"]}, args.json_saida); return 0
                if antigo.get("revisao", 0) != args.esperada_revisao: raise Conflito(f"conflito: revisão atual {antigo.get('revisao', 0)}, esperada {args.esperada_revisao}")
                dados = migrar_v1(antigo); validar(dados); dados["revisao"] += 1; dados["atualizado_em"] = agora(); _escrever(caminho_estado(raiz), dados); _emitir({"migrado": True, "revisao": dados["revisao"]}, args.json_saida); return 0
        dados = ler(raiz, aceitar_v1=True)
        if args.comando == "listar": _emitir({"revisao": dados.get("revisao", 0), "trabalhos": [t for t in dados["trabalhos"] if not args.abertos or t.get("situacao") != "concluido"]}, True); return 0
        if args.comando == "mostrar": _emitir(localizar(dados, args.id), True); return 0
        if args.comando == "contexto": _emitir(contexto(dados, args.sessao), args.json_saida); return 0
        if args.comando == "diagnosticar": _emitir({"raiz": str(raiz), "estado": str(caminho_estado(raiz)), "presente": caminho_estado(raiz).exists(), "formato": dados.get("formato"), "runtime": sys.version.split()[0]}, True); return 0
        if dados.get("formato") != FORMATO: raise ErroPacto("formato 1 requer migrar explicitamente antes de alterar")
        if args.comando == "verificar":
            t = localizar(dados, args.id); publicacao = situacao_publicacao(t.get("publicacao")); _emitir({"id": t["id"], "evidencias": [{**e, "vencida": evidencia_vencida(raiz, e)} for e in t["evidencias"]], "publicacao_situacao": publicacao, "publicacao_divergente": publicacao == "divergente", "publicacao_confirmada_automaticamente": False, "situacao": t["situacao"]}, True); return 0
        if args.comando == "iniciar":
            def op(d): t = _novo_trabalho(args); d["trabalhos"].append(t); return t["id"]
            novo, identificador = mutar(raiz, args.esperada_revisao, op); _emitir({"id": identificador, "revisao": novo["revisao"]}, args.json_saida); return 0
        if args.comando == "atualizar":
            def op(d):
                t = localizar(d, args.id)
                for campo in ("objetivo", "situacao", "bloqueio", "proximo_passo"):
                    valor = getattr(args, campo)
                    if valor is not None: t[campo] = valor
                if args.limpar_bloqueio: t["bloqueio"] = None
                if args.decisao: t["decisoes"].append({"id": uuid4().hex, "texto": args.decisao, "substitui": args.substitui_decisao, "fonte": args.fonte_decisao, "registrado_em": agora()})
                if args.resultado: t["ultimo_resultado"] = args.resultado
                if args.tentativa_descartada: t["tentativas_descartadas"].append({"id": uuid4().hex, "hipotese": args.tentativa_descartada, "resultado": args.resultado_tentativa, "registrado_em": agora()})
                for r in args.referencia or []:
                    if r not in t["referencias"]: t["referencias"].append(r)
                t["atualizado_em"] = agora(); return t["id"]
            novo, identificador = mutar(raiz, args.esperada_revisao, op); _emitir({"id": identificador, "revisao": novo["revisao"]}, args.json_saida); return 0
        if args.comando in {"associar", "alternar"}:
            def op(d):
                t = localizar(d, args.id)
                if t["situacao"] == "concluido" and not args.reabrir: raise ErroPacto("trabalho concluído exige --reabrir")
                if args.reabrir: t["situacao"] = "ativo"
                anterior = d["sessoes"].get(args.sessao)
                if args.comando == "alternar" and anterior and anterior != t["id"] and not any(s != args.sessao and w == anterior for s, w in d["sessoes"].items()): localizar(d, anterior)["situacao"] = "pausado"
                d["sessoes"][args.sessao] = t["id"]; return t["id"]
            novo, identificador = mutar(raiz, args.esperada_revisao, op); _emitir({"id": identificador, "revisao": novo["revisao"]}, args.json_saida); return 0
        if args.comando == "provar":
            configuracao = carregar_verificacoes(args.config or raiz / ".pacto" / "verificacoes.json")
            def op(d):
                t = localizar(d, args.id)
                for identificador in args.verificacao:
                    if identificador not in configuracao: raise ErroPacto(f"verificação inexistente: {identificador}")
                    registrar_prova(raiz, t, configuracao[identificador])
                return t["id"]
            novo, identificador = mutar(raiz, args.esperada_revisao, op)
            provas = localizar(novo, identificador)["evidencias"][-len(args.verificacao):]
            _emitir({"id": identificador, "revisao": novo["revisao"], "evidencias": provas}, True)
            return 0 if all(e["resultado"] in {"passou", "executada"} for e in provas) else 1
        if args.comando == "registrar-publicacao":
            def op(d):
                t = localizar(d, args.id)
                t["publicacao"] = {"modo": "informacao_manual", "esperado": {"ambiente": args.esperado_ambiente, "revisao": args.esperada_revisao_publicada}, "observado": {"ambiente": args.observado_ambiente, "revisao": args.observada_revisao_publicada, "fonte": args.fonte, "registrado_em": agora()}}; return t["id"]
            novo, identificador = mutar(raiz, args.esperada_revisao, op); _emitir({"id": identificador, "revisao": novo["revisao"]}, args.json_saida); return 0
        raise ErroPacto("comando desconhecido")
    except ErroPacto as erro:
        print(f"FALHOU: {erro}", file=sys.stderr); return erro.codigo


if __name__ == "__main__": raise SystemExit(main())
