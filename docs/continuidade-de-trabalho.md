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

`provar` é o único comando que executa verificações de `.pacto/verificacoes.json`; contexto e hooks não executam nada. Retorno zero sem critério declarado é `executada`; com critério, `passou` refere-se somente à verificação configurada. Nenhum dos dois conclui o trabalho automaticamente. Captura visual ou áudio é inspeção registrada, não prova automática de qualidade.

Na configuração, `arquivos` são entradas obrigatórias e estáveis; `saidas` são arquivos que o comando pode produzir; `ausentes` declara ausência esperada. Caminhos ficam dentro do projeto e não podem ter papéis conflitantes. Entrada ausente impede execução; alterada durante o comando torna a evidência inconclusiva. Uma prova vence se entrada, saída ou ausência declarada deixar de corresponder ao registro. Registros antigos são preservados, mas precisam de nova prova para receber essa proveniência.

Exemplo de verificação, adaptando os caminhos e a assertiva ao projeto:

```json
{"verificacoes":[{"id":"regressao","argv":["python","-m","unittest","tests.test_regra"],"arquivos":["src/regra.py","tests/test_regra.py"],"criterio":"A suíte verifica a regra e rejeita o cenário do bug"}]}
```

O critério precisa corresponder às assertivas reais do comando; escrever uma descrição não comprova o requisito. O registro conserva resultado e hashes, sem copiar stdout/stderr. A configuração é comando executável e deve ser revisada antes do uso. Detalhes de falha podem ser investigados executando o comando diretamente com os cuidados do projeto.

`provar` mostra as evidências produzidas. Retorna código 1 se houver falha, inconclusão ou comando não executado, preservando o registro e incrementando a revisão; releia a revisão antes de outra mutação. Código zero não transforma `executada` em prova suficiente nem aprova a tarefa inteira.

`registrar-publicacao` recebe informação manual. `verificar` distingue `nao_registrada`, `pendente`, `informada` e `divergente`. Revisão esperada sem observação permanece pendente. Fonte textual não comprova consulta remota; esta versão não oferece confirmação automática do ambiente. A prova externa pertinente continua necessária para afirmar que a entrega foi publicada corretamente.

## Instalação e recuperação

No repositório do método, rode primeiro:

```powershell
python scripts/instalar_pacto.py --destino CAMINHO_DO_PROJETO --perfil continuidade planejar
```

Só use `instalar --aplicar` ou `atualizar --aplicar` depois de conferir a prévia. A instalação cria suporte e instruções de entrada ausentes; contratos BRIEF, SPEC, PLAN e INVARIANTES só são criados quando solicitados por `--contrato NOME` antes do subcomando. Repita a opção para outro contrato. Não crie documentos apenas porque a opção existe.

Instruções, contratos e estado existentes pertencem ao projeto e são preservados. Suporte do pacote não gerido ou adaptado localmente gera conflito. Quando AGENTS ou CLAUDE precisam de integração, a saída informa `integracao_pendente`: suporte instalado não significa host integrado. O instalador não instala a skill nem ativa hooks. Atualizar não reinicia o estado; remover apaga apenas suporte do pacote ainda idêntico e preserva contratos, instruções, estado e evidências, inclusive em instalações antigas.

O hook do plugin Codex é opcional, somente de leitura e precisa de confiança explícita no aplicativo. Sem hook, o comando manual continua suficiente. O adaptador Claude Code não declara hook ativo enquanto essa integração não for observada no host.
