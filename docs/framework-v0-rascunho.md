# Framework para Desenvolvimento com Agentic Code

Criador: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método atual: PACTO

Versão: 0.1  
Data: 2026-06-23

Este framework é um passo a passo reutilizável para conduzir projetos de software com agentes de código como Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI ou ferramentas equivalentes.

A ideia central é simples: o agente acelera execução, leitura de código, testes, refatoração e documentação, mas você continua responsável por escopo, decisões de produto, validação funcional, prioridades e aceitação final.

## Princípios

1. **Não comece codificando.** Primeiro alinhe problema, usuários, escopo, restrições, stack e critérios de aceite.
2. **Use documentos curtos como fonte de verdade.** O chat é transitório; `SPEC.md`, `AGENTS.md`, `CLAUDE.md`, `README.md`, `CHANGELOG.md` e decisões registradas no repositório são mais confiáveis.
3. **Trabalhe por fatias pequenas.** Uma tarefa deve caber em um ciclo: entender, planejar, implementar, testar, revisar e registrar.
4. **Peça plano antes da execução.** Para mudanças multiarquivo, novas features, refatorações ou arquitetura, o agente deve explorar o projeto e propor plano antes de editar.
5. **Valide com evidência.** Todo ciclo deve terminar com testes, lint/build quando aplicável, verificação visual para UI e resumo claro do que mudou.
6. **Mantenha checkpoints humanos.** Você aprova escopo, arquitetura, dependências novas, alterações de banco, integrações pagas, segurança e comportamento final.
7. **Controle loops.** Se o agente falhar 3 vezes seguidas no mesmo erro de teste, build ou lint, ele deve parar, mostrar o erro e pedir orientação.
8. **Nunca exponha segredos.** Chaves reais não entram no código, nos testes, no chat ou nos commits. Use `.env.local` e `.env.example` com valores fictícios.

## Arquivos-padrão por projeto

### Obrigatórios

- `README.md`: visão humana do projeto, como rodar e status.
- `AGENTS.md`: instruções para agentes em geral.
- `SPEC.md`: escopo da fase atual, critérios de aceite e checklist granular.
- `.env.example`: variáveis necessárias com valores fictícios.
- `CHANGELOG.md`: histórico no padrão Keep a Changelog.

### Recomendados

- `CLAUDE.md`: comandos e regras específicas para Claude Code, se você usar Claude.
- `DECISIONS.md` ou `docs/decisions/`: decisões arquiteturais, trade-offs e motivos.
- `docs/PRODUCT.md`: problema, personas, jornadas, regras de negócio e não escopo.
- `docs/UI.md`: identidade visual, tokens, componentes, referências e regras de responsividade.
- `docs/DATA_MODEL.md`: entidades, relacionamentos e regras de dados.
- `docs/QA.md`: roteiro de testes manuais e casos críticos.

## O que fazer fora do chat do agente

Antes de chamar o agente para construir:

1. **Defina o problema em linguagem de negócio.**
   - Quem usa?
   - Que dor resolve?
   - O que acontece hoje?
   - O que muda quando o sistema estiver pronto?

2. **Separe MVP de evolução futura.**
   - MVP é o menor produto validável.
   - Evolução futura é importante, mas não deve contaminar a primeira entrega.

3. **Organize insumos.**
   - Logos, cores, referências visuais, documentos reais, planilhas, PDFs, exemplos de relatórios e fluxos atuais.
   - Nunca coloque credenciais reais nesses materiais.

4. **Escolha suas restrições.**
   - Prazo, orçamento, hospedagem, banco de dados, usuários esperados, dispositivos, integrações e nível de segurança.

5. **Valide decisões que o agente não deve inventar.**
   - Regras de negócio.
   - Prioridade das features.
   - Stack quando houver restrição real.
   - Modelo de cobrança, perfis de acesso e dados sensíveis.

6. **Teste o produto como usuário final.**
   - Clique nos fluxos principais.
   - Verifique telas em desktop e mobile.
   - Leia mensagens de erro.
   - Confirme se o comportamento bate com a necessidade real.

7. **Revise diffs antes de aceitar.**
   - Procure mudanças fora do escopo.
   - Verifique se arquivos de configuração, banco e seeds foram atualizados juntos.
   - Confirme se não houve segredo, chave ou dado real commitado.

## O que fazer dentro do chat do agente

Durante a conversa:

1. **Dê contexto objetivo.**
   - Explique o resultado desejado, não só a tela ou tecnologia.
   - Informe arquivos, referências, restrições e critérios de aceite.

2. **Use comandos por fase.**
   - Primeiro descoberta.
   - Depois arquitetura.
   - Depois documentos de trabalho.
   - Depois implementação por fatia.
   - Depois revisão e endurecimento.

3. **Peça perguntas críticas.**
   - O agente deve perguntar apenas o que bloqueia boas decisões.
   - Evite longas entrevistas quando a decisão puder ser assumida com baixo risco.

4. **Aprove ou ajuste o plano.**
   - Não aprove plano genérico.
   - Peça granularidade por banco, backend, frontend, testes e documentação.

5. **Mantenha uma tarefa principal por sessão.**
   - Sessões focadas reduzem confusão de contexto.
   - Para mudanças grandes, use uma `SPEC.md` por fase.

6. **Exija fechamento com evidências.**
   - O agente deve informar arquivos alterados, testes executados, falhas restantes e próximos passos.

## Fluxo macro recomendado

### Fase 0: Preparação humana

Resultado esperado: material mínimo para o agente não trabalhar no escuro.

Checklist:

- [ ] Problema descrito em 1 a 3 parágrafos.
- [ ] Usuários/personas definidos.
- [ ] MVP separado de ideias futuras.
- [ ] Regras críticas listadas.
- [ ] Restrições técnicas anotadas.
- [ ] Referências visuais e dados de exemplo organizados.
- [ ] Decisões que precisam de aprovação humana identificadas.

### Fase 1: Descoberta com o agente

Objetivo: transformar a necessidade em escopo, stack e roteiro.

O agente deve:

- propor stack e justificar;
- fazer até 5 perguntas críticas;
- registrar suposições;
- propor MVP e fases futuras;
- não escrever código de aplicação.

Saída esperada:

- decisão de stack;
- perguntas respondidas;
- roteiro de fases;
- riscos e premissas;
- lista do que entra e não entra no MVP.

### Fase 2: Criação dos contratos do projeto

Objetivo: criar a base de trabalho para o agente não depender só do chat.

Arquivos a criar ou atualizar:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`, se aplicável
- `SPEC.md`
- `.env.example`
- `CHANGELOG.md`
- `docs/PRODUCT.md`
- `docs/UI.md`, quando houver interface
- `docs/DATA_MODEL.md`, quando houver persistência

O agente ainda não deve implementar código de aplicação se o escopo não estiver aprovado.

### Fase 3: Setup técnico mínimo

Objetivo: criar o esqueleto executável do projeto.

Checklist:

- [ ] Repositório iniciado.
- [ ] Stack instalada.
- [ ] Comandos de desenvolvimento funcionando.
- [ ] Lint, formatador e testes configurados.
- [ ] `.env.example` criado.
- [ ] Estrutura de pastas definida.
- [ ] Primeiro build/teste passando, mesmo que ainda não haja feature real.

### Fase 4: Implementação por fatias verticais

Cada fatia deve entregar uma parte usável do produto, não apenas camadas isoladas.

Exemplo de fatia:

- banco de dados;
- backend/API;
- tela;
- validação;
- estados de carregamento, erro e sucesso;
- testes;
- seed;
- documentação.

Checklist por fatia:

- [ ] Ler `SPEC.md`, `AGENTS.md` e arquivos relevantes.
- [ ] Confirmar entendimento e suposições.
- [ ] Propor plano curto.
- [ ] Implementar apenas a fatia aprovada.
- [ ] Rodar lint/testes/build.
- [ ] Validar UI quando houver tela.
- [ ] Atualizar seed e `.env.example` se aplicável.
- [ ] Atualizar `CHANGELOG.md`.
- [ ] Preparar mensagem de commit.

### Fase 5: Revisão e endurecimento

Objetivo: reduzir risco antes de considerar a fase concluída.

Checklist:

- [ ] Fluxos principais testados manualmente.
- [ ] Casos de erro verificados.
- [ ] Responsividade validada.
- [ ] Acessibilidade básica verificada.
- [ ] Dados sensíveis revisados.
- [ ] Permissões e autenticação revisadas.
- [ ] Migrações e seeds coerentes.
- [ ] Testes automatizados verdes.
- [ ] Build de produção aprovado.
- [ ] Dívidas conhecidas registradas.

### Fase 6: Fechamento da fase

Saída esperada:

- resumo do que foi entregue;
- arquivos alterados;
- testes executados;
- limitações conhecidas;
- próximos passos sugeridos;
- `SPEC.md` da próxima fase, se necessário.

## Prompt 1: Projeto do zero, sem código ainda

Use quando a ideia ainda precisa virar escopo e stack.

```text
Estamos começando um projeto totalmente novo, do zero.

Não escreva código de aplicação ainda. Primeiro precisamos alinhar escopo, stack, riscos e roteiro.

Com base na necessidade abaixo, faça exatamente:

1. Reescreva o problema em linguagem objetiva de produto.
2. Separe MVP, fase 2 e evolução futura.
3. Proponha a stack ideal, incluindo linguagem, framework, banco, autenticação, UI, testes, hospedagem e ferramentas. Explique o porquê de cada escolha.
4. Liste decisões críticas que não devem ser assumidas sem aprovação humana.
5. Faça até 5 perguntas críticas, apenas se forem realmente necessárias para evitar retrabalho.
6. Proponha um roteiro de alto nível por fases.
7. Não crie arquivos e não implemente código ainda.

Necessidade:
[cole aqui a explicação do projeto]
```

## Prompt 2: Criar contratos do projeto

Use depois de aprovar MVP, stack e roteiro.

```text
Agora vamos criar os contratos de trabalho do projeto.

Antes de editar, analise os arquivos existentes do repositório para entender a stack, comandos e estrutura.

Crie ou atualize apenas os arquivos de documentação e configuração de orientação. Não implemente código de aplicação ainda.

Arquivos esperados:

1. README.md
2. AGENTS.md
3. CLAUDE.md, se o projeto for usado com Claude Code
4. SPEC.md
5. .env.example
6. CHANGELOG.md
7. docs/PRODUCT.md
8. docs/UI.md, se houver interface
9. docs/DATA_MODEL.md, se houver banco de dados

Regras:

- Inclua comandos exatos de instalar, rodar, testar, lintar e buildar.
- Defina prevenção de loops: após 3 tentativas consecutivas no mesmo erro, pare e peça orientação.
- Inclua diretrizes de segurança: nunca usar chaves reais no código, testes ou commits.
- Inclua regra de banco: mudança de schema exige atualização de seed correspondente.
- Inclua diretrizes de UI/UX, responsividade, estados assíncronos e acessibilidade.
- Em SPEC.md, inclua contexto da fase, critérios de aceite binários, checklist por camada e Definition of Done.
- Ao final, mostre um resumo para aprovação.
```

## Prompt 3: Implementar uma fatia da SPEC

Use para desenvolvimento real.

```text
Leia AGENTS.md, SPEC.md, README.md e os arquivos relevantes antes de editar.

Implemente apenas a próxima fatia da SPEC:

[descreva a fatia ou cole o item da SPEC]

Processo obrigatório:

1. Confirme entendimento e suposições.
2. Faça um plano curto por camada.
3. Implemente.
4. Rode lint, testes e build aplicáveis.
5. Valide estados de UI, erro, carregamento, responsividade e acessibilidade quando houver interface.
6. Atualize seed, .env.example, documentação e CHANGELOG.md se aplicável.
7. Prepare uma mensagem de commit em Conventional Commits.

Se falhar 3 vezes seguidas no mesmo erro, pare e mostre o erro atual.
```

## Prompt 4: Revisão de código antes de aceitar

Use quando o agente terminou uma mudança e você quer avaliar risco.

```text
Faça uma revisão técnica das mudanças atuais.

Priorize bugs, regressões, riscos de segurança, inconsistências com a SPEC, ausência de testes, problemas de acessibilidade, falhas de responsividade e mudanças fora de escopo.

Formato:

1. Achados por severidade, com arquivo e linha quando possível.
2. Perguntas abertas.
3. Testes que faltam.
4. Resumo curto do que parece correto.

Não corrija ainda. Apenas revise.
```

## Prompt 5: Corrigir falhas de teste/build/lint

Use quando algo quebrou.

```text
Analise a falha abaixo e corrija a menor causa provável, sem refatorações fora do escopo.

Regras:

- Leia o erro completo.
- Identifique a causa raiz provável.
- Faça uma correção mínima.
- Rode novamente o comando que falhou.
- Se surgir outro erro, trate como nova tentativa.
- Após 3 tentativas consecutivas sem resolver, pare e peça orientação.

Erro:
[cole o erro ou peça para o agente rodar o comando]
```

## Prompt 6: Refinamento de UI/UX

Use para telas e experiência visual.

```text
Revise a UI implementada com foco em usabilidade real.

Considere:

- clareza da hierarquia visual;
- densidade adequada ao público;
- responsividade desktop e mobile;
- estados de carregamento, vazio, erro e sucesso;
- acessibilidade;
- consistência com tokens de design, logo, cores e referências;
- ausência de deslocamento de layout;
- legibilidade de textos e tabelas.

Faça ajustes pequenos e objetivos. Depois valide visualmente com screenshot ou inspeção no navegador, se a ferramenta permitir.
```

## Prompt 7: Encerramento de fase

Use quando uma fase do MVP está pronta.

```text
Faça o fechamento da fase atual.

Entregue:

1. Resumo do que foi implementado.
2. Critérios de aceite atendidos e não atendidos.
3. Testes e validações executadas.
4. Riscos restantes.
5. Dívidas técnicas registradas.
6. Atualizações necessárias em README.md, SPEC.md, CHANGELOG.md e documentação.
7. Sugestão de SPEC.md para a próxima fase.

Não implemente novas features neste passo, exceto correções pequenas de documentação.
```

## Modelo de AGENTS.md

```md
# AGENTS.md

## Visão do projeto

[Explique em 3 a 6 linhas o que o sistema faz e para quem.]

## Comandos

- Instalar dependências: `[comando]`
- Rodar em desenvolvimento: `[comando]`
- Rodar testes: `[comando]`
- Rodar lint: `[comando]`
- Rodar build: `[comando]`

## Fluxo de trabalho

- Antes de mudanças multiarquivo, leia os arquivos relevantes e proponha um plano.
- Trabalhe em fatias pequenas, alinhadas à `SPEC.md`.
- Não implemente fora do escopo aprovado.
- Após 3 tentativas consecutivas no mesmo erro, pare e peça orientação.

## Código

- Siga os padrões existentes do projeto.
- Prefira soluções simples e explícitas.
- Não adicione dependências de produção sem justificar e pedir aprovação.
- Atualize testes junto com mudanças de comportamento.

## Segurança

- Nunca inclua chaves reais, tokens, senhas ou credenciais no código, testes ou documentação.
- Use variáveis de ambiente e mantenha `.env.example` com valores fictícios.
- Valide entradas e trate erros de forma segura.

## Banco de dados

- Qualquer mudança de schema exige migração, atualização de tipos e atualização de seed.
- Não destrua dados de desenvolvimento sem autorização explícita.

## UI/UX

- Use o design system e os tokens do projeto.
- Não invente cores arbitrárias quando houver tokens definidos.
- Toda ação assíncrona deve ter carregamento, sucesso e erro.
- Telas devem ser responsivas e acessíveis.
```

## Modelo de CLAUDE.md

```md
# CLAUDE.md

## Comandos

- Instalar: `[comando]`
- Desenvolvimento: `[comando]`
- Testes: `[comando]`
- Lint: `[comando]`
- Build: `[comando]`

## Regras de execução

- Não escreva código antes de entender a `SPEC.md`.
- Para mudanças complexas, use planejamento antes da implementação.
- Após editar, rode os comandos de validação aplicáveis.
- Se falhar 3 vezes seguidas no mesmo erro, pare, mostre o erro e peça orientação.

## Memória do projeto

- `SPEC.md` é a fonte de verdade da fase atual.
- `AGENTS.md` contém regras gerais para agentes.
- `docs/PRODUCT.md` contém regras de negócio.
- `docs/UI.md` contém diretrizes visuais.
- `docs/DATA_MODEL.md` contém decisões de dados.
```

## Modelo de SPEC.md

```md
# SPEC.md

## Fase atual

[Nome da fase]

## Contexto

[Explique a funcionalidade em linguagem de negócio.]

## Fora de escopo

- [Liste explicitamente o que não será feito agora.]

## Critérios de aceite

- [ ] [Regra binária: dado X, quando Y, então Z.]
- [ ] [Regra binária.]
- [ ] [Regra binária.]

## Checklist granular

### Banco de dados

- [ ] [Schema/migração]
- [ ] [Seed]

### Backend

- [ ] [Endpoint/serviço/validação]
- [ ] [Tratamento de erro]

### Frontend UI/UX

- [ ] [Tela/componente]
- [ ] [Estado vazio]
- [ ] [Carregamento]
- [ ] [Erro]
- [ ] [Sucesso]
- [ ] [Responsividade]
- [ ] [Acessibilidade]

### Testes

- [ ] [Teste unitário]
- [ ] [Teste de integração]
- [ ] [Teste manual crítico]

### Documentação

- [ ] README atualizado, se aplicável.
- [ ] CHANGELOG atualizado.
- [ ] `.env.example` atualizado, se aplicável.

## Definition of Done

- [ ] Implementação concluída.
- [ ] Lint e formatador aprovados.
- [ ] Build aprovado.
- [ ] Suíte de testes aprovada.
- [ ] Estados de UI validados, se aplicável.
- [ ] Acessibilidade básica verificada.
- [ ] Seeds e `.env.example` atualizados, se aplicável.
- [ ] CHANGELOG.md atualizado.
- [ ] Mensagem de commit preparada em Conventional Commits.
```

## Quando pedir plano, quando pedir código direto

Peça plano antes quando:

- é projeto novo;
- há mudança em vários arquivos;
- há banco de dados;
- há autenticação, permissões ou segurança;
- há integração com API externa;
- há UI importante;
- há refatoração;
- você não sabe exatamente o impacto.

Código direto é aceitável quando:

- é correção pequena;
- o arquivo e o comportamento estão claros;
- há teste evidente;
- não há dependência nova;
- não há mudança de arquitetura.

## Antipadrões a evitar

- Colar uma especificação gigante e pedir "faça tudo".
- Usar o chat como única documentação do projeto.
- Deixar o agente escolher regras de negócio sozinho.
- Implementar muitas features antes de rodar o app.
- Aceitar uma tela sem testar como usuário real.
- Não ter `.env.example`.
- Guardar chave de API no código.
- Deixar `AGENTS.md` enorme, contraditório ou desatualizado.
- Corrigir erro por tentativa infinita.
- Misturar MVP com ideias futuras.
- Pedir "melhore a UI" sem referência, público e critério.

## Checklist rápido para iniciar qualquer projeto

- [ ] Escrevi o problema em linguagem de negócio.
- [ ] Separei MVP e futuro.
- [ ] Tenho referências ou exemplos reais.
- [ ] Rodei o Prompt 1.
- [ ] Respondi perguntas críticas.
- [ ] Aprovei stack e roteiro.
- [ ] Rodei o Prompt 2.
- [ ] Aprovei `SPEC.md`.
- [ ] Criei setup técnico mínimo.
- [ ] Implementei a primeira fatia vertical.
- [ ] Validei com testes e uso real.

## Ajustes recomendados nos seus prompts atuais

Seus dois prompts já têm uma base boa: eles impedem o agente de começar codificando cedo demais e criam arquivos de orientação. Os principais ajustes recomendados são:

1. **Adicionar fonte de verdade de produto.** Além de `SPEC.md`, use `docs/PRODUCT.md` para regras de negócio, personas, fluxos e não escopo.
2. **Separar `AGENTS.md` de detalhes longos.** Mantenha o arquivo curto e direcione detalhes para `docs/`.
3. **Exigir critérios de aceite binários desde o início.** Isso melhora testes e revisão.
4. **Adicionar registro de decisões.** Use `DECISIONS.md` para explicar por que a stack, banco, autenticação e arquitetura foram escolhidos.
5. **Trabalhar por fatias verticais.** Evite pedir "faça backend inteiro" e depois "faça frontend inteiro".
6. **Criar prompts de revisão e encerramento.** O projeto melhora quando o agente revisa antes de continuar.
7. **Validar UI com evidência visual.** Para apps com interface, peça screenshots, responsividade e estados vazios/erro/carregamento.

## Fontes consultadas

- OpenAI Developers: `AGENTS.md` como instruções globais e por repositório para Codex.
- AGENTS.md: formato aberto para orientar agentes de código com comandos, estilo e testes.
- Anthropic Claude Code: uso de `CLAUDE.md`, memória do projeto e orientação específica.
- GitHub Copilot Docs: tarefas bem delimitadas, critérios de aceite, planejamento antes de código e sessões focadas.
- Addy Osmani: especificações pequenas, evolutivas e verificáveis para agentes.
- Discussões públicas em Reddit/YouTube/blogs técnicos: padrões recorrentes de Plan Mode, TDD, revisão humana, tarefas pequenas e evitar "vibe coding" sem processo.
