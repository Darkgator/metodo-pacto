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

## Nível de Validação

- Nível da alteração ou checkpoint: [`T0` direta | `T1` leve | `T2` relevante | `T3` marco]
- Prova automatizada ou determinística esperada: [preencher ou não aplicável em T0]
- Validação humana necessária: [nenhuma ou ação objetiva do usuário em T2/T3]
- Smoke clássico obrigatório ao fechar a fase: [sim/não/não aplicável]

## Segurança, Dados e Risco Legal

- [ ] [Entradas externas validadas, se aplicável.]
- [ ] [Dados sensíveis protegidos em logs, UI, testes e armazenamento, se aplicável.]
- [ ] [Credenciais fornecidas no chat, se houver, não foram persistidas, reexpostas ou incluídas em comandos visíveis, arquivos, logs ou commits.]
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

- [ ] [T0: nenhuma execução de teste, navegador, build, lint, typecheck ou checklist, se aplicável.]
- [ ] [T1: uma única prova curta e direcionada, se aplicável.]
- [ ] [T2: somente testes unitários, integração, regressão ou E2E necessários à fatia, se aplicável.]
- [ ] [T3: smoke clássico e verificações relevantes ao fechar fase, PR, release ou deploy, se aplicável.]
- [ ] [Validação visual no navegador apenas por requisito da SPEC, pedido explícito, fluxo funcional relevante ou fechamento visual de fase.]
- [ ] [Teste manual pedido ao usuário apenas quando ele for a única evidência confiável disponível.]

### Documentação

- [ ] `README.md` atualizado, se aplicável.
- [ ] `.env.example` atualizado, se aplicável.
- [ ] `CHANGELOG.md` atualizado.
- [ ] Arquivos textuais salvos em UTF-8 e textos em pt-BR sem mojibake, se aplicável.
- [ ] Textos explicativos sem travessões e com pontuação natural, se aplicável.

## Definition of Done

- [ ] Implementação concluída.
- [ ] Validação correspondente ao nível T0, T1, T2 ou T3 concluída.
- [ ] Smoke clássico executado se a fase criou ou alterou comportamento executável.
- [ ] Build, lint, typecheck, UI e acessibilidade executados apenas quando exigidos pelo nível, pela SPEC ou pela fase.
- [ ] Seeds e `.env.example` atualizados, se aplicável.
- [ ] Codificação UTF-8 preservada e acentuação pt-BR correta em chat, docs, arquivos e UI, se aplicável.
- [ ] Textos destinados a pessoas revisados para evitar travessões e manter leitura fluida, se aplicável.
- [ ] Obsoletos e backups tratados conforme turning point, se aplicável.
- [ ] Mensagem de commit preparada em Conventional Commits.
