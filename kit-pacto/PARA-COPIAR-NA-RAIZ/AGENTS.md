# Instruções do Projeto

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Propósito

Este projeto segue o Método PACTO: Preparar, Avaliar, Contratar, Trabalhar e Observar. A aplicação deve seguir o escopo aprovado, manter rastreabilidade suficiente e ser verificada na proporção do risco.

## Leitura eficiente de contexto

- Antes de agir, inspecione a estrutura imediata do projeto e os arquivos modificados relevantes. Não leia todo o repositório nem todos os documentos por padrão.
- Leia `SPEC.md` antes de implementar mudança de produto, comportamento, arquitetura ou fase.
- Leia `PLAN.md` antes de trabalho multiarquivo, mudança complexa, investigação longa ou execução em etapas.
- Leia `BRIEF.md` quando houver ambiguidade de problema, público, objetivo, restrição ou critério de sucesso.
- Leia documentação técnica específica apenas quando a tarefa tocar aquele assunto.
- Se faltar contexto decisivo, faça perguntas objetivas antes de escolher stack, arquitetura, IA, integração, hospedagem ou banco de dados.

## Fluxo PACTO

1. Preparar: entender problema, contexto, variáveis decisivas e riscos; registrar em `BRIEF.md` quando aplicável.
2. Avaliar: separar MVP, próxima fase e futuro; comparar no máximo duas opções de stack quando ainda não houver decisão.
3. Contratar: transformar a decisão aprovada em escopo verificável em `SPEC.md`.
4. Trabalhar: manter `PLAN.md` para mudanças complexas e implementar a menor fatia verificável, sem extrapolar a SPEC.
5. Observar: executar validações aplicáveis, registrar limitações e atualizar os contratos quando o comportamento ou a decisão mudar.

## Regras de execução

- Não escreva código, crie dependências nem escolha stack antes de entender o escopo e receber a aprovação necessária.
- Não implemente fora do escopo aprovado em `SPEC.md`.
- Para mudanças simples, execute diretamente e valide. Para mudanças complexas, apresente ou atualize um plano antes de editar.
- Após três tentativas consecutivas no mesmo erro, pare, apresente evidências e peça orientação.
- Preserve os padrões existentes do projeto. Não faça refatorações alheias à tarefa.
- Git é a fonte primária de histórico. Antes de um turning point, avalie backup mínimo ou arquivamento em `_archive/`.

## Segurança e dados

- Nunca exponha chaves, tokens, senhas, credenciais, dados pessoais, dados de clientes ou segredos em código, documentação, prompts, exemplos, testes, fixtures, logs, screenshots ou commits.
- Se o usuário fornecer uma chave no chat, avise brevemente sobre o risco de exposição, mas não bloqueie a tarefa somente por isso. Não repita, revele, grave ou inclua a chave em comandos visíveis, arquivos, logs, screenshots ou commits.
- Use credenciais fornecidas no chat apenas pelo mecanismo seguro disponível no ambiente. Prefira variável de ambiente ou secret manager e recomende rotação se houver exposição a pessoas não autorizadas.
- Use variáveis de ambiente e mantenha exemplos com valores fictícios.
- Valide entradas externas antes de processar, persistir ou encaminhar dados.
- Ações destrutivas, migrações, remoções grandes, mudanças de autenticação/autorização, deploys e uso de dados reais exigem aprovação humana explícita.
- Aplique o menor privilégio necessário a usuários, agentes, tokens, bancos, storage, APIs e serviços.

## Licença, privacidade e risco legal

- Antes de adicionar dependência, asset, fonte, ícone, modelo de IA, dataset, SDK, API, plugin ou serviço externo, confirme licença e termos para o uso pretendido.
- Gratuito, source-available ou uso pessoal não significam permissão comercial, redistribuição ou SaaS.
- Em dúvida sobre licença, copyleft, atribuição, privacidade, LGPD, marca, patente, retenção de dados ou transferência para IA externa, sinalize o risco e peça decisão humana.

## Qualidade e verificação

- Toda entrega deve ter uma forma objetiva de verificação: teste, build, lint, typecheck, inspeção manual, screenshot, smoke test ou outro sinal adequado.
- Escolha o menor teste confiável para a mudança e amplie a cobertura quando o risco justificar.
- Use smoke para fluxos essenciais; unitário para regras isoladas; integração para fronteiras; E2E para jornadas críticas. Spider/crawl serve para descoberta de rotas e links, não substitui testes funcionais.
- Ao corrigir defeito, adicione ou atualize uma proteção contra regressão quando for viável.

## UTF-8 e pt-BR

- Salve arquivos textuais em UTF-8.
- Ao escrever em pt-BR, use acentuação correta: ç, ã, õ, á, é, í, ó, ú, â, ê, ô e à.
- Não remova acentos para contornar problemas de codificação.
- Não aceite mojibake como `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“` ou `Â`. Antes de corrigir, confirme se o problema está no arquivo ou somente na exibição do terminal.

## Escrita Natural

- Não use travessões em textos explicativos, documentação, UI, prompts ou respostas. Prefira vírgulas, parênteses, dois-pontos, ponto e vírgula ou frases reestruturadas, mantendo leitura fluida, clara e gramaticalmente correta.
- Hífens necessários em termos técnicos, identificadores, comandos, URLs, listas Markdown ou sintaxe continuam permitidos.
