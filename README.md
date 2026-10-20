# Método PACTO

Criador: Alexandre Barroso de Miranda
Atuação: Consultor de Processos

Repositório oficial: [github.com/Darkgator/metodo-pacto](https://github.com/Darkgator/metodo-pacto)

Método prático para desenvolver software com agentes de código, com contexto e validação proporcionais ao risco.

O método se chama **PACTO**: Preparar, Avaliar, Contratar, Trabalhar e Observar. O objetivo é chegar a um processo prático, independente de stack, que funcione bem com **Claude Code** e **Codex**, cobrindo tanto:

- um **manual/checklist de trabalho** para o usuário humano;
- um **kit inicial de arquivos e prompts** para novos projetos.

## Estado atual

Kit `2026.10.19.2`: cinco modelos e uma política local sob demanda, com fontes oficiais em `templates/` e `docs/validacao-proporcional.md`. O BRIEF agora declara a decisão liberada, lacunas bloqueantes e premissas reversíveis. Documentos históricos são referências, não instruções de execução.

## Comece aqui

1. Abra o [kit e seus prompts](kit-pacto/LEIA-PRIMEIRO.md). Em projeto existente, preserve e adapte instruções que já existam, sem sobrescrevê-las por reflexo.
2. Copie `AGENTS.md` e a pasta `.pacto/` do kit para a raiz. Para Claude Code, acrescente a ponte `CLAUDE.md`. Preencha os comandos do projeto no `AGENTS.md`.
3. Para tarefa simples, descreva resultado e limites no pedido. Para mudança relevante, preencha somente os campos necessários da `SPEC.md`. Use `BRIEF.md` se faltar contexto e `PLAN.md` se precisar de continuidade.
4. Execute a menor fatia verificável. Consulte o [guia do zero](docs/guia-projeto-do-zero.md) somente para projeto novo; o [guia visual](guia-visual/index.html) pode ser aberto localmente.

Os [templates](templates/) são a fonte dos modelos. O kit inclui a política em `.pacto/validacao.md`, consultada por gatilho, não carregada por padrão em T0. O método não exige instalação, serviço ou ferramenta adicional. Atualizações preservam adaptações locais; publicar aqui não atualiza projetos antigos.

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
- [Benefícios observados](docs/evidencias-de-beneficios.md): catálogo de evidências, atribuição ao método e limites das promessas de economia e produtividade.
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

## Evidência e custo

Não há economia causal de tokens ou tempo demonstrada. Menos texto permanente não garante menos consumo por tarefa. Em comparação autorizada, registre escopo, qualidade, trabalho humano e contadores disponíveis; cache já integra a entrada e tokens não equivalem diretamente a dinheiro ou quota. [Critérios de avaliação](docs/evidencias-de-beneficios.md#como-avaliar-a-próxima-versão).

## Próximo passo

Usar o kit em uma próxima entrega autorizada, observando as provas e limitações reais. Novos experimentos e ferramentas continuam opcionais. A licença final permanece pendente.
