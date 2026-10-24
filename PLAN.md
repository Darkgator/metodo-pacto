# Continuidade da reengenharia

## Estado

Primeiro lote R1 a R4 autorizado em 24/10/2026. Branch local `reengenharia/arquitetura-2026-10-24`. Preservar o núcleo e reaproveitar por necessidade; não reiniciar método ou projetos do zero.

Base `ed19ebdd62d60b2b79ae2561d121b81af19aa904` preservada em `../metodo-pacto-arquivo/2026-10-24-pre-reengenharia/`: ZIP de 66 arquivos, manifesto SHA-256 e tag local `arquivo/pre-reengenharia-2026-10-24`. Inclui as duas análises que ainda não estavam versionadas; caches e `.git` ficaram fora do ZIP. Histórico Git preservado no repositório.

## Execução

- [x] Arquivar e conferir a base; separar instruções atuais das históricas.
- [x] R1: propriedade e manutenção dos arquivos.
- [x] R2/R4: evidências, publicação, schema e resumo priorizado.
- [x] R3: autorização persistente nos prompts ativos.
- [x] Regressões: 33 testes e seis controles negativos; distribuição conferida.

Resultado e limites: [primeiro lote](docs/resultado-reengenharia-2026-10-24.md). Próximo: R5 a R7, com consolidação enxuta das fontes e CI do pacote. A reengenharia completa não está encerrada. Confirmação de publicação por consulta remota não foi implementada; o registro manual fica explicitamente informado ou pendente.

Não carregar os relatórios inteiros por rotina. Escopo e aceite atuais estão em SPEC.md. O diagnóstico detalhado é `docs/revisao-arquitetural-pacto.md`, apenas para localizar um caso que esteja sendo corrigido. A análise dos episódios e a documentação anterior são referência, não novas instruções obrigatórias.

## Limites

Arquivo local e tag não são backup remoto. Nenhuma instalação antiga foi alterada. Integração em host real, ganho econômico, R5 a R7 e piloto de memória não estão concluídos por esta separação.
