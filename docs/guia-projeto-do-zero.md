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

Use `templates/BRIEF.template.md` quando quiser uma estrutura pronta para levantar as variáveis decisivas.

## Etapa 1: Descoberta sem código

Use este prompt:

```text
Estamos começando um projeto do zero.

Não escreva código ainda.

Leia o contexto abaixo e faça:
1. Reescreva o problema em linguagem objetiva.
2. Separe MVP, fase 2 e futuro.
3. Liste riscos técnicos, de segurança, legais e de produto.
4. Antes de sugerir stack, levante variáveis decisivas que possam mudar arquitetura, IA, banco, custo, segurança ou deploy.
5. Faça até 8 perguntas críticas, apenas se forem necessárias. Inclua, se aplicável: usuários simultâneos, dados sensíveis, uso de IA, integrações, autenticação, multi-cliente, hospedagem, orçamento, uso comercial e licenças.
6. Proponha até 2 modelos de stack, com prós, contras, riscos e quando escolher cada uma.
7. Recomende uma das stacks e explique por quê.
8. Proponha o menor primeiro contrato verificável.

Contexto:
[cole aqui o briefing]
```

Saída esperada:

- problema reescrito;
- MVP e fases;
- variáveis decisivas respondidas ou pendentes;
- até 2 stacks comparadas;
- recomendação final;
- riscos;
- perguntas críticas;
- primeira fatia verificável.

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
C:\Users\abmme\OneDrive\CODE\framework-agentic-code\templates

Crie ou atualize:
- BRIEF.md, se for útil manter o briefing no repositório
- README.md
- AGENTS.md
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
- rode a validação mínima possível.

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
- `AGENTS.md` está curto?
- `CLAUDE.md` aponta para `AGENTS.md` e `SPEC.md`?
- `.env.example` não tem segredo real?
- as dependências têm licença/termos aceitáveis?
- existe pelo menos uma verificação confiável?
- o projeto instala e roda?
- há turning point que exige backup mínimo ou pasta de obsoletos?

## Etapa 5: Primeira fatia vertical

Use este prompt:

```text
Implemente apenas o checkpoint 1 da SPEC.md.

Regras:
- não implemente checkpoints futuros;
- mantenha o diff pequeno;
- atualize testes ou validação mínima;
- verifique segurança, dados e licenciamento se tocar dependência ou entrada externa;
- se for turning point, avalie backup mínimo e obsoletos antes de alterar;
- rode o menor comando confiável que prova a fatia;
- pare ao concluir o checkpoint 1 e resuma.
```

Saída esperada:

- primeira funcionalidade real;
- teste ou validação;
- resumo do que mudou;
- próximos checkpoints ainda não implementados.

## Etapa 6: Revisão

Use este prompt:

```text
Revise o diff atual contra SPEC.md.

Procure:
- bug;
- regressão;
- escopo extra;
- ausência de teste;
- risco de segurança;
- risco legal/licenciamento;
- dados sensíveis;
- problemas de UX, se houver UI.

Não implemente nada ainda. Apenas revise.
```

Depois da revisão, corrija apenas problemas reais e siga para a próxima fatia.
