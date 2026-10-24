# Adaptador Claude Code

O núcleo e a skill são portáveis; o hook do Codex não é instalado automaticamente no Claude Code. Para uso manual, prefira o instalador do método ou copie/adapte `AGENTS.md`, `CLAUDE.md`, `.pacto/validacao.md` e `.pacto/operacao.md`; acrescente `.pacto/pacto-estado.py` e estado somente quando a continuidade for necessária. Preserve regras, contratos e estado que já existirem. A presença desses arquivos não comprova reconhecimento da skill pelo Claude.

Não há configuração de hook neste adaptador porque a documentação oficial disponível não permitiu validar, neste computador, um formato de plugin/hook Claude equivalente ao do Codex. Isso é deliberado: não registrar um manifesto especulativo como integração funcional. A continuidade manual continua disponível por `python .pacto/pacto-estado.py contexto` e `--sessao`.

Validação pendente para Claude: reconhecimento real da skill, eventos de início/retomada/compactação e confiança do usuário no host. Não confunda esta pasta com integração ativa.
