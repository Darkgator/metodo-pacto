# Adaptador Claude Code

O núcleo e a skill são portáveis; o hook do Codex não é instalado automaticamente no Claude Code. Para usar o PACTO no Claude Code, copie ou adapte `AGENTS.md`, `CLAUDE.md`, `.pacto/pacto-estado.py` e o estado do projeto, preservando as regras que já existirem.

Não há configuração de hook neste adaptador porque a documentação oficial disponível não permitiu validar, neste computador, um formato de plugin/hook Claude equivalente ao do Codex. Isso é deliberado: não registrar um manifesto especulativo como integração funcional. A continuidade manual continua disponível por `python .pacto/pacto-estado.py contexto` e `--sessao`.

Validação pendente para Claude: reconhecimento real da skill, eventos de início/retomada/compactação e confiança do usuário no host. Não confunda esta pasta com integração ativa.
