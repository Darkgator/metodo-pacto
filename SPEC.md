# SPEC.md

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Fase Atual

Aplicar o Método PACTO ao próprio projeto do framework.

## Contexto

O projeto já possui conteúdo avançado do Método PACTO, incluindo regras universais, guia visual, templates, pesquisa e prompts. A fase atual formaliza o próprio projeto como um caso de uso do método, criando contratos operacionais na raiz e alinhando documentação, templates e fluxo visual.

## Fora de Escopo

- Criar aplicação dinâmica.
- Publicar site.
- Criar pacote instalável.
- Remover conteúdo histórico.
- Criar backups desnecessários para alterações documentais pequenas.
- Definir licença pública final do método.

## Variáveis Decisivas

- Usuários totais e simultâneos: uso documental/local; simultaneidade não é fator de arquitetura.
- Dados sensíveis: não devem existir no projeto.
- Uso de IA: auxiliar para briefing, documentação, revisão e desenvolvimento assistido.
- Envio de dados para APIs externas: apenas conteúdo sem segredos ou dados sensíveis.
- Autenticação, autorização e perfis: não aplicável.
- Multi-cliente/multi-tenant: não aplicável.
- Integrações externas: nenhuma obrigatória.
- Hospedagem, operação e orçamento: local por enquanto.
- Uso comercial, licenças e obrigações legais: possível uso profissional; licença final ainda pendente.

## Critérios de Aceite

- [x] `BRIEF.md` existe na raiz e consolida o contexto do projeto.
- [x] `AGENTS.md` existe na raiz e orienta agentes de forma curta e prática.
- [x] `CLAUDE.md` existe na raiz e orienta Claude Code sem duplicação excessiva.
- [x] `SPEC.md` existe na raiz e descreve a fase atual.
- [x] `PLAN.md` existe na raiz e define próximos checkpoints.
- [x] README aponta para os contratos operacionais da raiz.
- [x] Regras de UTF-8, segurança, licenciamento, testes e turning points estão refletidas nos contratos.
- [x] Regra de escrita natural, sem travessões em textos explicativos, está refletida nos contratos, templates, kit e guia visual.
- [x] Chave fornecida pelo usuário no chat gera aviso de risco, sem bloqueio automático da tarefa, e não pode ser persistida ou reexposta.
- [x] Política de validação proporcional T0 a T3 relaciona alteração individual, checkpoint, fechamento de fase e pré-release.
- [x] Mudança trivial não gera teste, navegador, build, lint, typecheck, checklist, plano de teste ou lista para o usuário.
- [x] Smoke clássico permanece obrigatório ao fechar fase com comportamento executável e antes de PR relevante, release ou deploy.
- [x] Retomada em outro ambiente exige comparação segura entre branch local e upstream antes de editar, sem integração ou descarte automático diante de divergência.
- [x] Não há backup desnecessário para esta mudança documental.

## Segurança, Dados e Risco Legal

- [x] Nenhum segredo real foi inserido.
- [x] A regra de tratamento de chaves fornecidas no chat foi documentada sem adicionar exemplos com chaves reais.
- [x] A política de validação não reduz exigências para segurança, dados, autenticação, integração crítica, release ou deploy.
- [x] Dados sensíveis não foram adicionados.
- [x] Licença pública final permanece como decisão pendente.
- [x] Dependências externas novas não foram adicionadas.

## Obsoletos, Backups e Turning Points

- [x] A mudança foi avaliada como não destrutiva.
- [x] Repositório Git local e remoto público estão configurados para o histórico do método.
- [x] A sincronização entre ambiente local e remoto foi documentada sem permitir `reset`, descarte, `stash`, `rebase`, `merge` ou `force push` automático.
- [x] Backup adicional não é necessário para esta alteração documental.
- [x] Arquivos obsoletos não foram gerados.

## Checklist

### Documentação

- [x] `BRIEF.md` criado.
- [x] `AGENTS.md` criado.
- [x] `CLAUDE.md` criado.
- [x] `SPEC.md` criado.
- [x] `PLAN.md` criado.
- [x] `README.md` atualizado.

### Guia Visual

- [x] Validar se o guia visual ainda abre após as alterações.
- [x] Atualizar guia visual se novos prompts ou etapas forem alterados.

### Templates

- [x] Conferir se templates continuam alinhados ao método.
- [x] Atualizar templates se a SPEC da fase mudar regras universais.

### Verificação

- [x] Buscar termos principais: `Método PACTO`, `Alexandre Barroso de Miranda`, `turning point`, `UTF-8`.
- [x] Buscar termos principais: `T0`, `T1`, `T2`, `T3`, `smoke clássico`, `navegador`.
- [x] Buscar termos de sincronização: `git fetch --prune`, `git pull --ff-only`, `divergente`, `upstream`.
- [x] Verificar ausência de mojibake real nos arquivos alterados.
- [x] Revisar links e caminhos citados.

## Definition of Done

- [x] Implementação documental concluída.
- [x] Contratos operacionais criados na raiz.
- [x] README atualizado.
- [x] UTF-8 e acentuação pt-BR preservados.
- [x] Obsoletos e backups tratados conforme turning point, se aplicável.
- [x] Próximos passos registrados no `PLAN.md`.
