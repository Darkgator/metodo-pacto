# SPEC.md

## Objetivo e escopo aprovado

Entregar o PACTO `2026.10.22.2` com continuidade explícita entre chats e assuntos: estado local opcional de trabalhos, skill reutilizável, hook somente de leitura para Codex Desktop e verificações automatizadas do núcleo e da distribuição.

Preservar o kit existente, contratos proporcionais e adaptações locais. MCP permanece fora desta versão; não haverá serviço, banco central, sincronização entre máquinas ou leitura automática de históricos.

## Critérios de aceite

- [x] Seis modelos, política e estado inicial distribuídos correspondem às fontes oficiais; o caminho local está disponível fora do repositório do método.
- [x] AGENTS identifica a versão e encaminha por gatilho à política local; T0 não exige essa leitura.
- [x] Prompt operacional pede prova curta; orientação de variantes usa causa, comportamento e caminhos irmãos.
- [x] Política preserva entrega real, artefato visual, revisão corrigida, dados não afetados, registro de publicação e operação conjunta.
- [x] Atualização não sobrescreve adaptações nem presume que projetos antigos receberam a versão nova.
- [x] Verificação estática e cenários locais T2/T4 têm resultado e limite registrados; nenhuma nova comparação econômica é alegada.
- [x] Modelos, instruções de adoção e prompts ativos estão alinhados, em UTF-8.
- [x] Estado detecta escrita concorrente por revisão, grava de forma atômica e não armazena transcrição do chat.
- [x] Skill PACTO encaminha início, retomada, alternância e fechamento sem criar burocracia em tarefa trivial.
- [x] Hook do plugin só injeta resumo curto de trabalhos abertos nos eventos suportados, sem escrever no projeto.

## Verificação

Checagens do mantenedor: `python scripts/verificar_kit.py` e `python -m unittest discover -s tests -v`. Conferir cópias, caminho local, versão, estado, links, diff, comandos de continuidade e JSON do plugin. Executar controles negativos em pasta temporária isolada, sem novas sessões de IA.

Aceite funcional do kit não comprova que o agente cumprirá toda regra. Eficácia, tempo humano e economia exigem comparação equivalente; critérios estão em [Benefícios e avaliação](docs/evidencias-de-beneficios.md).

## Limites

Publicação no GitHub já autorizada pelo usuário. Sem ativação automática do plugin ou de hooks no computador, implantação em outros projetos, experimento pago ou alteração dos resultados anteriores. Licença final continua pendente.
