# Resultado do primeiro lote de reengenharia

Data: 24/10/2026. Candidato `2026.10.24.1`; plugin `0.2.1`. Escopo: R1 a R4 da revisão arquitetural. Resultado local, sem ativação em projetos ou hosts existentes.

## Preservação e contexto

A base `ed19ebdd62d60b2b79ae2561d121b81af19aa904` foi preservada antes de editar: ZIP com 66 arquivos, incluindo as duas análises locais, e manifesto SHA-256 em `../metodo-pacto-arquivo/2026-10-24-pre-reengenharia/`. Conteúdo de cada entrada e integridade do ZIP foram conferidos. A tag `arquivo/pre-reengenharia-2026-10-24` preserva a base Git; o ZIP também conserva os dois relatórios que ainda não estavam versionados.

Área ativa: `metodo-pacto`, branch `reengenharia/arquitetura-2026-10-24`. AGENTS, SPEC e PLAN encaminham ao trabalho atual e orientam consultar o arquivo apenas por necessidade. Não há extração ou leitura automática do histórico. A evolução reaproveita a base; o arquivo não vira uma segunda instalação.

## Correções e resultado observado

| Caso | Agora |
|---|---|
| D01 | Contratos opcionais não são criados por padrão. Remoção preserva instruções, contratos, estado e evidências, inclusive sob manifesto antigo. Skill não instalada por esse comando é explicitada. |
| D02 | AGENTS preexistente é preservado; suporte independente pode ser instalado. Adaptação das instruções aparece como integração pendente. |
| D03 | Estado usado não conflita com atualização de suporte e permanece byte a byte intacto. |
| D04 | Verificador usa a validação do runtime e rejeita o mesmo estado inválido. Tipos inválidos também recebem erro controlado. |
| D05 | O cenário original produz 4.000 caracteres, incluindo aviso; próximo passo está presente. Cenário adicional protege bloqueio e próximo passo nos limites de tamanho. |
| D06 | Entrada obrigatória ausente impede execução e gera registro inconclusivo. Ausência esperada pode ser declarada explicitamente. |
| D07 | Entradas são registradas antes da execução; alteração durante o comando torna a prova inconclusiva. Saída declarada pode ser produzida, com hash posterior. |
| D08 | stdout/stderr arbitrários não são capturados para persistência. Canário fictício não apareceu no estado. |
| D09 | Revisão esperada sem observação aparece pendente. Registro manual completo aparece informado; nenhum dos dois recebe confirmação automática. |
| R3 | Modelos e prompts ativos permitem avanço dentro do plano aprovado. Autorizar apenas uma fatia continua possível. |

O registro diferencia `executada`, `passou`, `falhou`, `inconclusiva` e `nao_executada`. `Passou` descreve a verificação configurada e exige critério declarado; o agente ainda precisa conferir se as assertivas provam o requisito. `Provar` mostra o resultado e retorna código 1 para falha, inconclusão ou comando não executado, mantendo o registro e sua nova revisão.

Evidências antigas permanecem no estado e não recebem proveniência retroativa. Precisam ser refeitas para uma confirmação atual. O formato geral do estado continua 2; não houve migração ou sobrescrita de trabalhos dos projetos do usuário.

## Validação

- `python -m unittest discover -s tests -v`: **33 testes passaram**. Proteções anteriores de revisão, concorrência, migração, retomada e remoção foram mantidas. O teste antigo que esperava bloquear tudo por AGENTS adaptado agora verifica preservação e integração pendente, conforme a mudança de contrato.
- Os nove cenários originais foram repetidos em pastas temporárias; resultados pertinentes constam na tabela.
- Seis controles negativos executaram os novos testes contra código da base arquivada em cópia temporária: D01 legado, D03, D04, D05, D06 e D08. Todos detectaram os defeitos anteriores; D03 reproduziu a exceção de conflito de estado, os outros cinco reprovaram por assertiva.
- Há cobertura adicional para saída produzida e ausente, ausência esperada, caminho externo, papéis conflitantes, falha de comando e falha simulada na gravação do manifesto com recuperação das criações.
- Distribuição das dez cópias e verificador do pacote passaram. Conferência final: ZIP e seus 66 arquivos íntegros, 69 arquivos ativos decodificados em UTF-8, dois guias com IDs e âncoras válidos, nenhum link local novo quebrado e diff sem erro de espaços.

Os testes são determinísticos e locais. Não houve benchmark com novas sessões de IA, consulta a produção ou teste real de confiança/eventos nos hosts.

## Próximo lote e limites

R1 a R4 estão implementados e testados localmente. A reengenharia completa continua aberta: R5 deve consolidar e encurtar a entrada operacional; R6 deve automatizar a entrega do pacote; R7 deve refinar as regras existentes de regressão, referência e fallback. R8 continua condicionado a uma necessidade de continuidade e a um piloto delimitado.

Sem promessa de economia: não foi adicionada leitura obrigatória deste relatório, do arquivo ou das transcrições. O texto permanente recebeu uma orientação de autorização persistente; tamanho e efeito da consolidação ainda precisam ser avaliados. Quantidade de testes e linhas de código não são medidas de produtividade.

Publicação da branch não atualiza instalações nem promove o candidato à versão consolidada do método. A main anterior permanece preservada enquanto a reengenharia evolui separadamente.

Publicação conferida por `git ls-remote`: implementação `27d66bd25320e0e204867d4f62abb9b36018a966` na branch de reengenharia; main e tag de arquivo na base `ed19ebdd62d60b2b79ae2561d121b81af19aa904`. O ZIP com os relatórios anteriores continua local; não foi enviado como release ou pacote de instalação.
