# Kit PACTO para Projetos

Criador do método: Alexandre Barroso de Miranda
Atuação: Consultor de Processos
Método: PACTO

## Como usar

1. Use templates/ como fonte oficial. A pasta PARA-COPIAR-NA-RAIZ distribui cópias idênticas dos cinco modelos principais. Copie AGENTS.md e, se usar Claude Code, CLAUDE.md; adicione os demais somente quando necessários.
2. Preencha BRIEF.md apenas quando faltar contexto; aproveite respostas já existentes.
3. Defina o contrato proporcional: uma frase para tarefa simples, SPEC.md para mudança relevante. Preencha somente campos aplicáveis.
4. Use `PLAN.md` somente quando a execução for complexa ou precisar sobreviver ao chat. Mais de um arquivo, sozinho, não exige plano persistente.
5. Abra o projeto no Codex ou Claude Code. Ambos carregam as regras centrais automaticamente.

Não copie esta pasta de instruções para o projeto-alvo. Não é necessário copiar documentos extensos do framework: o kit carrega regras curtas e consulta os contratos da fase apenas quando necessário.

Em projeto existente, preserve instruções e comandos que já funcionam. Adapte o conteúdo ao projeto; não sobrescreva contratos existentes automaticamente. Preencha os comandos de instalar, executar e verificar no AGENTS.md e remova campos sem aplicação.

## Primeiro comando para o agente

Cole no Codex ou Claude Code:

```text
Inicie pelo Método PACTO para esta tarefa: [resultado e limites]. Inspecione somente a estrutura, o diff e os contratos relevantes. Aproveite decisões existentes e pergunte apenas lacunas bloqueantes. Execute tarefa simples já autorizada diretamente; para mudança relevante, proponha o menor contrato verificável antes de implementar. Não escolha stack sem contexto e aprovação.
```

## Após a aprovação do escopo

```text
O contrato foi aprovado: [pedido ou SPEC.md]. Implemente somente a menor fatia verificável combinada. Atualize PLAN.md apenas se houver plano persistente. Ao concluir, informe o resultado e somente as validações, limitações e riscos reais proporcionais à tarefa.
```
