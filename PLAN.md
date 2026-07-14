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

## Checkpoints

- [x] Checkpoint 1: criar contratos operacionais na raiz.
- [ ] Checkpoint 2: revisar guia visual contra os contratos da raiz.
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

Como não há Git detectado no workspace pai, o rollback deve ser manual se necessário: remover os arquivos de raiz criados nesta fase e restaurar o README anterior a partir de cópia local, histórico do editor ou backup externo.

## Obsoletos e Backups

- É turning point? Não. É formalização documental sem remoção ou reestruturação destrutiva.
- Git cobre o histórico? Não foi detectado Git no workspace pai.
- Backup adicional necessário? Não para esta alteração pequena.
- Arquivos que ficarão obsoletos: nenhum.
- Pasta prevista: não aplicável.
- `README.md` de arquivamento necessário: não.

