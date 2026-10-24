# Continuidade da reengenharia

## Estado

Primeiro lote R1 a R4 autorizado em 24/10/2026. Branch de trabalho `reengenharia/arquitetura-2026-10-24`, publicada no GitHub. Preservar o núcleo e reaproveitar por necessidade; não reiniciar método ou projetos do zero.

Base `ed19ebdd62d60b2b79ae2561d121b81af19aa904` preservada em `../metodo-pacto-arquivo/2026-10-24-pre-reengenharia/`: ZIP de 66 arquivos, manifesto SHA-256 e tag local `arquivo/pre-reengenharia-2026-10-24`. Inclui as duas análises que ainda não estavam versionadas; caches e `.git` ficaram fora do ZIP. Histórico Git preservado no repositório.

## Execução

- [x] Arquivar e conferir a base; separar instruções atuais das históricas.
- [x] R1: propriedade e manutenção dos arquivos.
- [x] R2/R4: evidências, publicação, schema e resumo priorizado.
- [x] R3: autorização persistente nos prompts ativos.
- [x] Regressões: 33 testes e seis controles negativos; distribuição conferida.

Resultado e limites: [primeiro lote](docs/resultado-reengenharia-2026-10-24.md). R5 a R7 em execução, autorizados pelo usuário: consolidação enxuta das fontes, regressão/fallback e CI do pacote. Confirmação de publicação por consulta remota não foi implementada; o registro manual fica explicitamente informado ou pendente.

- [x] Consolidar entrada, políticas por assunto e prompts compartilhados.
- [x] Refinar regressão, referência e fallback nas fontes existentes.
- [x] Conferir estrutura e distribuição; 40 testes locais e workflow com dois ambientes.
- [ ] Publicar na branch separada e conferir a execução remota.

Não carregar os relatórios inteiros por rotina. Escopo e aceite atuais estão em SPEC.md. O diagnóstico detalhado é `docs/revisao-arquitetural-pacto.md`, apenas para localizar um caso que esteja sendo corrigido. A análise dos episódios e a documentação anterior são referência, não novas instruções obrigatórias.

## Limites

Implementação publicada no commit `27d66bd25320e0e204867d4f62abb9b36018a966`. Consulta remota confirmou a branch nesse commit, main na base `ed19ebd` e tag de arquivo apontando para essa mesma base. A tag também está no GitHub; o ZIP completo continua somente local. Nenhuma instalação antiga foi alterada. Integração em host real, ganho econômico, R5 a R7 e piloto de memória não estão concluídos por esta separação.
