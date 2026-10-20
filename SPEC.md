# SPEC.md

## Objetivo e escopo aprovado

Entregar o kit PACTO `2026.10.19.1` com política local consultada por gatilho, identidade de versão e orientações executáveis para texto operacional e correções de bugs.

Corrigir também a documentação vigente: papel humano em produção, evidências, limites de custo e atualização preservando adaptações. Enxugar os contratos do método, sem alterar aplicativos de referência ou a auditoria congelada.

## Critérios de aceite

- [x] Cinco modelos e política distribuída correspondem às fontes oficiais; o caminho local está disponível fora do repositório do método.
- [x] AGENTS identifica a versão e encaminha por gatilho à política local; T0 não exige essa leitura.
- [x] Prompt operacional pede prova curta; orientação de variantes usa causa, comportamento e caminhos irmãos.
- [x] Política preserva entrega real, artefato visual, revisão corrigida, dados não afetados, registro de publicação e operação conjunta.
- [x] Atualização não sobrescreve adaptações nem presume que projetos antigos receberam a versão nova.
- [x] Verificação estática e cenários locais T2/T4 têm resultado e limite registrados; nenhuma nova comparação econômica é alegada.
- [x] Modelos, instruções de adoção e prompts ativos estão alinhados, em UTF-8.

## Verificação

Checagem opcional do mantenedor: `python scripts/verificar_kit.py`. Conferir cópias, caminho local, versão, links, diff e preservação dos scripts do guia. Executar controles negativos e as provas locais dirigidas em pasta temporária isolada, sem novas sessões de IA.

Aceite funcional do kit não comprova que o agente cumprirá toda regra. Eficácia, tempo humano e economia exigem comparação equivalente; critérios estão em [Benefícios e avaliação](docs/evidencias-de-beneficios.md).

## Limites

Publicação no GitHub já autorizada pelo usuário. Sem implantação automática em outros projetos, instalação obrigatória, experimento pago, teste com alunos ou alteração dos resultados anteriores. Licença final continua pendente.
