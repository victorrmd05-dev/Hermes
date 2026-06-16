---
aliases: [Paperclip Skills, Monorepo Setup, GitHub Configuration]
tags: [wiki, paperclip, skills, github, monorepo]
---

# 🛠️ Paperclip: Configuração de Skills e GitHub Monorepo

## 📂 1. Arquitetura Monorepo no GitHub

Em vez de criar dezenas de repositórios individuais para cada Skill, adotamos a arquitetura de **Monorepo** (ex: `alavanca-ai-core`). 
Essa abordagem permite gerenciar todo o ecossistema de inteligência artificial com um único comando de versionamento (`git push`), facilitando a manutenção e a refatoração interdependente de múltiplos agentes.

A estrutura de diretórios no repositório separa estritamente a inteligência base e as ferramentas executáveis:
```text
alavanca-ai-core/
├── skills/
│   ├── minerador-skill/
│   └── ceo-strategy-skill/
└── agents/
    ├── ceo/
    └── minerador/
```

---

## ⚖️ 2. Diferenças Estruturais: `agent.md` vs `SKILL.md`

O Paperclip trata Agentes e Skills através de lógicas de processamento totalmente distintas. É **vital** não misturar os formatos.

### 📝 `agent.md` (Aba Instructions)
- **Método de Uso:** Copie todo o conteúdo em texto do `agent.md` e cole-o diretamente na caixa "Instructions" na interface web do Paperclip.
- **Regras de Formatação:** 
  - **NÃO** deve conter YAML Frontmatter.
  - **DEVE** começar imediatamente com um Título Markdown puro (ex: `# Nome do Agente`).
  - > [!WARNING] Cuidado com o Cabeçalho
    > Colocar três traços (`---`) ou blocos de código markdown (` ``` `) no topo do arquivo do agente quebrará a interpretação primária do LLM.

### 🔌 `SKILL.md` (Aba Skills)
- **Método de Uso:** No painel do Paperclip, importe a skill preenchendo a URL do GitHub que aponta especificamente para a **subpasta** em questão (ex: `https://github.com/user/repo/tree/main/skills/minerador-skill`).
- **Regras de Formatação:**
  - **EXIGE** obrigatoriamente o bloco de "YAML Frontmatter" nas primeiras linhas. Sem essa configuração oculta (`---` com `name:` e `description:`), o Paperclip não injeta a ferramenta adequadamente no fluxo de raciocínio da IA.
- **Anexo Automático de Scripts:** Durante a importação, o Paperclip procura e clona automaticamente qualquer diretório `scripts/` associado a esta skill. O ambiente virtual isolado é criado para rodar arquivos `.py` ou `.sh`.

---

## 📚 3. Biblioteca de Skills Atuais

Nosso monorepo inclui módulos de habilidades altamente especializadas:

| Nome da Skill | Descrição e Funcionalidade Principal |
| :--- | :--- |
| **Minerador Skill** | Centraliza a operação de busca de ofertas. Executa os scripts Python (`scrape_meta_ads.py` e `process_and_save_offer.py`) para interagir com a API do Scrape Creators e registrar os dados no Supabase. |
| **CEO Strategy Skill** | Engloba frameworks de raciocínio, matrizes de decisão executiva e métodos de delegação orientada a resultados. |
| **Infra Tech Skill** | Confere acesso aos módulos de monitoramento de servidores, leitura de logs vitais e administração de APIs do CTO. |
| **Outras** | Quality Check (Revisões e Compliance), Copywriting, Webmaster, e SEO Opt. |

---

## 🛑 4. Solução de Problemas Comuns (Troubleshooting)

> [!CAUTION] Erro de Scripts Desaparecidos (GitHub Rate Limit 403)
> Se você atualizar ou adicionar uma skill pelo link da subpasta e o script Python falhar ou não for listado, a culpa costuma ser do Rate Limit do GitHub. 
> O Paperclip faz requisições pesadas à API do GitHub em segundo plano. Para usuários anônimos, o limite é de apenas **60 requisições/hora**. Ao estourar esse limite, o sistema exibe o `SKILL.md` em cache, mas os executáveis silenciosamente falham no donwload.

### Passos para Resolução:
1. **Ative a Autenticação Nativa:** Acesse as configurações de conta no painel do Paperclip e faça a autenticação/login pelo GitHub. Isso imediatamente eleva seu limite para **5.000 requisições/hora**.
2. **Método Manual Alternativo:** Se o bloqueio persistir, gere um Personal Access Token (`PAT`) no GitHub e inclua as credenciais diretamente na URL do repositório no momento da importação.
3. **Padrões de Ambiente:** Certifique-se de que os scripts sempre possuam o shebang de execução nativa (`#!/usr/bin/env python3`) na primeira linha e que o commit no repositório possua as devidas permissões do Git (`chmod +x`).
