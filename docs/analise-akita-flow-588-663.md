# Akita, Flow 588 e 663: análise para o PACTO e ferramentas auxiliares

Data: 24/10/2026. Base do método conferida: `ed19ebdd62d60b2b79ae2561d121b81af19aa904`, kit `2026.10.22.3`.
Status: análise e propostas para decisão. Nenhuma regra, skill, integração ou configuração instalada por este documento.

## 1. Parecer

Há material muito útil nos dois episódios. A contribuição mais forte é transformar intenção em feedback verificável: definir o resultado, preservar restrições, confrontar a execução com uma referência capaz de acusar erro e manter a proteção contra regressão.

O PACTO já contém boa parte desses princípios. Recomendo poucos refinamentos nas instruções e mais investimento em provas executáveis. Acrescentar um grande manual inspirado nos podcasts teria pouco valor adicional e aumentaria o contexto permanente.

Como ferramenta separada, a oportunidade mais imediata é facilitar a reprodução de bugs e a construção de regressões pequenas. Para memória entre agentes, recomendo avaliar o AI Memory do próprio Akita antes de ampliar o sistema de memória do PACTO. São propostas distintas: memória recupera informação; teste verifica comportamento.

Também há uma correção de avaliação a fazer em nossa própria entrega: o planejamento de continuidade é mais amplo que a implementação comprovada. A bancada existente ainda não executa agentes. Resolver essa diferença vem antes de alegar que uma nova camada melhorou o método.

## 2. Leitura e origem

Li os dois arquivos completos, em blocos contíguos, incluindo as partes fora de desenvolvimento. Os horários abaixo são da transcrição fornecida, não de uma conferência do áudio original.

| Fonte | Extensão lida | Último horário | SHA-256 do arquivo |
|---|---|---|---|
| `AudioTranscriberAI_FABIO-AKITA---Flow-588.txt` | 305.056 caracteres, 956 linhas; intervalos 0–34.000, 34.000–68.000, 68.000–102.000, 102.000–136.000, 136.000–170.000, 170.000–204.000, 204.000–238.000, 238.000–272.000 e 272.000–305.056 | 04:44:08 | `3A9573535FC78B24956DEC7D600EF0F0D1891091F06E219282A96638269A7AC0` |
| `AudioTranscriberAI_FABIO-AKITA---Flow-663.txt` | 263.716 caracteres, 1.084 linhas; intervalos 0–34.000, 34.000–68.000, 68.000–102.000, 102.000–136.000, 136.000–170.000, 170.000–204.000, 204.000–238.000 e 238.000–263.716 | 04:17:22 | `DF6A9FA7D4BA68B7128AB630D72D71527ECFEFBF38F75DA15909A29C204976C4` |

Total: 568.772 caracteres e aproximadamente nove horas de conversa. A leitura foi do texto integral, não de uma seleção por palavras-chave. Isso não autentica cada transcrição nem confirma toda afirmação factual do podcast.

Há erros de reconhecimento, especialmente em nomes de ferramentas e endereços. Confirmei o blog e os repositórios nas fontes do autor antes de recomendá-los. Os podcasts continuam sendo relatos e argumentos, não um experimento causal de eficácia do PACTO.

Comparei os trechos com `templates/AGENTS.template.md`, `templates/SPEC.template.md`, `templates/INVARIANTES.template.md`, `docs/briefing-assistido.md`, `docs/validacao-proporcional.md`, `docs/evidencias-de-beneficios.md`, a skill PACTO e a implementação/testes de continuidade. Não reexecutei testes dos aplicativos anteriores nem fiz auditoria completa do núcleo.

## 3. Priorização das propostas

P0: corrigir uma lacuna da entrega já anunciada. P1: próxima implementação recomendada. P2: piloto ou melhoria condicionada. P3: adiar.

Nota de 0 a 10 = benefício esperado (0–5) + sustentação no material e no PACTO atual (0–3) + simplicidade da primeira intervenção (0–2). É julgamento de prioridade, não probabilidade de sucesso ou economia medida. Os componentes aparecem entre parênteses.

Confiança alta significa que o trecho e o mecanismo proposto são claros. Confiança média significa que o ganho para o seu ambiente depende de piloto. Nenhuma nota promete percentual de tokens poupados.

### Ajustes no método

| ID | Proposta e motivação | Situação atual | Prioridade / nota | Custo de contexto |
|---|---|---|---|---|
| M01 | Manter teste de regressão para bug comportamental automatizável, derivado da reprodução antes/depois. O teste precisa continuar no projeto e falhar diante do defeito, quando a reintrodução segura for viável. | O PACTO já pede reprodução e preservação dos testes; não explicita com a mesma força a retenção da nova proteção para cada bug pertinente. | P1, **10** (5+3+2), alta | Ajuste curto na seção de bugs; execução local depois, sem IA em cada rodada. |
| M02 | Fixar a fonte do resultado esperado. Um teste pode contradizer a implementação; não pode usar a própria saída defeituosa como gabarito. | SPEC e invariantes já pedem prova direta, mas deixam implícita a independência do esperado. | P1, **10** (5+3+2), alta | Uma frase no contrato existente, quando houver ambiguidade. |
| M03 | Proibir que uma alternativa de execução altere silenciosamente restrição explícita. Após falha, diagnosticar ou propor a mudança, indicando o impacto. | Há limites de escopo e de tentativas, mas o caso de fallback sob urgência pode ser amarrado melhor. | P1, **9** (4+3+2), alta | Refinar a regra de execução existente. |
| M04 | Reavaliar o risco quando um experimento ganha usuários externos, dados de terceiros ou compromisso de disponibilidade. Começar por remover coleta desnecessária. | Segurança antes de produção já está coberta; a mudança de contexto merece um gatilho mais claro. | P2, **9** (4+3+2), alta | Complemento sob demanda em entrega, sem questionário em toda tarefa. |
| M05 | Reconhecer a intervenção humana curta como alternativa à geração insistente: gravação de uma fala, aprovação de referência ou acesso indisponível. | Operação conjunta já está explícita. Recomendação é aplicar e medir, não criar nova regra. | Manter/aplicar, **9** (4+3+2), alta | Nenhum acréscimo permanente. |
| M06 | Distinguir lacuna que pede resposta humana de incerteza que um pequeno protótipo pode resolver. | Briefing é proporcional e opcional, mas o fluxo assistido termina em muitos campos e pode incentivar completude excessiva se mal aplicado. | P2, **8** (4+2+2), média | Ajustar orientação de descoberta; nenhum formulário novo. |

### Ferramentas ou execução separada

| ID | Proposta e primeira entrega | Por que deve ficar separada | Prioridade / nota |
|---|---|---|---|
| F01 | Completar a avaliação já planejada: fixtures reais, executor de agente, verificação do resultado e controles negativos. Mapear a matriz de testes ao que foi realmente exercitado. | É prova da implementação, não mais texto para o agente obedecer. | P0, **9** (5+3+1), alta para a lacuna; ganho futuro não medido. |
| F02 | Um fluxo sob demanda de reprodução de bug: entrada mínima, estado inicial, resultado esperado, comando e teste de regressão usando a stack existente. | Depende do projeto. Não cabe um catálogo universal de testes dentro do AGENTS. | P1, **9** (5+3+1), alta. |
| F03 | CI pequena para o próprio PACTO: conferir distribuição e testes relevantes em checkout limpo, com casos negativos. Depois considerar uma amostra de adesão, com orçamento próprio. | A execução fica no processo de entrega e pode rodar sem modelo. | P1, **9** (5+3+1), alta. |
| F04 | PoC com AI Memory para troca entre agentes, decisões duráveis e retorno após compactação. Comparar com continuidade local mínima. | É memória opcional, com instalação e armazenamento próprios. Não deve virar dependência obrigatória do método. | P2, **8** (5+2+1), média para benefício local. |
| F05 | Extrair solução comprovada para script ou referência reutilizável; criar skill só quando houver uso recorrente que justifique roteamento. | Evita repetir pesquisa sem carregar todas as soluções em cada tarefa. | P2, **8** (4+3+1), alta para o mecanismo. |
| F06 | Rastrear fonte → cópia/derivado → verificação. Começar pela tabela de distribuição existente e pelos documentos ativos afetados. | O inventário serve à manutenção e à análise de impacto. Não exige banco novo. | P2, **8** (4+3+1), alta para distribuição; média para outros derivados. |
| F07 | Avaliar sandbox quando o trabalho exigir maior autonomia ou contato com material não confiável. Considerar AI Jail no ambiente suportado. | É contenção de permissões, não regra de desenvolvimento nem instalação universal. | P3, **6** (3+2+1), média; sua necessidade depende da tarefa. |

## 4. Como ficaria na prática

### M01 + M02 + F02: parar de corrigir o mesmo bug

Base: Flow 588, 02:05:13–02:16:04; Flow 663, 00:52:42–00:59:25.

Antes: corrigir um cálculo, executar o aplicativo e concluir que está funcionando. Outro ajuste desfaz a correção; o usuário precisa reclamar de novo.

Depois: reproduzir com entrada e estado mínimos, declarar o resultado vindo da regra aprovada, corrigir e manter um teste que rejeita o defeito. No portal, por exemplo, incluir o caso da permissão afetada e a variante irmã pertinente. Em uma planilha, conferir valores ou fórmulas do intervalo afetado; no visual, usar a referência e o estado aprovados.

O exemplo numérico do teste não deve ser calculado chamando a mesma função que está sendo testada. Para referência visual ou sonora, o esperado pode ser um artefato aprovado e uma inspeção humana. Independência não exige outra IA nem um especialista em toda alteração.

Quando o bug só aparece depois de um longo fluxo, salvar uma fixture segura ou usar uma fábrica de estados e entrar diretamente no ponto relevante. Em vez de refazer cem ações no portal, preparar o usuário/perfil sintético e o estado que expõe o erro. Manter também a prova de integração quando ela for necessária: teste pequeno não substitui a fronteira real.

Texto candidato, para substituir/refinar a orientação existente:

> Em bug comportamental automatizável, preserve uma regressão mínima da reprodução. O resultado esperado vem da regra ou referência aprovada; confirme que a prova rejeita o defeito quando isso puder ser feito com segurança. Se a automação não couber, declare a limitação e a prova alternativa.

### M03: o fallback não decide outro objetivo

Base: Flow 663, 02:35:16–02:47:01, especialmente 02:41:31–02:42:53.

O caso do NAS é valioso: a IA propôs uma rota de cópia diferente porque a rota solicitada falhou. A alternativa aparentemente prudente ampliava o tempo de exposição ao problema, segundo a experiência relatada pelo Akita.

Aplicação geral: se o usuário fixa um ambiente, dado, referência, protocolo ou caminho crítico, falhar nesse caminho não autoriza substituí-lo silenciosamente. A IA deve diagnosticar a falha e explicitar o custo da alternativa. Se há evidência de que a premissa humana está errada, ela apresenta a evidência. Não se trata de insistir cegamente até funcionar.

Exemplo seu: produção não vira homologação por conveniência do agente. Uma tela diferente não comprova a tela pedida. O usuário dizer que continua vendo o erro é evidência a investigar; não basta repetir que ele deveria recarregar.

Texto candidato:

> Falha de execução não autoriza trocar restrição explícita: preserve o alvo e diagnostique; se a alternativa alterar o combinado, apresente a diferença antes de aplicá-la.

### M04 + M06: contexto muda o nível de engenharia

Base: Flow 663, 00:19:15–00:30:24 e 01:03:18–01:07:30; Flow 588, 04:33:50–04:37:43.

Um protótipo pode começar sem toda a operação de um produto público. Quando passam a existir terceiros, dados privados ou continuidade exigida, a decisão muda. O gatilho é essa mudança real, não o tamanho do repositório ou a palavra “produção” isolada.

Para dado coletado, perguntar primeiro se ele é necessário. Tirar um telefone que não tem uso pode resolver melhor que adicionar criptografia, consentimentos e manutenção para uma coleta inútil. Criptografia isolada não resolve autorização, acesso, retenção ou vazamento em logs.

Para incerteza de produto, uma tela ou prova de conceito delimitada pode esclarecer mais que outro ciclo de perguntas. O agente distingue essa hipótese barata e reversível de uma lacuna que impede decidir com responsabilidade. Em projeto em andamento, reaproveita stack e contratos existentes.

### F01: um ponto nosso que precisa de rigor

Na base inspecionada, `scripts/avaliar_continuidade.py` lê quatro descrições de cenários e imprime parâmetros de orçamento. Com `--executar-ia`, termina informando que não possui executor. Portanto, a bancada está esboçada, mas não executa o comparativo previsto. Isso foi confirmado por leitura do código.

As três classes de teste somam 13 métodos. Há testes úteis de conflito, contexto, migração, hash e instalação; a matriz planejada possui condições adicionais. Não encontrei nesses arquivos provas de morte do processo com lock, falha injetada de fsync/replace ou rollback de instalação. Ausência de teste não prova defeito, mas impede declarar esses contratos comprovados.

O teste de “caminho com espaço e acento” invoca Python e o arquivo diretamente; ele não executa a linha completa `commandWindows` declarada no hook. São provas de fronteiras diferentes.

O registrador de evidências classifica retorno zero como `aprovada`. Isso registra êxito do comando; não demonstra que o comando verificou o aceite. Um comando que só imprime “ok” também termina com zero. O próprio plano reconhece esse limite, que precisa permanecer claro na utilização e no fechamento.

Recomendação: reconciliar o PLAN com a cobertura real, completar os contratos essenciais de armazenamento/instalação e implementar uma avaliação pequena de agente com resultado verificável. Não reabrir a documentação inteira nem fingir que o podcast, por si só, prova falha no produto.

### F03: a menor automação de entrega

Base: Flow 663, 03:35:29–03:38:19.

Não há workflow `.github` nesta base. O primeiro candidato é conferir cópias e rodar os testes do próprio método em ambiente limpo. O teste deve reprovar uma cópia divergente e defeitos conhecidos, não apenas produzir uma lista verde.

CI não torna cada teste correto. Um teste que repete a implementação continua ruim quando executado no GitHub. Também não recomendo publicar automaticamente em produção dos seus aplicativos só porque um workflow ficou verde: isso depende dos seus contratos de entrega e autorização.

## 5. Ferramentas do próprio Akita: o que vale investigar

### AI Memory: principal candidato a PoC

No Flow 663, 03:11:51–03:18:50 e 03:49:19–03:52:00, ele descreve o problema de continuidade, memória útil e troca entre fornecedores. O projeto real existe e usa wiki Markdown versionada como fonte, com índice derivado e integrações de captura/consulta. A documentação prevê funcionamento sem LLM obrigatório. [Repositório](https://github.com/akitaonrails/ai-memory), [comparação mantida pelo autor](https://github.com/akitaonrails/ai-memory/blob/main/docs/comparison.md).

A matriz do mantenedor declara suporte a Codex, Claude Code e Antigravity CLI; Windows nativo é experimental. Isso é informação do projeto, não integração comprovada neste computador. [Matriz oficial](https://github.com/akitaonrails/ai-memory/blob/main/docs/support-matrix.md).

Meu desenho proposto é manter autoridade explícita:

- Pedido humano vigente e contratos aprovados decidem escopo e resultado.
- Estado por trabalho informa execução atual e próximo passo.
- Memória externa recupera conhecimento e histórico, com fonte e possibilidade de estar obsoleta.
- Testes e inspeções verificam o resultado.

Não manter duas fontes independentes para o mesmo estado. O piloto precisa decidir se há coexistência com papéis distintos ou se um componente pode ser removido. Não importar todo o seu histórico nem cruzar clientes automaticamente. Observar o que é capturado, exportado e recuperado.

O MCP futuro do PACTO deve ser reavaliado por esse problema concreto. Não há motivo, nesta análise, para construir um servidor concorrente só para cumprir a ideia antiga.

### AI Jail: opção de contenção, condicionada ao ambiente

O autor mantém um sandbox para agentes. A documentação distingue contenção de acidentes de defesa contra atacante determinado e não promete segurança absoluta. Windows nativo não é suportado; a orientação é WSL2 com backend Linux. [Repositório e limites](https://github.com/akitaonrails/ai-jail).

Para seu computador pessoal Windows, não recomendo migração de ambiente ou instalação universal por reflexo. A primeira decisão é o que precisa ser isolado e se as permissões já disponíveis no host resolvem. AI Jail é uma alternativa quando essa contenção adicional se justifica.

### LLM Coding Benchmark: aproveitar a metodologia

O repositório existe e disponibiliza código e versões do benchmark. É uma referência para investigar tarefas com sequência de alterações, conclusão e sabotagem controlada. [Repositório](https://github.com/akitaonrails/llm-coding-benchmark).

Não recomendo reproduzir a bateria de dezenas de modelos para o PACTO. Escolher poucos casos do seu uso, mesmo modelo/esforço/ambiente nas variantes e aceite externo. Resultados publicados do autor não equivalem a resultado na sua máquina ou no seu método.

### Livro e blog

Encontrei o blog oficial, o livro e a descrição do processo editorial com inventário de fontes e verificadores. O Markdown do livro informado anteriormente também está presente em Downloads; não há necessidade de pedir que você o baixe de novo para esta etapa. Não o reli integralmente nesta rodada. [Livro](https://ailair.akitaonrails.com/pt-br/book/), [bastidores da produção](https://akitaonrails.com/2026/10/13/auto-publiquei-meu-proprio-livro-ebook-competente-o-suficiente/).

O ganho transferível ao PACTO é manter a relação entre fonte e derivado para detectar o que ficou desatualizado. Aproveitar a tabela de cópias já existente é mais simples que criar um sistema editorial novo.

## 6. PoCs pequenos, com condição de abandono

Não executados nesta análise. Estes são recortes propostos para uma implementação posterior.

| PoC | Recorte | Prova de utilidade | Abandonar ou simplificar se |
|---|---|---|---|
| A. Regressão a partir de estado | Um bug real já corrigido, fixture sintética e uma variante relevante; stack de testes já existente. | Defeito original é rejeitado, correção passa, comando pode ser repetido sem IA e o caminho crítico continua coberto. Comparar preparo/reteste com o fluxo atual. | O teste só repete a função, depende de dados reais ou exige infraestrutura desproporcional. |
| B. Memória opcional | Projeto fictício ou cópia sanitizada; tarefa interrompida por pergunta, troca de assunto, retorno e decisão substituída. Depois, troca real de host disponível. | Recupera decisão vigente e próximo passo, não mistura trabalho/cliente, permite exportar/remover; medir contexto e intervenções contra continuidade mínima. | Contexto cresce sem melhorar acerto, exige cuidado constante ou duplica estado sem reconciliação. |
| C. Entrega do próprio PACTO | Mapa requisito → teste → resultado e CI pequena. | Erros conhecidos reintroduzidos em cópia temporária reprovam o pacote; casos sem execução permanecem pendentes. | A mudança só produz mais relatórios e não altera uma decisão de entrega. |

Para teste com novas chamadas de IA, definir executor e orçamento antes. Esta análise não fez chamadas adicionais de agentes, não instalou ferramentas e não iniciou processamento pago dos seus projetos. O custo da pesquisa/leitura atual não foi medido como ganho do método.

## 7. O que já está bem coberto e não precisa ser duplicado

| Argumento dos episódios | Cobertura atual | Decisão |
|---|---|---|
| Contexto e risco antes de tecnologia | Briefing por decisão, premissas reversíveis, alternativa simples. | Manter. |
| Iteração em vez de acerto perfeito no primeiro prompt | Menor fatia verificável e SPEC proporcional. | Manter; permitir experimento delimitado quando esclarecer a incerteza. |
| Não quebrar regras/identidade | INVARIANTES separa negócio, visual, texto, som e contratos. | Manter a separação e conferir execução. |
| Build não comprova fidelidade | Política exige observar artefato e referência. | Não criar outra skill universal para repetir a mesma obrigação. |
| Usuário participa quando melhora o resultado | Operação conjunta, ação humana objetiva e retomada pelo agente. | Aplicar; não pedir recarga, repetição ou teste genérico como resposta automática. |
| Segurança e responsabilidade na publicação | Política de produção com terceiros, autorização, menor privilégio e recuperação. | Manter, reforçando mudança de uso e minimização. |
| Benchmark tem escopo e custo | Catálogo de benefícios já exige comparação equivalente e não confunde tokens com preço. | Executar a avaliação necessária; não acrescentar mais teoria. |
| Ferramenta deve resolver necessidade | Regra permanente exige causa e necessidade demonstradas. | Usar isso também para decidir se uma ferramenta deve ser removida. |

## 8. Pontos que não transformaria em regra literal

Levar os argumentos a sério exige preservar a diferença entre exemplo, hipótese e garantia técnica.

1. **“Teste garante que o bug nunca volta.”** É uma orientação excelente para retenção de regressão. O alcance real é o cenário/assertiva protegidos, com execução efetiva; o teste pode ser incompleto ou estar errado.
2. **“Testar todas as combinações.”** Interpretar como cobrir regras relevantes, limites e combinações de risco. Espaços combinatórios grandes exigem seleção, propriedades ou amostragem; não prometer exaustão sem demonstrá-la.
3. **“Rodar a suíte inteira sempre.”** Preservar a motivação de não regredir; escolher a bateria adequada ao checkpoint, risco e custo. Testes rápidos de toda a aplicação podem ser bons, mas E2E pesado por alteração cosmética contraria a proporcionalidade já acertada.
4. **“O problema é sempre o prompt/usuário.”** Requisitos mal explicados podem causar erro. Modelo, ferramenta, ambiente, dados ou implementação também falham. O caso do offset duplicado no Flow 588, 04:00:11–04:03:38, mostra por que a observação humana deve ser investigada. Responsabilidade pela entrega não elimina a necessidade de diagnosticar a causa técnica.
5. **“Spec Driven Development é inútil.”** Aproveitar a crítica a formato mágico e especificação exaustiva. Não apagar contrato, aceite e limites: o próprio processo descrito usa ideias escritas, regras e verificadores. O PACTO deve continuar flexível e observável.
6. **Rankings de modelos e limiares de tokens/segundo.** São dependentes de tarefa, momento e ambiente. Entre os dois episódios há mudança importante na avaliação dos modelos chineses. O próprio autor publica medições novas. Nada disso justifica congelar marcas ou velocidades mínimas no método. [Atualização do autor em 22/10/2026](https://akitaonrails.com/2026/10/22/llm-benchmark-v4-o-veredito-de-open-source-ate-out-2026/).
7. **Explicações gerais sobre treinamento, consciência, limites futuros e mercado.** Não são necessárias para decidir estas correções. Nesta análise não auditei cada afirmação teórica, histórica, comercial ou política, nem as usei como requisito operacional.
8. **“Delimitar/sanitizar texto resolve prompt injection.”** Revisar origem e reduzir permissões ajuda. Um delimitador no prompt não é, sozinho, isolamento técnico ou garantia de que instrução maliciosa nunca terá efeito.
9. **“Não preciso de plugins.”** É evidência da experiência e do domínio do autor; não proibição geral. A consequência útil para nós é exigir problema concreto e remover o que não ajuda.
10. **“Mais geração significa mais produtividade.”** Os próprios episódios rejeitam isso. Não medir sucesso por linhas, quantidade de agentes, número de regras ou volume de tokens.

## 9. Rastreio das ideias relevantes

| Episódio / horário | Tema aproveitado ou avaliado | Destino nesta análise |
|---|---|---|
| 588, 00:06:32–00:09:45 | Benchmark de projeto, não só fragmento de algoritmo. | F01 e metodologia de avaliação. |
| 588, 00:20:22–00:28:02 | Modelo, harness e pendências após interrupção. | F01/F04; continuidade já coberta conceitualmente. |
| 588, 00:39:57–00:41:21 | Transferir contexto ao trocar ferramenta. | F04, sem ler toda cronologia por padrão. |
| 588, 01:59:55–02:16:04 | Integração incremental, dívida e regressão retida. | M01/F02. |
| 588, 02:16:25–02:21:48 | Segurança, escala real e custos externos. | M04; cobertura proporcional. |
| 588, 02:23:01–02:26:39 | Solução difícil vira skill/script; atenção a instrução externa. | F05 e fronteira de confiança. |
| 588, 02:38:22–02:40:48 | Revisão complementar, falso positivo e melhoria sem fim. | Prova externa e limite de revisão; não adicionar juiz permanente. |
| 588, 02:45:28–02:46:11 | Entradas adversas e limites de campos. | F02, casos pertinentes ao risco. |
| 588, 02:56:41–02:58:40 | Próximo passo humano e documentação de uso/teste. | Operação conjunta já coberta. |
| 588, 03:08:03–03:13:01 | Ambiente reproduzível e receitas de configuração. | F03/F05; usar ferramentas da stack. |
| 588, 03:47:02–03:51:43 | Crítica a formulário mágico; clareza do problema. | M06; preservar contrato proporcional. |
| 588, 04:00:11–04:03:38 | Extração verificável e erro visto pelo humano apesar da garantia da IA. | M02/M03; artefato real como referência. |
| 588, 04:03:44–04:09:51 | Comparação equivalente e troca de ferramentas. | F01/F04; evitar torcida por modelo. |
| 588, 04:33:50–04:37:43 | Protótipo antes de comprometer todo o investimento. | M06. |
| 663, 00:13:17–00:30:24 | Objetivos, ambiente, dado necessário e responsabilidade. | M04. |
| 663, 00:43:29–00:47:47 | Direção coerente de arte, voz e experiência. | Invariantes já cobertas; aplicar prova da referência. |
| 663, 00:52:42–00:57:45 | Manual de regras em testes e bug convertido em regressão. | M01/M02. |
| 663, 00:58:29–01:03:18 | Entrar no estado crítico sem simular todo o histórico. | F02. |
| 663, 01:03:18–01:07:30 | Staging justificado pelo contexto e público. | M04; sem ambiente adicional automático. |
| 663, 01:24:38–01:29:34 | Prática deliberada e próximo gargalo. | Pilotos focados no problema que realmente limita o trabalho. |
| 663, 01:37:12–01:43:21 | Esforço proporcional e benchmark com sabotagem. | F01 e custo medido por tarefa. |
| 663, 02:14:21–02:16:14 | Gravação humana curta pode superar tentativas pagas. | M05. |
| 663, 02:16:46–02:17:36 | Remover funcionalidades sem uso. | Critério para abandonar ferramenta/skill sem benefício. |
| 663, 02:35:16–02:47:01 | Risco, urgência e fallback de infraestrutura. | M03. |
| 663, 02:47:05–02:50:12 | Objetivo, proibições, oráculo, simulação e resultado. | M02/M03; distinguir dry-run de garantia da execução real. |
| 663, 03:11:51–03:18:50 | Memória curta/longa, decisões e handoff. | F04. |
| 663, 03:34:50–03:35:29 | Proveniência entre texto-fonte e derivado. | F06. |
| 663, 03:35:29–03:38:19 | CI, build e feedback executável. | F03. |
| 663, 03:49:19–03:55:50 | Pesquisa de alternativas, memória seletiva e custo do excesso de ferramentas. | F04 e limites de adoção. |
| 663, 04:09:49–04:11:20 | Tokens não equivalem a qualidade; cache e medição. | Critério de comparação, já coberto no catálogo. |

Trechos sem consequência operacional demonstrável foram considerados e não viraram propostas. Os IDs acima agrupam mecanismos; não significam 30 regras novas.

## 10. Recomendação de execução

1. Corrigir o registro de conclusão e completar as provas faltantes da continuidade já entregue, com recorte explícito: F01.
2. Refinar M01, M02 e M03 nas seções existentes. Sem novo questionário, agente permanente ou leitura obrigatória dos podcasts.
3. Executar o PoC A em um bug representativo e aproveitar os testes na CI do próprio projeto. Só extrair uma skill generalizada se ela evitar trabalho repetido em mais de uma situação.
4. Fazer o PoC B com AI Memory se a troca entre hosts ou perda de decisões ainda for um custo real. Decidir pela evidência se substitui, complementa ou dispensa parte da continuidade atual.
5. Manter M04/M06/F05/F06 como ajustes condicionados às necessidades observadas; F07 só com necessidade concreta de isolamento.

Você não precisa baixar livro, encontrar GitHub nem instalar nada para que esta análise avance. As fontes já foram localizadas. Em um piloto futuro, sua participação útil seria confirmar uma regra de negócio ou referência que só você conhece, ou realizar uma ação de confiança/acesso realmente exigida pelo host. Preparação de cenário e testes cabe ao agente quando ele tiver os meios.

Meta de tamanho: substituir redação existente e manter os detalhes em referências sob demanda. Meta de efeito: menos reincidência, menos reexecução manual e retomada mais fiel. Economia de tokens só será alegada se houver medição comparável com qualidade preservada.
