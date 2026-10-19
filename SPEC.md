# SPEC.md

## Fase atual

Consolidar o PACTO sem inflar o núcleo de instruções.

Complementos aprovados em 19/10/2026: POC-01, reconciliação do estado vigente na retomada; regressão de variantes próximas afetadas pela mesma causa; R2-01, smoke pelo caminho principal do pacote entregue; R2-02, comparação inicial com a referência visual aprovada; P4-01, preservar o aceite; P4-02, retestar a revisão corrigida e reconfirmar achados se a base mudar; P5-01, conferir preservação do não afetado em edição parcial. Sem alterações nos aplicativos de referência.

## Escopo aprovado

Aplicar recomendações 01 a 07 e incorporar 08 a 13 somente com seus gatilhos.
O piloto 14 continua opcional, sem automação, ferramenta ou documento obrigatório.

## Critérios de aceite

- [x] Modelos oficiais e cópias do kit idênticos; CLAUDE como ponte curta.
- [x] Documentos e leituras condicionais; descoberta sem recomendação prematura.
- [x] Caminhos portáveis, histórico separado e regras Git/tentativas coerentes.
- [x] Validação por impacto, evidência real, passagem de contexto e segurança condicionais.
- [x] Núcleo de instruções menor, sem arquivos ou dependências novos.
- [x] Guia e documentação operacional alinhados.
- [x] PLAN orienta atualizar resumo e próximo passo quando decisão os substituir; registros anteriores são identificados como históricos, sem checklist novo.
- [x] Regra de regressão e prompts de revisão incluem variantes próximas afetadas pela mesma causa, sem auditoria global ou suíte completa obrigatória.
- [x] R2-01 e R2-02 incorporados à política de validação sob demanda, sem ampliar modelos ou instruções permanentes.
- [x] P4-01 substitui a frase existente sem aumentar a contagem de palavras do núcleo; P4-02 fica na política sob demanda. Prompts de revisão alinhados, sem checklist novo.
- [x] P5-01 acrescenta somente uma frase na política sob demanda; modelos, kit e guia permanecem inalterados, sem auditoria global obrigatória.

## Verificação

T3 documental para publicação: comparar modelos/kit, conferir UTF-8, diff, referências e textos dos prompts; confirmar commit remoto após o envio.
Não há mudança funcional ou visual no guia; navegador e build não são necessários.

## Limites

Publicação no GitHub autorizada pelo usuário. Sem instalação de ferramentas, remoção de pesquisa ou cópia do livro.
Licença final do método continua pendente. Economia de tokens por tarefa não foi medida.
