# PLAN.md

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Objetivo

Aplicar o Método PACTO ao próprio projeto do framework e deixar a raiz pronta para uso por agentes de código.

## Escopo

- Criar contratos operacionais na raiz.
- Consolidar briefing do projeto.
- Registrar SPEC da fase atual.
- Registrar plano de continuidade.
- Atualizar README com os novos arquivos de raiz.
- Consolidar regras universais novas nos contratos, templates, kit e guia visual.
- Definir validação proporcional por alteração, checkpoint, fase e pré-release.
- Definir checagem segura de sincronização entre ambiente local e repositório remoto antes de retomar trabalho.

## Fora de Escopo

- Publicar o método.
- Criar site dinâmico.
- Definir licença final.
- Refatorar todos os documentos históricos.
- Criar backup sem turning point real.

## Decisões Aprovadas

- Nome do método: Método PACTO.
- Criador: Alexandre Barroso de Miranda.
- Atuação: Consultor de Processos.
- Stack do próprio projeto: documentação Markdown + HTML estático.
- Guia visual atual: `guia-visual/index.html`.

## Variáveis Decisivas Consideradas

- Usuários simultâneos: não decisivo para a fase documental.
- Dados e sensibilidade: não incluir dados sensíveis.
- IA e custo/privacidade: uso de IA apenas para apoio documental e desenvolvimento assistido.
- Integrações externas: nenhuma obrigatória.
- Autenticação/autorização/multi-cliente: não aplicável.
- Hospedagem/operação/orçamento: local por enquanto.
- Licenciamento/legal/comercial: licença pública final pendente.

## Arquivos ou Áreas Afetadas

- `BRIEF.md`
- `AGENTS.md`
- `CLAUDE.md`
- `SPEC.md`
- `PLAN.md`
- `README.md`
- `docs/regras-universais.md`
- `docs/validacao-proporcional.md`
- `docs/framework-v1-proposta.md`
- `docs/briefing-assistido.md`
- `templates/`
- `kit-pacto/`
- `guia-visual/`

## Checkpoints

- [x] Checkpoint 1: criar contratos operacionais na raiz.
- [x] Checkpoint 2: revisar guia visual contra os contratos da raiz.
- [x] Checkpoint 2a: aplicar a política de validação proporcional T0 a T3 nos contratos, templates, kit e guia visual.
- [x] Checkpoint 2b: aplicar regra de comparação entre local e remoto antes de retomar trabalho em outro ambiente.
- [ ] Checkpoint 3: decidir licença e política de distribuição do método.
- [ ] Checkpoint 4: criar pacote final ensinável, se desejado.

## Verificação

- Smoke: abrir `guia-visual/index.html`, se houver mudança visual.
- Documentação: verificar se README aponta para os contratos da raiz.
- Busca: procurar termos principais para consistência.
- Manual: revisar se `SPEC.md` e `PLAN.md` refletem o estado real.

## Riscos

- Segurança: baixo, desde que não sejam adicionados segredos.
- Licenciamento/legal: pendente para distribuição pública.
- Dados: baixo, pois o projeto deve usar apenas dados fictícios.
- Regressão: baixa, por ser alteração documental.

## Rollback

O repositório Git local e o remoto público são a fonte primária de rollback. Para uma mudança isolada, reverter o commit correspondente após revisar o impacto.

## Obsoletos e Backups

- É turning point? Não. É formalização documental sem remoção ou reestruturação destrutiva.
- Git cobre o histórico? Sim, com repositório local e remoto público.
- Backup adicional necessário? Não para esta alteração pequena.
- Arquivos que ficarão obsoletos: nenhum.
- Pasta prevista: não aplicável.
- `README.md` de arquivamento necessário: não.
