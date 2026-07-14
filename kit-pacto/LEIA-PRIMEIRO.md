# Kit PACTO para Projetos

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Como usar

1. Copie o conteúdo da pasta `PARA-COPIAR-NA-RAIZ` para a raiz do projeto-alvo.
2. Preencha `BRIEF.md` antes de iniciar um projeto novo ou uma fase relevante.
3. Defina e aprove `SPEC.md` antes de escrever código.
4. Atualize `PLAN.md` quando houver trabalho multiarquivo, risco relevante ou mais de uma etapa.
5. Abra o projeto no Codex ou Claude Code. Ambos carregam as regras centrais automaticamente.

Não copie esta pasta de instruções para o projeto-alvo. Não é necessário copiar documentos extensos do framework: o kit carrega regras curtas e consulta os contratos da fase apenas quando necessário.

## Primeiro comando para o agente

Cole no Codex ou Claude Code:

```text
Inicie pelo Método PACTO. Inspecione a estrutura e os contratos disponíveis. Informe a fase atual, quais documentos precisam ser preenchidos ou revisados e as perguntas críticas. Não escreva código nem escolha stack antes da minha aprovação.
```

## Após a aprovação do escopo

```text
O escopo da SPEC foi aprovado. Atualize o PLAN com a menor fatia verificável e implemente somente essa fatia. Ao concluir, informe o que foi validado, o que não foi validado e os riscos pendentes.
```

