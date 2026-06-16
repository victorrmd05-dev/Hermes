# Paperclip: Configuração de Skills e GitHub Monorepo

## 1. Arquitetura Monorepo no GitHub
Ao invés de criar dezenas de repositórios para cada Skill, usamos um **Monorepo** (ex: `alavanca-ai-core`). Isso permite gerenciar todo o exército de agentes com um único `git push`, facilitando refatoração e versionamento.
A estrutura da pasta no repositório deve separar `skills/` e `agents/`.

## 2. Importação no Paperclip: `agent.md` vs `SKILL.md`
O Paperclip lida com Agentes e Skills em telas e métodos separados. É vital não misturar os formatos:

### `agent.md` (Aba Instructions)
- **Como usar:** Copie e cole o texto do `agent.md` diretamente na caixa "Instructions" na interface do Paperclip.
- **Formatação:** NÃO DEVE TER YAML Frontmatter. Deve começar imediatamente com um Título Markdown (ex: `# Nome do Agente`). Colocar traços `---` ou crases quebrará o prompt do modelo.

### `SKILL.md` (Aba Skills)
- **Como usar:** No painel do Paperclip, importe colando a URL do GitHub apontando para a subpasta específica da skill (ex: `https://github.com/user/repo/tree/main/skills/minerador-skill`).
- **Formatação:** EXIGE obrigatoriamente o "YAML Frontmatter" no topo (as configurações ocultas delimitadas por `---` com `name` e `description`). Sem isso, o Paperclip não reconhece a ferramenta.
- **Scripts em anexo:** O Paperclip clonará automaticamente a pasta `scripts/` associada a esta skill, executando códigos Bash/Python de forma isolada.

## 3. Biblioteca de Skills
A estrutura possui diversas skills, incluindo:
- **Minerador Skill:** Usa scripts Python (`scrape_meta_ads.py` e `process_and_save_offer.py`) para interagir com a API do Scrape Creators e gravar no Supabase.
- **CEO Strategy Skill:** Frameworks para planejamento executivo e delegação.
- **Infra Tech Skill:** Manutenção de servidores e logs.
- Outras: Quality Check, Copywriting, Webmaster, e SEO Opt.

## 4. Problemas Conhecidos (Troubleshooting)
- **GitHub Rate Limit:** Ao adicionar ou atualizar skills pelo link de pasta, o Paperclip faz múltiplas requisições. O limite público do GitHub é de 60 requisições por hora. Se estourar (Erro 403), o Paperclip passa a ler o `SKILL.md` em cache, mas os scripts (como os `.py`) "desaparecem".
  - **Solução:** Autentique a conta do GitHub dentro do Paperclip para aumentar o limite para 5.000 req/hora. Se isso não for possível, inclua as chaves num `PAT (Personal Access Token)` via link direto de repositório. Use o shebang (`#!/usr/bin/env python3`) e permissões adequadas nos scripts.
