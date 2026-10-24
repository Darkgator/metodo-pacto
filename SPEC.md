# Contrato da reengenharia incremental

## Objetivo e autorização

Executar R5 a R7 da revisão arquitetural, autorizado após o primeiro lote: consolidar fontes operacionais, reduzir repetição, refinar regressão, resultado esperado e fallback e automatizar a verificação do pacote. Preservar o ciclo PACTO, a proporcionalidade e as decisões dos projetos existentes. A autorização cobre as fatias deste lote, sem nova aprovação a cada checkpoint.

## Primeiro lote preservado

- [x] Base anterior separada em ZIP fora da área ativa, com conteúdo e SHA-256 conferidos e tag local de recuperação.
- [x] Instalador distingue suporte do pacote, instruções e contratos do projeto e estado mutável; instalar não cria todos os contratos opcionais.
- [x] Adoção preserva AGENTS existente; atualização mantém trabalho registrado; remoção preserva contratos, estado e evidências.
- [x] Runtime e verificador compartilham a validação do estado.
- [x] Resumo respeita seu teto incluindo aviso e mantém próximo passo e bloqueio.
- [x] Evidência distingue execução de suficiência, trata entrada ausente e alterada durante a execução, distingue saídas e não copia stdout/stderr arbitrários para o estado.
- [x] Publicação incompleta aparece pendente; informação manual não equivale a confirmação automática.
- [x] Prompts ativos respeitam aprovação de plano inteiro, preservando a opção de autorizar só uma fatia.
- [x] Testes de regressão cobrem os casos pertinentes D01 a D09 e preservam proteções anteriores; distribuição e verificador passam.

## Limites e verificação

Sem reescrita do zero, MCP, memória obrigatória, serviço, banco central, novas sessões pagas de IA ou ativação em outros projetos/hosts. A cópia arquivada não muda instalações já existentes. Integração real no host e benefício econômico permanecem separados das provas locais.

Executar `python -m unittest discover -s tests -v`, `python scripts/distribuir_pacto.py --conferir` e `python scripts/verificar_kit.py`; testar somente em pastas temporárias próprias. Conferir referências locais, diff e UTF-8. Provas de comportamento não estabelecem adesão universal nem economia de tokens.

## Aceite do segundo lote

- [x] Entrada permanente menor, com regras críticas preservadas e detalhes condicionais encaminhados a fontes locais canônicas por assunto.
- [x] Prompts operacionais compartilhados têm fonte única; distribuição detecta divergência no Markdown e HTML, sem gerar o guia inteiro.
- [x] Regra de bug retém regressão proporcional que rejeita o defeito; resultado esperado vem de referência independente da implementação testada.
- [x] Fallback preserva restrições explícitas; mudança de alvo, ambiente ou critério exige decisão quando ultrapassar o combinado.
- [x] Verificador detecta problemas de UTF-8, referências locais, estrutura dos guias e distribuição sem rede ou chamadas de IA.
- [x] CI executa verificador e testes em Windows e Linux, com permissões de leitura e limite de duração.
- [x] Testes e controles negativos comprovam as falhas determinísticas cobertas; resultado remoto e limites de adesão são registrados.

R8 continua condicionado a uma necessidade e piloto próprios. Publicação não é ativação nos hosts. Não criar executor pago, novo serviço ou avaliação de IA neste lote.

## Fechamento autorizado

O pedido de concluir o que ainda for executável cobre o teste da linha completa de comando declarada, smoke do kit instalado e integração da entrega validada na main. A versão anterior continua recuperável pela tag e ZIP, sem ativação em outros projetos/hosts.

- [x] Smoke isolado de instalação, verificação, execução distribuída, retomada, atualização e remoção preservadora.
- [x] Linha completa declarada do hook validada em Windows e Linux na CI, incluindo espaço/acento, associação da sessão e ausência de escrita.
- [x] Integração por PR com checks aprovados, sem bypass, e confirmação da revisão efetiva na main.
