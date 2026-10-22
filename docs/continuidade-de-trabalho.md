# Continuidade de trabalho

Use a continuidade apenas quando uma tarefa relevante precisa sobreviver à troca de assunto, sessão ou compactação. Ela não é briefing novo e não é obrigatória para pergunta ou tarefa trivial.

## Uso mínimo

```powershell
python .pacto/pacto-estado.py contexto --sessao minha-sessao
python .pacto/pacto-estado.py mostrar ID
```

Se não houver trabalho associado, o contexto mostra até cinco opções e não escolhe sozinho. Associe ou alterne explicitamente usando a revisão mostrada por `listar`:

```powershell
python .pacto/pacto-estado.py associar ID --sessao minha-sessao --esperada-revisao 3
python .pacto/pacto-estado.py atualizar ID --resultado "Teste reproduziu o erro" --esperada-revisao 4
```

Toda gravação compara a revisão dentro de uma trava do sistema operacional. Quando ocorrer conflito, releia, reconcilie a informação real e execute uma nova alteração. Não tente repetir uma escrita antiga com a revisão nova.

## O que registrar

Registre só decisão vigente, resultado verificável, tentativa descartada que evite repetição, bloqueio, troca relevante, publicação observada ou conclusão. Referencie arquivos longos. Nunca grave transcrições, segredos ou saída completa de terminal.

`provar` é o único comando que executa verificações de `.pacto/verificacoes.json`; contexto e hooks não executam nada. Uma prova vence se um arquivo declarado mudar. Captura visual ou áudio é inspeção registrada, não prova automática de qualidade.

## Instalação e recuperação

No repositório do método, rode primeiro:

```powershell
python scripts/instalar_pacto.py --destino CAMINHO_DO_PROJETO --perfil continuidade planejar
```

Só use `instalar --aplicar` ou `atualizar --aplicar` depois de conferir a prévia. Arquivo não gerido ou alterado localmente vira conflito, não sobrescrita. `remover --aplicar` remove somente arquivos PACTO ainda idênticos e preserva estado/evidências.

O hook do plugin Codex é opcional, somente de leitura e precisa de confiança explícita no aplicativo. Sem hook, o comando manual continua suficiente. O adaptador Claude Code não declara hook ativo enquanto essa integração não for observada no host.
