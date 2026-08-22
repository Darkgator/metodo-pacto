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
- Não escreva código antes de entender o escopo da tarefa.
- Em projeto novo ou decisão de stack, levante variáveis decisivas antes de recomendar arquitetura: usuários simultâneos, dados, IA, segurança, integrações, operação, custo, licenciamento e risco legal.
- Para mudanças grandes, planeje antes de implementar.
- Depois de editar, rode os comandos de validação aplicáveis.
- Se falhar 3 vezes seguidas no mesmo erro, pare, mostre o erro e peça orientação.
- Nunca inclua segredos reais no código, testes, documentação, logs ou commits.
- Se o usuário fornecer uma chave no chat, avise brevemente sobre o risco, mas não bloqueie a tarefa somente por isso. Não repita, revele, grave ou inclua a chave em comandos visíveis, arquivos, logs, screenshots ou commits.
- Use credenciais fornecidas no chat apenas pelo mecanismo seguro disponível no ambiente. Prefira variável de ambiente ou secret manager e recomende rotação se houver exposição a pessoas não autorizadas.
- Não adicione dependências, assets, modelos, datasets, APIs ou serviços externos sem confirmar licença/termos e compatibilidade com o uso pretendido.
- Para mudanças com segurança, dados, banco, autenticação, autorização, produção ou clientes reais, peça aprovação antes de executar ações de risco.
- Salve arquivos textuais em UTF-8 e preserve acentuação correta em pt-BR.
- Não aceite mojibake como `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“` ou `Â`; verifique se é problema real do arquivo ou apenas visualização do terminal antes de corrigir.
- Não use travessões em textos explicativos, documentação, UI, prompts ou respostas. Prefira vírgulas, parênteses ou frases reestruturadas, com pontuação fluida e gramaticalmente correta.

## Arquivos de Contexto

- `AGENTS.md`: regras gerais para agentes.
- `SPEC.md`: escopo e checklist da fase atual.
- `docs/PRODUCT.md`: regras de negócio, se existir.
- `docs/UI.md`: diretrizes visuais, se existir.
- `docs/DATA_MODEL.md`: modelo de dados, se existir.
