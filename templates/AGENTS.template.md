# AGENTS.md

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Visão do Projeto

[Explique em 3 a 6 linhas o que este projeto faz, para quem e qual problema resolve.]

## Comandos

- Instalar dependências: `[comando]`
- Rodar em desenvolvimento: `[comando]`
- Testes: `[comando]`
- Lint/formatador: `[comando]`
- Build: `[comando]`

## Fluxo de Trabalho

- Leia `SPEC.md` antes de implementar qualquer mudança de produto.
- Em projeto novo ou decisão de stack, avalie variáveis decisivas antes de recomendar arquitetura: usuários simultâneos, dados, IA, segurança, integrações, operação, custo, licenciamento e risco legal.
- Para mudanças complexas ou multiarquivo, proponha um plano antes de editar.
- Trabalhe em fatias pequenas e verificáveis.
- Não implemente fora do escopo aprovado.
- Após 3 tentativas consecutivas no mesmo erro, pare, mostre o erro e peça orientação.

## Segurança

- Nunca inclua chaves reais, tokens, senhas ou credenciais no código, testes, documentação ou commits.
- Se o usuário fornecer uma chave no chat, avise brevemente sobre o risco de exposição, mas não bloqueie a tarefa somente por isso. Não repita, revele, grave ou inclua a chave em comandos visíveis, arquivos, logs, screenshots ou commits.
- Use credenciais fornecidas no chat apenas pelo mecanismo seguro disponível no ambiente. Prefira variável de ambiente ou secret manager e recomende rotação se houver exposição a pessoas não autorizadas.
- Use variáveis de ambiente.
- Mantenha `.env.example` com valores fictícios.
- Valide toda entrada externa antes de processar ou persistir.
- Não exponha dados sensíveis em logs, mensagens de erro, screenshots ou fixtures.
- Ações destrutivas, mudanças em autenticação/autorização, migrações de dados, deploys e uso de dados reais exigem aprovação humana explícita.
- Use o menor privilégio necessário para contas, tokens, serviços, banco, storage, APIs e permissões do agente.

## Licenciamento e Risco Legal

- Antes de adicionar dependência, asset, fonte, ícone, modelo de IA, dataset, SDK, API, plugin ou serviço externo, confirme se a licença/termos permitem o uso pretendido.
- "Gratuito", "source-available" e "free for personal use" não significam liberação para uso comercial.
- Se houver dúvida sobre uso comercial, redistribuição, SaaS, copyleft, atribuição, privacidade, marca ou patente, pare e peça validação humana.
- Para dependências novas de produção, registre nome, fonte, licença/termos, motivo de uso e obrigações relevantes quando aplicável.

## Qualidade

- Siga os padrões existentes do projeto.
- Atualize testes junto com mudanças de comportamento.
- Rode as validações aplicáveis antes de concluir.
- Use Git como fonte primária de histórico.
- Antes de turning points, avalie se é necessário backup mínimo ou mover obsoletos para `_archive/`.
- Turning points incluem migração de banco, troca de stack, refatoração grande, reestruturação de UI, substituição de protótipo, remoção de muitos arquivos, integração crítica ou operação destrutiva.
- Não faça backup por reflexo em alteração pequena.
- Não arquive dependências, caches, builds ou arquivos recriáveis.
- Salve arquivos textuais em UTF-8.
- Ao escrever em pt-BR, preserve acentuação correta e caracteres como ç, ã, õ, á, é, í, ó, ú, â, ê, ô e à.
- Não aceite mojibake como `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“` ou `Â`; verifique se o problema está no arquivo ou apenas na visualização do terminal antes de corrigir.
- Não remova acentos para contornar problema de codificação.
- Não use travessões em textos explicativos, documentação, UI, prompts ou respostas. Prefira vírgulas, parênteses ou frases reestruturadas, com pontuação fluida e gramaticalmente correta.
- Hífens necessários em termos técnicos, identificadores, comandos, URLs, listas Markdown ou sintaxe continuam permitidos.

## Testes e Verificação

- Todo trabalho deve ter uma forma clara de verificação: teste automatizado, build, lint, typecheck, screenshot, inspeção manual ou outro sinal objetivo.
- Escolha o menor teste confiável para a mudança e amplie quando o risco justificar.
- Use smoke tests para checar rapidamente fluxos essenciais após setup, deploy ou mudanças críticas.
- Use testes unitários para regras isoladas, integração para fronteiras entre módulos e E2E para jornadas críticas.
- Crie ou atualize teste de regressão ao corrigir bug.
- Para UI, valide estados, responsividade e acessibilidade básica quando aplicável.
- Use spider/crawl apenas como descoberta de rotas, links e superfície exposta; isso não substitui smoke, integração ou E2E.
