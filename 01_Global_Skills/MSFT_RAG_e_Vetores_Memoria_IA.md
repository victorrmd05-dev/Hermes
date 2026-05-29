---
tags: [rag, vetores, embeddings, busca-semantica, memoria-ia, microsoft, aula-08, aula-15]
fonte: https://github.com/microsoft/generative-ai-for-beginners
licoes: [08, 15]
status: profundo
---

# 🔍 RAG e Vetores — Memoria Real para IAs (Aulas 8 e 15)

> Nota profunda extraida das Licoes 8 e 15 do curriculo Microsoft GenAI.
> **Impacto no Nexus.AI:** Base teorica para aprimorar o sistema de memoria do JARVIS e Camila.
> Conectada a: [[Skill_Microsoft_GenAI_Curriculum]] | [[🤖 Skill_LangGraph_Vendedora_DNA]] | [[🛡️Conexao_Supabase]] | [[00_Mapa_Mestre]]

---

## O Problema Fundamental que RAG Resolve

LLMs nao sabem o que aconteceu depois do seu treinamento. Nao conhecem seus dados privados.
**RAG e a solucao:** injeta contexto real no momento da inferencia, sem retreinar o modelo.

> "Em vez de mudar o modelo, mudamos o que ele ve antes de responder."

---

## AULA 8 — Busca Semantica: Embeddings como Lingua da IA

### O que sao Embeddings?

- Representacoes numericas densas de texto em espaco vetorial de alta dimensao
- Um texto como `"Azure Machine Learning"` vira um vetor de **1536 numeros** (Ada-002)
- Cada numero representa uma dimensao de significado
- Textos com significado similar ficam **geometricamente proximos** no espaco vetorial

```
"Quero comprar imovel de alto padrao"  →  [0.023, -0.441, 0.891, ...]
"Apartamento de luxo a venda"          →  [0.021, -0.438, 0.887, ...]  (muito proximo!)
"Receita de bolo de chocolate"         →  [-0.312, 0.654, -0.221, ...] (longe)
```

### Busca Semantica vs Busca por Palavras-Chave

| Tipo | Como Funciona | Limitacao |
|------|---------------|-----------|
| Keyword Search | Procura palavras exatas | Nao entende sinonimos nem contexto |
| Semantic Search | Compara significado via vetores | Requer embedding model + vector DB |
| Hybrid (melhor) | Combina ambos | Mais complexo, mais preciso |

**Exemplo real da Microsoft:** busca de videos do YouTube por pergunta em linguagem natural, retornando o timestamp exato onde a resposta esta.

### Pipeline de Criacao do Indice (Aula 8 — implementacao real)

```python
# Passo 1: Baixar transcript do YouTube
# Passo 2: Chunking em segmentos de 3 minutos (overlap de 20 palavras)
# Passo 3: Resumir cada chunk com GPT (60 palavras)
# Passo 4: Gerar embedding com text-embedding-ada-002
# Passo 5: Armazenar no indice (JSON → producao: Vector DB)

# Resultado: embedding_index_3m.json com:
# { "text": "...", "summary": "...", "embedding": [...1536 floats...], "url": "..." }
```

---

## AULA 15 — RAG: Pipeline Completo de Memoria para LLMs

### Como RAG Funciona (Arquitetura Encoder-Decoder)

```
FASE OFFLINE (Ingestao — feita uma vez)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Documentos → Chunking → Embedding Model → Vector Database
                        (Encoder)

FASE ONLINE (Por cada query do usuario)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
User Query → Embedding Query → Busca por Similaridade → Top-K Chunks
                                    ↓
             [Chunks + Query] → LLM → Resposta Fundamentada
                               (Decoder)
```

### Os 4 Pilares do RAG (Microsoft)

- **Knowledge Base:** documentos pre-processados em chunks, convertidos em embeddings
- **User Query:** pergunta do usuario, tambem convertida em embedding
- **Retrieval:** busca os chunks cujos vetores sao mais proximos da query (cosine similarity)
- **Augmented Generation:** LLM usa os chunks como contexto adicional ao prompt

### Dois Paradigmas (Paper Original — Lewis et al. 2020)

```
RAG-Sequence  → usa documentos recuperados para prever a MELHOR RESPOSTA COMPLETA
                Ideal para: perguntas diretas, QA

RAG-Token     → usa documentos para gerar TOKEN POR TOKEN
                Ideal para: textos longos que precisam de multiplas fontes
                Mais caro computacionalmente
```

### Tipos de Busca no Vector Database

```python
# 1. KEYWORD SEARCH — busca exata por palavras
# Limitado: nao entende sinonimos

# 2. VECTOR SEARCH — semantico
from sklearn.neighbors import NearestNeighbors
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)
distances, indices = nbrs.kneighbors([query_vector])

# 3. HYBRID (melhor para producao) — combina os dois
# Azure AI Search faz isso automaticamente com semantic reranker
```

### Similaridade Coseno — A Matematica por Tras

- Mede o angulo entre dois vetores (nao a distancia euclidiana)
- **Score 1.0** = identicos | **Score 0.0** = sem relacao | **Score -1.0** = opostos
- Vantagem: funciona bem mesmo com vetores de tamanhos diferentes
- Alternativas: Euclidean Distance, Dot Product

### Re-ranking — Refinando os Resultados

```python
# Apos a busca vetorial, re-ranquear por relevancia semantica
distances, indices = nbrs.kneighbors([query_vector])
for i in range(3):
    index = indices[0][i]
    print(flattened_df['chunks'].iloc[index])

# Azure AI Search faz re-ranking automatico com Semantic Reranker
```

### Codigo Completo do Chatbot com RAG (Microsoft)

```python
def chatbot(user_input):
    # 1. Converter pergunta em vetor
    query_vector = create_embeddings(user_input)

    # 2. Buscar chunks similares no indice
    distances, indices = nbrs.kneighbors([query_vector])

    # 3. Montar contexto com chunks recuperados
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])
    history.append(user_input)

    # 4. Passar contexto + query para o LLM
    messages = [
        {"role": "system", "content": "Voce e um assistente de IA."},
        {"role": "user", "content": "\n\n".join(history)}
    ]

    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )
    return response.choices[0].message
```

---

## Bancos de Dados Vetoriais — Opcoes e Quando Usar

| Banco | Tipo | Melhor Para |
|-------|------|-------------|
| Supabase + PGVector | Open Source | **JA CONFIGURADO no Nexus.AI** |
| Azure AI Search | Cloud Microsoft | Producao enterprise + hybrid search |
| Azure Cosmos DB | Cloud Microsoft | Multi-modelo, escala global |
| Pinecone | Cloud | Escala massiva, managed |
| Chroma | Local | Prototipagem rapida |
| Weaviate | Open Source | GraphQL nativo |
| Redis | Cache+Vector | Baixa latencia |
| FAISS (Meta) | Library | In-memory, ultra-rapido |

### Estrategias de Chunking

```
Chunking Fixo          → 512 tokens, overlap 50 (simples, padrao)
Chunking Semantico     → por paragrafo/secao (preserva contexto)
Chunking por Sentenca  → boundary detection com nlp
Chunking Hierarquico   → chunks grandes + pequenos (multi-granular)
Chunking por 3 minutos → estrategia Microsoft para video transcripts
```

---

## Metricas de Avaliacao de RAG (Microsoft)

- **Quality:** resposta soa natural, fluente e humana
- **Groundedness:** resposta vem dos documentos fornecidos (nao alucinacao)
- **Relevance:** resposta e relacionada com a pergunta feita
- **Fluency:** resposta faz sentido gramaticalmente
- **Cost:** custo por query (chunking reduz tokens passados ao LLM)

---

## Casos de Uso para o Nexus.AI

- **Camila Imobiliaria** — busca semantica de imoveis (`match_documents` no Supabase)
- **Jarvis_Voz** — memoria de conversas passadas como knowledge base
- **Agente_Agendamento_Clinica** — FAQ e protocolos da clinica como contexto RAG
- **DashboardMobi** — historico de eventos como contexto para analytics IA

### Implementacao Nexus.AI (Padrao ja Existente)

```python
# Supabase + PGVector ja configurado em [[🛡️Conexao_Supabase]]
response = supabase.rpc('match_documents', {
    'query_embedding': embedding_vector,  # vetor da query
    'match_threshold': 0.78,              # similaridade minima
    'match_count': 10                     # top-K resultados
}).execute()
```

---

## RAG vs Fine-Tuning vs Prompt Engineering

| Criterio | Prompt Engineering | RAG | Fine-Tuning |
|----------|-------------------|-----|-------------|
| Custo de implementacao | Baixo | Medio | Alto |
| Atualizacao de dados | Imediata | Imediata | Requer retreino |
| Escala de conhecimento | Limitada ao contexto | Ilimitada | Dataset estruturado |
| Precisao | Media | Alta | Muito alta |
| **Recomendacao Microsoft** | Prototipo | **Producao** | Dominio hiper-especializado |

---

*Aulas 8 e 15 — Microsoft GenAI for Beginners*
*Links: [Aula 08](https://github.com/microsoft/generative-ai-for-beginners/tree/main/08-building-search-applications) | [Aula 15](https://github.com/microsoft/generative-ai-for-beginners/tree/main/15-rag-and-vector-databases)*
