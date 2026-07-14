# Variáveis Decisivas

Criador: Alexandre Barroso de Miranda  
Atuação: Consultor de Processos  
Método: PACTO

Antes de sugerir stack, IA, banco, hospedagem, arquitetura ou custo, o agente precisa levantar variáveis que mudam a solução inteira.

Essas perguntas não são burocracia. Elas evitam escolher uma stack boa para um cenário errado.

## Quando usar

Use esta etapa em projeto novo, feature crítica, integração com IA, produto com usuários reais, sistema com dados sensíveis ou qualquer solução que possa escalar.

Para tarefa trivial, não precisa aplicar este bloco completo.

## Perguntas essenciais

### Uso e escala

- Quantas pessoas usarão o sistema no início?
- Quantas pessoas podem usar ao mesmo tempo?
- O uso será interno, externo, público ou por cliente?
- Existem picos previsíveis de acesso?
- O sistema precisa funcionar offline ou em rede instável?
- Qual é a expectativa de crescimento em 6 e 12 meses?

### Dados

- Que tipos de dados serão armazenados?
- Há dados pessoais, financeiros, médicos, fiscais, contábeis, jurídicos ou sigilosos?
- Há arquivos, áudios, imagens, PDFs, planilhas ou documentos?
- Quanto volume de dados é esperado?
- Existe necessidade de auditoria, histórico ou rastreabilidade?
- Existe retenção obrigatória ou prazo para exclusão de dados?

### IA e automação

- A IA é parte central do produto ou apenas recurso auxiliar?
- O sistema precisa gerar texto, classificar, transcrever, extrair dados, pesquisar ou tomar decisões?
- O uso de IA precisa ser rastreável ou revisado por humano?
- Pode enviar dados de usuários/clientes para APIs externas de IA?
- Há exigência de modelo local, privado ou com retenção zero?
- O custo por uso de IA precisa ter limite?

### Segurança e acesso

- Haverá login?
- Quais perfis de acesso existem?
- Há clientes diferentes no mesmo sistema?
- Um usuário pode ver dados de outro cliente?
- É necessário MFA, SSO, logs de auditoria ou trilha de aprovação?
- O sistema terá operação em produção com dados reais?

### Integrações

- Quais APIs externas serão usadas?
- Há serviços pagos, limites de requisição ou dependência de terceiros?
- Existem webhooks, envio de e-mail, WhatsApp, pagamentos ou automações?
- Alguma integração exige contrato, chave, escopo de permissão ou revisão legal?

### Plataforma e operação

- O sistema será web, mobile, desktop, CLI, automação ou backend?
- Onde será hospedado?
- Quem vai operar e manter?
- Há orçamento de infraestrutura?
- O deploy precisa ser simples para usuário não técnico?
- O projeto precisa rodar localmente sem internet?

### Legal e licenciamento

- O produto será usado comercialmente?
- Será distribuído, vendido, entregue a cliente ou usado só internamente?
- Pode usar dependências com copyleft?
- Pode usar assets, fontes, modelos, datasets ou templates externos?
- Há obrigação de LGPD, contratos com clientes ou normas do setor?

## Saída esperada

Depois dessas perguntas, o agente deve produzir:

- premissas confirmadas;
- dúvidas bloqueantes;
- riscos por categoria;
- impacto na stack;
- impacto em banco e hospedagem;
- impacto em IA;
- impacto em segurança;
- primeira fatia verificável.

## Prompt curto

```text
Antes de sugerir stack ou arquitetura, levante as variáveis decisivas do projeto.

Pergunte apenas o que pode mudar a stack, banco, IA, segurança, custo, deploy ou arquitetura.

Cubra, quando aplicável:
- usuários totais e simultâneos;
- tipo e sensibilidade dos dados;
- necessidade de IA e limites de envio de dados;
- autenticação, autorização e multi-cliente;
- integrações externas;
- hospedagem, operação e orçamento;
- uso comercial, licenças e obrigações legais.

Depois, explique como cada resposta impacta a solução.
Não escreva código ainda.
```
