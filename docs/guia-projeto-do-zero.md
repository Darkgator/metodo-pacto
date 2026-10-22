# Guia Prático: Projeto do Zero

Criador: Alexandre Barroso de Miranda
Atuação: Consultor de Processos
Método: PACTO

Este guia mostra como iniciar um desenvolvimento do zero usando o Método PACTO.

## Etapa -1: Briefing Assistido

Use esta etapa quando o usuário ainda não sabe explicar bem o que quer construir.

O objetivo é conversar com uma IA antes de abrir Claude Code, Codex ou outro agente de coding. Essa IA entrevista o usuário e gera um `BRIEF.md` pronto.

Use o prompt em:

`prompts/briefing-assistido-customgpt.md`

Saída esperada:

- problema organizado;
- usuários;
- MVP;
- fora de escopo;
- variáveis decisivas;
- riscos;
- dúvidas pendentes;
- prompt pronto para agente de coding.

O briefing só está pronto para a próxima etapa quando declarar: decisão liberada, lacunas bloqueantes, premissas reversíveis e a próxima decisão que exigirá novo briefing. Consulte `docs/briefing-assistido.md` para os quatro estados de prontidão.

Não use esta etapa se o briefing já estiver claro.

## Etapa 0: Preparar contexto

Antes do chat, reúna:

- problema e objetivo;
- usuários;
- restrições;
- exemplos reais;
- referências visuais;
- regras de negócio;
- dados de exemplo sem informação sensível;
- itens fora do MVP.

Não coloque segredos, credenciais ou dados reais sensíveis nos materiais.

Se você estiver retomando um projeto em outro computador, peça ao agente para executar `git fetch --prune` e comparar a branch local com o upstream antes de analisar ou editar. Se o remoto estiver apenas à frente e a árvore estiver limpa, ele pode usar `git pull --ff-only`. Se houver divergência, integração remota com pendências ou sobreposição não preservável, ele deve mostrar o estado e pedir sua decisão, sem descartar ou integrar trabalho automaticamente.

Use `templates/BRIEF.template.md` quando quiser uma estrutura pronta para levantar as variáveis decisivas.

Se houver regra de negócio, identidade visual, textual ou sonora, contrato técnico ou dado que seja caro de quebrar, registre somente esses pontos em `templates/INVARIANTES.template.md`. Não crie o arquivo por reflexo.

## Etapa 1: Descoberta sem código

Use este prompt:

```text
Estamos começando um projeto do zero.

Não escreva código ainda.

Aproveite o briefing existente, sem reescrever respostas consolidadas. Pergunte apenas o que falta. Se houver dúvida bloqueante, aguarde a resposta antes de recomendar stack.

Com o contexto suficiente, faça:
1. Confirme o problema somente se houver ambiguidade.
2. Separe MVP, fase 2 e futuro.
3. Liste riscos técnicos, de segurança, legais e de produto.
4. Antes de sugerir stack, levante variáveis decisivas que possam mudar arquitetura, IA, banco, custo, segurança ou deploy.
5. Faça até 8 perguntas críticas, apenas se forem necessárias. Inclua, se aplicável: usuários simultâneos, dados sensíveis, uso de IA, integrações, autenticação, multi-cliente, hospedagem, orçamento, uso comercial e licenças.
6. Proponha até 2 modelos de stack, com prós, contras, riscos e quando escolher cada uma.
7. Recomende uma das stacks e explique por quê.
8. Proponha o menor primeiro contrato verificável.
9. Declare se o briefing está pronto para stack/MVP ou bloqueado, informando a decisão afetada, lacunas bloqueantes e premissas reversíveis.

Contexto:
[cole aqui o briefing]
```

Saída esperada:

- problema confirmado, sem repetir o briefing;
- MVP e fases;
- variáveis decisivas respondidas ou pendentes;
- até 2 stacks comparadas;
- recomendação final;
- riscos;
- perguntas críticas;
- primeira fatia verificável.
- estado de prontidão e motivo.

## Etapa 2: Aprovação humana

Você aprova ou ajusta:

- stack;
- MVP;
- não escopo;
- primeira fatia;
- riscos aceitos;
- integrações;
- dependências externas;
- dados sensíveis;
- restrições de licenciamento.

Não deixe o agente decidir sozinho banco, autenticação, autorização, dependências pagas, licenças duvidosas, uso comercial, dados reais ou deploy.

## Etapa 3: Base inicial com templates

Use este prompt:

```text
Agora crie a base inicial do projeto, mas ainda não implemente a feature principal.

Use os templates oficiais do framework em:
[caminho do repositório metodo-pacto]/templates

Crie ou atualize somente arquivos aplicáveis. Preserve contratos existentes; não preencha campos irrelevantes:

- BRIEF.md, se for útil manter o briefing no repositório
- INVARIANTES.md, se houver verdade crítica de negócio, identidade ou contrato/dado a preservar
- README.md
- AGENTS.md
- .pacto/validacao.md, cópia de docs/validacao-proporcional.md do repositório do método
- CLAUDE.md, se aplicável
- SPEC.md
- .env.example, se aplicável
- PLAN.md, se o plano precisar sobreviver ao chat
- estrutura inicial do projeto
- configuração mínima de build/test/lint, se aplicável

Regras:
- não implemente a feature principal ainda;
- não invente stack além da aprovada;
- não inclua segredos reais;
- não adicione dependências sem licença/termos compatíveis;
- mantenha os docs curtos;
- classifique a base como marco `T3` e rode smoke clássico somente para provar que ela instala e roda;
- não abra navegador por reflexo, a menos que a base tenha fluxo visual funcional que precise ser comprovado.

Ao final, informe:
- arquivos criados;
- comandos disponíveis;
- validações executadas;
- o que ainda falta antes da primeira fatia.
```

Saída esperada:

- documentação-base;
- setup técnico mínimo;
- comandos conhecidos;
- validação inicial;
- nenhuma feature principal implementada.

## Etapa 4: Revisar a base

Antes de seguir, confira:

- `SPEC.md` tem objetivo, não objetivos, critérios de aceite e verificação?
- se houver `INVARIANTES.md`, a SPEC identifica os itens afetados e a prova de preservação ou mudança aprovada?
- `AGENTS.md` está curto?
- A versão está identificada e a política local `.pacto/validacao.md` está disponível?
- `CLAUDE.md` usa a ponte curta para `AGENTS.md`, se aplicável?
- se o projeto usa Git remoto, o agente verificou se a branch local está sincronizada, à frente, atrás ou divergente antes de retomar?
- `.env.example` não tem segredo real?
- as dependências têm licença/termos aceitáveis?
- existe pelo menos uma verificação confiável?
- o projeto instala e roda?
- o nível de validação de cada checkpoint está definido como `T0`, `T1`, `T2` ou `T3` quando não for óbvio?
- há turning point que exige backup mínimo ou pasta de obsoletos?

## Etapa 5: Primeira fatia vertical

Use este prompt:

```text
Implemente apenas o checkpoint 1 da SPEC.md.

Regras:
- não implemente checkpoints futuros;
- mantenha o diff pequeno;
- classifique o checkpoint silenciosamente como `T0`, `T1`, `T2` ou `T3`;
- respeite a fronteira T0/T1 do AGENTS e consulte a política local somente pelo gatilho aplicável;
- em `T0`, não rode teste, navegador, build, lint, typecheck, checklist ou plano de teste;
- em `T1`, rode apenas uma prova curta; em `T2`, somente o necessário; em `T3`, smoke clássico e verificações relevantes;
- verifique segurança, dados e licenciamento se tocar dependência ou entrada externa;
- se for turning point, avalie backup mínimo e obsoletos antes de alterar;
- não abra navegador ou capture screenshot por reflexo;
- pare ao concluir o checkpoint 1 e resuma.
```

Saída esperada:

- primeira funcionalidade real;
- validação correspondente ao nível do checkpoint, quando aplicável;
- resumo do que mudou;
- próximos checkpoints ainda não implementados.

## Etapa 6: Revisão

Use este prompt:

```text
Revise o diff atual contra SPEC.md.

Procure:
- bug;
- regressão;
- em bug, caminhos irmãos pela causa e comportamento, não só pelo nome, sem auditoria global;
- escopo extra;
- validação faltante proporcional ao risco;
- risco de segurança;
- risco legal/licenciamento;
- dados sensíveis;
- problemas de UX, se houver UI.

Não implemente nada ainda. Apenas revise.
```

Depois da revisão, corrija apenas problemas reais e siga para a próxima fatia.
