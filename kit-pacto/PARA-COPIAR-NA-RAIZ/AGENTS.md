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

- Classifique a alteração silenciosamente como `T0`, `T1`, `T2` ou `T3`.
- `T0`: texto, cor, espaçamento, posição estática, ajuste visual isolado, comentário ou documentação simples. Faça a alteração e confira o diff silenciosamente. Não rode teste, navegador, build, lint, typecheck, checklist ou plano de teste.
- `T1`: comportamento local, regra pequena, endpoint simples ou configuração com risco local. Rode somente uma prova curta e determinística.
- `T2`: integração, banco, autenticação, vários módulos, fluxo funcional de UI ou risco de regressão. Execute somente as validações necessárias e peça ao usuário apenas o que exigir percepção humana ou ambiente real.
- `T3`: fechamento de fase, PR relevante, release, deploy ou fluxo crítico. Rode smoke clássico obrigatório e os testes relevantes definidos para a fase.
- Não abra navegador nem capture screenshot por reflexo. Use validação visual apenas por pedido explícito, requisito da SPEC, fluxo funcional relevante, fechamento visual de fase ou investigação de falha.
- Use unitário para regra isolada, integração para fronteira entre módulos e E2E para jornada crítica. Não execute todos por padrão. Spider/crawl serve para descoberta de rotas e links, não substitui teste funcional.
- Ao corrigir defeito, adicione ou atualize teste de regressão quando for viável e proporcional ao risco.

## UTF-8 e pt-BR

- Salve arquivos textuais em UTF-8.
- Ao escrever em pt-BR, use acentuação correta: ç, ã, õ, á, é, í, ó, ú, â, ê, ô e à.
- Não remova acentos para contornar problemas de codificação.
- Não aceite mojibake como `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“` ou `Â`. Antes de corrigir, confirme se o problema está no arquivo ou somente na exibição do terminal.

## Escrita Natural

- Não use travessões em textos explicativos, documentação, UI, prompts ou respostas. Prefira vírgulas, parênteses, dois-pontos, ponto e vírgula ou frases reestruturadas, mantendo leitura fluida, clara e gramaticalmente correta.
- Hífens necessários em termos técnicos, identificadores, comandos, URLs, listas Markdown ou sintaxe continuam permitidos.
