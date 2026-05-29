---
tags: [agentes, llmops, autogen, langchain, jarvis, orquestracao, microsoft, aula-14, aula-17]
fonte: https://github.com/microsoft/generative-ai-for-beginners
licoes: [14, 17]
status: profundo
---

# 🤖 Orquestracao de Agentes e LLMOps — Mapa para o JARVIS (Aulas 14 e 17)

> Nota profunda extraida das Licoes 14 e 17 do curriculo Microsoft GenAI.
> **Impacto no Nexus.AI:** Mapa conceitual completo para o desenvolvimento do ecossistema JARVIS e multi-agentes.
> Conectada a: [[Skill_Microsoft_GenAI_Curriculum]] | [[🧠 Skill_Anthropic_Global_Suite_V5]] | [[00_Mapa_Mestre]]

---

## AULA 17 — O Que Sao Agentes de IA?

### Definicao Microsoft (a mais clara e direta)

> "AI Agents allow Large Language Models (LLMs) to perform tasks by giving them access to a **state** and **tools**."

Os 3 pilares de um agente:

| Pilar | O que e | Exemplo Nexus.AI |
|-------|---------|-----------------|
| **LLM** | O cerebro — raciocina e planeja | Claude, GPT-4, Llama |
| **State** | Memoria da conversa e acoes anteriores | Historico LangGraph, PostgreSQL |
| **Tools** | Ferramentas que o LLM pode usar | APIs, banco de dados, outro LLM |

---

## Os 4 Frameworks de Agentes da Microsoft

### 1. LangChain Agents

O framework mais popular. Usa o padrao `AgentExecutor`:

```python
# AgentExecutor gerencia:
# - O agente (LLM + logica de decisao)
# - As tools disponíveis
# - O historico de chat (state)

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.tools import TavilySearchResults

tools = [TavilySearchResults(max_results=1)]
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

**Visibilidade:** LangSmith para monitorar quais tools o LLM usou e por que.
**Catalogo de Tools:** centenas de integrações pre-prontas (databases, APIs, web search).

---

### 2. AutoGen (Microsoft) — Multi-Agente Conversacional

**Principal foco:** agentes conversando entre si para completar tarefas.

**Dois tipos de agente:**
- `AssistantAgent` — LLM com system message especifico (tem papel definido)
- `UserProxyAgent` — representa o humano, pode executar codigo ou dar feedback

```python
import autogen

# Criar agentes especializados
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
    system_message="Voce e um engenheiro Python senior."
)

product_manager = autogen.AssistantAgent(
    name="Product_Manager",
    system_message="Voce e criativo em ideias de produto de software.",
    llm_config=llm_config,
)

# UserProxy inicia e gerencia a conversa
user_proxy = autogen.UserProxyAgent(name="user_proxy")

# Iniciar conversa multi-agente
user_proxy.initiate_chat(
    coder,
    message="Preciso de uma API para gerenciar imoveis."
)
```

**Fluxo AutoGen:**
1. Human manda mensagem
2. AssistantAgent sugere uma tool/funcao para chamar
3. Tool e executada (auto ou com aprovacao)
4. Resultado volta para o agente
5. Agente decide proxima acao ou encerra

**Aplicacao JARVIS:** criar `AssistantAgents` especializados (VoiceAgent, CRMAgent, CalendarAgent) que conversam via AutoGen para completar tarefas complexas.

---

### 3. TaskWeaver (Microsoft) — Code-First Agent

**Diferencial:** trabalha com DataFrames Python, nao apenas strings.
Ideal para analise de dados e geracao de graficos.

```
Planner (LLM) → recebe request do usuario
      ↓
Mapeia para Plugins (ferramentas em Python)
      ↓
Plugins armazenados como EMBEDDINGS para o LLM buscar o correto
      ↓
Experience (YAML) — memória de longo prazo das conversas
```

```python
# Plugin de deteccao de anomalias
class AnomalyDetectionPlugin(Plugin):
    def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
        # analise de series temporais
```

**Key insight:** os plugins sao armazenados como embeddings — o LLM busca semanticamente qual plugin usar. Isso e RAG aplicado a agentes!

---

### 4. JARVIS (Microsoft HuggingGPT) — O Orquestrador de Modelos

**O mais sofisticado:** usa um LLM geral para orquestrar **modelos de IA especializados**.

```
Usuario: "Me de uma descricao e contagem dos objetos nessa imagem"
    ↓
LLM (GPT-4) — planeja as tarefas
    ↓
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "foto.jpg"}}]
    ↓
Modelo especializado (DETR) executa object-detection
    ↓
LLM consolida resultados → Resposta final ao usuario
```

**Analogia com Nexus.AI:** JARVIS e exatamente o que o [[Jarvis_Voz]] aspira ser — um LLM central que coordena:
- Modelo de TTS/STT para voz
- Modelo de busca de imoveis
- Modelo de agendamento
- Modelo de analytics

---

## AULA 14 — LLMOps: O Ciclo de Vida de Apps GenAI

### MLOps vs LLMOps — A Mudanca de Paradigma

| MLOps (antigo) | LLMOps (novo) |
|----------------|---------------|
| Focado em Data Scientists | Focado em App Developers |
| Treinar modelos customizados | Models-as-a-Service |
| Metricas: accuracy, F1, AUC | Metricas: Quality, Harm, Honesty, Cost, Latency |
| Pipeline linear | Loops iterativos |

### As 5 Metricas LLMOps da Microsoft

```
Quality   → qualidade da resposta (clareza, utilidade)
Harm      → responsible AI (conteudo perigoso, bias)
Honesty   → groundedness (resposta e correta e verificavel?)
Cost      → budget da solucao (tokens, API calls)
Latency   → tempo medio para resposta por token
```

### O Ciclo de Vida em 3 Fases (Nao Linear — Loops Iterativos)

```
FASE 1: IDEATING/EXPLORING
━━━━━━━━━━━━━━━━━━━━━━━━━━
Explorar LLMs → Criar PromptFlow → Testar hipotese
Ferramentas: Azure AI Studio, PromptFlow

FASE 2: BUILDING/AUGMENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Implementar → Avaliar em datasets maiores → Aplicar RAG/Fine-tuning
Validar robustez → Verificar metricas → Iterar se necessario

FASE 3: OPERATIONALIZING
━━━━━━━━━━━━━━━━━━━━━━━━
Deploy → Integracao → Monitoramento + Alertas
Cycle overarching: Security + Compliance + Governance
```

### Ferramentas LLMOps Microsoft

- **Azure AI Studio** — portal web: explorar modelos, gerenciar recursos, desenvolver flows
- **PromptFlow** — do POC ate producao:
  - Design visual no VS Code
  - Test e fine-tune de qualidade
  - Deploy rapido via Azure AI Studio
- **Azure AI Platform** — vector search, databases, monitoramento

---

## Patterns de Agentes para o JARVIS Nexus.AI

### Pattern 1: Agente Unico com Tools (LangChain)
```
User → Agent → [search, calendar, crm, tts] → Response
```
**Quando usar:** tarefas sequenciais simples, um dominio

### Pattern 2: Multi-Agente Conversacional (AutoGen)
```
User → OrchestratorAgent → [CRMAgent, CalendarAgent, VoiceAgent]
                         → Consolidation → Response
```
**Quando usar:** tarefas complexas com multiplos dominios

### Pattern 3: Orquestrador + Especialistas (JARVIS)
```
User → LLM Central → [VoiceModel, ImageModel, SearchModel]
                   → Consolidation → Response
```
**Quando usar:** quando cada subtarefa precisa de um modelo especializado

### Aplicacao Direta no Nexus.AI

- [[🤖 Skill_LangGraph_Vendedora_DNA]] ja implementa o Pattern 1 (LangGraph = AgentExecutor avancado)
- [[Jarvis_Voz]] deve evoluir para Pattern 3 (JARVIS — orquestrador de modelos)
- **Proximo passo:** adicionar AutoGen para criacao de reunioes multi-agente

---

## LLMOps Checklist para Cada Projeto Nexus.AI

- Definir as 5 metricas (Quality, Harm, Honesty, Cost, Latency) antes de lancar
- Implementar PromptFlow para rastrear experimentos de prompt
- Adicionar monitoramento de custo por sessao (ver [[📉 Monitoramento_de_Custos_Claude]])
- Configurar alertas de Harm para conteudo inadequado
- Loop iterativo: Explorar → Construir → Operar → Monitorar → Iterar

---

*Aulas 14 e 17 — Microsoft GenAI for Beginners*
*Links: [Aula 14](https://github.com/microsoft/generative-ai-for-beginners/tree/main/14-the-generative-ai-application-lifecycle) | [Aula 17](https://github.com/microsoft/generative-ai-for-beginners/tree/main/17-ai-agents)*
