# Validação Proporcional por Alteração, Checkpoint e Fase

Criador: Alexandre Barroso de Miranda
Atuação: Consultor de Processos
Método: PACTO

## Princípio

Sempre classificar pelo impacto, mas não testar tudo sempre. Texto que altera regra operacional, permissão ou comportamento não é T0 apenas por ser texto. Quantidade de arquivos ou comandos não define sozinha o risco.

O agente não deve gastar tokens criando plano de testes, lista para o usuário, build, lint, navegador, screenshot ou relatório de validação para mudanças triviais. A validação cresce apenas quando a alteração, o checkpoint ou a fase justificar.

## Níveis de validação

| Nível | Quando usar | O que o agente faz | O que o usuário faz |
|---|---|---|---|
| `T0: direta` | Texto, cor, espaçamento, posição estática, ajuste visual isolado, comentário ou mudança documental simples | Implementa e confere o diff silenciosamente. Não roda teste, navegador, build, lint, typecheck, checklist ou plano de teste. | Nada por padrão. Pode revisar visualmente junto com outras mudanças, quando desejar. |
| `T1: leve` | Regra pequena, comportamento isolado, endpoint simples, configuração com risco local ou bug simples | Executa a menor prova direcionada e determinística suficiente, como teste do módulo, typecheck local, lint local ou requisição HTTP. | Nada por padrão. Recebe uma linha com a validação executada e o resultado. |
| `T2: relevante` | Integração, banco, autenticação, autorização, vários módulos, fluxo funcional de UI ou mudança com risco de regressão | Define apenas as validações necessárias para aquela fatia. Pode executar teste unitário, integração, regressão ou E2E focado. | Testa apenas o que exige percepção humana, ambiente real, credencial real, dispositivo específico ou serviço de terceiros. |
| `T3: marco` | Fechamento de fase, PR relevante, release, deploy ou fluxo crítico | Executa smoke clássico obrigatório, mais os testes relevantes já definidos para a fase. | Valida a jornada principal e itens humanos pendentes antes de aprovar entrega ou publicação. |

A prova verifica o resultado esperado, não apenas a implementação. Para bug, reproduza antes e confira depois quando viável; não enfraqueça testes, suprima alertas ou redefina o aceite. Ao alterar integração, confira a fronteira afetada com amostras seguras e representativas; mock sozinho não comprova compatibilidade. Não exigir serviço pago ou dados de produção por padrão.

Confirme que o reteste usa a revisão corrigida; se a base mudar durante uma análise, reconfirme os achados.

Em edição parcial, confira também que dados e saídas não afetados foram preservados.

Ao corrigir um bug, confira variantes próximas que compartilhem a causa, como os geradores de documento padrão e específico. Valide somente os caminhos afetados e informe limitação relevante do que não pôde verificar. Isso não exige auditoria global, documento novo, suíte completa ou revisão de áreas sem relação com o defeito.

## Relação com etapas e fases do PACTO

### Durante uma alteração individual

O agente classifica a alteração silenciosamente como `T0`, `T1`, `T2` ou `T3`.

- Em `T0`, não deve gerar lista de testes ou perguntas para o usuário.
- Em `T1`, executa a menor validação curta suficiente e não transforma a tarefa em uma bateria de testes.
- Em `T2`, só apresenta o que precisa ser validado, incluindo pedido ao usuário somente se houver evidência que o agente não consegue obter.
- `T3` não deve ser usado para uma alteração isolada sem marco de entrega.

### Durante um checkpoint

Cada checkpoint da `SPEC.md` deve declarar o nível esperado quando não for óbvio.

- Checkpoint visual simples: normalmente `T0`.
- Checkpoint de comportamento local: normalmente `T1`.
- Checkpoint que conecta áreas ou altera fluxo: normalmente `T2`.

O agente não deve executar testes de checkpoints futuros nem antecipar validações completas de fase.

### Ao fechar uma fase

Se a fase criou ou alterou comportamento executável, o smoke clássico é obrigatório. Ele prova rapidamente que o essencial sobe e responde. Na entrega de aplicativo, o smoke usa o pacote entregue pelo caminho principal do usuário; outro modo de execução não comprova esse caminho.

O fechamento da fase também reúne apenas os testes que correspondem aos riscos efetivamente introduzidos. Não exige E2E completo, browser, carga, crawl ou acessibilidade ampla quando eles não forem aplicáveis.

### Antes de PR, release ou deploy

Tratar como `T3`. Rodar smoke obrigatório quando houver comportamento executável e as verificações definidas na `SPEC.md`, no pipeline ou na política do projeto. Em publicação exclusivamente documental, conferir integridade do kit, links e diff; não inventar build, teste de aplicação ou inspeção visual sem mudança que os justifique. Pendências humanas precisam ser mostradas antes de publicar.

Após publicar, confronte ambiente e revisão efetivos com o estado vigente nos registros existentes. Se documentação ou versionamento estiverem pendentes, informe “publicação realizada, fechamento pendente”; não declare a entrega encerrada.

## Navegador, screenshot e validação visual

Navegador não é validação padrão de toda mudança de UI.

Não abrir navegador, capturar screenshot ou fazer inspeção visual automática em `T0` e `T1`, salvo pedido explícito do usuário.

Usar navegador apenas quando:

- o usuário pedir validação visual, responsiva ou de UX;
- a `SPEC.md` exigir evidência visual;
- um checkpoint `T2` alterar fluxo funcional de UI, navegação, formulário, estado de erro ou carregamento;
- uma fase `T3` encerrar jornada visual relevante;
- houver falha que não possa ser entendida por teste determinístico, log ou inspeção de código.

Quando houver requisito de fidelidade visual, compare a primeira tela representativa com a referência aprovada antes de replicar o padrão.

Quando a mudança exigir layout, responsividade, imagem ou legibilidade, observe o artefato final no viewport e estado relevantes, com dados representativos. Build, teste de dados, DOM ou CSS não substituem essa prova; sem ela, não declare a validação visual concluída.

## O que pedir ao usuário

Não gerar lista de testes para o usuário em `T0` ou `T1`.

Em `T2` ou `T3`, pedir somente validações que o agente não possa executar com confiança, por exemplo:

- percepção de aparência, clareza e usabilidade;
- autenticação real ou serviço externo protegido;
- pagamento, permissão de cliente ou dado real;
- dispositivo, navegador ou ambiente específico;
- aprovação de resultado de negócio.

O pedido deve ser curto, acionável e vinculado a um resultado esperado.

Antes de transferir validação em `T2` ou `T3`, considere se a operação conjunta produz a melhor prova. Se produzir, recomende-a e coordene: o agente prepara cenário seguro e executa o que controla; o usuário faz somente a ação, acesso ou percepção que depende dele; o agente retoma e conclui. Não peça ao usuário o que o agente pode executar nem entregue lista genérica de testes.

## Modos que o usuário pode pedir

- `Modo enxuto`: aplicar `T0` quando cabível. Não criar plano de teste, lista, navegador, build ou lint para mudança trivial.
- `Teste direcionado`: executar somente uma prova escolhida pelo usuário ou diretamente relacionada à alteração.
- `Validar checkpoint`: usar o nível registrado para o checkpoint atual.
- `Fechar fase`: aplicar `T3`, com smoke obrigatório e validações relevantes.
- `Pré-release`: aplicar `T3` antes de PR relevante, release ou deploy.
- `Validação visual`: abrir navegador somente para o fluxo, tela ou viewport indicado.

## Comunicação ao concluir

- `T0`: informar apenas a alteração concluída. Não anexar relatório de teste vazio.
- `T1`: informar a validação necessária executada e o resultado.
- `T2`: informar validações executadas, pendências reais e, se necessário, um pedido curto ao usuário.
- `T3`: informar smoke, testes relevantes, pendências humanas e riscos residuais.

## Regra de decisão

Quando houver dúvida entre dois níveis, começar pelo menor que não esconda risco real. Só subir o nível quando a mudança afetar comportamento, integração, dados, segurança, fase ou entrega.
