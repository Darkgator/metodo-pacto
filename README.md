# Método PACTO

Criador: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos

Repositório oficial: [github.com/Darkgator/metodo-pacto](https://github.com/Darkgator/metodo-pacto)

Projeto para construirmos, do zero e de forma iterativa, um framework de desenvolvimento de software com agentes de código.

O método se chama **PACTO**: Preparar, Avaliar, Contratar, Trabalhar e Observar. O objetivo é chegar a um processo prático, independente de stack, que funcione bem com **Claude Code** e **Codex**, cobrindo tanto:

- um **manual/checklist de trabalho** para o usuário humano;
- um **kit inicial de arquivos e prompts** para novos projetos.

## Estado atual

Este projeto está em rascunho. A versão inicial foi baseada nos seus prompts atuais e em uma pesquisa preliminar, mas ainda precisa ser confrontada com uma investigação mais profunda.

## Estrutura

- `BRIEF.md`: contexto consolidado do próprio projeto.
- `AGENTS.md`: regras operacionais para agentes atuarem neste projeto.
- `CLAUDE.md`: instruções específicas para Claude Code.
- `SPEC.md`: contrato da fase atual.
- `PLAN.md`: plano de continuidade.
- `docs/briefing-assistido.md`: etapa opcional para transformar uma ideia solta em briefing antes do agente de coding.
- `docs/gestao-obsoletos-backups.md`: regra para arquivar obsoletos e criar backups em turning points relevantes.
- `docs/variaveis-decisivas.md`: perguntas que precisam ser respondidas antes de stack, IA, arquitetura e deploy.
- `docs/resumo-atual.md`: resumo curto do que existe hoje.
- `docs/framework-v0-rascunho.md`: rascunho inicial completo, mantido como material de referência.
- `docs/sintese-pesquisa.md`: síntese dos relatórios de pesquisa aprofundada.
- `docs/framework-v1-proposta.md`: proposta v1, redesenhada a partir da pesquisa.
- `docs/regras-universais.md`: regras universais de segurança, testes e risco legal.
- `docs/guia-projeto-do-zero.md`: passo a passo operacional para começar um projeto novo.
- `docs/decisoes-abertas.md`: pontos que ainda precisamos decidir juntos.
- `guia-visual/index.html`: versão atual do fluxo visual "olhar e fazer", em estilo Claude/Claude Code.
- `guia-visual/index-v1-acessivel.html`: primeira versão preservada do guia visual.
- `guia-visual/index-v2-claude.html`: cópia versionada da versão atual em estilo Claude/Claude Code.
- `prompts/pesquisa-aprofundada.md`: prompt direto para pesquisar melhores práticas na internet.
- `prompts/briefing-assistido-customgpt.md`: prompt para criar um Custom GPT ou assistente de briefing antes do desenvolvimento.
- `research/`: relatórios originais usados como insumo.
- `templates/AGENTS.template.md`: modelo inicial de `AGENTS.md`.
- `templates/CLAUDE.template.md`: modelo inicial de `CLAUDE.md`.
- `templates/SPEC.template.md`: modelo inicial de `SPEC.md`.
- `templates/README.template.md`: modelo inicial de `README.md`.
- `templates/PLAN.template.md`: modelo opcional para plano persistente.
- `templates/BRIEF.template.md`: briefing inicial com variáveis decisivas.
- `templates/ARCHIVE-README.template.md`: modelo para documentar backups e obsoletos.
- `templates/ENV.template`: modelo base para `.env.example`.

## Próximo passo

1. Revisar `docs/framework-v1-proposta.md`.
2. Decidir se o nome e o loop "Contrato Primeiro" fazem sentido.
3. Ajustar os templates para refletir a v1.
4. Criar o kit inicial final.
