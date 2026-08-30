# Regras Universais

Criador: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

Estas regras valem para desenvolvimento de qualquer solução com agente de código, independentemente de stack, linguagem, framework, banco ou tipo de produto.

## 1. Segurança

- Nunca colocar segredos reais no código, testes, documentação, logs, screenshots ou commits.
- Tratar como segredo: API key, token, senha, cookie, certificado, chave privada, credencial de banco, webhook secret e URL com credencial embutida.
- Se o usuário fornecer um segredo no chat, avisar de forma breve sobre o risco de exposição, mas não bloquear a tarefa somente por esse envio. O chat não substitui um mecanismo de gestão de segredos.
- Não repetir, revelar, gravar, versionar ou incluir o segredo fornecido no chat em comandos visíveis, arquivos, prompts reutilizáveis, logs, screenshots, relatórios ou commits.
- Quando for necessário usar um segredo fornecido no chat, usar apenas o mecanismo seguro disponível no ambiente, como variável de ambiente temporária, secret manager ou mecanismo equivalente da stack. Evitar passá-lo como argumento de linha de comando.
- Recomendar a rotação da chave se ela puder ter sido exposta a pessoas não autorizadas, em canal público ou em local persistente inadequado.
- Usar variáveis de ambiente, secrets do ambiente, vault ou mecanismo equivalente da stack.
- Manter `.env.example` apenas com valores fictícios quando houver configuração por ambiente.
- Validar toda entrada externa antes de processar, persistir ou executar: usuário, API, webhook, upload, arquivo, áudio, imagem, planilha, prompt, HTML, URL, query string e dados de terceiros.
- Não expor dados sensíveis em logs, mensagens de erro, respostas de API, fixtures, seeds ou analytics.
- Separar dados reais de dados de desenvolvimento, teste e demonstração.
- Usar menor privilégio para usuários, serviços, tokens, banco, storage, filas, APIs, CI/CD e permissões do agente.
- Pedir aprovação humana antes de ações destrutivas, migrações de dados, mudanças de permissão, deploy em produção, envio externo de mensagens ou manipulação de dados reais.
- Se a tarefa tocar segurança, dados, banco, autenticação, autorização, pagamento, produção ou clientes reais, tratar como tarefa crítica.

## 2. Licenciamento e Risco Legal

- Antes de adicionar dependência, biblioteca, template, fonte, ícone, imagem, áudio, vídeo, modelo de IA, dataset, SDK, API, plugin ou serviço externo, confirmar se a licença/termos permitem o uso pretendido.
- Não assumir que algo pode ser usado comercialmente apenas porque está público, gratuito ou disponível no GitHub.
- "Source-available", "free for personal use", "non-commercial" e "research only" exigem bloqueio ou validação humana antes de uso comercial.
- Verificar se há obrigações de atribuição, copyright notice, copyleft, redistribuição de código, abertura de código derivado, restrição de SaaS, uso de marca, patente, privacidade ou treinamento de IA.
- Para dependência nova de produção, registrar quando relevante: nome, fonte, licença/termos, uso no projeto, permissão comercial, obrigações e alternativa considerada.
- Se a licença ou os termos não forem claros, não prosseguir por inferência. Parar e pedir validação humana.
- Não copiar código, imagens, textos, datasets, templates ou prompts de origem incerta para dentro do projeto.

## 3. Validação Proporcional

Sempre classificar o risco da alteração, mas não testar tudo sempre. A política completa está em `docs/validacao-proporcional.md`.

- `T0: direta`: para texto, cor, espaçamento, posição estática, ajuste visual isolado, comentário ou documentação simples. Não rodar teste, navegador, build, lint, typecheck, checklist ou plano de teste. O agente só confere o diff silenciosamente.
- `T1: leve`: para comportamento local, regra pequena, endpoint simples ou configuração com risco local. Rodar somente uma prova curta e determinística.
- `T2: relevante`: para integração, banco, autenticação, vários módulos, fluxo funcional de UI ou risco de regressão. Executar apenas as validações necessárias e pedir ao usuário somente o que exigir percepção humana ou ambiente real.
- `T3: marco`: para fechamento de fase, PR relevante, release, deploy ou fluxo crítico. Smoke clássico é obrigatório, junto dos testes realmente aplicáveis.
- Navegador, screenshot e inspeção visual não são padrão para toda mudança de UI. Usar apenas por pedido explícito, requisito da `SPEC.md`, fluxo funcional relevante, fechamento visual de fase ou investigação de falha.
- `Smoke test`: checagem rápida de que o essencial sobe e responde. É obrigatório ao fechar uma fase com comportamento executável e antes de PR relevante, release ou deploy.
- `Unit test`: para regra, função, componente ou módulo isolado. `Integration test`: para fronteiras entre partes. `E2E test`: para jornadas críticas. Não executar todos por reflexo.
- `Regression test`: criar ou atualizar quando um bug for corrigido, se for viável e proporcional ao risco.
- `Accessibility test`, `performance/load test`, `fuzz/property test` e `spider/crawl` só entram quando o risco ou a fase justificar. Spider/crawl é descoberta, não substitui teste funcional.
- Teste manual é aceitável quando a automação não existe ou não compensa. Em `T2` e `T3`, deve ter passos e resultado esperado. Em `T0` e `T1`, não criar lista para o usuário por padrão.

## 4. Codificação, Idioma e Mojibake

- Todo arquivo textual criado ou editado deve ser salvo em UTF-8.
- Ao escrever em português do Brasil, usar acentuação e caracteres corretos: ç, ã, õ, á, é, í, ó, ú, â, ê, ô, à.
- Não aceitar mojibake em arquivos, chat, documentos ou UI. Exemplos de erro: `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“`, `Â`.
- Se o terminal mostrar caracteres quebrados, não assumir imediatamente que o arquivo está errado. Verificar a codificação real do arquivo antes de reescrever.
- Se o arquivo estiver com mojibake real, corrigir o texto mantendo o conteúdo e salvar novamente em UTF-8.
- Para HTML, declarar `<meta charset="utf-8">`.
- Para respostas JSON, APIs, importações e exportações, garantir `UTF-8` no transporte ou na configuração equivalente da stack.
- Não "resolver" removendo acentos. Em pt-BR, a saída correta deve preservar a acentuação.

## 5. Escrita Natural e Pontuação

- Não usar travessões em textos explicativos, documentação, UI, prompts, mensagens de erro ou respostas de agentes, exceto quando for indispensável preservar uma citação literal.
- Ajustar a pontuação com vírgulas, parênteses, dois-pontos, ponto e vírgula ou reestruturação das frases, para manter leitura fluida, clara e gramaticalmente correta.
- Evitar construções artificiais ou excessivamente padronizadas que deixem o texto com aparência genérica de saída de IA.
- Hífens continuam permitidos quando forem necessários em palavras compostas, identificadores, comandos, URLs, listas Markdown, sintaxe ou termos técnicos.

## 6. Obsoletos, Backups e Turning Points

- Git ou outro versionamento deve ser a fonte primária de histórico.
- Pastas de obsoletos e backups são exceções úteis, não substitutos de versionamento.
- Antes de mudança grande, avaliar se ela é um turning point.
- Turning points incluem: troca de stack, migração de banco, refatoração grande, reestruturação de UI, substituição de protótipo funcional, remoção de muitos arquivos, integração crítica ou operação destrutiva.
- Se arquivos deixarem de ser usados, mas ainda forem úteis como referência temporária, mover para `_archive/obsolete/YYYY-MM-DD_descricao/`.
- Se for necessário preservar um snapshot além do Git, criar backup mínimo em `_archive/backups/YYYY-MM-DD_HHMM_descricao/`.
- Toda pasta de backup ou obsoleto deve ter `README.md` explicando data, motivo, origem, conteúdo e condição de remoção futura.
- Não copiar dependências, caches, builds, arquivos temporários ou artefatos recriáveis para backups.
- Não criar backup por reflexo em toda alteração pequena.
- Se houver dúvida, o agente deve perguntar antes de mover, copiar ou arquivar arquivos.

## 7. Critério Prático

Antes de implementar, responder:

```text
Pronto significa: [resultado observável]
Nível de validação: [T0, T1, T2 ou T3]
Verificado por: [somente a prova proporcional, ou não aplicável em T0]
Teste do usuário: [nenhum, ou uma ação humana específica em T2/T3]
Risco legal/segurança: [nenhum, baixo, médio, alto, ou pendente de validação]
Codificação/idioma: [UTF-8 preservado, se houver texto em pt-BR]
Escrita: [sem travessões e com pontuação natural, se houver texto destinado a pessoas]
Turning point/backups: [não aplicável, coberto por Git, ou backup/obsoleto necessário]
```

Se qualquer uma dessas respostas estiver vaga em tarefa relevante, a implementação ainda não deve começar.
