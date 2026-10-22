---
name: pacto
description: Conduz trabalho de software pelo Método PACTO quando for necessário iniciar, retomar, pausar, alternar ou encerrar uma tarefa de projeto. Não use para uma pergunta isolada sem trabalho de projeto.
---

# PACTO

Use o estado e os contratos do projeto para manter continuidade com o menor contexto necessário.

1. Inspecione estrutura, diff e o estado persistido aplicável. Em projeto existente, aproveite decisões vigentes; não reinicie briefing, stack ou arquitetura sem uma lacuna que bloqueie a tarefa atual.
2. Para tarefa simples já autorizada, execute a menor fatia verificável. Para mudança relevante, proponha ou atualize o menor contrato que declare resultado, escopo, prova e invariantes afetadas.
3. Pergunta no meio da execução não cancela o trabalho ativo. Quando o pedido trocar a prioridade, preserve objetivo, último resultado e próximo passo antes de iniciar o novo trabalho. Ao retornar, confirme o estado real antes de continuar.
4. Atualize `.pacto/estado.json` somente quando houver decisão, resultado verificável, tentativa descartada, bloqueio, troca relevante de trabalho ou conclusão. Use `.pacto/pacto-estado.py` se existir; se não existir, use o PLAN já adotado pelo projeto e informe a cobertura reduzida.
5. Para bug, registre hipótese e tentativa descartada quando isso evitar repetição. Procure caminhos irmãos pela causa e comportamento. Para requisito visual, textual, sonoro, contrato ou dado protegido, consulte somente as invariantes afetadas e obtenha a prova correspondente.
6. Antes de concluir, informe resultado, provas, limitações e próximo passo real. Em publicação, confronte o ambiente e a revisão efetivamente publicados com os registros; não chame produção de homologação nem o contrário.

Não crie estado, SPEC, PLAN, testes, screenshot ou questionário por reflexo. Aplique apenas o que a tarefa exige.
