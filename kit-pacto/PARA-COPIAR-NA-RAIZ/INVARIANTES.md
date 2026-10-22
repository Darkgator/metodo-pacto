# Invariantes do Projeto

Use este arquivo somente quando o projeto tiver comportamento, identidade ou contrato que seja caro, arriscado ou difícil de perceber depois de quebrado. Não repita a SPEC nem registre preferências genéricas.

Cada invariante precisa informar a fonte aprovada e uma prova direta. Ela pode mudar, mas a mudança exige decisão explícita e atualização da prova.

## Regras de negócio que não podem quebrar

| ID | Verdade a preservar | Escopo afetado | Fonte aprovada | Prova direta |
|---|---|---|---|---|
| RN-01 | [regra observável] | [fluxo, tela, API ou dado] | [SPEC, decisão ou teste] | [teste, cenário ou inspeção] |

## Identidade

### Visual

- Referência ou design aprovado:
- Tokens, componentes, layout ou estados que não podem divergir:
- Tela ou viewport representativo para comparação:
- Prova necessária quando afetada:

### Textual

- Termos oficiais e nomes de funcionalidades:
- Tom, público e linguagem esperados:
- Textos, formatos ou palavras que não podem mudar sem decisão:
- Prova necessária quando afetada:

### Sonora

- Sons, alertas, locução ou silêncio esperados:
- Gatilhos, prioridade e contexto de uso:
- Controle do usuário, volume, silenciamento e acessibilidade:
- Prova necessária quando afetada:

## Contratos técnicos e dados a preservar

| ID | Contrato ou dado | Consumidores | Fonte aprovada | Prova direta |
|---|---|---|---|---|
| CT-01 | [schema, API, arquivo, permissão ou saída] | [quem depende] | [contrato, migração ou decisão] | [teste, amostra ou verificação] |

## Mudança intencional de invariante

- ID alterado:
- Decisão e responsável:
- Nova verdade e nova prova:
- Compatibilidade, migração ou comunicação necessária:
