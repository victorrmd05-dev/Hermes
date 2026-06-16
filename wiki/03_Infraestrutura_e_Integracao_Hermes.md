---
aliases: [Infraestrutura VPS, Integração Hermes e Paperclip, MCP Setup]
tags: [wiki, infraestrutura, hermes, paperclip, mcp, vps, coolify]
---

# 🖥️ Infraestrutura VPS e Integração Hermes + Paperclip

Este documento sumariza a arquitetura, o estado do servidor e o fluxo técnico que interliga os sistemas vitais da Alavanca AI.

## 🎯 1. Objetivo da Integração
O objetivo central é conectar o **Hermes Agent** ao **Paperclip** de forma que o Hermes atue autonomamente como o **Iniciador de Tarefas**. 
Através do Model Context Protocol (MCP), o Hermes pode criar issues, delegar comandos operacionais para o CEO do Paperclip e acompanhar o progresso global da agência.

---

## ☁️ 2. Infraestrutura e Hospedagem
- **Servidor:** VPS Hostinger (Plano KVM 2).
- **Sistema Operacional:** Ubuntu 24.04 LTS.
- **Endereço IP:** `76.13.238.201`.
- **Gerenciador de Infra:** Coolify v4.1.0 (`coolify.zedocarro.cloud`).
- **Endereço Paperclip:** `paperclip.zedocarro.cloud` (tunelado via Cloudflare, operando na porta 3100).
- **Provedor de LLM:** Modelo `deepseek-v4-flash-free` hospedado via OpenCode (`https://opencode.ai/zen/v1`).

---

## 🟢 3. Status dos Componentes (100% Operacionais)

### 🤖 Hermes Agent
- **Versão e Local:** Instalado localmente (v0.15.1) e ativo dentro do container em `/app/hermes-agent/`.
- **Configuração de Conexão:** Em `~/.hermes/config.yaml`, o Hermes possui o bloco `mcp_servers` configurado com `paperclip_api` ativo via `stdio`.
- **Capacidades Ativas:** `toolsets: terminal, file, mcp`.

### 📎 Paperclip
- **Hospedagem:** Deploy mantido pelo Coolify sob o projeto "Alavancaai".
- **Dados da Empresa:** **Alavanca AI** (Slug: `ALA`, ID: `c15cfa60-b67f-4405-aa6a-b34277260b8e`).
- **Segurança:** A API Key foi gerada via banco de dados PostgreSQL e vinculada permanentemente ao Hermes.

---

## 🔄 4. O Fluxo de Integração MCP

A antiga dependência de rodar scripts Python soltos dentro do container Node.js foi substituída por uma integração limpa e bidirecional baseada em **MCP**. A integração está **100% concluída**.

### Fluxo "Invertido" (Hermes como Iniciador)
O ecossistema roda de forma assíncrona da seguinte maneira:
1. **Identificação da Liderança:** O Hermes usa o endpoint MCP `list_agents` para rastrear dinamicamente o ID do "CEO Paperclip".
2. **Delegação de Issue:** Utilizando a ferramenta `create_issue`, o Hermes cria uma tarefa descritiva na interface web do Paperclip, atrelando o `assigneeId` diretamente ao CEO.
3. **Comunicação Contínua:** O Hermes engaja usando `comment_on_issue`. Assim que o CEO responde pela interface do Paperclip, o `hermes-paperclip-adapter` detecta a notificação e "acorda" o Hermes para retrucar, fechando o loop de colaboração.

### Servidor MCP Ativo
- **Projeto Fonte:** `paperclip-mcp` (Wizarck).
- **Diretório Raiz:** `/root/paperclip-mcp`.
- **Binário/Atalho:** `/usr/local/bin/paperclip-mcp`.
- **Conexão:** Fala com a API interna do Paperclip via porta local `3100`.

---

## 🛠️ 5. Ferramentas e Atalhos Úteis

> [!TIP] Criação de Tarefas via CLI
> Para facilitar a gestão sem precisar abrir o navegador web, foi criado um script global de injeção de tarefas no VPS.

**Atalho Bash (`/usr/local/bin/paperclip`):**
Você pode dar ordens ao CEO e criar Issues diretamente do seu terminal (via SSH) rodando:
```bash
paperclip "Título da sua tarefa aqui" "Descrição estendida e opcional aqui"
```
