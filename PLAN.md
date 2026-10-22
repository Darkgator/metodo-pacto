# PLAN.md

## Estado atual

Kit `2026.10.22.2` pronto para publicação: estado local opcional por trabalho, skill PACTO e hook somente de leitura para Codex Desktop. O núcleo automatizado passou nos cenários de ciclo, conflito, trava, contexto de hook e kit corrompido. A ativação real do hook continua dependente de revisão e confiança manual no Codex Desktop.

Fontes oficiais: `templates/` para os seis modelos e `docs/validacao-proporcional.md` para a política distribuída. Histórico de alterações fica no Git. Benefícios e limites estão em [evidências](docs/evidencias-de-beneficios.md).

## Menor fatia verificável

- [x] Implementar estado com gravação atômica, revisão e contexto curto.
- [x] Criar skill e hook sem escrita automática.
- [x] Executar controles negativos do kit e conferir todas as referências ativas.
- [ ] Publicar a versão e registrar o commit e a sincronização remota.

## Decisões e continuidade

- Não criar MCP, servidor, sincronização entre máquinas, registro de chat ou hook que escreva estado automaticamente nesta versão.
- A instalação e confiança de hooks continuam ação humana explícita no Codex Desktop.
- Adesão, economia e acerto de interpretação não estão comprovados pelos testes locais; piloto em trabalho real continua necessário.
