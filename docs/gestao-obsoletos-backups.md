# Gestão de Obsoletos e Backups

Criador: Alexandre Barroso de Miranda
Atuação: Consultor de Processos
Método: PACTO

## Objetivo

Evitar perda de contexto e retrabalho em pontos de virada relevantes, sem transformar o projeto em um acúmulo de arquivos velhos.

A regra principal é: **Git é a fonte primária de histórico; pastas de obsoletos e backups são exceções úteis, não substitutos de versionamento.**

## Quando usar

Use pasta de obsoletos ou backup quando:

- ainda não há Git ou o projeto está fora de um repositório;
- há arquivos binários, referências visuais, documentos, planilhas, PDFs ou assets difíceis de reconstruir;
- uma decisão muda radicalmente a direção do projeto;
- uma refatoração grande remove arquivos antigos, mas eles podem ser úteis como referência temporária;
- antes de migração, mudança de banco, mudança de arquitetura, troca de stack ou integração crítica;
- antes de limpeza grande de arquivos;
- antes de substituir um protótipo funcional por uma versão nova.

Não use para:

- cada pequena alteração;
- arquivo que já está bem versionado no Git;
- lixo temporário sem valor;
- duplicar dependências, `node_modules`, builds ou caches;
- esconder arquivo que deveria ser removido de verdade.

## Estrutura recomendada

Use nomes simples e explícitos:

```text
_archive/
  obsolete/
    2026-07-01_nome-do-turning-point/
      README.md
      arquivos-antigos...
  backups/
    2026-07-01_1430_nome-do-turning-point/
      README.md
      snapshot...
```

Se o projeto já tiver padrão próprio, siga o padrão existente.

## O que vai para obsoletos

Use `_archive/obsolete/` para arquivos que:

- deixaram de ser usados;
- foram substituídos por abordagem nova;
- ainda podem ajudar como referência temporária;
- não devem continuar misturados ao código ativo.

Todo pacote de obsoletos deve ter um `README.md` curto com:

- data;
- motivo;
- arquivos movidos;
- decisão relacionada;
- prazo ou condição para remoção definitiva, se houver.

## O que vai para backups

Use `_archive/backups/` para snapshots em turning points.

Turning points típicos:

- antes de trocar stack;
- antes de migração de banco;
- antes de refatoração grande;
- antes de remover grande volume de arquivos;
- antes de reestruturar UI;
- antes de substituir protótipo;
- antes de automação destrutiva.

O backup deve ser mínimo. Não copie dependências, caches, builds ou arquivos gerados que possam ser recriados.

Antes de excluir ou migrar, confira os alvos e as premissas. Consulta falha ou inesperadamente vazia interrompe a ação. Git cobre arquivos versionados, não todo banco ou upload. Backup no mesmo disco não protege contra perda do disco; quando necessário, confira a integridade de arquivos restaurados.

## Prompt operacional

```text
Antes de executar esta mudança, avalie se ela é um turning point.

Considere turning point quando envolver:
- migração de banco;
- troca de stack;
- refatoração grande;
- remoção de muitos arquivos;
- substituição de protótipo funcional;
- reestruturação de UI;
- integração crítica;
- operação destrutiva.

Se for turning point:
1. Explique se Git já cobre o histórico.
2. Se Git não for suficiente, proponha um backup mínimo em `_archive/backups/YYYY-MM-DD_HHMM_descricao/`.
3. Se arquivos forem substituídos mas ainda úteis como referência, mova para `_archive/obsolete/YYYY-MM-DD_descricao/`.
4. Crie um `README.md` dentro da pasta explicando motivo, data, origem e condição de remoção.
5. Não copie dependências, caches, builds ou arquivos gerados recriáveis.

Não faça backup por reflexo. Faça apenas se houver valor real de recuperação ou rastreabilidade.
```

## Checklist

- [ ] Git ou outro versionamento cobre o histórico?
- [ ] A mudança é um turning point real?
- [ ] O backup é necessário além do Git?
- [ ] Arquivos obsoletos foram removidos do fluxo ativo?
- [ ] A pasta criada tem `README.md` explicando o motivo?
- [ ] Dependências, caches e builds foram excluídos do backup?
- [ ] Há condição de limpeza futura?
