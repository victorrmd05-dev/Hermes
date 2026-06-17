---
name: mcp-paperclip-integration
description: >
  Documentação das ferramentas MCP do Paperclip disponíveis para o Hermes Agent
  (create_issue, comment_on_issue, list_agents, get_dashboard, etc.) usadas para
  delegar tarefas e orquestrar os agentes da Alavanca AI.
---

## 🎯 Objetivo

Catalogar e descrever todas as funções MCP do servidor `paperclip_api` que o Hermes Agent pode invocar para interagir com a plataforma Paperclip e orquestrar a agência Alavanca AI.

---

## 🛠️ Ferramentas Disponíveis

### Issues (Tarefas)

| Ferramenta | Descrição |
|---|---|
| `mcp_paperclip_api_create_issue` | Cria uma nova issue. Parâmetros: `title` (obrigatório), `description`, `assignee_agent_id`, `project_id`, `parent_issue_id`, `priority` (urgent/high/medium/low) |
| `mcp_paperclip_api_list_issues` | Lista issues por status. Filtros: `status` (todo,in_progress,blocked,done,cancelled), `assignee_agent_id`, `project_id`, `label` |
| `mcp_paperclip_api_get_issue` | Obtém detalhes completos de uma issue por ID |
| `mcp_paperclip_api_update_issue` | Atualiza campos de uma issue: `title`, `description`, `status`, `assignee_agent_id`, `priority` |
| `mcp_paperclip_api_delete_issue` | Exclui permanentemente uma issue |
| `mcp_paperclip_api_checkout_issue` | Atribui a issue ao agente atual e marca como `in_progress` (atomic checkout) |
| `mcp_paperclip_api_release_issue` | Desfaz o checkout: desatribui e retorna ao estado anterior |
| `mcp_paperclip_api_comment_on_issue` | Adiciona comentário em Markdown. Opção `reopen` para reabrir issue fechada |

### Agentes

| Ferramenta | Descrição |
|---|---|
| `mcp_paperclip_api_list_agents` | Lista todos os agentes da empresa com nome, role, status e config |
| `mcp_paperclip_api_get_agent` | Detalhes de um agente específico (use "me" para agente atual) |
| `mcp_paperclip_api_invoke_agent_heartbeat` | Dispara um ciclo de trabalho manual para um agente |

### Metas e Projetos

| Ferramenta | Descrição |
|---|---|
| `mcp_paperclip_api_list_goals` | Lista metas estratégicas e projetos da empresa |
| `mcp_paperclip_api_create_goal` | Cria uma nova meta estratégica com título e descrição |
| `mcp_paperclip_api_update_goal` | Atualiza título/descrição de uma meta existente |

### Monitoramento e Auditoria

| Ferramenta | Descrição |
|---|---|
| `mcp_paperclip_api_get_dashboard` | Resumo de saúde da empresa: contagem de agentes, issues abertas/em progresso/bloqueadas, tarefas paradas, atividade recente, custos |
| `mcp_paperclip_api_get_cost_summary` | Gasto de tokens da empresa no período atual: total gasto, orçamento restante, detalhamento por agente |
| `mcp_paperclip_api_list_activity` | Histórico de ações recentes (audit trail). Filtro opcional por `agent_id` |
| `mcp_paperclip_api_list_approvals` | Lista solicitações de aprovação pendentes |

### Aprovações

| Ferramenta | Descrição |
|---|---|
| `mcp_paperclip_api_approve` | Aprova uma solicitação pendente com comentário opcional |
| `mcp_paperclip_api_reject` | Rejeita com motivo obrigatório |
| `mcp_paperclip_api_request_approval_revision` | Solicita revisão sem rejeitar completamente — o agente recebe o feedback e pode reenviar |

---

## 🔄 Fluxo de Trabalho Típico

### Delegar tarefa ao CEO
```
1. list_agents → descobre ID do CEO
2. create_issue(title, description, assignee_agent_id=CEO_ID)
3. invoke_agent_heartbeat(agent_id=CEO_ID)  → acorda o CEO para pegar a tarefa
```

### Fallback CLI (via terminal)
```bash
paperclip "Título da Tarefa" "Descrição detalhada"
```

---

## ⚠️ Observações

- O Hermes Agent atua como **Iniciador de Tarefas** — cria issues para o CEO do Paperclip executar
- `checkout_issue` retorna **409 Conflict** se outro agente já estiver com a issue
- Use `get_dashboard` para visão geral rápida antes de tomar decisões
- Commands de aprovação permitem workflow de revisão humana no loop
