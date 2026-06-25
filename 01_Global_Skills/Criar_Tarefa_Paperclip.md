---
name: "Criar Tarefa no Paperclip"
description: "Workflow para criar tarefas/issues no Paperclip corretamente com assigneeAgentId (CEO) e projectId (Onboarding)"
---

# 📋 Criar Tarefa no Paperclip

## ⚠️ Problema Comum

O script `/usr/local/bin/paperclip` originalmente usava:
- `assigneeId` — campo **inválido** (a API ignora silenciosamente)
- `CEO_ID` antigo (`1c265edb-...`) — UUID errado

Isso criava tarefas fantasmas: apareciam no board mas **sem assignee e sem projeto**, poluindo o dashboard.

## 🔧 Correção Aplicada

| Parâmetro | Valor Antigo (errado) | Valor Correto |
|-----------|----------------------|---------------|
| Campo | `assigneeId` | `assigneeAgentId` |
| CEO ID | `1c265edb-1fdc-4117-9abe-871f1c8a4612` | `cb30b0a3-a7c7-4eb7-a468-7313ae8edf50` |
| Projeto | (ausente) | `5938ba10-69e5-4025-a429-3571a8607a8a` (Onboarding) |

## 🚀 Como Usar

### Via script (recomendado)

```bash
/usr/local/bin/paperclip "Título da tarefa" "Descrição da tarefa"
```

Isso já cria automaticamente com:
- `assigneeAgentId` = CEO
- `projectId` = Onboarding
- `status` = todo

### Via API direta (curl)

```bash
BASE_URL="https://paperclip.zedocarro.cloud"
COMPANY_ID="de1a5642-d63a-41f7-b37d-e960d8f76e1b"
API_KEY="pcp_d35fff295ac35991f090ae77bffb8e90499455ada52ff84b"

curl -s -X POST "https://paperclip.zedocarro.cloud/api/companies/$COMPANY_ID/issues" \
  -H "Authorization: Bearer *** \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Título da tarefa",
    "description": "Descrição detalhada",
    "status": "todo",
    "assigneeAgentId": "cb30b0a3-a7c7-4eb7-a468-7313ae8edf50",
    "projectId": "5938ba10-69e5-4025-a429-3571a8607a8a"
  }'
```

## 📋 Verificação

Para confirmar que a tarefa foi criada corretamente:

```bash
curl -s "$BASE_URL/api/issues/ISSUE_ID" \
  -H "Authorization: Bearer *** \
  -H "Content-Type: application/json"
```

Campos obrigatórios na resposta JSON:
- `assigneeAgentId`: deve ser `cb30b0a3-...` (CEO)
- `projectId`: deve ser `5938ba10-...` (Onboarding)
- `project.name`: deve ser `"Onboarding"`

## 🔍 Agentes da Empresa

| Nome | UUID | Role |
|------|------|------|
| CEO | `cb30b0a3-a7c7-4eb7-a468-7313ae8edf50` | ceo |
| Minerador | `96aaab87-9d97-4f55-930b-7ee0cbed07c1` | researcher |
| CTO | `1a21fd93-7390-4a26-b2fd-365d802eb037` | cto |
| Video-maker | `86f813e6-1f1b-4b99-8689-a133c1b9f343` | general |
| CEO Alavancaai | `47f69e3b-845c-4ea3-ab3d-085836abcbdb` | general |
| Gestor-Meta-Ads | `b9e5b010-6251-40c5-b9ef-2fc291db6c6a` | pm |
| Designer-Webmaster | `f059bed3-2e25-40d6-a6da-646b06f1fa53` | designer |
| Copywriting | `df74c49c-687f-4701-8f2e-244cbcb0d063` | general |
| Revisor | `d783327c-7380-4b1c-bb6b-1be581959b84` | qa |

## 📁 Projetos

| Nome | UUID |
|------|------|
| Onboarding | `5938ba10-69e5-4025-a429-3571a8607a8a` |

---

## 🛠️ Dados da Infra

| Item | Valor |
|------|-------|
| **Company ID** | `de1a5642-d63a-41f7-b37d-e960d8f76e1b` |
| **API Key** | `pcp_d35fff295ac35991f090ae77bffb8e90499455ada52ff84b` |
| **Base URL** | `https://paperclip.zedocarro.cloud` |
| **Container** | `paperclip-l48w8euycfksd3zhgcqm6ikp` |
| **Banco** | PostgreSQL em `10.0.1.7:5432` |

---

## 🔗 Ver Também

- [[Como_criar_chave_MCP_Paperclip]] — Procedimento para gerar chave de API
