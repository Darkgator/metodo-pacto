# CLAUDE.md

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Comandos

- Instalar: `[comando]`
- Desenvolvimento: `[comando]`
- Testes: `[comando]`
- Lint/formatador: `[comando]`
- Build: `[comando]`

## Regras

- `SPEC.md` é a fonte de verdade da fase atual.
- Antes de iniciar ou retomar trabalho em repositório Git com remoto, execute `git fetch --prune` e compare a branch local com o upstream. Não edite antes de saber se o local está sincronizado, à frente, atrás ou divergente. Use `git pull --ff-only` somente com árvore limpa e avanço remoto sem conflito. Em divergência ou alterações locais pendentes, peça decisão. Nunca use `reset`, descarte, `stash`, `rebase`, `merge` ou `force push` sem aprovação explícita.
- Não escreva código antes de entender o escopo da tarefa.
- Em projeto novo ou decisão de stack, levante variáveis decisivas antes de recomendar arquitetura: usuários simultâneos, dados, IA, segurança, integrações, operação, custo, licenciamento e risco legal.
- Para mudanças grandes, planeje antes de implementar.
- Siga a matriz `T0`, `T1`, `T2` e `T3` definida em `docs/validacao-proporcional.md`, se existir. Em `T0`, não rode teste, navegador, build, lint, typecheck, checklist ou plano de teste. Em `T1`, rode uma única prova curta. Em `T2`, valide somente o necessário. Em `T3`, rode smoke clássico e validações relevantes da fase.
- Se falhar 3 vezes seguidas no mesmo erro, pare, mostre o erro e peça orientação.
- Nunca inclua segredos reais no código, testes, documentação, logs ou commits.
- Se o usuário fornecer uma chave no chat, avise brevemente sobre o risco, mas não bloqueie a tarefa somente por isso. Não repita, revele, grave ou inclua a chave em comandos visíveis, arquivos, logs, screenshots ou commits.
- Use credenciais fornecidas no chat apenas pelo mecanismo seguro disponível no ambiente. Prefira variável de ambiente ou secret manager e recomende rotação se houver exposição a pessoas não autorizadas.
- Não adicione dependências, assets, modelos, datasets, APIs ou serviços externos sem confirmar licença/termos e compatibilidade com o uso pretendido.
- Para mudanças com segurança, dados, banco, autenticação, autorização, produção ou clientes reais, peça aprovação antes de executar ações de risco.
- Salve arquivos textuais em UTF-8 e preserve acentuação correta em pt-BR.
- Não aceite mojibake como `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“` ou `Â`; verifique se é problema real do arquivo ou apenas visualização do terminal antes de corrigir.
- Não use travessões em textos explicativos, documentação, UI, prompts ou respostas. Prefira vírgulas, parênteses ou frases reestruturadas, com pontuação fluida e gramaticalmente correta.
- Não abra navegador ou capture screenshot por reflexo. Use validação visual somente por pedido explícito, requisito da SPEC, fluxo funcional relevante ou fechamento visual de fase.

## Arquivos de Contexto

- `AGENTS.md`: regras gerais para agentes.
- `SPEC.md`: escopo e checklist da fase atual.
- `docs/PRODUCT.md`: regras de negócio, se existir.
- `docs/UI.md`: diretrizes visuais, se existir.
- `docs/DATA_MODEL.md`: modelo de dados, se existir.
