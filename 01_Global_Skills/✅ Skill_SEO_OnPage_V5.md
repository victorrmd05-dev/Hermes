---
name: skill-seo-onpage-v5
description: >
  Skill_SEO_OnPage_V5 — Nexus SEO Engine
---

# Skill_SEO_OnPage_V5 — Nexus SEO Engine
> Extraído de: seobuild-onpage v1.5.0 | Nível: AGENTE | Uso: Geração e auditoria de páginas SEO

---

## MÓDULO 1 — PIPELINE DE PESQUISA (Data Layer)

### 1.1 Cascade de Fontes (ordem de prioridade)
| # | Fonte | Dados fornecidos |
|---|-------|-----------------|
| 1 | DataForSEO API | SERP live, content parsing, PAA, volumes |
| 2 | Ahrefs MCP | KD, DR, tráfego estimado, backlinks |
| 3 | SEMRush MCP | Keyword analytics, organic research |
| 4 | Google Search Console | CTR, posição, canibalização |
| 5 | WebSearch | Fallback sem chaves de API |

### 1.2 Comandos de Execução
```python
# Pesquisa completa (com credenciais DataForSEO)
python3 research.py "<keyword>" --output=brief

# Sem credenciais — modo mock para testes
python3 research.py "<keyword>" --mock --output=compact

# Canibalização via GSC
python3 gsc_pull.py "<site_url>" --keyword="<kw>" --cannibalization

# Output JSON para pipeline downstream
python3 research.py "<keyword>" --output=json --save-dir=./output/
```

### 1.3 Schema de Output da Pesquisa
```json
{
  "keyword": "string",
  "intent": "informational|commercial|transactional|navigational",
  "word_count_stats": {
    "min": 800, "max": 3200, "median": 1800,
    "recommended_min": 1440, "recommended_max": 2340
  },
  "paa_questions": ["..."],
  "topic_frequency": [{"topic": "string", "competitor_count": 5}],
  "heading_patterns": {
    "avg_h2_count": 6.2, "avg_h3_count": 8.1,
    "median_h2_count": 5, "median_h3_count": 7
  }
}
```

---

## MÓDULO 2 — DETECÇÃO DE INTENÇÃO (serp_analyze.detect_intent)

### 2.1 Sinais de Intenção (ordem de avaliação)
```python
# NAVIGATIONAL → highest precedence
signals = ["login", "sign in", "website", "official", ".com"]

# TRANSACTIONAL
signals = ["buy", "purchase", "order", "download", "subscribe",
           "deal", "discount", "coupon", "price", "pricing", "cost", "cheap"]

# COMMERCIAL INVESTIGATION
signals = ["best", "top", "review", "comparison", "vs", "versus",
           "alternative", "pros and cons"]

# INFORMATIONAL
signals = ["how to", "what is", "what are", "why", "guide",
           "tutorial", "learn", "example", "definition", "explain"]

# Default fallback: "commercial"
```

### 2.2 Regra de Aplicação
- Avaliar na ordem acima; primeiro match vence.
- Se `featured_snippet` presente no SERP → `informational`.
- Se ambíguo → inspecionar `title` dos top-5 orgânicos.
- Fallback final: `"commercial"`.

---

## MÓDULO 3 — ANÁLISE SEMÂNTICA DE HEADINGS

### 3.1 Extração de Headings (DataForSEOClient._extract_headings)
```python
# Extrai h1, h2, h3 do page_content parseado
for level in ["h1", "h2", "h3"]:
    for heading in page_content.get(level, []):
        headings.append(f"{level.upper()}: {heading}")
# Output: ["H1: Main Title", "H2: Section One", "H3: Sub A"]
```

### 3.2 Frequência de Tópicos (topic_frequency)
```python
# Para cada competitor, extrai H2/H3, normaliza e conta frequência
def _normalize_topic(topic):
    # Remove prefixos: "the ", "a ", "an ", "our ", "your ", "my ", "about "
    # Remove pontuação final: ".:!?"
    return topic.strip()

# Resultado: top-30 tópicos ordenados por competitor_count DESC
```

### 3.3 Padrões de Heading (heading_patterns)
```python
{
    "avg_h2_count": statistics.mean(h2_counts),  # float
    "avg_h3_count": statistics.mean(h3_counts),
    "median_h2_count": statistics.median(h2_counts),  # int
    "median_h3_count": statistics.median(h3_counts),
}
```

### 3.4 Regras Críticas de SEO para Headings
- ✅ **1 único H1** por página (múltiplos H1 = penalidade confirmada)
- ✅ H2/H3/H4 usam **entity names**, nunca keyword exata verbatim
- ✅ Exceção EMQ: se 2/3 dos top-3 competitors têm keyword exata no H1 → `EMQ_REQUIRED: true`
- ❌ Nunca keyword exata verbatim em H2/H3/H4 (anti-SEO over-optimization)
- ❌ Nunca headings vazios sem conteúdo

---

## MÓDULO 4 — REGRAS ON-PAGE: TÍTULO, META & ESTRUTURA

### 4.1 Title Tag
- `< 60 chars` com keyword alvo de forma natural
- Não "overstuffed" — promete resultado concreto
- Keyword exata no título ✅ — keyword exata na meta description ❌

### 4.2 Meta Description
- `< 155 chars`
- Usa **entity names + value proposition**, não keyword verbatim
- Exemplo: `"Compare JFK airport parking from $8/day. Official lots, off-site savings, shuttle times."`

### 4.3 URL
- Streamlined com keyword alvo, sem palavras extras
- ✅ `/airports/fll`
- ❌ `/airports/fort-lauderdale-fll-airport-parking-guide-2026`

### 4.4 Image Alt Text
- Descritivo do conteúdo da imagem
- ❌ Keyword stuffing em alt text = sinal negativo de ranking
- ❌ Stock photos = demoção leve confirmada (use originais ou AI-generated)

---

## MÓDULO 5 — ARQUITETURA 500-TOKEN (Chunk Architecture)

### 5.1 Dimensões do Chunk
| Engine | Chunk Size | Overlap |
|--------|-----------|---------|
| Google AI | ~500 tokens (~375 palavras) | — |
| LLMs (GPT/Gemini) | ~600 palavras | ~300 palavras |

### 5.2 Regras de Chunk
1. **H2 = query real ou QFO question** (People Also Ask ou fan-out lógico)
2. **Snippet Answer**: primeiras 2-3 frases após cada H2 = resposta direta, sem preâmbulo
3. **Contrast Statement**: comparação X vs Y com números no mesmo chunk
4. **Self-contained**: nunca dividir tabela entre chunks; mínimo 250 palavras entre dois H2s
5. **Front-load**: material mais forte nos primeiros 3 chunks
6. **QFO Facet Label**: cada chunk responde 1 sub-query específica (não 2)

### 5.3 Signals de Otimização Google AI (7 Signals)
| Signal | Como otimizar |
|--------|--------------|
| Gecko Score (embeddings) | Cobrir semantic neighbors, sinônimos, entidades relacionadas |
| BM25 | Incluir termos exact-match, nomes de entidades, sinônimos de alto volume |
| PCTR | Títulos com números/power words, meta descriptions com valor proposital |
| Freshness | Datas "últimas verificações", conteúdo sazonal, preços atualizados |
| Boost/Bury | Evitar seções thin, headings vazios, conteúdo duplicado |
| Jetstream | Análises genuínas, comparações honestas, framing único |
| Base Ranking | Autoridade topical sólida, SEO técnico limpo |

---

## MÓDULO 6 — LINKS INTERNOS & CANÔNICOS

### 6.1 Hub & Spoke Architecture
```
Hub Page (ex: "ATL Airport Parking")
├── Spoke 1: Terminal 1 Parking Guide
├── Spoke 2: Off-Airport Lots Comparison
├── Spoke 3: EV Charging Options at ATL
├── Spoke 4: Long-term vs Short-term Costs
└── Spoke 5: Shuttle Frequency & Wait Times

Regras:
- Cada spoke → links de volta ao hub
- Hub → links para os spokes mais importantes
- Dead-end content (flat lists sem links) = desperdício de crawl equity
- Link density alta: cada spoke → hub + 2+ spokes irmãos
```

### 6.2 Flags de Oportunidade
```
QDD_SIGNAL: HIGH_CONFIDENCE_TAKEOVER
→ UGC (Reddit, Pinterest, TikTok) no top-10 = nenhuma authority page existe
→ Estratégia: estrutura > socialização; tabelas + entity signals ganham de UGC

NICHE_PIVOT_OPPORTUNITY: true
→ 2 dos top-3 são domínios generalistas sem silo topical
→ Ação: hub + mínimo 5 spokes + high internal link density

SITE_DOMINANCE_OPPORTUNITY: HIGH
→ Quando 2/3 top resultados são generalistas sem silo
→ Google rewards site-level topicality sobre single-page optimization
```

### 6.3 Linking para Map Embed (Local SEO)
- Páginas informacionais de alto tráfego → link contextual para página de localização/mapa
- Shift de sinais: da intent informacional para commercial/local
- Especialmente eficaz para negócios multi-localização

---

## MÓDULO 7 — ESTRUTURA OBRIGATÓRIA DA PÁGINA

```
[0] AI Summary Nugget (200 chars max)
    → Bloco <div class="ai-summary"> ACIMA do H1
    → Facts puras: entidade primária + número chave + distinção
    → Otimizado para Perplexity/Gemini/ChatGPT "answer nuggets"

[1] Title + URL
    → < 60 chars, keyword natural, outcome claro

[2] Opening Answer Block (100-150 palavras)
    → Resposta direta à query principal
    → Diferenciação + distinção principal

[3] Fast-Scan Summary (imediatamente após opening)
    → 3-5 bullets COM fatos concretos OU tabela de comparação OU decision matrix
    → NUNCA omitir

[4] Main Body (sections 500-token QFO facets)
    → Cada seção = 1 job único: explicar, comparar, quantificar, ranquear, avisar, precificar

[5] Tabela HTML <table> Real
    → Colunas úteis: "Best For", "Main Tradeoff", "Typical Cost {{VERIFY}}"
    → NUNCA simular tabelas com bullet points

[6] Prove-It Section (Information Gain)
    → 2+ fatos operacionais duros com citations rastreáveis
    → Passa o Reddit Test

[7] "Not For You" Block
    → Cenários específicos em que este NÃO é o choice certo
    → ≥ 1 linha que um concorrente nunca publicaria

[8] Original Research / Data Experiment Block (MANDATÓRIO)
    → Seção com dados próprios, metodologia ou cross-reference único
    → Sem isto: score máximo = 20/38

[9] FAQ Section
    → ≥ 3 PAA questions respondidas
    → Cada par Q&A em FAQPage schema JSON-LD

[10] Hub/Spoke Internal Links
     → "Related Pages" ou "More Guides" com targets reais

[11] Conclusion / Next Step
     → Direto: decisão + próxima ação. Não restate a página inteira.

[12] JSON-LD Schema Block (OBRIGATÓRIO)
     → FAQPage + HowTo/Product/LocalBusiness + BreadcrumbList
     → Também embed RDFa/Microdata inline para LLMs
```

---

## MÓDULO 8 — VERIFICATION TAGS SYSTEM

| Tag | Quando usar |
|-----|-------------|
| `{{VERIFY: claim \| source}}` | Preço, taxa, capacidade, horários, distâncias |
| `{{RESEARCH NEEDED: topic \| source}}` | Seção com dado que falta |
| `{{SOURCE NEEDED: claim}}` | Claim sem corroboração em 2+ fontes |

**Regra Entity Consensus:** Toda claim factual deve ser corroborada por ≥ 2 fontes de alto ranking para o mesmo tópico. Claims únicos + originais → metodologia explícita.

---

## MÓDULO 9 — QUALITY CHECKLIST (38 itens — threshold 30/38)

### Critical Pass/Fail (primeiros 24)
| # | Check | Crítico? |
|---|-------|---------|
| 1 | Information gain sobre top-10 Google | ✅ |
| 3 | Core answer nas primeiras 150 palavras | ✅ |
| 4 | Fast-scan summary nos primeiros 200 palavras | ✅ |
| 6 | ≥ 1 tabela HTML real (não bullet lists) | ✅ |
| 8 | Números específicos com `{{VERIFY}}` | ✅ |
| 10 | Bloco "Not For You" presente | ✅ |
| 11 | Conteúdo estruturado em chunks de 500-token | ✅ |
| 14 | JSON-LD schema incluído e corresponde ao page type | ✅ |
| 15 | FAQ com ≥ 3 PAA questions | ✅ |
| 21 | Single H1 tag (nunca múltiplos H1) | ✅ |
| 22 | Sem keyword exata na meta description | ✅ |
| 24 | Alt text descritivo (não keyword-stuffed) | ✅ |

### Advanced Checks (25-38)
| # | Check |
|---|-------|
| 25 | AI Summary Nugget (200-char) ao topo |
| 26 | Original Research/Data Experiment block |
| 32 | Sem banned 2026 content patterns |
| 33 | Mínimo 1.500 palavras de conteúdo substantivo |
| 35 | QDD check executado — UGC no top-10 flagged ou cleared |
| 36 | Site vs. Page audit — tipo de competitor identificado |
| 37 | EMQ ratio verificado — flag aplicada corretamente |
| 38 | Cada chunk 500-token targeta QFO facet distinto |

---

## MÓDULO 10 — BANNED PATTERNS (2026)

### Nunca fazer:
- Intros genéricos ou preambles definicionais
- "In today's fast-paced world" (ou variantes)
- "Whether you're a X or a Y..."
- A palavra "nestled" | Em-dashes
- FAQ fluff repetitivo sem dados operacionais únicos
- Bullet lists fingindo ser tabelas
- Seções quase-idênticas com mudança apenas de wording
- Headings vazios sem conteúdo
- Keyword stuffing em qualquer campo
- Múltiplos H1 tags
- Conteúdo fora do "core topical circle" do domínio
- Páginas "catchall" broad — detalhes específicos sempre ganham
- 300-word "LLM chunk" pages (confirmado penalizado em 2026)
- Generic AI FAQ sem dados únicos ou operacionais específicos

---

## MÓDULO 11 — INTEGRAÇÃO SHOPIFY

### 11.1 Mapeamento de Componentes Shopify
```liquid
{% comment %} AI Summary Nugget — acima do H1 no template {% endcomment %}
<div class="ai-summary" itemscope itemtype="https://schema.org/Article">
  {{ page.content | truncate: 200 }}
</div>

{% comment %} Single H1 — nunca usar h1 em snippets de section {% endcomment %}
<h1>{{ page.title }}</h1>

{% comment %} Tabela de comparação — usar table HTML, não bullets {% endcomment %}
<table>
  <thead><tr><th>Opção</th><th>Preço</th><th>Melhor Para</th></tr></thead>
  <tbody>
    {% for variant in product.variants %}
    <tr>
      <td>{{ variant.title }}</td>
      <td>{{ variant.price | money }}</td>
      <td>{{ variant.metafields.seo.best_for }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
```

### 11.2 Schema em Shopify (via theme.liquid)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{ faq.question }}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ faq.answer | strip_html }}"
      }
    }
  ]
}
```

### 11.3 Metafields Recomendados para SEO On-Page
```
namespace: seo
keys:
  - ai_summary_nugget (single_line_text, max 200 chars)
  - information_gain   (multi_line_text)
  - reddit_test        (single_line_text)
  - not_for_you_block  (rich_text)
  - prove_it_facts     (json — array of {fact, source, verify_tag})
  - page_intent        (single_line_text — informational|commercial|transactional)
  - emq_required       (boolean)
  - qdd_signal         (boolean)
  - word_count_target  (number_integer)
```

### 11.4 Workflow Nexus + Shopify
```
1. Nexus executa research.py → gera brief JSON
2. Nexus cria page draft via Shopify Admin API (GraphQL mutation pageCreate)
3. Nexus popula metafields seo.* via metafieldDefinitionCreate
4. Nexus insere JSON-LD schema no <head> via theme.liquid snippet
5. Nexus valida Quality Checklist 38 items antes de publicar
6. GSC conectado ao site → post-publish: monitorar CTR e posição
```

---

## REFERÊNCIAS RÁPIDAS

```bash
# Testar sem API keys
python3 research.py "SEO para Shopify" --mock --output=compact

# Rodar todos os testes
python3 tests/test_serp_analyze.py
python3 tests/test_dataforseo.py

# Verificar configuração de credenciais
python3 scripts/lib/env.py
```

---
*Skill_SEO_OnPage_V5 — Gerado por Nexus | seobuild-onpage v1.5.0 | 2026-04-12*
