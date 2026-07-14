# SPEC.md

Criador do método: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

## Fase Atual

[Nome da fase]

## Contexto

[Explique a funcionalidade em linguagem de negócio.]

## Fora de Escopo

- [Liste o que não será feito agora.]

## Variáveis Decisivas

- Usuários totais e simultâneos: [preencher ou n/a]
- Dados sensíveis: [preencher ou n/a]
- Uso de IA: [central/auxiliar/não aplicável]
- Envio de dados para APIs externas: [sim/não/restrições]
- Autenticação, autorização e perfis: [preencher ou n/a]
- Multi-cliente/multi-tenant: [sim/não/n/a]
- Integrações externas: [preencher ou n/a]
- Hospedagem, operação e orçamento: [preencher ou n/a]
- Uso comercial, licenças e obrigações legais: [preencher ou n/a]

## Critérios de Aceite

- [ ] [Regra binária: dado X, quando Y, então Z.]
- [ ] [Regra binária.]
- [ ] [Regra binária.]

## Segurança, Dados e Risco Legal

- [ ] [Entradas externas validadas, se aplicável.]
- [ ] [Dados sensíveis protegidos em logs, UI, testes e armazenamento, se aplicável.]
- [ ] [Permissões, autenticação e autorização revisadas, se aplicável.]
- [ ] [Dependências, assets, modelos, datasets, APIs ou serviços novos tiveram licença/termos avaliados, se aplicável.]
- [ ] [Uso comercial, redistribuição, SaaS, copyleft, atribuição e privacidade verificados quando houver item externo novo.]

## Obsoletos, Backups e Turning Points

- [ ] [A mudança foi avaliada como turning point ou não.]
- [ ] [Git cobre o histórico ou foi definido backup mínimo, se aplicável.]
- [ ] [Arquivos obsoletos foram movidos para `_archive/obsolete/`, se aplicável.]
- [ ] [Backups foram criados em `_archive/backups/`, se aplicável.]
- [ ] [Toda pasta arquivada possui README com motivo, origem e condição de remoção.]

## Checklist

### Dados

- [ ] [Schema, migração, seed ou estrutura de armazenamento.]

### Backend

- [ ] [Serviços, endpoints, validações, integrações ou regras.]

### Frontend/UI

- [ ] [Telas, componentes, estados de carregamento, vazio, erro e sucesso.]

### Testes

- [ ] [Smoke test ou validação mínima do fluxo essencial, se aplicável.]
- [ ] [Testes unitários para regras isoladas, se aplicável.]
- [ ] [Testes de integração para fronteiras entre módulos, se aplicável.]
- [ ] [E2E para jornadas críticas, se aplicável.]
- [ ] [Teste de regressão para bug corrigido, se aplicável.]
- [ ] [Acessibilidade, responsividade ou validação visual para UI, se aplicável.]
- [ ] [Spider/crawl para descoberta de rotas, links ou superfície exposta, se aplicável.]
- [ ] [Testes manuais críticos.]

### Documentação

- [ ] `README.md` atualizado, se aplicável.
- [ ] `.env.example` atualizado, se aplicável.
- [ ] `CHANGELOG.md` atualizado.
- [ ] Arquivos textuais salvos em UTF-8 e textos em pt-BR sem mojibake, se aplicável.

## Definition of Done

- [ ] Implementação concluída.
- [ ] Lint/formatador aprovado.
- [ ] Build aprovado.
- [ ] Testes aprovados.
- [ ] UI validada, se aplicável.
- [ ] Acessibilidade básica verificada, se aplicável.
- [ ] Seeds e `.env.example` atualizados, se aplicável.
- [ ] Codificação UTF-8 preservada e acentuação pt-BR correta em chat, docs, arquivos e UI, se aplicável.
- [ ] Obsoletos e backups tratados conforme turning point, se aplicável.
- [ ] Mensagem de commit preparada em Conventional Commits.
