# Validação proporcional

Política sob demanda do PACTO. Leia somente a seção acionada; não carregue este arquivo em tarefa trivial por padrão. T0 a T3 medem impacto e marco de entrega, não quantidade de arquivos.

## Escolher a prova

- T0: aparência ou documentação sem efeito operacional. Confira o diff silenciosamente, sem testes, build, lint, navegador ou relatório vazio.
- T1: comportamento local. Use a menor prova curta e determinística suficiente.
- T2: integração, dados, segurança ou fluxo. Verifique somente os riscos da fatia.
- T3: entrega, fechamento de fase, PR relevante, release ou deploy. Faça smoke se houver comportamento executável, mais as provas pertinentes. Publicação só documental verifica integridade, links e diff, não inventa build.

Prompt de aplicativo, rótulo consumido por código e configuração funcional não são T0. Ao editar um prompt, confira a montagem com entradas fictícias, os parâmetros e o formato de saída exigido; um teste local de renderização/contrato pode bastar. Não exigir chamada paga por padrão. A integração real só está comprovada quando sua fronteira afetada também foi verificada com amostra segura e representativa; mock sozinho não comprova compatibilidade.

Classifique silenciosamente. Explique a escolha somente quando a fronteira for relevante ou houver limitação material. Não rode provas de checkpoints futuros.

## Corrigir bugs

Formule a hipótese de causa e localize os caminhos irmãos que possam compartilhá-la, pelos consumidores e comportamento, não apenas por nome ou expressão idêntica. Exemplo: geradores diferentes que aplicam a mesma regra de negócio.

Reproduza antes e confira depois quando viável, incluindo somente as variantes afetadas. Preserve o aceite, testes e alertas; não resolva a revisão enfraquecendo-os. Uma hipótese sem outro caminho afetado não exige auditoria global. Informe limitação relevante.

Reteste a revisão corrigida; se a base mudar durante a análise, reconfirme os achados.

## Invariantes do projeto

Se existir `INVARIANTES.md`, identifique somente os IDs que a tarefa pode afetar. Para cada um, use a prova direta indicada no próprio item ou declare a limitação. Não basta afirmar que “nada mudou”.

- Regra de negócio: confirme cenário, limite ou resultado observável correspondente.
- Identidade visual: compare a referência, viewport ou estado indicado quando aparência fizer parte da invariante.
- Identidade textual: confira os termos, tom, formato ou texto fixado.
- Identidade sonora: confirme gatilho, ausência indevida de som, controle de silenciamento e acessibilidade quando o som fizer parte da experiência.
- Contrato técnico ou dado: confira os consumidores, schema, permissão, entrada ou saída indicada.

Uma mudança deliberada exige atualização do item, decisão explícita e nova prova. Não crie navegador, áudio, suíte completa ou checklist quando a invariante não exigir isso.

## Dados e edição parcial

Confira que dados e saídas não afetados foram preservados. Antes de excluir ou migrar, confira alvos, premissas e recuperação necessária; consulta falha ou inesperadamente vazia interrompe a ação. Git protege o versionado, não todo banco, upload ou arquivo ignorado.

Pedido explícito que define ação e alvos já autoriza essa operação; confirme novamente se houver ambiguidade ou se escopo e risco ultrapassarem o autorizado. Não crie backup ou segunda aprovação por reflexo.

## Entrega e publicação

O smoke de aplicativo usa o pacote entregue pelo caminho principal do usuário. Outro modo de execução não comprova esse caminho.

Antes de produção com dados de terceiros, reúna as provas dos riscos aplicáveis, como acesso autorizado, separação de dados e recuperação. Aprovação de negócio não substitui prova técnica. Se persistir risco relevante sem prova que o usuário consiga avaliar, obtenha revisão técnica independente antes de publicar. Não exija revisão externa em toda entrega nem dados reais para testar.

Mostre pendências humanas antes da publicação. Depois, confronte ambiente e revisão efetivos com o estado vigente nos registros existentes. Se documentação ou versionamento estiverem pendentes, informe “publicação realizada, fechamento pendente”; não declare a entrega encerrada.

## Artefato visual

Use navegador ou outra inspeção visual por pedido, requisito visual, fluxo funcional relevante, fechamento visual de fase ou investigação que dependa disso, não por reflexo.

Se houver fidelidade à referência aprovada, compare a primeira tela representativa antes de replicar o padrão. Quando layout, responsividade, imagem ou legibilidade fizerem parte do aceite, observe o artefato final no viewport e estado relevantes, com dados representativos. Isso vale para páginas, planilhas, documentos e imagens. Build, dados, DOM ou CSS não substituem essa prova; sem ela, não declare validação visual concluída.

## Operação conjunta

Quando IA + usuário produzir a melhor prova, recomende e coordene essa opção: o agente prepara cenário seguro e executa o que controla; o usuário faz apenas a ação, acesso ou percepção que depende dele; o agente retoma e conclui.

Dê o próximo passo concreto e o resultado esperado, um passo por vez quando houver dependência entre ações. Não transfira ao usuário o que o agente pode executar, nem entregue lista genérica. T0/T1 não geram testes para o usuário por padrão.

## Comunicação

Em T0, informe somente a alteração. Em T1, acrescente a prova curta e seu resultado. Em T2/T3, informe provas executadas, riscos residuais e pendências reais, incluindo smoke quando aplicável. Não atribua economia, segurança ou conclusão a uma prova que não foi feita.
