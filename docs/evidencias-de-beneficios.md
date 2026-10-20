# Benefícios observados do PACTO

Levantamento retrospectivo de 19/10/2026. Registro de pesquisa consultado sob demanda; não acrescenta regra de execução.

## Como interpretar

O catálogo reúne 14 observações de 12 episódios, em seis aplicativos e na manutenção do próprio método. Observações do mesmo episódio não são sucessos independentes. A seleção é intencional, não aleatória, e não permite calcular taxa de sucesso do PACTO.

A investigação anterior selecionava principalmente falhas e cobranças. Aqui foram procuradas também decisões bem executadas, provas úteis e proteções nos registros já disponíveis. Código, testes, commits e relatos foram cruzados quando possível. Os testes dos aplicativos não foram reexecutados nesta rodada.

Classificação da atribuição:

| Classe | O que a evidência permite afirmar |
|---|---|
| A: aplicação explícita | Há ligação documentada entre regra/contrato do PACTO vigente e a ação realizada. Isso comprova aplicação, não causalidade exclusiva. |
| B: contribuição plausível | O projeto adotava o método e o acerto é coerente com ele, mas a decisão também é explicada por boa engenharia ou competência da IA. |
| C: humano + IA | Pedido, correção ou decisão humana teve papel explícito. O resultado pertence à operação conjunta; não é atribuído só ao método. |
| D: atribuição não demonstrada | Existe um acerto de engenharia, mas não foi confirmado vínculo suficiente com o PACTO naquele episódio. |

Nenhum caso tem demonstração experimental de que o mesmo trabalho, com a mesma IA e sem o método, daria resultado inferior. A força do resultado observado é avaliada separadamente da sua atribuição.

## Catálogo anonimizado

As fontes detalhadas, projetos, caminhos e IDs das conversas ficam no registro local da auditoria, fora deste repositório. Os IDs abaixo permitem correspondência sem publicar históricos dos projetos.

| ID | Acerto observado | Evidência e alcance | Classe |
|---|---|---|---|
| BP01 | Adaptar o método ao projeto existente | A adoção preservou o backlog já usado e as instruções específicas; contrato da fase ganhou papel distinto. Conversa e commit corroboram a organização. Não mede tempo poupado. | A |
| BP02 | Dispensar suíte de backend em mudança documental | O encerramento registra que o backend não foi executado; o commit contém contratos, documentação e plano. Houve outras checagens. Não foi uma execução sem validação, nem há economia medida. | A |
| BP03 | Usar informação determinística em vez de inferência da IA | Registro relaciona explicitamente a regra do projeto à identificação de oradores no arquivo. Parser e testes foram alterados. O resultado histórico tem recorte de dois arquivos, não de todas as transcrições. | A |
| BP04 | Reaproveitar sugestão de IA já produzida e conservar revisão humana | Código devolve o resultado guardado; teste verifica que abrir a sugestão mantém uma única chamada ao extrator e que a confirmação continua separada. Não mede tokens economizados em produção. | A |
| BP05 | Filtrar criticamente uma revisão externa | Recomendações foram aceitas, ajustadas, adiadas ou excluídas por escopo; aprovação técnica não virou aceite operacional geral. Registro e diff conferidos. Não demonstra número de bugs evitados. | B |
| BP06 | Bloquear prévia antes de comandos de banco | Guarda de build e teste que exige ausência de chamadas aos comandos de migração. Proteção concreta para a condição testada; não prova que houve incidente real impedido. | B |
| BP07 | Proteger contra submissão repetida | Há testes do serviço e de dois POSTs consecutivos exigindo um único registro. Resultado de correção e proteção de regressão; reincidências futuras evitadas não foram contadas. | B |
| BP08 | Homologar com cenário sintético e limpar a massa | Registro de prova no banco e de jornada autenticada na interface, seguido de limpeza. A condução visual exigiu cobrança humana anterior. Mérito compartilhado; não comprova antecipação autônoma pelo método. | C |
| BP09 | Tornar testes repetíveis e isolar dados | Suíte solicitada pelo usuário, com infraestrutura de diretórios temporários e comandos repetíveis; resultados históricos registrados. Não equivale a E2E completo ou prova da integração real de IA. | C |
| BP10 | Verificar restauração, além de criar backup | Teste abre o arquivo de backup e confere banco, workspace e upload restaurados. Código e relato de execução corroboram o mecanismo sintético. Não certifica toda recuperação em produção. | B |
| BP11 | Conferir fronteira externa e melhorar a regressão | Chamada com dados sintéticos revelou schema que teste offline aceitava. Registro informa que a prova corrigida rejeitou o defeito reintroduzido; código associado conferido. O teste inicial insuficiente continua sendo uma falha. | B |
| BP12 | Inspecionar o pacote e executar a stack entregue | Registro descreve descoberta de conteúdo indevido no pacote e três problemas de build/permissão; Dockerfile corrobora a montagem seletiva. A autoria causal do método não foi confirmada. | D |
| BP13 | Reduzir o texto dos modelos do próprio método | Contagem local reproduzível: cinco modelos somavam 2.419 palavras antes da consolidação e 1.266 no estado auditado, redução de 47,7%. É tamanho textual, não consumo real por tarefa. | A |
| BP14 | Aceitar custo adicional delimitado para melhorar qualidade | Registro de comparação com gabarito em dois exemplos relata 8/8 resultados corretos na deduplicação e explicita custo/latência adicional. Houve ajuste anterior de atribuição no prompt. Medidas são históricas, não um benchmark independente do PACTO. | A |

Classes: A = 6 observações; B = 5; C = 2; D = 1. Essa distribuição descreve a seleção, não a proporção de eficácia do método em todos os projetos.

## O que as promessas do método já têm de evidência

| Benefício | Estado nesta amostra |
|---|---|
| Escopo e decisões mais claros | Aplicações documentadas: BP01 e BP05. Não foi medida a quantidade de decisões erradas evitadas. |
| Menos execução desnecessária | Há registro de dispensa de backend em BP02. Não há comparação de duração ou tokens. |
| Menos chamadas repetidas à IA no aplicativo | Mecanismo e asserção do caminho específico em BP04. Não é economia do agente desenvolvedor. |
| Verificação e proteção de regressão | Testes e barreiras concretas em BP03, BP06, BP07, BP09, BP10 e BP11. Não há contagem contrafactual de bugs ou retestes evitados. |
| Preservação e teste com dados controlados | Evidências em BP04, BP08, BP09, BP10 e BP12, com os limites de cada caso. |
| Menor contexto permanente | Redução textual medida em BP13. O efeito depende dos arquivos que o agente realmente lê e do tokenizer/cache. |
| Qualidade com custo explícito | Experimento local relatado em BP14; custo adicional foi reconhecido e autorizado. |
| Menor tempo do desenvolvedor | Não demonstrado: faltam tempos de trabalho ativo e comparação equivalente. |
| Menos tokens do agente desenvolvedor | Não demonstrado: existem contadores históricos de trabalho, mas não uma comparação válida com e sem método. |
| Menos retestes e bugs em uso futuro | Não demonstrado como taxa ou quantidade. Existência de regressão automatizada não prova quantos defeitos futuros deixaram de ocorrer. |

Os contadores históricos do agente não devem ser somados como se cada evento cumulativo fosse consumo novo. Tokens em cache já integram a entrada. Não foram calculados faturamento, quota poupada, percentual de produtividade ou retorno financeiro.

## Origem dos refinamentos operacionais

Esta tabela resume a motivação histórica, não comprova que adicionar cada frase causou melhoria. Decisões, mensagens e diffs detalhados permanecem nos registros locais dos projetos, sem publicar conversas ou dados privados. O Git preserva a implementação anterior.

| Refinamento | Caso documentado e alcance |
|---|---|
| POC-01: estado vigente | Resumos de retomada contrariavam decisões posteriores em mais de um projeto. Atualizar estado e próximo passo; não reler toda a cronologia. |
| Variantes pela causa | Uma correção em um gerador deixou um caminho irmão com o mesmo problema. Verificar consumidores afetados; não fazer auditoria global. |
| R2-01/02: entrega e referência | Executável validado por outro caminho falhou na janela principal; pedidos visuais reiterados divergiram da referência. |
| P4-01/02: aceite e revisão | Histórico registrou cobranças de preservação do critério e retestes ligados à revisão errada. |
| P5-01: edição parcial | Edição de uma parte exigiu conferir preservação de dados e saídas não afetados. |
| P6-01: publicação e registro | Produção foi publicada, mas registros vigentes continuaram descrevendo homologação; falha de cumprimento de fechamento já exigido. |
| P7-01/P8-01: artefato e cooperação | Validação visual insuficiente e transferência inadequada de passos ao usuário motivaram prova no artefato e operação conjunta. |

A auditoria externa de 19/10/2026 confirmou a falha de distribuição e observou falhas em T0 e variantes. Casos retrospectivos justificam investigar o mecanismo, não alegar taxa de sucesso. Antes de criar regra, ligar problema, causa, necessidade e prova proporcional; recorrência ou risco grave confirmado não dispensam essa análise.

## Como avaliar a próxima versão

Aceite desta correção: as seis cópias correspondem às fontes, versão e caminho local são identificáveis, a política está acessível fora do repositório do método e a checagem rejeita pacote incompleto. Provas T2/T4 verificam os cenários, não adesão de um novo agente.

Verificação local de 19/10/2026: seis cópias idênticas; kit isolado aprovado; controles de política ausente e AGENTS antigo rejeitados. Em cópias temporárias, T2 passou em 4/4 provas e rejeitou prompt com chaves JSON não escapadas; T4 rejeitou a correção parcial e passou em 2/2 após corrigir ambos os relatórios. O executor conhecia os cenários e testes; não houve novo ensaio cego nem sessão independente de agente. Origens da auditoria preservadas.

Tamanho textual por separação em espaços: AGENTS de 721 para 744 palavras (+3,2%); política de 1.255 para 703 (-44,0%). São contagens de palavras, não medições de consumo de tokens.

Para avaliar eficácia em um piloto separado:

- Fixar antes tarefa, aceite, riscos, mesmo escopo aprovado, modelo/versão, esforço, ambiente, instruções globais, política de cache, repetições e orçamento. Comparar PACTO com uma linha de base mínima, registrando também perguntas e respostas; aprovação vaga não deve mudar o escopo comparado.
- Em T2, observar se o agente verifica montagem do prompt, parâmetros e contrato. Em T4, observar se encontra e verifica caminhos irmãos da mesma causa. Medir defeitos e severidade além da contagem de testes.
- Considerar ganho somente se preservar aceite e segurança e melhorar qualidade, trabalho humano ou consumo; registrar o custo das outras dimensões, não escondê-lo em uma média.
- Alegar economia somente com qualidade e escopo equivalentes e menor consumo comparável. Separar entrada, cache já incluído nela, saída, duração e tempo humano ativo. Indisponível não significa zero; volume não é preço financeiro nem quota.
- Registrar falhas e acertos, variabilidade e limites antes de generalizar. Uma execução não prova taxa de eficácia nem quantidade de bugs evitados.

Nada disso exige ficha por tarefa. Usar PLAN e contadores existentes quando houver piloto autorizado. Teste com público leigo continua pendente; não há nova sessão de agente, pessoa ou experimento pago agendado.

## Decisão e continuidade

Preservar os mecanismos que funcionaram: contrato proporcional, reaproveitamento de contexto, escolhas determinísticas, revisão humana útil, testes dirigidos e evidência do resultado. O catálogo não justifica aumentar o núcleo de instruções ou criar relatório obrigatório por tarefa.

Esta primeira rodada positiva está registrada. A próxima oportunidade é acompanhar uma entrega real já autorizada, usando o PLAN e os contadores existentes. Para atribuir economia ao método, será necessária comparação equivalente quanto a tarefa, modelo, versão, ambiente e cache. Um cronômetro de uma única entrega não prova ganho causal. Não há experimento agendado ou automação criada.
