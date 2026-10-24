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

Resultados e limites: [primeiro lote](docs/resultado-reengenharia-2026-10-24.md) e [R5 a R7](docs/resultado-reengenharia-r5-r7.md). R1 a R7 implementados e verificados no pacote. Confirmação de publicação por consulta remota não foi implementada; o registro manual fica explicitamente informado ou pendente.

- [x] Consolidar entrada, políticas por assunto e prompts compartilhados.
- [x] Refinar regressão, referência e fallback nas fontes existentes.
- [x] Conferir estrutura e distribuição; 40 testes locais e workflow com dois ambientes.
- [x] Publicar na branch separada e conferir a execução remota: commit `16c38e4f35f00f410874342b9c3f77bc32291024`, [CI 40111620530](https://github.com/Darkgator/metodo-pacto/actions/runs/40111620530), 40 testes em cada sistema.

Próximo passo útil: usar o candidato `2026.10.24.2` numa tarefa real para observar adesão, retomada e custo. R8, novos MCPs e memória extra não têm necessidade demonstrada agora. Integração/confiança real dos hosts e ganhos econômicos continuam não comprovados. Main e instalações anteriores permanecem preservadas; o código novo está na branch de reengenharia.

Não carregar os relatórios inteiros por rotina. Escopo e aceite atuais estão em SPEC.md. O diagnóstico detalhado é `docs/revisao-arquitetural-pacto.md`, apenas para localizar um caso que esteja sendo corrigido. A análise dos episódios e a documentação anterior são referência, não novas instruções obrigatórias.

## Limites

Implementação publicada no commit `27d66bd25320e0e204867d4f62abb9b36018a966`. Consulta remota confirmou a branch nesse commit, main na base `ed19ebd` e tag de arquivo apontando para essa mesma base. A tag também está no GitHub; o ZIP completo continua somente local. Nenhuma instalação antiga foi alterada. Integração em host real, ganho econômico, R5 a R7 e piloto de memória não estão concluídos por esta separação.
