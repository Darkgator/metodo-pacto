# Resumo Atual

Criador: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Intenção

Criar um framework reutilizável para desenvolver qualquer projeto com agentes de código, especialmente Claude Code e Codex, sem depender de uma stack específica.

## Ideia central do rascunho

O processo atual está organizado em fases:

1. Preparação humana fora do chat.
2. Descoberta com o agente, sem escrever código.
3. Criação dos documentos-base do projeto.
4. Setup técnico mínimo.
5. Implementação por fatias verticais.
6. Revisão, testes e endurecimento.
7. Fechamento da fase e preparação da próxima.

## Arquivos sugeridos para cada projeto

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`, quando usar Claude Code
- `SPEC.md`
- `.env.example`
- `CHANGELOG.md`
- `docs/PRODUCT.md`
- `docs/UI.md`, se houver interface
- `docs/DATA_MODEL.md`, se houver banco
- `docs/QA.md`, se houver validação manual relevante

## Regras fortes propostas

- Não começar codificando antes de alinhar escopo, stack e MVP.
- Usar documentos do repositório como fonte de verdade, não apenas o chat.
- Trabalhar por fatias pequenas e verificáveis.
- Pedir plano antes de mudanças grandes.
- Rodar validações ao final de cada ciclo.
- Parar após 3 tentativas consecutivas no mesmo erro.
- Nunca colocar segredos reais em código, testes, documentação ou commits.

## Pontos ainda provisórios

- Se a quantidade de documentos está adequada ou pesada demais.
- Se `SPEC.md` deve ser único por fase ou dividido por feature.
- Se o kit deve gerar arquivos manualmente por prompt ou por script/template.
- Qual deve ser o mínimo universal para projetos pequenos.
- Como adaptar o fluxo para Claude Code e Codex sem duplicar regras.
