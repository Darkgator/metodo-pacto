# Continuidade de Trabalho

O PACTO separa a verdade durável do projeto do contexto passageiro do chat.

- `AGENTS.md`, contratos, testes e invariantes guardam regras do projeto.
- `PLAN.md` continua sendo o resumo da fase quando ela precisar sobreviver a sessões.
- `.pacto/estado.json` guarda somente trabalhos em aberto e seus próximos passos. Não guarda conversa, segredo, log completo ou decisão já documentada em outro contrato.

## Quando usar estado

Use-o em trabalho que possa ser interrompido, retomado em outro chat, alternado com outro assunto ou executado em paralelo. Tarefa trivial não cria registro por reflexo.

Ao abrir, retomar ou voltar a um trabalho, execute:

```text
python .pacto/pacto-estado.py contexto
```

Crie um trabalho somente quando fizer sentido preservar continuidade:

```text
python .pacto/pacto-estado.py iniciar --titulo "Corrigir acesso" --objetivo "Corrigir a autorização da rota" --proximo-passo "Reproduzir com perfil sem permissão"
```

Após decisão, resultado, bloqueio, tentativa descartada, troca relevante ou conclusão, atualize apenas o trabalho correspondente. O comando devolve a revisão nova. Ao atualizar um estado lido antes por outro chat, use `--esperada-revisao N`; conflito significa que o estado real precisa ser reconciliado antes de qualquer gravação.

```text
python .pacto/pacto-estado.py atualizar ID --resultado "Bug reproduzido" --proximo-passo "Cobrir caminhos irmãos" --esperada-revisao N
```

## Troca e retorno de assunto

Uma pergunta incidental não interrompe trabalho. Quando o usuário trocar a prioridade, registre o ponto de parada do trabalho atual e inicie ou recupere outro. Ao retornar, confira arquivos, diff e estado antes de concluir que o resultado anterior ainda vale.

Estado concluído permanece como referência curta até ser removido por manutenção deliberada. O PACTO não apaga automaticamente o histórico do projeto.

## Hook experimental no Codex Desktop

`plugin-pacto/` contém a skill `pacto` e um hook que lê o estado na abertura, retomada, fork e compactação. Ele não escreve arquivos, não lê transcrição e não decide o que implementar. A instalação exige revisão e confiança explícita do hook pelo Codex Desktop.

O hook acrescenta no máximo três trabalhos em aberto ao contexto. Se o estado estiver ausente, ilegível ou sem trabalhos abertos, ele não produz contexto adicional.

## Limites

O estado ajuda a recuperar objetivo e pendências; não prova que a IA entendeu a intenção do usuário, que a validação foi suficiente ou que uma publicação ocorreu. Esses pontos continuam exigindo a prova proporcional definida no projeto.
