# 🗂️ Índice de Notas Semânticas (Hermes)

## 🕸️ Protocolo RAG Semântico (Graphify Intelligence Layer)
O vault possui um grafo de conhecimento gerado pelo Graphify. Este grafo transforma o cofre numa rede de intenções.
- **Consultas Semânticas:** Sempre consulte o `graph.json` via `graphify query` antes de responder sobre o negócio.
- **Atualização Incremental:** Após modificar documentos, rode `python -m graphify update . --force` para sincronizar.
- **Integridade UTF-8:** Nunca propague escape sequences Unicode (ex: \uXXXX) do graphify para o Markdown.
- **Métricas:** Use os God Nodes para navegar: CLAUDE.md, Mapa Mestre.


## 🔧 Infraestrutura de Ingestao (claude-obsidian — Deploy 2026-05-28)
- `.raw/` : Caixa de entrada de arquivos brutos (PDFs, planilhas, relatorios). Use `/wiki-ingest` para processar.
- `wiki/` : Conhecimento estruturado gerado pela IA — `sources/`, `concepts/`, `entities/`, `domains/`, `meta/`.
- `commands/` : Definicoes dos comandos `/wiki-ingest`, `/autoresearch`, `/think`, `/canvas`, `/save`.
- `agents/` : Agentes especializados — `wiki-ingest.md`, `wiki-lint.md`, `verifier.md`.
- `scripts/` : Scripts operacionais de rerank, retrieve, bm25-index, tiling-check.
- `bin/` : Setup scripts (dragonscale, vault, multi-agent, retrieve).


## 🌐 Global Skills
- [[⚡Elite_Claw_Skills]] : Motor Python/Claw — padroes de comando, registry, execucao estruturada.
- [[⚡Elite_Claw_V3_Turbo]] : Motor V3 — Post-hoc Analyzer, Comparator Agent, Grader Agent.
- [[Skill_Logic_Google_SEO_Integration]] : Integração SEO Google avançada.
- [[Skill_Synabun_Knowledge_v1]] : Base de conhecimento do Synabun.
- [[✅ Skill_SEO_OnPage_V5]] : SEO On-Page otimizado.
- [[🎨 Skill_Frontend_Design_Elite]] : Framework UI/UX Pro Max para SaaS/IA.
- [[🎯Skill_MetaAds_Intelligence_V5]] : Inteligência avançada de anúncios no Meta Ads.
- [[💎 Skill_HighEnd_UI_V5]] : Interface de Luxo de Alta Performance.
- [[🔒 Skill_Security_V5]] : Regras de segurança gerais.
- [[🖋️ Skill_Luxury_Copywriting_V5]] : Copy de alto padrão e luxo.
- [[🛍️ Skill_Liquid_Mastery_V5]] : Mastery em Shopify Liquid.
- [[🛍️ Skill_Performance_V5]] : Foco em performance web.
- [[🛍️ Skill_Shopify_Functions_V5]] : Funções avançadas da Shopify.
- [[🛍️ Skill_Shopify_GraphQL_V5]] : Manipulação de dados com GraphQL (Shopify).
- [[🥷GSD_Core_Protocol]] : Protocolo do Framework de Gerenciamento.
- [[🧠 Skill_Anthropic_Global_Suite_V5]] : Motor global de auto-evolução Anthropic.
- [[🧠 Skill_Claude_Design_Elite_V5]] : Diretrizes Elite de Design e UI.
- [[🧠 Skill_GStack_Executive_Suite]] : Suite executiva Google Stack.
- [[🧠 Skill_Karpathy_Coding_V5]] : Padrões de Engenharia (Karpathy Protocol).
- [[🧼 Skill_Clean_Code_V5]] : Boas práticas de código limpo.
- [[🪨 Skill Caveman Token Optimizer]] : Otimização extrema de tokens/contexto.
- [[📉 Monitoramento_de_Custos_Claude]] : Otimização e monitoramento de custos de tokens API.

## 🧭 Navegação Central
- [[00_Mapa_Mestre]] : Hub Central de Navegação do Cofre.

