# Continuidade local PACTO

Use somente quando o projeto já tiver `.pacto/pacto-estado.py` e a tarefa precisar sobreviver a uma troca de assunto ou sessão.

- `contexto --sessao ID` recupera o trabalho associado; se não houver associação, ele mostra opções sem escolher uma sozinho.
- `mostrar ID` traz o registro completo de um trabalho. Leia-o apenas se o resumo não bastar.
- Toda mutação exige `--esperada-revisao N`. Em conflito, releia e reconcilie; não repita a alteração cega com a revisão nova.
- `associar` vincula uma sessão. `alternar` pausa a anterior quando ela não estiver ativa em outra sessão. Trabalho concluído exige reabertura explícita.
- `provar` é o único comando que executa verificações configuradas. Hooks, contexto e verificar nunca executam comandos.
- Evidência verde só vale enquanto os arquivos declarados não mudarem. Uma captura visual ou áudio registra inspeção, mas não prova fidelidade por si só.
- Publicação precisa separar ambiente e revisão esperados dos observados. Informação sem fonte verificável permanece como informada.

Não grave conversas, segredos ou saídas completas de terminal no estado. Guarde arquivos longos no projeto e referencie-os.
