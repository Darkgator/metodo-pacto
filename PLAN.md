# PLAN.md

## Estado atual

Protótipo `2026.10.22.2` publicado na main do GitHub no commit `4384cf6`, com fechamento documental em `01d0d03`. A implementação local `2026.10.22.3` corrige a perda silenciosa por leitura antiga e a ausência de contexto em subpasta, adiciona esquema 2, instalação segura, evidências dirigidas, publicação comparada e uma bancada sem consumo implícito.

Planejamento e contratos: [PLANO-IMPLEMENTACAO-CONTINUIDADE.md](docs/PLANO-IMPLEMENTACAO-CONTINUIDADE.md). Resultado honesto de validação: [resultado-validacao-continuidade.md](docs/resultado-validacao-continuidade.md). A implementação e os testes locais foram concluídos nesta rodada; integração real de host e avaliação com IA continuam pendentes por exigirem confiança, executor e orçamento explícitos.

Fontes oficiais: `templates/` para os seis modelos e `docs/validacao-proporcional.md` para a política distribuída. Histórico de alterações fica no Git. Benefícios e limites estão em [evidências](docs/evidencias-de-beneficios.md).

## Menor fatia verificável

- [x] Publicar o protótipo de estado, skill e hook com cinco testes básicos e conferir a distribuição inicial.
- [x] Revisar a entrega contra o plano completo e identificar defeitos e etapas omitidas.
- [x] Preparar roteiro executável de conclusão, com contratos e critérios de aceite.
- [x] E00 a E07, E09, E10 e E13: núcleo, distribuição, instalação, documentação e bateria local.
- [x] E08 local: plugin Codex conferido contra documentação oficial e adaptador Claude delimitado sem manifesto especulativo.
- [x] E11 local: bancada de quatro cenários e oito execuções máximas preparada sem chamar IA.
- [ ] E12: confiança e eventos reais do Codex, reconhecimento no Claude e piloto comparativo dependem do host, de intervenção humana e de orçamento/executor.
- [ ] E14: revisar, versionar e publicar esta entrega após a validação final desta rodada.

## Decisões e continuidade

- MCP, servidor, sincronização entre máquinas e registro de chat continuam fora do escopo. A conclusão planejada terá automações locais proporcionais e estado atualizado pelo agente em mudanças relevantes.
- A instalação e confiança de hooks continuam ação humana explícita no Codex Desktop; esta implementação não contorna a confiança do aplicativo.
- Adesão, economia e acerto de interpretação não estão comprovados pelos testes locais; piloto em trabalho real continua necessário e não deve consumir IA sem orçamento explícito.
