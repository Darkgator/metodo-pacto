# Resultado de R5 a R7

Data: 24/10/2026. Candidato `2026.10.24.2`; plugin `0.2.2`. Base de comparação textual: `eec7224abbdb7168f32460ebe19f80be6ca0d23e`.

## Entrega

| Frente | Alteração | Prova e limite |
|---|---|---|
| R5: entrada | AGENTS de projeto menor, com gatilhos por assunto; decisões existentes e autorização preservadas. | Contagem textual e revisão dos destinos. Não comprova que todo host/agente lerá as instruções. |
| R5: fontes | Validação/entrega em `docs/validacao-proporcional.md`; operação em `docs/operacao.md`. Regras Universais virou índice. | Instalador e kit distribuem ambas; teste detecta política referenciada ausente. Consulta é por assunto, sem carregar as duas por padrão. |
| R5: prompts | Fonte única em `prompts/operacionais.md` para execução, revisão, fechamento e bloco global. Markdown e HTML são derivados; o segundo HTML é cópia conferida do principal. | Testes corrompem um prompt/cópia, exigem rejeição, regeneração correta e preservação do entorno. Conteúdo com `<`, `>` e `&` é escapado no HTML sem alterar o pedido. |
| R7: regressão | Bug automatizável retém proteção mínima; conferir rejeição do defeito quando seguro. | Regressões existentes e novos controles negativos. Não obriga infraestrutura nova nem automação desproporcional. |
| R7: esperado | Regra, contrato, fixture conferida ou referência aprovada definem o resultado esperado. | Orientação explícita na política. Gabarito não é a própria função/saída testada. Adesão semântica de outra IA ainda não medida. |
| R7: fallback | Falha não autoriza mudar restrição, ambiente, alvo ou aceite; mudança do combinado exige decisão. | Entrada e fonte operacional alinhadas. O bloco global antigo que exigia plano por quantidade de arquivos foi substituído pelo critério de decisão material. |
| R6: pacote | Verificador sem rede confere distribuição, prompts, UTF-8, Python/JSON, referências locais, IDs/âncoras HTML e destinos dos botões de cópia. | Sete testes novos exercitam erros e recuperação pertinentes; total local de 40 testes passou. Links externos e todos os formatos possíveis de Markdown não são auditados. |
| R6: CI | Dois jobs: Ubuntu/Python 3.10 e Windows/Python 3.14, leitura apenas, cinco minutos cada, cancelamento de execução superada. | Ambos passaram; logs confirmam 40 testes em cada ambiente. CI não chama modelos nem instala dependências Python do produto. |

## Tamanho e custo

Contagem por separação em espaços, incluindo a marcação, sem tokenizador:

| Conteúdo | Antes | Depois |
|---|---:|---:|
| AGENTS do modelo | 886 palavras | 504 palavras |
| Validação/entrega | 839 palavras | 983 palavras |
| AGENTS + validação, se ambos forem lidos inteiros | 1.725 palavras | 1.487 palavras |
| Prompt global do guia | 362 palavras | 64 palavras |
| Quatro prompts HTML de execução/revisão/avanço/fechamento | 417 palavras | 198 palavras |

A entrada permanente caiu aproximadamente 43%; a soma estática de entrada e validação caiu aproximadamente 14%. A operação condicional fica em arquivo separado, sem nova leitura universal. Se a tarefa exigir vários assuntos, o contexto necessário pode aumentar. Não somar essas reduções nem convertê-las em economia comprovada de tokens, dinheiro ou tempo.

A primeira tentativa de consolidação concentrou detalhes na política e elevaria o custo de uma leitura integral comum. A separação por assunto corrigiu essa consequência antes da entrega. Não foi criado questionário, agente fiscal permanente, banco, MCP ou memória obrigatória.

## Verificações

- 40 testes locais passaram, preservando as proteções anteriores. Os novos controles cobrem divergência/regeneração de prompt, escape HTML, marcador ausente sem sobrescrita, cópia alterada, política referenciada ausente, referências/estrutura do guia e UTF-8/Python/JSON inválidos.
- Distribuição de 12 cópias e trechos conferida pelo verificador. Nenhum arquivo de projeto do usuário foi usado para corromper ou testar o pacote.
- Skill PACTO validada pelo `quick_validate.py` da skill-creator. PyYAML 6.0.3, licença MIT conferida no PyPI, foi usado apenas em diretório temporário e removido ao terminar; não foi adicionado ao produto ou à CI.
- ZIP anterior e os 66 hashes individuais reconferidos: íntegros e sem modificação.
- Actions oficiais [checkout](https://github.com/actions/checkout) e [setup-python](https://github.com/actions/setup-python), MIT, fixadas pelos commits das tags v7 consultadas nesta entrega. O workflow não recebe permissão de escrita nem conserva credenciais de checkout.

## Situação e próximo passo

R5/R7 implementados e verificados documentalmente; R6 passou localmente e na [CI 40111620530](https://github.com/Darkgator/metodo-pacto/actions/runs/40111620530), commit `16c38e4f35f00f410874342b9c3f77bc32291024`. Jobs Windows/Python 3.14 e Ubuntu/Python 3.10 concluíram com sucesso; logs conferidos registram 40 testes em cada um. Relatório sem leitura obrigatória no projeto.

Integração/confiança real nos hosts e eficácia em sessões de IA continuam separadas dessas provas. R8 não foi iniciado: primeiro usar o pacote em uma tarefa real e observar retomada, aplicação e custo. Não há necessidade demonstrada de acrescentar memória, MCP ou outra ferramenta agora. Main e instalações existentes continuam preservadas enquanto a branch é validada.
