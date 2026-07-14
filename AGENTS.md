# AGENTS.md

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Visão do Projeto

Este repositório documenta e organiza o Método PACTO, um framework prático para desenvolvimento de soluções com agentes de código. O objetivo é oferecer guia, templates, prompts e regras universais para iniciar projetos do zero com segurança, clareza e verificação.

## Comandos

- Não há build obrigatório para a documentação.
- Validação visual do guia: abrir `guia-visual/index.html` no navegador.
- Busca rápida no projeto: usar `rg` quando disponível.
- Verificação manual principal: revisar links, prompts, acentuação UTF-8 e consistência entre `docs/`, `templates/` e `guia-visual/`.

## Fluxo de Trabalho

- Leia `BRIEF.md`, `SPEC.md`, `PLAN.md` e `docs/regras-universais.md` antes de alterar o método.
- Em mudanças conceituais, atualize também o guia visual e os templates afetados.
- Trabalhe em fatias pequenas e verificáveis.
- Não implemente fora do escopo aprovado na `SPEC.md`.
- Em projeto novo ou decisão estrutural, avalie variáveis decisivas antes de recomendar arquitetura, stack, IA ou automação.
- Após 3 tentativas consecutivas no mesmo erro, pare, mostre o erro e peça orientação.

## Segurança

- Nunca inclua chaves reais, tokens, senhas ou credenciais no código, docs, exemplos, prompts, testes, logs ou commits.
- Use dados fictícios em exemplos.
- Não exponha dados sensíveis em screenshots, fixtures, HTML ou relatórios.
- Ações destrutivas, migrações, remoções grandes e reestruturações devem ser tratadas como turning points.

## Licenciamento e Risco Legal

- Antes de adicionar dependência, asset, fonte, ícone, modelo de IA, dataset, SDK, API, plugin ou serviço externo, confirme se a licença/termos permitem o uso pretendido.
- "Gratuito", "source-available" e "free for personal use" não significam liberação para uso comercial.
- Se houver dúvida sobre uso comercial, redistribuição, SaaS, copyleft, atribuição, privacidade, marca ou patente, pare e peça validação humana.

## Obsoletos e Backups

- Git deve ser a fonte primária de histórico quando disponível.
- Este workspace não foi detectado como repositório Git ativo durante a aplicação inicial do método.
- Antes de turning points, avalie se é necessário backup mínimo ou mover obsoletos para `_archive/`.
- Não faça backup por reflexo em alteração pequena.
- Não arquive dependências, caches, builds ou arquivos recriáveis.
- Se criar `_archive/`, use `templates/ARCHIVE-README.template.md`.

## Qualidade

- Preserve acentuação correta em pt-BR.
- Salve arquivos textuais em UTF-8.
- Não aceite mojibake como `Ã§`, `Ã£`, `Ã©`, `Ã³`, `â€“` ou `Â`.
- Não remova acentos para contornar problema de codificação.
- Mantenha documentos curtos quando forem carregados por agentes.
- Mova detalhes longos para `docs/`.

## Testes e Verificação

- Todo trabalho deve ter forma clara de verificação: revisão documental, validação visual, teste manual, busca por termos ou renderização do HTML.
- Use smoke visual para `guia-visual/index.html` após mudanças relevantes.
- Revise consistência entre prompts do guia visual e documentos em `docs/`.
- Verifique se templates refletem as regras universais.

