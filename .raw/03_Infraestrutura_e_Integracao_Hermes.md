# Infraestrutura VPS e Integração Hermes + Paperclip

Este documento sumariza a arquitetura e o estado do servidor onde residem os sistemas da Alavanca AI.

## 1. Objetivo da Integração
Conectar o **Hermes Agent** ao **Paperclip** de forma que o Hermes atue como o **Iniciador de Tarefas**, criando issues, delegando comandos para o CEO do Paperclip e acompanhando o progresso da agência via ferramentas MCP (Model Context Protocol).

## 2. Infraestrutura e Hospedagem
- **Servidor:** VPS Hostinger (KVM 2), Ubuntu 24.04 LTS (IP: `76.13.238.201`).
- **Coolify v4.1.0:** Gerenciador da infraestrutura e containers. Endereço: `coolify.zedocarro.cloud`.
- **Domínio Paperclip:** `paperclip.zedocarro.cloud` (tunelado via Cloudflare, Porta 3100).
- **Provedor de IA (OpenCode):** Utilizando o modelo `deepseek-v4-flash-free` via `https://opencode.ai/zen/v1`.

## 3. Status dos Componentes (100% Conectados e Operacionais)

### Hermes Agent
- Instalado localmente (v0.15.1) e presente dentro do container em `/app/hermes-agent/`.
- **Configuração (`~/.hermes/config.yaml`):** O Hermes Agent possui o bloco de `mcp_servers` configurado com o `paperclip_api` conectado via stdio.
- **Integração:** `toolsets: terminal,file,mcp` ativos.

### Paperclip
- Deploy ativo pelo Coolify no projeto "Alavancaai".
- Empresa configurada: **Alavanca AI** (Slug: `ALA`, ID: `c15cfa60-b67f-4405-aa6a-b34277260b8e`).
- API Key criada diretamente no banco de dados (PostgreSQL) e conectada ao Hermes.

## 4. A Integração via MCP (Hermes ↔ Paperclip)
Os antigos gargalos de dependência de Python no container do Paperclip foram resolvidos adotando uma abordagem baseada em MCP bidirecional. A integração está **100% concluída**.

### Como funciona o Fluxo "Invertido" (Hermes como Iniciador):
1. **Identificar a Liderança:** O Hermes acessa a API usando `list_agents` para pegar o ID do CEO Paperclip.
2. **Delegação via Issue:** Usando a ferramenta `create_issue`, o Hermes cria a tarefa na interface do Paperclip e atrela o `assigneeId` ao CEO.
3. **Comunicação Ativa:** O Hermes pode interagir usando `comment_on_issue` na tarefa. O adaptador (`hermes-paperclip-adapter`) detecta os comentários do CEO e "acorda" o Hermes para responder, estabelecendo um ciclo contínuo de colaboração.

### Servidor MCP
- **Projeto:** `paperclip-mcp` (Wizarck), instalado em `/root/paperclip-mcp`.
- **Atalho do Executável:** O script de execução está em `/usr/local/bin/paperclip-mcp`.
- Conecta-se à API interna pela porta `3100`.

## 5. Ferramentas e Atalhos Úteis
Foi criado um script de atalho Bash (`/usr/local/bin/paperclip`) no host VPS para injetar tarefas manualmente direto pelo terminal sem abrir o navegador:
```bash
# Como criar uma tarefa manualmente para o CEO via CLI:
paperclip "Título da sua tarefa" "Descrição opcional"
```
