# Contrato da reengenharia incremental

## Objetivo e autorização

Preservar a base anterior e corrigir o primeiro lote aprovado da revisão arquitetural de 24/10/2026: R1 a R4, com regressões. Preservar o ciclo PACTO, a proporcionalidade e as decisões dos projetos existentes. A autorização cobre as fatias deste lote, sem nova aprovação a cada checkpoint.

## Aceite deste lote

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

As etapas R5 a R7 e eventual piloto R8 continuam identificadas no relatório de revisão; não são condição para declarar concluído este primeiro lote. Publicação não é ativação nos hosts.
