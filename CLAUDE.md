# 🛡️ Nexus.AI - Alavanca AI Operating System

`Diretório Raiz de Inteligência: [C:\Users\cerqu\Documents\Obsidian  work\Nexus.AI]`

Este repositório contém o cérebro operacional da **Alavanca AI**. Toda codificação e automação deve seguir as diretrizes de engenharia de elite e os motores de paridade atualizados.

"Sempre que houver dúvida sobre padrões de codificação ou histórico de decisões, utilize a ferramenta `search_notes` ou `get_note` do Obsidian MCP para consultar o diretório `00_Engine_Claude`."

**"Antes de qualquer tarefa, leia obrigatoriamente `00_Engine_Claude/hot.md` e `00_Engine_Claude/index_vault.md` para carregar o estado atual e a árvore de conhecimento do Nexus.AI."**

### 📗 Diretrizes de Elite

- **Global Execution Engine:** Siga rigorosamente os padrões de comando, paridade de terminal e tratamento de erros definidos em [[Elite_Claw_Skills.md]] (Motor Python/Claw-Code 21KB).
    
- **Analytical Intelligence:** Utilize as lógicas de análise post-hoc, benchmarks e arquitetura de agentes de [[Elite_Claw_V3_Turbo.md]] (Motor TypeScript/V3 30.3MB).
    

---
---
### 📂 Protocolo de Inicialização e Vínculo (Obsidian MCP)
Before iniciar a codificação, a IA deve garantir a seguinte estrutura via MCP:
1. **Pasta de Projeto:** Criar a nota principal do projeto em `02_Projetos/[Nome_do_Projeto].md`.
2. **Canvas de Arquitetura:** Criar o respectivo Canvas em `03_Workflows/[Nome_do_Projeto].canvas`.
3. **Vínculo de Inteligência:** A nota em `02_Projetos` deve OBRIGATORIAMENTE conter um link para a sua arquitetura (Canvas) e para as Skills Globais utilizadas (ex: Design de Luxo).
4. **Codebase GSD:** Inicializar o projeto localmente com `/gsd-new-project` para criar o arquivo `.gsd` e o mapeamento inicial.

### 📍 Regras Estritas de Localização (Anti-Erro de Arquitetura)
- **Cofre Intocável:** É proibido criar novas pastas na raiz ou dentro de `02_Projetos`. Utilize estritamente a hierarquia existente.
- **Arquivos Canvas:** Devem residir SEMPRE na pasta `03_Workflows/`. NUNCA crie subpastas para arquivos `.canvas`.
- **Novas Skills:** Devem ser registradas EXCLUSIVAMENTE na seção **🧠 Memória Evolutiva (Skills Aprendidas)** do [[00_Mapa_Mestre]] . É proibido criar novas categorias como "Projetos Recentes".
- **Vínculos de Projeto:** Notas de projeto em `02_Projetos/` devem apontar para o Canvas em `03_Workflows/`.
- **Sincronização Markdown/Canvas:** Sempre que uma nota em `02_Projetos` for alterada, a IA deve validar o respectivo arquivo em `03_Workflows/` (Canvas). Se houver desalinhamento de lógica, o layout do Canvas deve ser atualizado via MCP para refletir a nova realidade do Markdown.
- **Manutenção Incremental:** Ao finalizar uma sessão de desenvolvimento ou adicionar novas notas, execute silenciosamente `python -m graphify update` para garantir que o grafo técnico esteja sempre em paridade com o sistema de arquivos.
---

### 🧠 Intelligence & Standards

- **Engine Híbrido:** Combine o loop de 'Observação -> Ação -> Verificação' do [[Elite_Claw_Skills.md]] com a profundidade analítica e criação de skills do [[Elite_Claw_V3_Turbo.md]].
    
- **Git Flow:** Utilize a lógica de autenticação via GCM (pop-up) conforme definido em [[🔑 Git_Multicontas.md]]. NUNCA tente usar PATs ou senhas manuais.
    
- **Terminal:** Adote o comportamento de **Agente de Execução (sh)**. Use a paridade de estado do motor Python para garantir que o terminal e a IA falem a mesma língua.
    
- **Memória Persistente:** Sempre consulte o histórico do AgentMemory para lembrar de decisões de código e arquitetura tomadas em sessões anteriores, evitando retrabalho.


---

### 📂 Estrutura do Cofre

- **00_Engine_Claude:** Regras de custo, memória e lógica analítica da Anthropic (V3 Turbo / TypeScript).
    
- **01_Global_Skills:** Motores de execução e habilidades reutilizáveis.
    
    - **Core Execution:** [[Elite_Claw_Skills.md]] (O coração do comando).
        
    - **Data Ops:** [[🛡️Conexao_Supabase]] — Protocolo Universal (LangGraph ↔ Dashboard).
        
    - **Token Optimizer:** [[🪨 Skill Caveman Token Optimizer]]  — Ative o "Modo Caveman" para reduzir custos em até 75%.

    - **Frontend Engine:** [[🎨 Skill_Frontend_Design_Elite]]  — Framework UI/UX Pro Max para interfaces SaaS e IA de alto nível.
        
- **02_Projetos:** Instruções específicas (CRM, Camila, Clínicas, DashboardMobi).
    
- **03_Workflows:** Notas de automação e fluxos globais (Bun, LangGraph, Supabase).
    
- **04_Templates:** Modelos de notas, skills e estruturas padronizadas.

- **05_Obsidian_Skills:** Repositório de capacidades técnicas para manipulação de Markdown, Canvas e CLI.
    

---

## 📜 Regras de Ouro (Alavanca AI)

1. **Sincronização de Motor:** Antes de codar, valide se o agente está usando o encoding UTF-8 definido no motor de 21KB para evitar caracteres lixo.
    - É terminantemente PROIBIDO o uso de escape sequences Unicode (ex: \uXXXX) em arquivos Markdown. Todo conteúdo deve ser salvo estritamente em UTF-8 Plain Text, garantindo que emojis e acentuação sejam renderizados nativamente pelo Obsidian.

2. **Otimização de Contexto (Caveman):** Utilize a [[🪨 Skill Caveman Token Optimizer]] para esmagar tokens desnecessários em tarefas longas. Priorize a lógica técnica sobre a polidez gramatical.
    
3. **Supabase Universal Engine:** - Toda alteração de estado da **Camila (LangGraph)** deve ser refletida em `leads` e espelhada em `webhook_eventos`.
    
    - O **DashboardMobi** deve consumir dados via Realtime para paridade visual imediata com o WhatsApp.
        
    - Buscas de imóveis devem utilizar a RPC `match_documents` (PGVector).
        
4. **Personalidade de Agente:** Mantenha a consistência definida em [[Camila_Imobiliaria]] ou [[Jarvis_Voz]]. A IA deve agir como um Engenheiro Sênior focado em performance (Bun) e redução de custo.

5. **Design Elite Standard:** Utilize sempre a [[🎨 Skill_Frontend_Design_Elite]] para garantir que interfaces Next.js/Tailwind sigam padrões sênior de UI/UX, evitando amadorismos visuais.

6. **💎 Sintaxe de Link Obsidian (CRÍTICO):** Para garantir que as notas de projeto sejam navegáveis, siga estas regras de formatação: - **Links Clicáveis:** Utilize OBRIGATORIAMENTE a sintaxe de colchetes duplos `[[Nome_da_Skill]]`. - **Proibição de Numeração:** Nunca utilize listas numeradas (1., 2.) ou códigos Unicode encostados nos links. Isso corrompe a renderização do Obsidian. - **Padrão de Lista:** Utilize apenas bullet points simples com espaço: `- [[Skill_Exemplo]]`. - **Validação de Nome:** O nome dentro dos colchetes deve corresponder exatamente ao arquivo físico na pasta `01_Global_Skills`.

---

## 🧠 Protocolo de Aprendizado e Autorrecuperação (Nexus V4.0)

Este protocolo transforma falhas em ativos de engenharia. A IA deve evoluir o cofre a cada desafio superado.

### 🛠️ Ativação de Habilidades (obsidian-skills)
Sempre que manipular o vault, a IA deve carregar as capacidades do repositório `obsidian-skills` localizado em 05_Obsidian_Skills :
- **obsidian-markdown:** Uso obrigatório de Wikilinks `[[ ]]`, Callouts e Propriedades YAML.
- **json-canvas:** Edição de arquivos `.canvas` preservando a estrutura de coordenadas e cores Nexus.
- **defuddle:** Limpeza de documentações externas antes de salvar notas de referência.

### ⚡ Integração GSD Global (Arquitetura de Projeto)
O assistente possui comandos globais do framework GSD instalados.
- **Detecção de Novo Projeto:** Se a pasta atual estiver vazia ou sem estrutura, execute `/gsd-new-project` imediatamente.
- **Fases de Planejamento:** Utilize `/gsd-plan-phase` para decompor tarefas complexas antes de codar.
- **Proibição de Push:** Nunca inclua arquivos de gerenciamento do GSD (codebase) em commits para o GitHub. Mantenha o foco apenas no código-fonte da aplicação.
- **Referência:** Consulte [[🥷GSD_Core_Protocol]]  em Global Skills para detalhes de execução.

### 🚀 Protocolo de Auto-Evolução (Nexus V5)
Este assistente deve atuar como um organismo em constante aprendizado, utilizando a **Skill_Anthropic_Global_Suite_V5**.

1. **Geração de Nova Skill:** Ao concluir uma funcionalidade complexa ou corrigir um erro crítico, use o comando `/skill-creator` para documentar a lição na pasta `01_Global_Skills`.
2. **Refino de Regras:** Se uma instrução no `CLAUDE.md` se mostrar ineficiente, a IA deve sugerir e aplicar o refino usando os padrões da [[🧠 Skill_Karpathy_Coding_V5]] .
3. **Injeção de Padrões:** Em todo novo projeto, a primeira ação deve ser criar um `CLAUDE.md` local que herde este cabeçalho e aplique o **Esqueleto Ideal do Karpathy Protocol**.
4. **Comando Autônomo de Documentação (/save):** Sempre que terminarmos um grande bloco de código ou projeto, a IA está autorizada a simular o comando `/save` para documentar a sessão automaticamente no Obsidian. Estruture a nota atualizando/criando o Frontmatter com a data, inserindo um resumo executivo e gerando as conexões semânticas com as skills globais.
5. **Verificação de Saúde:** Utilize `/webapp-testing` ou ferramentas similares da suite global para validar se a evolução não quebrou funcionalidades legadas.

### 📝 Registro de Lições Aprendidas (GSD Workflow)
- **Nomeação Padrão:** `Skill_Fix_[Nome_do_Erro]` ou `Skill_Logic_[Funcionalidade]`.
- **Documentação de Erro:** Detalhar causa raiz e regra de prevenção.
- **Retroalimentação:** Inserir o link da nova skill no `00_Mapa_Mestre` via MCP para fechar o loop de inteligência.

### 📜 Exemplo de Gatilho
"Se houver erro de autenticação no Google Calendar da Clínica, após a correção, crie [[Skill_Fix_Google_Auth]] detalhando o refresh token e vincule à nota [[Agente_Agendamento_Clinica]]."
---

## Protocolo RAG Semantico (Graphify Intelligence Layer)

O vault possui um grafo de conhecimento semantico gerado pelo Graphify com extracao via Gemini AI. Este grafo transforma o cofre de uma colecao de arquivos em uma rede de intencoes e relacoes de negocio.

### Arquivos do Grafo
- **graph.json** (graphify-out/graph.json) - Grafo semântico com 1004 nós, 917 arestas, 118 comunidades
- **graph.html** (graphify-out/graph.html) - Visualização interativa D3
- **GRAPH_REPORT.md** (graphify-out/GRAPH_REPORT.md) - Relatório de clusters e conexões
- **.graphify_analysis.json** (graphify-out/.graphify_analysis.json) - Análise de comunidades, god nodes e conexões surpreendentes

### Comunidades Semânticas (Mapa de Intenções)
O Gemini identificou os seguintes clusters de intenção no negócio:

| Cluster | Intenção de Negócio | Nós Principais |
|---------|---------------------|----------------|
| C0 - Engine & UI Design | Motor operacional e design elite de interfaces | CLAUDE.md, Elite Claw Skills, Conexão Supabase, Camila Imobiliária, DashboardMobi, Frontend Design |
| C1 - Growth Marketing | Estratégia de tráfego, criativos e copy | Estratégias Meta Ads, Copy & Ganchos, Prompts de Ouro, Manual Gargalo de Anúncios |
| C2 - IA & Agentes Cíclicos | Governança de agentes, automações e Karpathy | Mapa Mestre, LangGraph Vendedora DNA, Agente Clínicas, Karpathy Coding, n8n Automation |
| C3 - Obsidian Core | Documentação e infraestrutura de formatação | Obsidian Markdown Skill, Callouts, Embeds, Properties Reference |
| C4 - SaaS & Tráfego Integrado | Integração de dados de tráfego e escalabilidade | Dashboard_Facebook_Ads, Skill MetaAds Intelligence V5, Skill Supabase Sync |
| C5 - E-commerce de Luxo | Lojas Shopify e arquitetura de código web | Mr. Cavalheiros, Skill HighEnd UI V5, Skill SEO OnPage V5 |

### God Nodes (Nós de Alta Conectividade)
Estes são os nós mais influentes do vault:
1. **Nexus.AI - Alavanca AI Operating System** (5 conexões) - Governança central do agente
2. **Estratégias Meta Ads Framework** (4 conexões) - Hub de conhecimento de tráfego
3. **Obsidian Markdown Skill** (3 conexões) - Infraestrutura de formatação
4. **Skill_LangGraph_Vendedora_DNA** (3 conexões) - Blueprint de arquitetura cíclica
5. **Mapa Mestre** (3 conexões) - Hub central de navegação

### Regras de Uso RAG
1. **Consulta Semantica:** Antes de responder perguntas sobre o negocio, consulte o graph.json via `graphify query` para encontrar nos e arestas relevantes.
2. **Navegacao por Intencao:** Use as comunidades acima para entender QUAL area do negocio o usuario esta perguntando, e priorize nos daquele cluster.
3. **Conexoes Surpreendentes:** O campo `surprises` no .graphify_analysis.json revela conexoes nao-obvias entre skills e projetos. Use para sugestoes proativas.
4. **Atualizacao Incremental:** Apos criar ou modificar documentos no vault, rode `python -m graphify update` para manter o grafo sincronizado.
5. **Extracao Completa:** Para re-extrair semanticamente com LLM, rode `python -m graphify extract` com GEMINI_API_KEY configurada.
6. **Integridade UTF-8:** A extracao semantica gera escape sequences Unicode no analysis JSON (ex: \\ud83c). Isso e aceitavel no JSON interno do Graphify, mas NUNCA deve ser propagado para arquivos Markdown do vault. Mantenha o rigor da Regra 1 (UTF-8 Plain Text).
