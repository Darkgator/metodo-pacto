# Síntese da Pesquisa Aprofundada

Criador: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

Fontes recebidas:

- `research/gemini-deep-research-report.txt`
- `research/chatgpt-deep-research-report.md`

## Conclusão central

Os dois relatórios apontam para um framework mais leve e mais disciplinado do que o rascunho v0.

O padrão mais forte não é "encher o projeto de documentos" nem "mandar o agente fazer tudo". O padrão é:

1. **Explorar antes de editar.**
2. **Planejar quando houver ambiguidade, risco ou mudança multiarquivo.**
3. **Transformar o trabalho em contrato verificável.**
4. **Implementar em fatias pequenas.**
5. **Validar com comandos, testes, build, lint ou evidência visual.**
6. **Revisar o diff antes de aceitar.**
7. **Mover aprendizados recorrentes para arquivos, skills ou hooks.**

## Consensos fortes

- Instruções permanentes devem ser curtas, práticas e versionadas.
- `AGENTS.md` e `CLAUDE.md` não devem virar manuais enormes.
- Procedimentos recorrentes devem ir para skills, comandos ou templates, não para arquivos sempre carregados.
- Plano antes de código é essencial para tarefas complexas, mas exagerado para correções triviais.
- SPEC boa é contrato de trabalho, não documento visionário.
- O melhor ciclo é pequeno: escopo curto, implementação curta, validação curta.
- "Done" precisa ter prova: teste, build, lint, screenshot, comportamento manual validado ou outro sinal verificável.
- Sessões devem ser focadas em uma tarefa coerente.
- Trabalho paralelo exige isolamento por branch, worktree ou thread separada.
- O usuário humano deve aprovar decisões de escopo, arquitetura, interfaces públicas, banco, segurança, dependências e operações destrutivas.
- Segurança, licenciamento e risco legal precisam ser tratados como gates universais, mas proporcionais ao risco da tarefa.
- Tipos de teste devem ser escolhidos pelo risco e pelo comportamento afetado, não por uma lista fixa aplicada a todo projeto.

## Pontos controversos

### 1. Quanto especificar antes de codar

Há defesa forte de spec-driven development, mas os relatórios também mostram que formalizar demais atrapalha tarefas pequenas.

Síntese: use SPEC formal para projeto novo, feature relevante, refatoração, migração, banco, segurança e UI importante. Para correções simples, use um plano curto ou instrução direta.

### 2. TDD obrigatório

Os relatórios não sustentam "TDD sempre" como regra universal. A recomendação mais robusta é desenvolvimento orientado a verificação.

Síntese: escreva testes antes quando o comportamento estiver claro e for fácil de isolar. Quando não estiver, explore primeiro, defina critérios de aceite e então implemente testes ou validações.

### 3. Autonomia do agente

As ferramentas caminham para mais autonomia, mas isso só é seguro quando há boas instruções, validações e limites.

Síntese: comece com baixa autonomia e aumente apenas em repositórios conhecidos, com comandos de validação confiáveis.

### 4. Número de tentativas antes de parar

O rascunho v0 usava 3 tentativas. A pesquisa sugere ser mais conservador em falhas repetidas.

Síntese proposta: 2 tentativas para o mesmo erro antes de parar em tarefas de alto risco; 3 como máximo absoluto em tarefas simples.

## O que muda em relação ao rascunho v0

- Reduzir obrigatoriedade de muitos documentos em projetos pequenos.
- Tratar `SPEC.md` como contrato da tarefa/fase, não como enciclopédia do projeto.
- Separar melhor:
  - contexto permanente;
  - contrato da tarefa;
  - plano de execução;
  - procedimento reutilizável.
- Adotar o Método PACTO como loop principal.
- Trocar "TDD sempre" por "verificação sempre".
- Usar skills/templates para workflows repetidos.
- Registrar que parte das afirmações dos relatórios precisa ser validada antes de virar fato oficial do framework.

## Artefatos recomendados

### Essenciais para quase todo projeto

- `AGENTS.md`: regras curtas e portáveis para agentes.
- `CLAUDE.md`: entrada curta para Claude Code, com comandos e ponte para as regras do projeto.
- `SPEC.md`: contrato da fase ou tarefa atual.
- `.env.example`: variáveis esperadas com valores fictícios, quando houver configuração.
- `README.md`: instruções humanas mínimas.

### Opcionais, conforme necessidade

- `PLAN.md`: plano técnico aprovado para tarefas grandes.
- `CHANGELOG.md`: quando houver versionamento ou entregas formais.
- `docs/PRODUCT.md`: quando regras de negócio forem complexas.
- `docs/UI.md`: quando UI/UX for relevante.
- `docs/DATA_MODEL.md`: quando houver banco ou modelo de domínio importante.
- `docs/DECISIONS.md`: quando decisões arquiteturais precisarem de histórico.
- `.claude/skills/` ou equivalente: procedimentos reutilizáveis.
- hooks: validações automáticas e filtros de saída, apenas quando o fluxo manual já estiver estável.

## Fórmula do framework v1

**Enquadrar -> Explorar -> Contratar -> Fatiar -> Implementar -> Verificar -> Revisar -> Externalizar**

Essa fórmula substitui a ideia anterior de "criar muitos documentos antes de tudo".
