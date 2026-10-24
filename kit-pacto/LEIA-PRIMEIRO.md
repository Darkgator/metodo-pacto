# Kit PACTO para Projetos

Criador do método: Alexandre Barroso de Miranda
Atuação: Consultor de Processos
Método: PACTO
Versão do kit: `2026.10.24.1`

## Como usar

1. Copie apenas os modelos necessários de `PARA-COPIAR-NA-RAIZ/` ou use o instalador. Em projeto existente, prefira a prévia `python scripts/instalar_pacto.py --destino CAMINHO --perfil continuidade planejar`; ela não escreve. A pasta `.pacto/` inclui política, estado vazio e comando local de estado. Para Claude Code, copie também `CLAUDE.md`.
2. Preencha BRIEF.md apenas quando faltar contexto; aproveite respostas já existentes.
3. Defina o contrato proporcional: uma frase para tarefa simples, SPEC.md para mudança relevante. Preencha somente campos aplicáveis.
4. Use `PLAN.md` somente quando a execução for complexa ou precisar sobreviver ao chat. Mais de um arquivo, sozinho, não exige plano persistente.
5. Abra o projeto no Codex ou Claude Code. Confira se o host reconheceu as instruções; a presença do arquivo não comprova sua leitura.

Não é necessário copiar este leia-me nem todo o framework. A política `.pacto/validacao.md` acompanha o kit, mas o AGENTS encaminha somente à seção acionada por T2/T3, bug, texto operacional ou requisito visual; T0 não exige essa leitura.

O instalador não cria BRIEF, SPEC, PLAN ou INVARIANTES por padrão. Se um contrato for necessário, use `--contrato SPEC` antes do subcomando, repetindo a opção para outros nomes. Instruções existentes e estado usado são preservados. Confira `integracao_pendente` na saída: preservar AGENTS local pode exigir integrar as orientações pertinentes. Skill e hooks não são instalados por esse comando.

Em projeto existente, preserve instruções e comandos que já funcionam. Adapte o conteúdo ao projeto; não sobrescreva contratos existentes automaticamente. `python .pacto/pacto-estado.py contexto --sessao ID` recupera o trabalho correto; toda alteração exige `--esperada-revisao N`. Em conflito, releia e reconcilie. Preencha os comandos de instalar, executar e verificar no AGENTS.md e remova campos sem aplicação.

## Atualizar um projeto existente

Compare a versão no comentário do AGENTS com a versão pretendida. Revise o diff das regras e da política; preserve comandos, decisões e adaptações locais. Atualize a política e o identificador juntos, depois de conferir os caminhos. Não copie BRIEF, SPEC, PLAN ou INVARIANTES por cima dos contratos existentes. Só marque a nova versão após concluir a adaptação.

Publicar o método no GitHub não atualiza projetos antigos automaticamente. Não baixar o repositório a cada tarefa. A checagem `python scripts/verificar_kit.py`, no repositório do método, é opcional para o mantenedor e não vai para os projetos.

## Primeiro comando para o agente

Cole no Codex ou Claude Code:

```text
Inicie pelo Método PACTO para esta tarefa: [resultado e limites]. Inspecione somente a estrutura, o diff e os contratos relevantes. Aproveite decisões existentes e pergunte apenas lacunas bloqueantes. Execute tarefa simples já autorizada diretamente; para mudança relevante, proponha o menor contrato verificável antes de implementar: pronto significa [resultado], verificado por [prova]. Não escolha stack sem contexto e aprovação.
```

## Após a aprovação do escopo

```text
O contrato foi aprovado: [pedido ou SPEC.md]. Implemente o escopo autorizado em fatias verificáveis, avançando entre checkpoints já aprovados. Atualize PLAN.md apenas se houver plano persistente. Ao concluir, informe o resultado e somente as validações, limitações e riscos reais proporcionais à tarefa.
```
