# Framework v1 Proposto: Método PACTO

Status: orientação vigente consolidada; modelos oficiais em templates/
Criador: Alexandre Barroso de Miranda
Atuação: Consultor de Processos
Stack: independente
Agentes prioritários: Claude Code e Codex

## Tese

O melhor uso de agentes de código não é pedir código mais rápido. É criar um ciclo em que o agente sempre trabalha contra um contrato claro, pequeno e verificável.

O contrato pode ser uma frase, um plano curto ou uma `SPEC.md`, dependendo do risco da tarefa.

O método se chama **PACTO**:

- **Preparar** contexto.
- **Avaliar** variáveis decisivas.
- **Contratar** escopo e verificação.
- **Trabalhar** em fatias.
- **Observar** resultados e externalizar aprendizados.

Antes do PACTO, pode existir uma etapa opcional chamada **Briefing Assistido**. Ela serve para usuários que ainda não sabem explicar bem a solução. Nesse caso, uma IA conduz uma entrevista e entrega um `BRIEF.md` pronto para entrar no método.

## Regra de ouro

Se você não consegue escrever "pronto significa X, verificado por Y", a tarefa ainda não está pronta para implementação autônoma.

## Variáveis decisivas antes da stack

Antes de sugerir stack, IA, banco, hospedagem ou arquitetura, o agente precisa levantar informações que podem mudar a solução inteira.

Exemplos:

- quantidade de usuários totais e simultâneos;
- tipo e sensibilidade dos dados;
- volume de arquivos, anexos, áudios, imagens ou documentos;
- necessidade de IA, custo por uso e permissão para enviar dados a APIs externas;
- autenticação, autorização, perfis e multi-cliente;
- integrações externas, webhooks, pagamentos, e-mail ou WhatsApp;
- operação, hospedagem, orçamento e manutenção;
- uso comercial, licenças, LGPD e obrigações legais.

Se uma resposta puder mudar stack, banco, arquitetura, segurança, IA, custo ou deploy, ela deve ser perguntada antes da recomendação técnica.

## Briefing Assistido

Use antes da descoberta quando o usuário chega com uma ideia solta.

Objetivo:

- transformar conversa inicial em briefing estruturado;
- levantar problema, usuários, MVP e não escopo;
- identificar variáveis decisivas;
- separar fatos, suposições e dúvidas;
- gerar um prompt pronto para o agente de coding.

O Briefing Assistido pode ser:

- um prompt colado em uma IA comum;
- um Custom GPT;
- um assistente interno;
- uma conversa manual guiada pelo template `BRIEF.template.md`.

Ele não deve:

- escolher stack;
- criar arquitetura;
- escrever código;
- inventar respostas que o usuário não deu.

## Níveis de processo

### Nível 1: Tarefa trivial

Use quando:

- mudança em um arquivo;
- comportamento óbvio;
- sem banco;
- sem autenticação;
- sem dependência nova;
- sem risco de arquitetura.

Fluxo:

1. Peça a alteração direta.
2. Peça validação mínima.
3. Revise o diff.

Artefatos:

- Nenhum documento novo obrigatório.

### Nível 2: Feature comum

Use quando:

- há mais de um arquivo;
- há UI;
- há API;
- há regra de negócio;
- há risco moderado de regressão.

Fluxo:

1. Explorar arquivos relevantes.
2. Criar plano curto.
3. Aprovar plano.
4. Implementar a primeira fatia.
5. Verificar.
6. Continuar fatia por fatia.

Artefatos:

- `SPEC.md` leve ou plano salvo.
- `AGENTS.md` e `CLAUDE.md` se ainda não existirem.

### Nível 3: Feature crítica ou projeto novo

Use quando:

- projeto começa do zero;
- há decisão de stack;
- há banco de dados;
- há autenticação/permissão;
- há integração externa;
- há migração;
- há refatoração grande;
- há impacto em várias áreas.

Fluxo:

1. Enquadrar o problema fora do chat.
2. Avaliar variáveis decisivas: usuários simultâneos, dados, IA, segurança, integrações, operação, licenciamento e risco legal.
3. Usar o agente para descoberta, sem código, incluindo até 2 opções de stack com prós, contras, riscos e recomendação.
4. Aprovar stack, MVP, não escopo e primeira fatia verificável.
5. Criar a base inicial usando os templates oficiais do framework: documentos-base e setup técnico mínimo.
6. Validar que a base instala, roda e tem comandos mínimos confiáveis.
7. Implementar por checkpoints pequenos.
8. Verificar cada checkpoint.
9. Fazer revisão independente.
10. Registrar aprendizados.

Artefatos:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`, somente se usar Claude Code
- `SPEC.md`
- `.env.example`
- `PLAN.md`, quando necessário
- `docs/PRODUCT.md`, `docs/UI.md`, `docs/DATA_MODEL.md` ou `docs/DECISIONS.md`, conforme o caso

## Regras universais

Estas regras valem para qualquer solução, com qualquer stack. Elas orientam decisões, mas não obrigam o projeto a criar todos os artefatos em todos os casos.

As políticas completas estão em `docs/regras-universais.md` e `docs/validacao-proporcional.md`. Não as duplique em cada contrato. Os modelos operacionais oficiais estão em `templates/`, com cópias idênticas no kit.

## O que fica fora do chat

- Regras permanentes do projeto.
- Comandos de build, teste e lint.
- Critérios de aceite.
- SPEC ou plano aprovado.
- Decisões arquiteturais.
- Variáveis de ambiente fictícias.
- Testes e scripts de validação.
- Referências visuais e dados de exemplo.

## O que fica dentro do chat

- Perguntas de esclarecimento.
- Aprovação ou ajuste do plano.
- Decisões de trade-off.
- Autorização para dependências, migrações e operações destrutivas.
- Pedidos de próxima fatia.
- Revisões e correções pontuais.

## Arquivos e papéis

### `AGENTS.md`

Arquivo curto, portável e estável. Deve conter:

- visão do projeto;
- comandos essenciais;
- regras de segurança;
- limites de escopo;
- padrão de validação;
- ponte para documentos mais detalhados.

Evitar:

- tutoriais longos;
- padrões óbvios;
- exemplos extensos de código;
- regras que mudam por tarefa.

### `CLAUDE.md`

Entrada curta para Claude Code.

Recomendação:

- manter comandos e regras operacionais;
- apontar para `AGENTS.md` e `SPEC.md`;
- evitar duplicação longa.

### `SPEC.md`

Contrato da tarefa ou fase atual.

Formato recomendado:

```md
# SPEC.md

## Objetivo

## Não objetivos

## Restrições e invariantes

## Áreas afetadas

## Critérios de aceite

## Comandos de verificação

## Riscos e rollback

## Checkpoints

## Definition of Done
```

### `PLAN.md`

Opcional. Use quando o plano for importante o suficiente para sobreviver ao chat.

Mantenha o resumo vigente e o próximo passo reconciliados quando uma decisão os substituir. Acrescentar uma entrada no histórico não atualiza a retomada: marque a orientação anterior como histórica no mesmo ajuste, sem revisar toda a documentação a cada tarefa.

Deve conter:

- arquivos a alterar;
- alternativas consideradas;
- ordem dos checkpoints;
- testes por checkpoint;
- riscos.

### Skills, hooks e automações

Use apenas quando um fluxo manual já estiver estável.

Boa ordem:

1. Repetir manualmente.
2. Transformar em prompt/template.
3. Transformar em skill.
4. Automatizar com hook ou rotina agendada.

## Loop principal

### 1. Enquadrar

O humano define:

- problema;
- usuário;
- resultado esperado;
- restrições;
- não escopo;
- materiais de referência;
- riscos.

### 2. Avaliar variáveis decisivas

O agente aproveita respostas já consolidadas e pergunta somente o que falta. Aguarda respostas bloqueantes antes de recomendar stack. Em decisões estruturais, compara com a alternativa mais simples que atende ao objetivo, inclusive sem IA ou nova dependência.

As perguntas podem envolver:

- usuários totais e simultâneos;
- dados e sensibilidade;
- IA e limites de envio/custo;
- autenticação, autorização e multi-cliente;
- integrações externas;
- hospedagem, operação e orçamento;
- uso comercial, licenças e obrigações legais.

O objetivo é evitar uma stack tecnicamente boa para um cenário errado.

### 3. Explorar

O agente:

- lê apenas arquivos relevantes;
- resume o estado atual;
- identifica áreas afetadas;
- faz perguntas críticas;
- não edita código.

### 4. Contratar

Humano e agente fecham:

- critérios de aceite;
- plano ou SPEC;
- comandos de verificação;
- limites de escopo;
- checkpoints.

### 5. Fatiar

A tarefa é dividida em partes pequenas.

Boa fatia:

- altera poucos arquivos;
- tem resultado observável;
- tem validação clara;
- não depende de "confia que depois fecha".

### 6. Implementar

O agente executa apenas a fatia aprovada.

Regras:

- não adiantar checkpoints futuros;
- não refatorar fora do escopo;
- não adicionar dependência sem aprovação;
- não fazer operações destrutivas sem aprovação.
- antes de turning point, avaliar backup/obsoletos conforme `docs/gestao-obsoletos-backups.md`.

### 7. Verificar

Aplicar o nível de validação do checkpoint:

- `T0`: encerrar após conferir o diff, sem teste ou relatório de validação vazio;
- `T1`: rodar a menor prova curta suficiente;
- `T2`: rodar somente as provas necessárias e pedir ao usuário apenas o que ele precisa observar;
- `T3`: rodar smoke clássico e verificações relevantes ao fechar fase ou preparar entrega.

Não abrir navegador ou capturar screenshot por reflexo.

### 8. Revisar

Preferir revisão com contexto limpo:

- revisar diff contra `SPEC.md`;
- procurar regressões, escopo extra e testes ausentes;
- em correção de bug, conferir variantes próximas afetadas pela mesma causa, sem ampliar para auditoria global;
- não focar estilo se a ferramenta determinística já cuida disso.

### 9. Externalizar

Somente quando houver causa recorrente confirmada, e não uma falha passageira:

- atualizar `AGENTS.md` ou `CLAUDE.md`, se for regra permanente;
- criar template/prompt, se for procedimento;
- criar skill, se for workflow recorrente;
- criar teste/hook, se for validação determinística.

## Regras de parada

- Três tentativas no mesmo erro são o teto geral. Pare antes se não houver evidência nova ou houver risco. Cada hipótese nova precisa de prova e resultado observável.
- Nunca entrar em ciclo de "corrige uma coisa, quebra outra" sem resumir o estado e pedir decisão.
- Se o contexto estiver poluído, gerar resumo curto e iniciar nova sessão/thread.

## Decisões que exigem aprovação humana

- Stack principal.
- Dependências novas de produção.
- Mudanças de banco ou migrações.
- Interfaces públicas e contratos de API.
- Autenticação, autorização e segurança.
- Integrações pagas ou com dados sensíveis.
- Operações destrutivas.
- Refatorações grandes.
- Mudanças de escopo do MVP.

## Padrão para projetos novos

0. Se o usuário não souber explicar bem o projeto, usar o Briefing Assistido para gerar um `BRIEF.md`.
1. Descrever problema e resultado esperado.
2. Preencher ou revisar `templates/BRIEF.template.md`, principalmente as variáveis decisivas.
3. Pedir descoberta sem código, com perguntas sobre variáveis decisivas antes de stack.
4. Pedir até 2 modelos de stack e recomendação final.
5. Aprovar stack, MVP, riscos aceitos, não escopo e primeira fatia.
6. Criar a base inicial usando `templates/` como referência oficial:
   - `README.md`
   - `AGENTS.md`
   - `CLAUDE.md`, se aplicável
   - `SPEC.md`
   - `.env.example`, se aplicável
   - `PLAN.md`, se a tarefa exigir plano persistente
   - `BRIEF.md`, se for útil manter o briefing no repositório
   - estrutura técnica mínima
   - comandos mínimos de build/test/lint quando aplicáveis
7. Validar que a base instala, roda e tem pelo menos uma verificação confiável. Esta validação inicial é um marco `T3` da base, não uma obrigação repetida em cada ajuste trivial posterior.
8. Revisar documentos e setup antes de produto real.
9. Implementar a primeira fatia vertical da `SPEC.md`.

## Padrão para projetos existentes

1. Pedir exploração read-only.
2. Identificar padrões reais do código.
3. Criar ou ajustar instruções curtas.
4. Planejar a mudança.
5. Implementar com validação localizada.
6. Rodar revisão contra diff.

## Padrão para projetos pequenos

Documentação mínima:

- `AGENTS.md`
- `CLAUDE.md`, somente se usar Claude Code
- `SPEC.md` leve, se houver feature não trivial

Evitar:

- excesso de docs;
- skills antes de maturidade;
- hooks sofisticados cedo demais.

## Padrão para projetos grandes

Adicionar:

- instruções por subdiretório;
- `PLAN.md`;
- worktrees ou branches isoladas;
- validação por módulo;
- revisão independente;
- docs de produto, UI, dados e decisões quando necessário.
