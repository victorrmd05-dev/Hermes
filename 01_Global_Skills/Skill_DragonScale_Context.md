---
name: skill-dragonscale-context
description: >
  Lógicas de persistência, linting de sanidade e prevenção de duplicação do DragonScale.
---

# 🐉 Skill_DragonScale_Context (Memória Evolutiva)

Esta skill consolida as lógicas de elite do ecossistema DragonScale para o Nexus.AI, injetando capacidades avançadas de persistência, linting de sanidade e documentação autônoma baseada na arquitetura original.

## 💾 1. Automação de Documentação (/save)
A lógica nativa de `save` foi incorporada para garantir que nenhum insight estrutural ou bloco de código se perca no limbo do chat ("amnésia zero").
- **Comando Gatilho:** `/save`, "salve isso", "documente a sessão".
- **Fluxo:** O agente escaneia a conversa atual para extrair o conhecimento vital, define a tipologia ideal da nota (synthesis, concept, decision, etc.) e cria/atualiza a nota correspondente no cofre (com Frontmatter, tags e links semânticos).
- **Pós-ação (Cache Rápido):** Após o salvamento, o agente atualiza o `00_Engine_Claude/hot.md` e o índice semântico para garantir que o contexto imediato do runtime seja mantido.

## 🧹 2. Linting de Sanidade e Limpeza de Órfãos (wiki-lint)
O grafo semântico deve ser cirurgicamente preciso. O agente está autorizado a executar verificações de saúde no cofre:
- **Limpeza de Órfãos:** Identifica páginas "ilhadas" (sem inbound links) e sugere remoção ou conexão a `00_Mapa_Mestre.md` ou afins.
- **Dead Links:** Encontra wikilinks (`[[quebrados]]`) que não resolvem para nenhum arquivo real.
- **Frontmatter Gaps:** Acusa arquivos que não possuem metadados vitais de indexação.

## 👯 3. Linting de Duplicatas (Semantic Tiling)
Baseado nos mecanismos DragonScale:
- Prevenção ativa de conhecimento duplicado: se a IA detectar que a essência de um prompt ou estrutura já existe (ex: duas lógicas de SEO idênticas com nomes diferentes), o agente deve fundir o conteúdo e deletar a cópia desnecessária.
- Manutenção rigorosa do princípio DRY (Don't Repeat Yourself) na árvore de habilidades do agente.

## ⚙️ Injeção de Autodescoberta
O ambiente foi configurado com Links Simbólicos (Junctions) injetando as pastas nativas de `skills/` do repositório clonado do DragonScale diretamente no diretório global do nosso agente (`.gemini/config/skills/`). Isso garante que os scripts locais dele, definições de linting e `SKILL.md` nativos sejam "lidos" silenciosamente antes de toda interação complexa no nosso motor Nexus.AI.
