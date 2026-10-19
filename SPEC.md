# SPEC.md

## Fase atual

Consolidar o PACTO sem inflar o núcleo de instruções.

Rodada atual: registrar benefícios observados com fontes, atribuição e limites, em catálogo sob demanda. A pesquisa não acrescenta regras ao núcleo. Comparação causal de tempo e tokens continua sem demonstração.

Complementos aprovados em 19/10/2026: POC-01, reconciliação do estado vigente na retomada; regressão de variantes próximas afetadas pela mesma causa; R2-01, smoke pelo caminho principal do pacote entregue; R2-02, comparação inicial com a referência visual aprovada; P4-01, preservar o aceite; P4-02, retestar a revisão corrigida e reconfirmar achados se a base mudar; P5-01, conferir preservação do não afetado em edição parcial; P6-01, reconciliar ambiente e revisão publicados com os registros vigentes, distinguindo publicação de fechamento concluído; P7-01, prova visual no artefato final; P8-01, considerar operação conjunta IA+usuário quando ela melhorar a evidência. Sem alterações nos aplicativos de referência.

## Escopo aprovado

Aplicar recomendações 01 a 07 e incorporar 08 a 13 somente com seus gatilhos.
O piloto 14 continua opcional, sem automação, ferramenta ou documento obrigatório.

## Critérios de aceite

- [x] Modelos oficiais e cópias do kit idênticos; CLAUDE como ponte curta.
- [x] Documentos e leituras condicionais; descoberta sem recomendação prematura.
- [x] Caminhos portáveis, histórico separado e regras Git/tentativas coerentes.
- [x] Validação por impacto, evidência real, passagem de contexto e segurança condicionais.
- [x] Consolidação inicial reduziu o núcleo sem arquivos ou dependências novos.
- [x] Guia e documentação operacional alinhados.
- [x] PLAN orienta atualizar resumo e próximo passo quando decisão os substituir; registros anteriores são identificados como históricos, sem checklist novo.
- [x] Regra de regressão e prompts de revisão incluem variantes próximas afetadas pela mesma causa, sem auditoria global ou suíte completa obrigatória.
- [x] R2-01 e R2-02 incorporados à política de validação sob demanda, sem ampliar modelos ou instruções permanentes.
- [x] P4-01 substitui a frase existente sem aumentar a contagem de palavras do núcleo; P4-02 fica na política sob demanda. Prompts de revisão alinhados, sem checklist novo.
- [x] P5-01 acrescenta somente uma frase na política sob demanda; modelos, kit e guia permanecem inalterados, sem auditoria global obrigatória.
- [x] P6-01 refina o fechamento na política sob demanda e no prompt 7B do guia, sem ampliar o núcleo ou exigir novo documento/checklist.
- [x] P7-01 exige prova visual do artefato final somente quando houver requisito visual; P8-01 orienta operação conjunta em T2/T3 apenas quando ela for a melhor prova. Ambos ficam na política sob demanda e no prompt 7B, sem ampliar o núcleo ou criar checklist.
- [x] Catálogo positivo registra 14 observações em 12 episódios, separa aplicação explícita, contribuição plausível, participação humana e atribuição não demonstrada; resumo público anonimizado e rastreabilidade local.
- [x] Redução textual dos modelos foi medida separadamente de tokens consumidos; tempo de desenvolvedor, bugs e retestes evitados permanecem sem quantidade causal demonstrada.

## Verificação

T3 documental para publicação: comparar modelos/kit, conferir UTF-8, diff, referências e textos dos prompts; confirmar commit remoto após o envio.
Não há mudança funcional ou visual no guia; navegador e build não são necessários.

## Limites

Publicação no GitHub autorizada pelo usuário. Sem instalação de ferramentas, remoção de pesquisa ou cópia do livro.
Licença final do método continua pendente. Economia de tokens por tarefa não foi medida.
