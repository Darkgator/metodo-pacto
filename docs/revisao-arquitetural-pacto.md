# Revisão arquitetural do PACTO

Data: 24/10/2026. Base inspecionada: `ed19ebdd62d60b2b79ae2561d121b81af19aa904`, versão `2026.10.22.3`.

Estado deste documento: diagnóstico e proposta sobre a base anterior. O primeiro lote foi implementado depois desta revisão; situação atual em [resultado da reengenharia](resultado-reengenharia-2026-10-24.md). Este relatório preserva os achados da base e não integra a leitura obrigatória dos projetos.

## 1. Parecer

**Recomendo uma reengenharia parcial.** Preservar o ciclo PACTO, o contrato proporcional, as invariantes do projeto e a validação orientada ao resultado. Reorganizar as fontes de instrução, a propriedade dos arquivos e o significado dos registros de continuidade e evidência.

O problema central demonstrado é de fronteira: orientação concorrente decide quando parar; arquivo do projeto é tratado como arquivo do instalador; execução de comando recebe o nome de prova aprovada; ausência de divergência de publicação não explicita ausência de confirmação.

Acrescentar mais recomendações ao AGENTS não resolve essas causas. Uma parte exige substituir instruções contraditórias; outra exige corrigir código e reter regressões. Não há evidência suficiente para justificar reescrever todo o método, adotar memória externa obrigatória ou construir um MCP agora.

Esta revisão amplia a [análise dos episódios do Akita](analise-akita-flow-588-663.md), examinando a implementação e os caminhos ativos do próprio método. As recomendações arquiteturais são julgamento desta revisão, não afirmações atribuídas a ele.

## 2. Decisões recomendadas, em ordem

Notas de 1 a 10 indicam prioridade relativa, considerando impacto, alcance e evidência. Não são percentuais de eficácia nem estimativas de economia. Esforço é relativo dentro deste repositório.

| Ordem | Decisão | Nota | Esforço | Justificativa e limite |
|---|---|---:|---|---|
| R1 | Separar dado do projeto de arquivo gerido pelo pacote. | 10 | Médio | Uso normal bloqueou atualização; remoção apagou contratos intactos de instalação em cenário isolado. Corrigir propriedade, não pedir ao usuário para restaurar o estado vazio. |
| R2 | Separar comando executado, evidência suficiente e publicação confirmada. | 10 | Médio | Arquivo ausente recebeu prova aprovada; revisão publicada ausente não apareceu como confirmação pendente. O agente ainda precisa avaliar adequação semântica. |
| R3 | Respeitar autorização do plano inteiro e eliminar ordens gerais de parar por checkpoint. | 9 | Baixo | Guia ativo manda parar após o primeiro checkpoint. Verificar etapas continua obrigatório conforme o risco; repetir autorização já concedida não deve ser a rotina. |
| R4 | Priorizar próximo passo e bloqueio no contexto de retomada; compartilhar o validador de estado. | 9 | Baixo a médio | Resumo válido perdeu o próximo passo e excedeu o teto; kit aprovou estrutura rejeitada pela CLI. |
| R5 | Consolidar instruções operacionais e reduzir a entrada permanente. | 8 | Médio | Existem fontes ativas divergentes. Centralizar trechos compartilhados e referências, sem transformar todo o guia HTML em um novo sistema complexo. |
| R6 | Completar as provas da entrega atual e automatizar a verificação do pacote. | 8 | Médio | Os 13 testes passaram apesar dos cenários novos. A bancada de continuidade prepara cenários, mas não executa comparação com IA. |
| R7 | Refinar regras existentes de regressão, resultado esperado e fallback. | 7 | Baixo | Preservar bug como teste útil; confrontar resultado com referência; não resolver obstáculo enfraquecendo restrição. Complementa R2 sem um novo questionário. |
| R8 | Comparar memória atual com alternativa externa somente em piloto delimitado. | 5 | Médio, condicionado | Nenhum ensaio desta revisão demonstrou que trocar o mecanismo de memória melhora o resultado. Não instalar outra autoridade paralela por antecipação. |

**Primeiro lote recomendado:** R1 a R4 e regressões correspondentes. Depois, R5 a R7 e verificação automática do pacote. R8 só se persistir um problema de continuidade que o núcleo corrigido não resolver.

## 3. O que manter, retirar, automatizar ou substituir

| Tratamento | Elemento | Resultado desejado |
|---|---|---|
| Manter | Ciclo PACTO e execução em fatias verificáveis. | Preservar organização e feedback rápido, com continuidade dentro da autorização recebida. |
| Manter | Briefing suficiente para a decisão seguinte. | Perguntar quando faltar informação que afete uma decisão material; usar contexto existente e premissas reversíveis quando adequado. |
| Manter | Invariantes de negócio, contratos, dados, visual, texto e som. | Seleção pertinente ao projeto, com referência e prova adequadas à mudança. Não inventar identidade sonora onde não existe. |
| Manter | Operação conjunta usuário + IA. | Agente prepara e executa o que puder; ação humana é específica, útil e seguida de retomada pelo agente. |
| Manter | Proporcionalidade T0 a T3 e continuidade opcional. | Tarefa pequena não cria automaticamente um conjunto de documentos ou uma sessão de gestão de estado. |
| Retirar | Paradas gerais por checkpoint já autorizado. | Parar por decisão pendente, limite de autorização ou bloqueio real. |
| Retirar | Criação automática de todos os contratos como consequência de instalar suporte. | Disponibilizar modelos e materializar somente o contrato necessário ao trabalho. |
| Retirar | Tratamento de estado mutável como cópia do template do pacote. | Atualização do método preserva o trabalho; migração de formato é explícita e verificável. |
| Automatizar | Distribuição, UTF-8, formato, referências locais e regressões determinísticas. | Erro conhecido reprova o pacote antes da entrega. Não confundir verificação textual com compreensão de todas as instruções. |
| Automatizar | Proveniência de evidência e comparação de publicação, quando houver consulta disponível. | Registrar o que foi observado, onde e para qual revisão. Sem observação, situação pendente. |
| Substituir | Fontes concorrentes de instrução. | Entrada curta, política canônica por assunto e conteúdo derivado conferível. |
| Substituir | Um booleano de publicação divergente como única síntese. | Distinguir registro informado, confirmação, divergência e pendência, sem declarar entrega por falta de diferença. |
| Avaliar depois | Backend de memória e MCP. | Interface pequena que permita trocar implementação caso o piloto justifique. Nenhum servidor novo neste lote. |

## 4. Arquitetura proposta

Quatro responsabilidades, sem obrigação de criar quatro ferramentas ou quatro arquivos novos:

```text
Pedido e autorização vigentes
        |
        v
Entrada curta do PACTO -> política pertinente, sob demanda
        |
        v
Contratos e referências do projeto -> definem o resultado esperado
        |
        v
Continuidade opcional -> decisão vigente, bloqueio e próximo passo
        |
        v
Verificações da stack e observação do artefato -> evidência e limites
```

O instalador distribui suporte. Não é proprietário do contrato que o projeto passou a usar. A continuidade aponta para decisões e evidências, sem criar uma segunda especificação. Uma memória futura pode ajudar a recuperar contexto, mas não sobrescreve instruções atuais nem decide qual requisito é verdadeiro por frequência histórica.

### Autoridade e persistência

- Orientação do método tem uma fonte canônica por assunto; exemplos e guias não podem impor procedimento incompatível.
- Decisões locais pertencem ao projeto. Atualizar o método não reabre briefing, stack ou escopo já estabelecidos sem causa concreta.
- Autorização continua valendo até ser alterada ou até a ação extrapolar seu alcance. Checkpoint é ponto de verificação, não pedido automático de permissão.
- Estado guarda o mínimo útil para retomar. Documentos e referências conservam o contexto detalhado; não replicar a transcrição inteira.
- Resultado de processo, resultado do artefato e confirmação de publicação são fatos diferentes. Cada registro deve declarar o que efetivamente comprova.

### Evidência mínima com significado

Configurações de teste precisam distinguir entrada relevante e saída produzida. Para a entrada, registrar a versão examinada; para a saída, verificar existência e critério esperado. Se a verificação legitimamente testa ausência ou modifica um arquivo, isso deve ser declarado, sem tornar toda modificação uma falha.

Código de saída zero pode ser suficiente para uma verificação bem definida, como uma suíte com assertivas pertinentes. Não comprova automaticamente fidelidade visual, ambiente de produção ou requisito de negócio. O esperado deve vir do contrato, fixture ou referência independente da saída que o agente acabou de gerar.

Saída de comando não deve virar memória persistente por padrão. Preferir código de saída, identificação da verificação e referência a log local controlado; conteúdo adicional somente quando necessário e sem dados indevidos. Uma expressão regular não garante remoção de todos os segredos.

## 5. Evidências verificadas

### Base e alcance

- Inspeção do README, contratos do repositório, modelos, política, framework, guias, skill, hook, manifesto, instalador, distribuição, estado e avaliador.
- Conferência de distribuição e `verificar_kit.py`: passaram; dez cópias e UTF-8 conferidos.
- `python -m unittest discover -s tests -v`: 13 testes passaram, em 6,474 segundos nesta execução.
- Nove cenários adicionais executados com módulos reais em pastas temporárias isoladas. Os dados, comandos e publicação eram sintéticos. Nenhum projeto do usuário foi instalado, desinstalado ou publicado nesses ensaios.

Os nove cenários abaixo são reproduções de comportamento ou demonstrações de limite. Não equivalem a nove incidentes reais, nem estabelecem frequência em produção.

| Caso | Preparação e observação | Classificação | Aceite da correção proposta |
|---|---|---|---|
| D01 | Instalar perfil `continuidade` em pasta vazia e remover sem editar. Criou os seis contratos; remoção apagou AGENTS, CLAUDE, BRIEF, SPEC, PLAN e INVARIANTES. Estado foi preservado. Nenhuma skill foi instalada nesse destino. | Propriedade e composição do pacote. Não houve perda de contrato personalizado neste teste. | Desinstalação preserva contratos do projeto; componentes incluídos e ausentes são informados com precisão. |
| D02 | AGENTS local preexistente com conteúdo próprio. Planejamento apontou conflito; aplicação recusou toda a instalação, inclusive política independente. AGENTS permaneceu intacto. | Proteção correta, adoção incompleta. Não é sobrescrita de dado. | Oferecer adoção explícita e delimitada, preservando conteúdo local; conflito em um componente não exige abandonar todos os demais quando puderem ser separados com segurança. |
| D03 | Instalar continuidade, criar um trabalho pelo mecanismo normal e planejar atualização. Retornou `conflito local: .pacto/estado.json`. | Falha funcional reproduzida. | Atualização preserva estado usado e prossegue nos arquivos do pacote compatíveis; migração não compara trabalho real com template vazio. |
| D04 | Substituir estado por `{"formato":2,"revisao":"invalida","trabalhos":"invalido"}`. Verificador de instalação retornou zero erros; CLI `listar` recusou com código 2. | Validação inconsistente reproduzida. | Kit e runtime usam o mesmo contrato de dados, com tratamento explícito de formato antigo ou futuro. |
| D05 | Trabalho válido com UUID normal, cinco decisões vigentes de mil caracteres e próximo passo identificável. Resumo teve 4.016 caracteres para teto de 4.000; próximo passo desapareceu. | Falha funcional de retomada reproduzida. | Próximo passo, bloqueio e identificação cabem no resumo. O orçamento inclui o aviso de corte e prioriza informação, sem truncar tudo pela ordem de concatenação. |
| D06 | Configurar comando que imprime `ok`, retorna zero e declara `nao-existe.txt`. Evidência ficou `aprovada`, hash `null`, `vencida: false`. | Lacuna de significado demonstrada. Ausência pode ser legítima, mas não foi declarada como critério. | Entrada obrigatória ausente impede confirmação; teste de ausência precisa ser explícito. Retorno zero sozinho não substitui essa distinção. |
| D07 | Declarar `alvo.txt`; comando muda seu conteúdo de ANTES para DEPOIS. Evidência ficou aprovada e vigente, com hash apenas após execução. | Proveniência insuficiente demonstrada. Modificação legítima de saída não deve ser proibida. | Identificar entrada e saída e a revisão efetivamente examinada; não atribuir a uma entrada anterior uma prova que só registrou a posterior. |
| D08 | Comando imprime `CREDENCIAL_FICTICIA_PACTO_123`. Texto apareceu no estado serializado. Nenhum segredo real foi usado. | Persistência de saída bruta reproduzida; risco, sem vazamento real demonstrado. | Resumo de evidência não copia stdout/stderr arbitrários automaticamente. Retenção adicional é delimitada e documentada. |
| D09 | Registrar ambiente esperado/observado iguais, revisão esperada `abc123`, observada omitida e fonte textual sem consulta. Registro aceito; `verificar` retornou `publicacao_divergente: false`. Trabalho continuou ativo. | Falta de confirmação explícita. Não houve conclusão automática da tarefa. | Revisão esperada sem observação fica pendente. Texto livre de fonte não vira prova de consulta real. |

### Contradições documentais confirmadas

| Fonte ativa | Evidência | Consequência |
|---|---|---|
| `docs/guia-projeto-do-zero.md:179` e `:191` | Implementar apenas checkpoint 1 e parar ao concluir. | Pode orientar parada mesmo quando o pedido atual autorizou o plano inteiro. |
| `guia-visual/index.html:1060`, `:1072` e `:1149` | Reproduz a execução limitada e manda parar antes de outro checkpoint. | O mesmo problema entra pelo caminho visual de adoção. |
| `docs/framework-v1-proposta.md:333` | Não adiantar checkpoints futuros. | Precisa distinguir trabalho não autorizado de próximos checkpoints já aprovados. |
| `guia-visual/index.html:790` | Qualquer alteração local leva a parar e pedir decisão. | Conflita com AGENTS do próprio repositório, que admite mudanças locais compatíveis e preservadas. |

Um prompt intencionalmente limitado ao checkpoint 1 continua válido quando essa for a escolha do usuário. A correção é tornar esse recorte uma opção explícita, sem contrariar autorização mais ampla.

### O que as checagens atuais não demonstram

- O verificador confere cópias e parte da estrutura. Não detecta todos os conflitos de orientação entre guias, nem comprova comportamento real dos hosts.
- `scripts/avaliar_continuidade.py` prepara quatro cenários e informa limites. Não contém executor de IA; mesmo com orçamento confirmado não realiza comparação. Portanto, bancada preparada não significa benefício medido.
- O adaptador Claude presente é documentação; isso não constitui integração executável validada. A ativação real no host continua sendo uma fronteira separada.
- Não havia workflow em `.github` na base examinada. Testes locais não significam execução automática em cada entrega.
- Limites de concorrência, recuperação após interrupção e funcionamento real nos hosts exigem provas específicas; os 13 testes não encerram todo o plano de aceitação.

## 6. Contexto e custo: o que podemos afirmar

Contagem textual desta base, por separação em espaços, sem tokenizador de modelo:

| Componente | Palavras | Caracteres |
|---|---:|---:|
| AGENTS do modelo | 869 | 5.925 |
| Política de validação | 839 | 5.705 |
| Skill PACTO | 304 | 2.134 |
| Referência de continuidade da skill | 179 | 1.191 |
| Framework | 1.969 | 13.375 |
| Guia de projeto do zero | 1.208 | 8.096 |
| Regras universais | 1.796 | 12.051 |

Esses arquivos não são necessariamente carregados juntos. Somá-los e chamar o total de custo por conversa seria incorreto. O teto do resumo é em caracteres, não tokens, e a presença de uma skill no disco não comprova que o host a leu.

Meta inicial: reduzir repetição da entrada permanente e carregar detalhes por gatilho. Preservar regra crítica ou local quando removê-la aumentar erro ou retrabalho. Economia só será alegada medindo sessões comparáveis, com a mesma qualidade exigida, incluindo tempo humano e custo de preparar e manter a solução.

Evitar neste lote: LLM em todo turno para fiscalizar o método, leitura automática de todos os chats, screenshot universal, banco central, nova coleção obrigatória de documentos e benchmark amplo sem decisão concreta a tomar.

## 7. Como deve funcionar no cotidiano

| Situação | Comportamento esperado |
|---|---|
| Chat novo em projeto em andamento | Ler entrada local e apenas contexto pertinente. Recuperar decisão vigente e próximo passo; não reiniciar briefing ou stack por adoção do método. |
| Pedido pequeno e claro | Executar com prova proporcional, sem criar seis documentos nem registrar estado por ritual. |
| Plano inteiro aprovado | Implementar, verificar e avançar nas fatias autorizadas. Pedir decisão apenas quando houver lacuna material ou ação fora do alcance autorizado. |
| Pergunta no meio do trabalho | Responder e preservar a tarefa ativa, retomando quando a pergunta não a cancelar nem exigir espera. |
| Troca de assunto e retorno | Separar trabalhos quando necessário e recuperar o certo; diante de ambiguidade real, pedir escolha curta. Não escolher pelo último horário de arquivo. |
| Visual, texto ou som fora do esperado | Comparar com referência do projeto e mostrar a divergência; usar participação humana específica se ela for a melhor forma disponível de verificar ou decidir. |
| Publicação | Distinguir intenção, execução, ambiente e revisão observados. Se não for possível confirmar, informar exatamente a pendência. |
| Encerramento | Informar resultado, prova, limite relevante e próximo passo, ou dizer que acabou. Não abrir melhoria adicional só para continuar trabalhando. |

## 8. Sequência de implementação e condição de entrega

1. **Corrigir propriedade e manutenção:** separar ativos do pacote de dados e contratos do projeto; cobrir D01 a D03. Prévia e preservação continuam existindo. Não usar conflito como motivo para sobrescrever.
2. **Corrigir o significado dos registros:** compartilhamento de schema, resumo priorizado, entrada/saída da prova, retenção mínima e confirmação de publicação; cobrir D04 a D09.
3. **Alinhar o percurso de uso:** revisar fontes e prompts ativos para autorização persistente, adoção em andamento e proporcionalidade. Centralizar somente trechos com repetição demonstrada. Não criar um gerador de documentação completo sem necessidade.
4. **Refinar regras existentes:** regressão útil para bug, comparação com resultado esperado e fallback compatível com restrições. Atualizar os exemplos afetados no mesmo lote.
5. **Automatizar a entrega:** distribuição, verificador, regressões e referências locais em CI, sem serviço ou dados externos. Um defeito conhecido reintroduzido em cópia isolada deve reprovar.
6. **Validar integração e benefício separadamente:** provar leitura/injeção e retomada no host disponível antes de declarar suporte validado. Comparação com sessões de IA fica delimitada a executor e orçamento definidos; não é requisito para corrigir um bug determinístico já reproduzido.

Aceite mínimo do lote: os 13 testes atuais preservados; regressões pertinentes aos nove cenários; falhas conhecidas reprovando nos controles negativos; nenhum contrato ou estado real perdido; nenhuma aprovação sem critério correspondente; guias sem instruções gerais contraditórias de parada. Registros de planejamento devem separar implementado, testado localmente, integrado no host e eficácia medida.

Para remover ou trocar a continuidade atual, exigir antes exportação, preservação de decisões, retomada correta e custo comparável. Se uma solução externa vencer o piloto, substituir a responsabilidade correspondente; não manter dois registros mestres indefinidamente.

## 9. Ações do usuário e limites desta revisão

Nenhuma instalação, compra, download de livro ou preparação manual é necessária para as correções determinísticas propostas. O agente pode preparar cenários, fixtures, alterações e verificações.

Participação sua só quando houver decisão de negócio ou referência que não esteja registrada, ou ação de acesso/confiança exigida pelo ambiente real. Esses pontos não precisam impedir correções independentes.

Esta revisão não alterou os arquivos operacionais do método, não ativou hooks, não instalou memória, não publicou mudanças e não executou novas sessões de IA para benchmark. Os cenários sintéticos demonstram as fronteiras descritas; não provam que elas causaram todos os problemas históricos dos seus projetos.
