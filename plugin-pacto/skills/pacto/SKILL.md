---
name: pacto
description: Conduz trabalho de software pelo Método PACTO quando for necessário iniciar, retomar, pausar, alternar ou encerrar uma tarefa de projeto. Não use para uma pergunta isolada sem trabalho de projeto.
---

# PACTO

Use o estado e os contratos do projeto para manter continuidade com o menor contexto necessário. O estado não substitui a instrução humana vigente nem concede autorização nova.

1. Inspecione estrutura, diff e o estado persistido aplicável. Em projeto existente, aproveite decisões vigentes; não reinicie briefing, stack ou arquitetura sem uma lacuna que bloqueie a tarefa atual.
2. Aproveite o contrato e a autorização vigentes; execute o escopo aprovado em fatias verificáveis. Só proponha ou atualize o contrato se faltar resultado, limite ou prova decisivos. Consulte a política local, se existir, pela seção pertinente.
3. Pergunta no meio da execução não cancela o trabalho ativo. Quando o pedido trocar a prioridade, preserve objetivo, último resultado e próximo passo antes de iniciar o novo trabalho. Ao retornar, recupere o trabalho explicitamente associado; não reinicie briefing, stack ou arquitetura por reflexo.
4. Atualize `.pacto/estado.json` somente quando houver decisão, resultado verificável, tentativa descartada, bloqueio, troca relevante de trabalho ou conclusão. Use `.pacto/pacto-estado.py` se existir; se não existir, use o PLAN já adotado pelo projeto e informe a cobertura reduzida. Para comandos, migração, evidências e instalação, leia [a referência de continuidade](references/continuidade.md).
5. Para bug ou requisito protegido, consulte a política disponível e somente as invariantes afetadas. Compare com a referência aprovada e preserve a regressão útil; fallback não altera restrição explícita.
6. Antes de concluir, informe resultado, provas, limitações e próximo passo real. Em publicação, confronte o ambiente e a revisão efetivamente publicados com os registros; não chame produção de homologação nem o contrário.

Não crie estado, SPEC, PLAN, testes, screenshot ou questionário por reflexo. Aplique apenas o que a tarefa exige.
