# Integração Hermes Agent + Paperclip

Este repositório/documento detalha a integração do **Hermes Agent** com o **Paperclip** rodando em uma VPS, com o objetivo de criar um assistente pessoal via Telegram e terminal que também atua como um agente de SEO automatizado dentro da plataforma Paperclip.

## 🎯 Objetivo
1. **Assistente Pessoal:** Controlar e dar ordens ao Paperclip através do Telegram e do terminal via Hermes.
2. **Agente SEO (Paperclip):** Executar tarefas corporativas e de SEO automaticamente dentro da empresa virtual "Alavancaai".

## 🏗️ Arquitetura
```text
Você (Telegram / Terminal)
    ↓ fala com
Hermes Agent (VPS - 24/7)
    ↓ gerencia via MCP
Paperclip (paperclip.zedocarro.cloud)
    ↓ opera em
Empresa Virtual (Alavancaai)
```

## 🖥️ Infraestrutura (VPS)
- **Provedor:** Hostinger (Plano KVM 2)
- **SO:** Ubuntu 24.04 LTS
- **IP:** `76.13.238.201` (`ssh root@76.13.238.201`)
- **Domínios (via Cloudflare Tunnel):**
  - `coolify.zedocarro.cloud` → Painel Coolify (Porta 8000)
  - `paperclip.zedocarro.cloud` → Instância Paperclip (Porta 3100)

## 📦 Componentes e Serviços

### 1. Coolify v4.1.0 (✅ Operacional)
- Rodando em `coolify.zedocarro.cloud`.
- Gerencia infraestrutura de proxy (Traefik), banco de dados, Redis, Sentinel, etc.

### 2. Hermes Agent v0.14.0 (✅ Operacional)
- **Local de Instalação:** `/app/hermes-agent/` (Executável em `/app/hermes-agent/hermes`, com symlink em `/usr/local/bin/hermes`).
- **Configurações:** `/root/.hermes/`
- **Provedor de LLM:** OpenRouter (Modelo: `nvidia/nemotron-3-super-120b-a12b:free`).
- **Integração Telegram:** Bot `Hermesclip` devidamente configurado e funcional.
- **Status:** Gateway rodando em background como serviço do sistema.

### 3. Paperclip (⚠️ Requer Configuração)
- Implantado via Coolify no projeto "Alavancaai".
- **URL:** `paperclip.zedocarro.cloud`
- **Status:** Instância ativa, banco de dados (PostgreSQL) funcional (volume limpo e recriado), mas no momento exige setup inicial (Onboard).

---

## 🚧 Estado Atual e Próximos Passos

**Problema em Aberto:** O Paperclip possui suporte nativo ao Hermes Agent, mas quando tenta acioná-lo internamente, falha porque o container Docker do Paperclip (Node.js) não possui Python instalado para rodar o script do Hermes. Tentativas de fazer cópias do executável, rodar `pip install` ou montar volumes com a instalação do Python diretamente no container não foram bem sucedidas ou causaram problemas de permissão.

### 📋 Próximos Passos (Ordem de Execução)
1. **Completar Onboard:** Rodar o Quickstart do Paperclip via CLI.
2. **Conta Admin:** Gerar o link de convite (`bootstrap-ceo`) e criar a conta administrativa.
3. **Setup de Empresa:** Criar a empresa "Alavancaai" focada em dropshipping e infoprodutos.
4. **Resolução de Ambiente (Hermes Adapter):** Configurar o adaptador do Hermes no Paperclip, resolvendo a ausência de Python dentro do container (apontando caminho absoluto + dependências).
5. **Integração MCP:** Instalar o MCP do Paperclip no Hermes para controle remoto via Telegram.
6. **Teste Fim-a-Fim:** Validar o fluxo `Você → Telegram → Hermes → Paperclip`.

---

## 🛠️ Comandos Úteis

**Gestão Docker:**
```bash
docker ps # Ver todos os containers em execução
docker logs $(docker ps | grep paperclip | awk '{print $1}') --tail 50 # Logs recentes do Paperclip
docker exec -it $(docker ps | grep paperclip | awk '{print $1}') bash # Entrar no container do Paperclip
```

**Comandos Paperclip (dentro ou via container):**
```bash
# Executar Onboard
docker exec -it $(docker ps | grep paperclip | awk '{print $1}') pnpm paperclipai onboard

# Gerar link de convite do CEO
docker exec -it $(docker ps | grep paperclip | awk '{print $1}') pnpm paperclipai auth bootstrap-ceo
```

**Comandos Hermes:**
```bash
hermes chat           # Iniciar chat via CLI
hermes gateway        # Iniciar gateway
hermes gateway status # Ver status do gateway
hermes doctor         # Diagnóstico de saúde do Hermes
```
