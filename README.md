# Método PACTO

Criador: Alexandre Barroso de Miranda
Atuação: Consultor de Processos

Repositório oficial: [github.com/Darkgator/metodo-pacto](https://github.com/Darkgator/metodo-pacto)

Método prático para desenvolver software com agentes de código, com contexto e validação proporcionais ao risco.

O método se chama **PACTO**: Preparar, Avaliar, Contratar, Trabalhar e Observar. O objetivo é chegar a um processo prático, independente de stack, que funcione bem com **Claude Code** e **Codex**, cobrindo tanto:

- um **manual/checklist de trabalho** para o usuário humano;
- um **kit inicial de arquivos e prompts** para novos projetos.

## Estado atual

Método consolidado com contratos proporcionais ao risco. templates/ é a fonte oficial; o kit distribui cópias idênticas dos cinco modelos principais. Documentos históricos são referências, não instruções de execução.

## Comece aqui

1. Abra o [kit e seus prompts](kit-pacto/LEIA-PRIMEIRO.md). Em projeto existente, preserve e adapte instruções que já existam, sem sobrescrevê-las por reflexo.
2. Use `AGENTS.md` e, para Claude Code, a ponte `CLAUDE.md`. Preencha os comandos do projeto no `AGENTS.md`.
3. Para tarefa simples, descreva resultado e limites no pedido. Para mudança relevante, preencha somente os campos necessários da `SPEC.md`. Use `BRIEF.md` se faltar contexto e `PLAN.md` se precisar de continuidade.
4. Execute a menor fatia verificável. Consulte o [guia do zero](docs/guia-projeto-do-zero.md) somente para projeto novo; o [guia visual](guia-visual/index.html) pode ser aberto localmente.

Os [templates](templates/) são a fonte oficial. O kit contém cópias idênticas dos cinco modelos principais, prontas para copiar com os nomes corretos. O método não exige instalação, serviço ou ferramenta adicional.

## Arquivos de referência

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
- `docs/framework-v1-proposta.md`: orientação vigente consolidada; o nome do arquivo foi preservado para manter os links.
- `docs/regras-universais.md`: regras universais de segurança, testes e risco legal.
- `docs/validacao-proporcional.md`: níveis T0 a T3 para decidir o que validar em uma alteração, checkpoint, fase ou release.
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

Licença e política de distribuição permanecem pendentes. Novas ferramentas e o piloto de custo são opcionais; economia de tokens por tarefa ainda não foi medida.
