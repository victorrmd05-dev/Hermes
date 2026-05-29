# 🗂️ Índice de Notas Semânticas (Nexus.AI)

## 🕸️ Protocolo RAG Semântico (Graphify Intelligence Layer)
O vault possui um grafo de conhecimento gerado pelo Graphify. Este grafo transforma o cofre numa rede de intenções.
- **Consultas Semânticas:** Sempre consulte o `graph.json` via `graphify query` antes de responder sobre o negócio.
- **Atualização Incremental:** Após modificar documentos, rode `python -m graphify update . --force` para sincronizar.
- **Integridade UTF-8:** Nunca propague escape sequences Unicode (ex: \uXXXX) do graphify para o Markdown.
- **Métricas:** 1313 nós, 1206 arestas, 138 comunidades. Use os God Nodes para navegar: CLAUDE.md, Estratégias Meta Ads, Obsidian Markdown, LangGraph Vendedora, Mapa Mestre.


## 🔧 Infraestrutura de Ingestao (claude-obsidian — Deploy 2026-05-28)
- `.raw/` : Caixa de entrada de arquivos brutos (PDFs, planilhas, relatorios). Use `/wiki-ingest` para processar.
- `wiki/` : Conhecimento estruturado gerado pela IA — `sources/`, `concepts/`, `entities/`, `domains/`, `meta/`.
- `commands/` : Definicoes dos comandos `/wiki-ingest`, `/autoresearch`, `/think`, `/canvas`, `/save`.
- `agents/` : Agentes especializados — `wiki-ingest.md`, `wiki-lint.md`, `verifier.md`.
- `scripts/` : Scripts operacionais de rerank, retrieve, bm25-index, tiling-check.
- `bin/` : Setup scripts (dragonscale, vault, multi-agent, retrieve).

## 🧠 Microsoft GenAI Curriculum (Ingestao 2026-05-28)
- [[Skill_Microsoft_GenAI_Curriculum]] : Indice Mestre das 21 licoes — 3 veias de ouro identificadas.
- [[MSFT_RAG_e_Vetores_Memoria_IA]] : Pipeline RAG completo, embeddings, vector DBs, busca semantica (Aulas 8 e 15).
- [[MSFT_Agentes_e_LLMOps_JARVIS]] : AutoGen, LangChain, TaskWeaver, JARVIS, ciclo de vida LLMOps (Aulas 14 e 17).
- [[MSFT_Prompt_Engineering_e_UX_IA]] : Zero-shot, CoT, Self-refine, Trust, Transparency, Chat UX (Aulas 4, 5 e 12).

## 🌐 Global Skills
- [[Elite_Claw_Skills]] : Motor Python/Claw — padroes de comando, registry, execucao estruturada.
- [[Elite_Claw_V3_Turbo]] : Motor V3 — Post-hoc Analyzer, Comparator Agent, Grader Agent.
- [[Nexus_Protocol_Layout_Canvas]] : Padrões de arquitetura visual e navegação.
- [[Skill_Logic_Google_SEO_Integration]] : Integração SEO Google avançada.
- [[Skill_Synabun_Knowledge_v1]] : Base de conhecimento do Synabun.
- [[⚡Skill_n8n_Automation_V5]] : Automações n8n.
- [[✅ Skill_SEO_OnPage_V5]] : SEO On-Page otimizado.
- [[🎨 Skill_Frontend_Design_Elite]] : Framework UI/UX Pro Max para SaaS/IA.
- [[🎯Skill_MetaAds_Intelligence_V5]] : Inteligência avançada de anúncios no Meta Ads.
- [[🏎️ Skill_3D_Porsche_Animation]] : Animação 3D automotiva.
- [[💎 Skill_HighEnd_UI_V5]] : Interface de Luxo de Alta Performance.
- [[📊 Skill_GoogleSheets_Contacts]] : Automações e gerenciamento no Google Sheets.
- [[🔄 Skill_Supabase_Sync]] : Sincronização em tempo real via Supabase.
- [[🔑 Git_Multicontas]] : Regras de autenticação Git Flow.
- [[🔒 Skill_Security_V5]] : Regras de segurança gerais.
- [[🖋️ Skill_Luxury_Copywriting_V5]] : Copy de alto padrão e luxo.
- [[🛍️ Skill_Liquid_Mastery_V5]] : Mastery em Shopify Liquid.
- [[🛍️ Skill_Performance_V5]] : Foco em performance web.
- [[🛍️ Skill_Shopify_Functions_V5]] : Funções avançadas da Shopify.
- [[🛍️ Skill_Shopify_GraphQL_V5]] : Manipulação de dados com GraphQL (Shopify).
- [[🛡️Conexao_Supabase]] : Protocolo Universal Supabase.
- [[🤖 Skill_LangGraph_Vendedora_DNA]] : Blueprint LangGraph p/ IA de Vendas.
- [[🥷GSD_Core_Protocol]] : Protocolo do Framework de Gerenciamento.
- [[🧠 Skill_Anthropic_Global_Suite_V5]] : Motor global de auto-evolução Anthropic.
- [[🧠 Skill_Claude_Design_Elite_V5]] : Diretrizes Elite de Design e UI.
- [[🧠 Skill_GStack_Executive_Suite]] : Suite executiva Google Stack.
- [[🧠 Skill_Karpathy_Coding_V5]] : Padrões de Engenharia (Karpathy Protocol).
- [[🧼 Skill_Clean_Code_V5]] : Boas práticas de código limpo.
- [[🪨 Skill Caveman Token Optimizer]] : Otimização extrema de tokens/contexto.

## 🚀 Projetos Ativos
- [[00_Mapa_Mestre]] : Hub Central de Navegação do Cofre.
- [[Agente_Agendamento_Clinica]] : Automação para clínicas.
- [[Camila_Imobiliaria]] : Imobiliária Inteligente / Vendedora LangGraph.
- [[DashboardMobi]] : Dashboard Mobile de visualização em tempo real.
- [[Dashboard_Facebook_Ads]] : Integração para Analytics do FB Ads.
- [[Estetica_Automotiva]] : Sistema/Automação para Estética.
- [[Jarvis_Voz]] : Assistente Jarvis com TTS/STT.
- [[Mr_Cavalheiros]] : E-commerce de Luxo / Sistema Mr. Cavalheiros.
- [[armorglass_lp]] : Landing page ArmorGlass.
