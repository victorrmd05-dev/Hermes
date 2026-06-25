# 🧠 Alavanca Synapse

**Plataforma própria de orquestração de agentes IA** para substituir o Paperclip como sistema central da Alavanca AI (agência de marketing digital).

---

## 🎯 Intenção

Montar uma **agência de marketing digital operada por IA**, onde 8 agentes especializados operam em sincronia através do Supabase como "sinapse central". A esteira pega um anúncio vencedor e produz a campanha inteira com mínima intervenção manual.

### Os 8 Agentes

| Agente | Cérebro (.md) | Mãos (rota) | Status |
|---|---|---|---|
| CEO | ✅ sync | Aprovação/suporte | Camada humana |
| CTO | ✅ sync | Suporte técnico | Camada humana |
| **Minerador** | ✅ régua nova | ✅ `/api/mineracao/run` | **Validado ponta a ponta** |
| Copywriting | ✅ sync | ✅ `/api/copywriting/generate` | Gera copy (revisar max_tokens) |
| Revisor | ⚠️ sync | ❌ falta rota | Pendente |
| Designer-Webmaster | ⚠️ sync | ❌ falta rota | Pendente |
| Video-Maker | ⚠️ sync | ❌ falta Higgsfield | Pendente |
| Gestor-Meta-Ads | ⚠️ sync | ❌ falta rota | Pendente |

---

## 💡 Conceito-chave: Cérebro vs Mãos

Diferente do Paperclip (onde o agente rodava scripts sozinho):

- **🧠 Cérebro** = `AGENTS.md` + `SKILL.md` → system prompt da IA. Réguas de decisão, critérios, rubrica de pontuação, formato JSON de saída. **NÃO** tutoriais de "rodar script".
- **✋ Mãos** = rotas TypeScript em `src/app/api/...` que fazem chamadas externas e gravam no Supabase. A IA só avalia/gera JSON; a rota executa.

### Loop de autoria local
```
agentes/<slug>/AGENTS.md, SKILL.md, ...   ← arquivos editáveis
npm run agents:pull    # Supabase → local
npm run agents:push [slug]   # local → Supabase (vale na hora)
```

---

## 🏗️ Stack
- **Framework:** Next.js 14 App Router + TypeScript strict (`metascale-app`)
- **Estilo:** Tailwind CSS — dark glassmorphism
- **Banco:** Supabase (PostgreSQL + Realtime `postgres_changes`)
- **IA (agentes):** OpenCode Zen → `deepseek-v4-flash-free` via SDK OpenAI
- **IA (diagnóstico Meta Ads):** Anthropic Claude 3.5 Sonnet
- **Auth:** Supabase Auth (futuramente JWT próprio)

---

## 📦 O que já foi construído

### ✅ Minerador — VALIDADO
- Busca na ScrapeCreators (Meta Ad Library)
- Rubrica de score 0–100 com corte em 50
- Blacklist de marketplaces/gateways (antes da IA — economiza crédito)
- Fallback heurístico se IA falhar
- UI funcional em `/mineracao` com campo de keyword + "Minerar com IA"
- Validação real: "Pague 1 Leve 2" → 12 avaliados, 9 ofertas reais validadas

### ✅ Copywriting — Cérebro + Mãos prontos
- Gera copy via IA
- ⚠️ Revisar `max_tokens` (modelo de raciocínio, igual bug do minerador)

### ✅ Camada de dados
- 6 tabelas do pipeline (ads_minerados, campanhas_producao, workflow_*)
- RLS corrigido com policies públicas (provisório — trocar quando houver auth)
- Realtime ligado nas tabelas

---

## 🗺️ Próximos Passos (planejados em 25/06/2026)

1. **Terminar dashboard** (validação no Supabase) — *em andamento*
2. **Construir rota do Revisor** (`/api/revisor/review`)
3. **Construir rota do Designer** (produção de criativos)
4. **Construir rota do Gestor-Meta-Ads** (publicação)
5. **Integrar Video-Maker** (Higgsfield)
6. **Criar fluxo de esteira completo** (`/api/esteira/executar`)
7. **Migrar dados do Paperclip** e desligar legado
8. **Autenticação real** (trocar RLS público por policies com auth)

---

## 🔄 Sessão Atual — 25/06/2026

**Decisão estratégica:** Foi decidido entre Fernando (CEO) e Hermes Agent que:
- **NÃO** vamos construir do zero — vamos aproveitar o Alavanca Synapse que já está validado
- Fernando vai terminar o dashboard no Supabase primeiro
- Depois voltamos para expandir os agentes restantes e integrar a orquestração do Hermes
- O Paperclip continua rodando até o novo sistema estar pronto, depois é desligado

**Integração futura com Hermes:**
- Hermes vai consumir a API do Supabase diretamente (service_role)
- Vai orquestrar a esteira: criar tarefas, comentar, disparar agentes, notificar no Telegram
- Quando o sistema estiver pronto, Hermes vira o orquestrador central

---

## 🔗 Links
- Projeto no Supabase: (pendente — Fernando compartilha quando terminar)
- Repo GitHub: (pendente — subir quando estiver pronto)
- [[03_Infraestrutura_e_Integracao_Hermes]] — referência de integração
- [[Agentes MCP Paperclip vs Synapse.canvas]] — canvas de comparação (criar depois)

---

*Nota criada em 25/06/2026 — atualizar após cada validação de tarefa.*
