# Regras Universais

Criador: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

Estas regras valem para desenvolvimento de qualquer solução com agente de código, independentemente de stack, linguagem, framework, banco ou tipo de produto.

## 1. Segurança

- Nunca colocar segredos reais no código, testes, documentação, logs, screenshots ou commits.
- Tratar como segredo: API key, token, senha, cookie, certificado, chave privada, credencial de banco, webhook secret e URL com credencial embutida.
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

## 3. Testes e Verificação

Todo trabalho precisa ter uma forma clara de prova. O tipo de teste depende do risco e do tipo de mudança.

- `Smoke test`: checagem rápida de que o essencial sobe e responde. Usar em setup, deploy, mudanças críticas e fluxos principais.
- `Unit test`: valida regra, função, componente ou módulo isolado. Usar para lógica de negócio, cálculos, parsing e transformação de dados.
- `Integration test`: valida a comunicação entre partes. Usar para API + banco, serviço + fila, autenticação + sessão, componente + estado ou integrações externas mockadas.
- `E2E test`: valida jornada real do usuário. Usar para fluxos críticos, não para todas as combinações.
- `Regression test`: criado ou atualizado quando um bug é corrigido para impedir que o problema volte.
- `Accessibility test`: usar quando houver interface relevante. Deve cobrir pelo menos labels, navegação, foco, contraste e estados básicos.
- `Performance/load test`: usar quando tempo de resposta, concorrência, volume, escala ou custo operacional forem riscos.
- `Fuzz/property test`: usar quando entradas malformadas, parsers, importadores, segurança ou robustez forem relevantes.
- `Spider/crawl`: usar para descobrir rotas, links, páginas quebradas e superfície exposta. É descoberta, não substitui smoke, integração ou E2E.
- Teste manual é aceitável quando automação ainda não existe, mas deve ter passos claros, entrada esperada e resultado esperado.

## 4. Codificação, Idioma e Mojibake

- Todo arquivo textual criado ou editado deve ser salvo em UTF-8.
- Ao escrever em português do Brasil, usar acentuação e caracteres corretos: ç, ã, õ, á, é, í, ó, ú, â, ê, ô, à.
- Não aceitar mojibake em arquivos, chat, documentos ou UI. Exemplos de erro: `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“`, `Â`.
- Se o terminal mostrar caracteres quebrados, não assumir imediatamente que o arquivo está errado. Verificar a codificação real do arquivo antes de reescrever.
- Se o arquivo estiver com mojibake real, corrigir o texto mantendo o conteúdo e salvar novamente em UTF-8.
- Para HTML, declarar `<meta charset="utf-8">`.
- Para respostas JSON, APIs, importações e exportações, garantir `UTF-8` no transporte ou na configuração equivalente da stack.
- Não "resolver" removendo acentos. Em pt-BR, a saída correta deve preservar a acentuação.

## 5. Obsoletos, Backups e Turning Points

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

## 6. Critério Prático

Antes de implementar, responder:

```text
Pronto significa: [resultado observável]
Verificado por: [teste, comando, revisão, screenshot ou validação manual]
Risco legal/segurança: [nenhum, baixo, médio, alto, ou pendente de validação]
Codificação/idioma: [UTF-8 preservado, se houver texto em pt-BR]
Turning point/backups: [não aplicável, coberto por Git, ou backup/obsoleto necessário]
```

Se qualquer uma dessas respostas estiver vaga em tarefa relevante, a implementação ainda não deve começar.
