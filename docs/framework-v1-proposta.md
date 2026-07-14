# Framework v1 Proposto: Método PACTO

Status: proposta para discussão  
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
- `CLAUDE.md`
- `SPEC.md`
- `.env.example`
- `PLAN.md`, quando necessário
- `docs/PRODUCT.md`, `docs/UI.md`, `docs/DATA_MODEL.md` ou `docs/DECISIONS.md`, conforme o caso

## Regras universais

Estas regras valem para qualquer solução, com qualquer stack. Elas orientam decisões, mas não obrigam o projeto a criar todos os artefatos em todos os casos.

### Segurança

- Nunca inserir chaves reais, tokens, senhas, cookies, certificados, credenciais ou segredos no código, nos testes, na documentação, em logs ou commits.
- Usar variáveis de ambiente, secrets do ambiente, vault ou mecanismo equivalente da stack.
- Manter `.env.example` apenas com valores fictícios quando o projeto usar configuração por ambiente.
- Validar toda entrada externa: usuário, API, webhook, upload, arquivo, áudio, planilha, prompt, HTML, URL, query string e dados de terceiros.
- Não registrar dados sensíveis em logs. Logs devem conter o suficiente para depurar, sem vazar segredo, dado pessoal ou conteúdo confidencial.
- Separar dados reais de dados de desenvolvimento, testes e seeds.
- Aplicar menor privilégio para usuários, serviços, tokens, banco, buckets, filas, APIs e permissões do agente.
- Exigir aprovação humana para ações destrutivas, alteração de permissões, mudanças em autenticação/autorização, publicação em produção, migração de dados, envio externo de mensagens ou uso de dados sensíveis.
- Se a tarefa tocar segurança, dados, banco, autenticação, autorização, pagamento, produção ou clientes reais, tratar como tarefa crítica.

### Licenciamento e risco legal

- Antes de adicionar dependência, biblioteca, template, fonte, ícone, imagem, áudio, modelo de IA, dataset, SDK, API, plugin ou serviço externo, confirmar se o uso pretendido é permitido.
- "Disponível na internet", "gratuito", "source-available" e "free for personal use" não significam permissão para uso comercial.
- Se a solução tiver restrição de uso comercial, redistribuição, SaaS, marca, patente, atribuição, privacidade, treinamento de IA ou copyleft, registrar o risco e pedir aprovação humana.
- Para dependências novas de produção, registrar quando relevante: nome, fonte, licença/termos, uso no projeto, permissão comercial, obrigações e alternativa considerada.
- Se a licença ou os termos não forem claros, não assumir compatibilidade. A decisão deve ficar bloqueada até validação humana.
- Não copiar código, imagens, fontes, textos, datasets ou templates de origem incerta para dentro do projeto.

### Testes e verificação

- Todo contrato precisa dizer como será verificado. O tipo de teste depende do risco, da stack e do tipo de mudança.
- Usar o menor teste confiável primeiro, depois ampliar a validação se a mudança justificar.
- `Smoke test`: verifica rapidamente se o essencial sobe e responde. É recomendado para projeto novo, deploy, mudança de configuração e fluxo crítico.
- `Unit test`: valida regra, função, componente ou módulo isolado. É útil para lógica de negócio e transformação de dados.
- `Integration test`: valida a comunicação entre partes, como API e banco, serviço e fila, autenticação e sessão, ou componente e estado.
- `E2E test`: valida jornada real do usuário. Deve cobrir fluxos críticos, não todas as combinações possíveis.
- `Regression test`: deve ser criado ou atualizado quando um bug é corrigido para impedir retorno do problema.
- `Accessibility test`: deve existir quando houver interface relevante, junto com validação manual mínima de navegação, labels e contraste.
- `Performance/load test`: aplicar quando tempo de resposta, escala, volume, concorrência ou custo operacional forem riscos reais.
- `Fuzz/property test`: aplicar quando entradas malformadas, formatos variáveis, parsers, importadores, segurança ou robustez forem importantes.
- `Spider/crawl`: usar para descobrir rotas, links, páginas quebradas e superfície exposta. É técnica de descoberta e segurança; não substitui smoke, integração ou E2E.
- Se não houver automação viável, registrar teste manual objetivo com passos, entrada esperada e resultado esperado.

### Codificação e idioma

- Todo arquivo textual criado ou editado deve ser salvo em UTF-8.
- Ao escrever em pt-BR, preservar acentuação correta e caracteres como ç, ã, õ, á, é, í, ó, ú, â, ê, ô e à.
- Não aceitar mojibake em arquivos, documentos, UI ou prompts. Exemplos: `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“`, `Â`.
- Se o terminal exibir caracteres quebrados, verificar se o problema está no arquivo ou apenas na visualização antes de reescrever.
- Não remover acentos para contornar codificação.

### Obsoletos e backups

- Git é a fonte primária de histórico.
- Antes de turning points, avaliar se Git basta ou se é necessário backup mínimo.
- Turning points incluem troca de stack, migração de banco, refatoração grande, reestruturação de UI, substituição de protótipo, remoção de muitos arquivos, integração crítica ou operação destrutiva.
- Arquivos substituídos mas ainda úteis como referência temporária devem ir para `_archive/obsolete/YYYY-MM-DD_descricao/`.
- Snapshots necessários além do Git devem ir para `_archive/backups/YYYY-MM-DD_HHMM_descricao/`.
- Toda pasta arquivada deve ter `README.md` com motivo, origem, conteúdo e condição de remoção.
- Não arquivar dependências, caches, builds ou arquivos recriáveis.
- Não fazer backup por reflexo em alteração pequena.

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

O agente identifica perguntas que mudam a solução:

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

Validação mínima obrigatória:

- menor teste/comando que prova a fatia;
- build/lint/typecheck quando aplicável;
- screenshot ou inspeção visual para UI;
- teste manual quando automação não existir.

### 8. Revisar

Preferir revisão com contexto limpo:

- revisar diff contra `SPEC.md`;
- procurar regressões, escopo extra e testes ausentes;
- não focar estilo se a ferramenta determinística já cuida disso.

### 9. Externalizar

Se o mesmo erro acontecer duas vezes:

- atualizar `AGENTS.md` ou `CLAUDE.md`, se for regra permanente;
- criar template/prompt, se for procedimento;
- criar skill, se for workflow recorrente;
- criar teste/hook, se for validação determinística.

## Regras de parada

- Em tarefa crítica: se o mesmo erro persistir após 2 tentativas, parar e pedir orientação.
- Em tarefa simples: 3 tentativas é o máximo absoluto.
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
7. Validar que a base instala, roda e tem pelo menos uma verificação confiável.
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
- `CLAUDE.md`
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
