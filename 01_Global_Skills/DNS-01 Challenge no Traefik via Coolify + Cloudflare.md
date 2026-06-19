---
name: dns-01-challenge-traefik-cloudflare
description: Procedimento completo para configurar DNS-01 Challenge no Traefik (Coolify) com Cloudflare, permitindo certificados Let's Encrypt mesmo com proxy Cloudflare ativado (nuvem laranja).
---

# DNS-01 Challenge no Traefik via Coolify + Cloudflare

## Quando usar

- Quando o **HTTP-01 Challenge** falha porque o Cloudflare proxy está ativado (nuvem laranja) e o Traefik não consegue responder ao desafio ACME na porta 80
- Quando o domínio está atrás do proxy Cloudflare e você precisa de certificados **Let's Encrypt** válidos
- Quando o Traefik (coolify-proxy) mostra erros como `acme: error: 403` ou `Invalid response from http://...` no ACME challenge
- Sintomas no log do Traefik:
  ```
  ERR Unable to obtain ACME certificate for domains error="...Invalid response from http://... 502"
  ERR ...acme: error: 403 :: urn:ietf:params:acme:error:unauthorized
  ```

## Pré-requisitos

- **Traefik v3.x** rodando como `coolify-proxy` no Coolify
- **Conta Cloudflare** com o domínio gerenciado
- **Token Cloudflare API** com permissão **DNS:Edit** (escopo: `zone:dns:edit`)
- Acesso SSH ao servidor VPS onde o Coolify roda

## Procedimento

### 1. Gerar token Cloudflare DNS:Edit

1. Acesse https://dash.cloudflare.com/profile/api-tokens
2. Clique em **"Create Token"** → **"Create Custom Token"**
3. Dê um nome (ex: `Coolify Traefik DNS-01`)
4. Permissões:
   - `Zone - DNS - Edit`
5. Recursos do token:
   - `Include - Specific zone - {seu-dominio}` (ou `All zones`)
6. Clique em **"Continue to summary"** → **"Create Token"**
7. **Copie o token imediatamente** (começa com `cfut_...`)

> ⚠️ Importante: O token precisa da permissão `DNS:Edit`, não apenas `DNS:Read`. O DNS-01 Challenge precisa criar e remover registros `_acme-challenge` TXT temporários.

### 2. Salvar token no servidor

```bash
# Crie o arquivo com o token
echo 'cfut_SEU_TOKEN_AQUI' > /root/.cloudflare_token
chmod 600 /root/.cloudflare_token

# Verifique se o token é válido
curl -s "https://api.cloudflare.com/client/v4/user/tokens/verify" \
  -H "Authorization: Bearer $(cat /root/.cloudflare_token)" | jq .
# Deve retornar: {"result":{"id":"...","status":"active"}, "success":true}
```

### 3. Modificar o Traefik (coolify-proxy) para usar DNS-01 Challenge

Edite o arquivo de configuração do proxy:

```bash
nano /data/coolify/proxy/docker-compose.yml
```

**Alterações necessárias:**

**a) Substituir HTTP-01 Challenge por DNS-01 Challenge** no `command:`:

```yaml
# REMOVER estas linhas:
- '--certificatesresolvers.letsencrypt.acme.httpchallenge=true'
- '--certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=http'

# ADICIONAR estas linhas:
- '--certificatesresolvers.letsencrypt.acme.dnschallenge=true'
- '--certificatesresolvers.letsencrypt.acme.dnschallenge.provider=cloudflare'
```

> Opcional: defina um servidor DNS específico:
> ```yaml
> - '--certificatesresolvers.letsencrypt.acme.dnschallenge.resolvers=1.1.1.1:53,8.8.8.8:53'
> ```

**b) Adicionar variável de ambiente** com o token Cloudflare:

```yaml
services:
  traefik:
    # ... demais configurações ...
    environment:
      - CF_DNS_API_TOKEN=${CF_DNS_API_TOKEN:-}
```

> Nota: O provedor Cloudflare do Traefik lê a variável `CF_DNS_API_TOKEN` (ou `CF_API_EMAIL` + `CF_API_KEY` para API Key tradicional). O token DNS:Edit é suficiente e preferível.

**c) Recarregar o Traefik** com a nova configuração:

```bash
docker compose -f /data/coolify/proxy/docker-compose.yml up -d
```

**d) Verificar logs** para confirmar que o DNS-01 Challenge está ativo:

```bash
docker logs coolify-proxy --tail 20 2>&1 | grep -i acme
```

### 4. Configurar variável de ambiente CF_DNS_API_TOKEN

Crie ou edite o arquivo `.env` do proxy Coolify:

```bash
# Verifique se já existe
cat /data/coolify/proxy/.env

# Adicione o token (se não existir)
echo 'CF_DNS_API_TOKEN=cfut_SEU_TOKEN_AQUI' >> /data/coolify/proxy/.env

# OU edite manualmente
nano /data/coolify/proxy/.env
```

> 💡 Alternativa: Defina a env var diretamente no `environment:` do docker-compose.yml (menos seguro, mas funcional).

### 5. Corrigir DNS no Cloudflare (se necessário)

Se o domínio estiver com **CNAME** apontando para `cfargotunnel.com` (Cloudflare Tunnel) sem um tunnel rodando, substitua por um **A record**:

1. Acesse **Cloudflare Dashboard** → **DNS** → seu domínio
2. Remova o CNAME existente (ex: `CNAME paperclip → cfargotunnel.com`)
3. Adicione um **A record**:
   - **Name**: `paperclip` (ou o subdomínio desejado)
   - **IPv4 address**: IP do seu VPS (ex: `76.13.238.201`)
   - **Proxy status**: **Proxied** (laranja) ☁️
4. Salve

> 🔍 Verifique a propagação:
> ```bash
> dig @1.1.1.1 paperclip.seudominio.cloud
> ```
> Deve retornar o IP do VPS (se proxy desligado) ou IPs Cloudflare (se proxy ligado).

### 6. Verificar labels Traefik no container da aplicação

O container da aplicação precisa das labels Traefik corretas. Exemplo para Paperclip:

```yaml
labels:
  - traefik.enable=true
  - traefik.http.middlewares.gzip.compress=true
  - traefik.http.middlewares.redirect-to-https.redirectscheme.scheme=https
  - traefik.http.routers.http-0-{HASH}-{SERVICO}.entryPoints=http
  - traefik.http.routers.http-0-{HASH}-{SERVICO}.middlewares=redirect-to-https
  - 'traefik.http.routers.http-0-{HASH}-{SERVICO}.rule=Host(`paperclip.seudominio.cloud`) && PathPrefix(`/`)'
  - traefik.http.routers.https-0-{HASH}-{SERVICO}.entryPoints=https
  - traefik.http.routers.https-0-{HASH}-{SERVICO}.middlewares=gzip
  - 'traefik.http.routers.https-0-{HASH}-{SERVICO}.rule=Host(`paperclip.seudominio.cloud`) && PathPrefix(`/`)'
  - traefik.http.routers.https-0-{HASH}-{SERVICO}.tls.certresolver=letsencrypt
  - traefik.http.routers.https-0-{HASH}-{SERVICO}.tls=true
```

> ⚠️ **Importante**: Se as labels não tiverem `traefik.http.services...loadbalancer.server.port=PORTA`, o Traefik assume a porta 80. Para aplicações que escutam em outras portas, adicione:
> ```yaml
> - traefik.http.services.{NOME-SERVICO}.loadbalancer.server.port=3100
> ```

### 7. Garantir que o container está na rede coolify

O container precisa estar na mesma rede Docker do `coolify-proxy`:

```bash
# Verifique as redes do container
docker inspect CONTAINER_NAME --format='{{range $net,$v := .NetworkSettings.Networks}}{{$net}} {{end}}'

# Se não estiver na rede coolify, conecte:
docker network connect coolify CONTAINER_NAME
```

### 8. Verificar certificado

Depois de reiniciar o Traefik, ele tentará obter o certificado automaticamente via DNS-01 Challenge.

```bash
# Monitore os logs
docker logs coolify-proxy --tail 50 2>&1 | grep -E "acme|certificate|letsencrypt"

# Teste o HTTPS
curl -s -o /dev/null -w "HTTP %{http_code}\n" --max-time 20 https://seudominio.cloud/

# Verifique o certificado
echo | openssl s_client -connect seudominio.cloud:443 -servername seundominio.cloud 2>/dev/null | openssl x509 -noout -dates
```

### 9. Forçar renovação manual (se necessário)

Se o certificado não for obtido automaticamente:

```bash
# Opção 1: Reiniciar o Traefik
docker restart coolify-proxy

# Opção 2: Remover o arquivo acme.json e reiniciar
# ⚠️ CUIDADO: Isso perde todos os certificados existentes!
systemctl stop coolify-proxy  # ou docker compose down
rm /data/coolify/proxy/acme.json
systemctl start coolify-proxy  # ou docker compose up -d

# Opção 3: Usar certbot manualmente como fallback
certbot certonly --manual --preferred-challenges dns -d seudominio.cloud
```

## Troubleshooting

### Erro: "rateLimited" ou "too many failed authorizations"

```
ERR Unable to obtain ACME certificate for domains ... acme: error: 429
```

**Causa**: Muitas tentativas falhas de validação ACME (limite: 5 falhas por hora por domínio).

**Solução**: 
- **Aguarde 1 hora** para o rate limit resetar (naturalmente)
- Enquanto isso, corrija a configuração do DNS-01 Challenge
- Após o reset, o Traefik tentará automaticamente

### Erro: "Invalid response from http://... 502"

**Causa**: O Cloudflare proxy está retornando 502 porque não há certificado válido (deadlock: sem certificado → proxy 502 → ACME não valida).

**Solução**: Configure DNS-01 Challenge (este procedimento). O DNS-01 não depende da porta 80/443, então funciona mesmo com proxy Cloudflare ativado.

### Erro: "error while parsing rule Host(``)"

```
ERR error="error while parsing rule Host(``) && PathPrefix(`...`)
```

**Causa**: Label Traefik com Host vazio no container.

**Solução**: Reconfigure as labels do container via Coolify ou edite o docker-compose.yml diretamente.

### Erro: "connection reset by peer" na porta 8080 (Traefik API)

**Causa**: A API do Traefik está em modo `insecure=false` e não aceita conexões externas.

**Solução**: Use a rede interna do Docker para acessar a API:
```bash
curl -s http://10.0.1.3:8080/api/http/routers
```

## Diferença entre HTTP-01 e DNS-01

| Característica | HTTP-01 | DNS-01 |
|---|---|---|
| Validação | Responde na porta 80 | Cria registro TXT no DNS |
| Funciona com Cloudflare proxy (laranja)? | ❌ Não | ✅ Sim |
| Depende de porta 80 aberta? | ✅ Sim | ❌ Não |
| Requer token DNS API? | ❌ Não | ✅ Sim |
| Suporta wildcard `*.dominio`? | ❌ Não | ✅ Sim |

## Referências

- [Traefik Documentation: DNS Challenge](https://doc.traefik.io/traefik/https/acme/#dnschallenge)
- [Traefik Documentation: Cloudflare Provider](https://doc.traefik.io/traefik/https/acme/#providers)
- [Cloudflare API Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)
- [Let's Encrypt Rate Limits](https://letsencrypt.org/docs/rate-limits/)
