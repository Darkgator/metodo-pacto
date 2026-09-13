# CLAUDE.md

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Regras

- `SPEC.md` é a fonte de verdade da fase atual.
- `AGENTS.md` contém as regras operacionais para agentes.
- `BRIEF.md` contém o contexto consolidado do projeto.
- `PLAN.md` contém a sequência de continuidade.
- Antes de iniciar ou retomar trabalho em um repositório Git com remoto, execute `git fetch --prune` e compare a branch local com o upstream. Não edite antes de saber se o local está sincronizado, à frente, atrás ou divergente. Use `git pull --ff-only` somente com árvore limpa e avanço remoto sem conflito. Em divergência ou alterações locais pendentes, peça decisão. Nunca use `reset`, descarte, `stash`, `rebase`, `merge` ou `force push` sem aprovação explícita.
- Não escreva código ou documentação nova antes de entender o escopo da tarefa.
- Para mudanças grandes, planeje antes de implementar.
- Para mudanças no método, atualize documentos, templates e guia visual quando aplicável.
- Siga `docs/validacao-proporcional.md`. Em `T0`, não rode teste, navegador, build, lint, typecheck, checklist ou plano de teste. Em `T1`, rode uma única prova curta; em `T2`, apenas o necessário; em `T3`, smoke clássico e verificações relevantes da fase.
- Nunca inclua segredos reais em código, docs, exemplos, prompts, logs ou commits.
- Se o usuário fornecer uma chave no chat, avise brevemente sobre o risco, mas não bloqueie a tarefa somente por isso. Não repita, revele, grave ou inclua a chave em comandos visíveis, arquivos, logs, screenshots ou commits.
- Use credenciais fornecidas no chat apenas pelo mecanismo seguro disponível no ambiente. Prefira variável de ambiente ou secret manager e recomende rotação se houver exposição a pessoas não autorizadas.
- Não adicione dependências, assets, modelos, datasets, APIs ou serviços externos sem confirmar licença/termos e compatibilidade com o uso pretendido.
- Para mudanças com segurança, dados, licenciamento, reestruturação grande, obsoletos, backups ou turning points, peça aprovação antes de executar ações de risco.
- Salve arquivos textuais em UTF-8 e preserve acentuação correta em pt-BR.
- Não aceite mojibake como `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“` ou `Â`; verifique se é problema real do arquivo ou apenas visualização do terminal antes de corrigir.
- Não use travessões em textos explicativos, documentação, UI, prompts ou respostas. Prefira vírgulas, parênteses ou frases reestruturadas, com pontuação fluida e gramaticalmente correta.

## Arquivos de Contexto

- `BRIEF.md`: contexto do projeto.
- `SPEC.md`: contrato da fase atual.
- `PLAN.md`: plano de continuidade.
- `AGENTS.md`: regras para agentes.
- `docs/regras-universais.md`: regras universais.
- `docs/validacao-proporcional.md`: política de validação por alteração, checkpoint, fase e release.
- `docs/variaveis-decisivas.md`: perguntas que mudam stack, IA, arquitetura, custo e deploy.
- `docs/gestao-obsoletos-backups.md`: regra para obsoletos, backups e turning points.
- `guia-visual/index.html`: guia visual atual.
