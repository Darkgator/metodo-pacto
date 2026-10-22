# Resultado de validação da continuidade

Data: 22/10/2026. Revisão local: em desenvolvimento, posterior a `01d0d03`.

## Verificado localmente

- Estado no esquema 2, migração explícita do esquema 1, validação de tipos e IDs.
- CAS obrigatório, mutex nomeado do Windows ou trava POSIX e recusa de conflito de revisão. A regressão de sobrescrita silenciosa foi reproduzida e coberta; o cenário concorrente foi repetido 30 vezes no Windows local.
- Descoberta de raiz a partir de subpasta, contexto por sessão, decisões substituídas e alternância de trabalhos.
- Provas dirigidas, vencimento por hash de arquivo e divergência entre publicação esperada e observada.
- Prévia, instalação, atualização conflituosa, remoção preservando estado e distribuição byte a byte.

## Não comprovado nesta validação

- Reconhecimento e confiança do plugin/hook no Codex instalado.
- Eventos reais de abertura, retomada e compactação em Codex ou Claude Code.
- Reconhecimento de skill e hook no Claude Code.
- Economia de tokens, qualidade conversacional e ganho cotidiano. A bancada está preparada em `scripts/avaliar_continuidade.py`; ela não faz chamadas de IA sem executor e orçamento explícitos.

Essas pendências não são falhas ocultas nem aprovação implícita. Antes de afirmar operação em host ou economia, registre ambiente, revisão, cenário, modelo, esforço, tokens disponíveis, duração, resultado e limitações.
