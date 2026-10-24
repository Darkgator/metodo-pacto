# Continuidade local PACTO

Use somente quando o projeto já tiver `.pacto/pacto-estado.py` e a tarefa precisar sobreviver a uma troca de assunto ou sessão.

- `contexto --sessao ID` recupera o trabalho associado; se não houver associação, ele mostra opções sem escolher uma sozinho.
- `mostrar ID` traz o registro completo de um trabalho. Leia-o apenas se o resumo não bastar.
- Toda mutação exige `--esperada-revisao N`. Em conflito, releia e reconcilie; não repita a alteração cega com a revisão nova.
- `associar` vincula uma sessão. `alternar` pausa a anterior quando ela não estiver ativa em outra sessão. Trabalho concluído exige reabertura explícita.
- `provar` é o único comando que executa verificações configuradas. Hooks, contexto e verificar nunca executam comandos.
- `executada` não comprova suficiência; `passou` refere-se à verificação configurada. Entrada ausente ou alterada impede confirmação; uma prova vence quando entradas, saídas ou ausências declaradas mudam. Registros antigos precisam ser refeitos para essa proveniência. Captura visual/áudio não prova fidelidade por si só.
- Publicação separa ambiente e revisão esperados dos observados. Registro manual é informado, incompleto é pendente; este comando não confirma automaticamente o ambiente remoto.

Não grave conversas, segredos ou saídas completas de terminal no estado. Guarde arquivos longos no projeto e referencie-os.
