---
name: skill-logic-google-seo-integration
description: >
  🚀 Skill_Logic_Google_SEO_Integration
---

# 🚀 Skill_Logic_Google_SEO_Integration

## 📍 Contexto
Integração avançada entre uma Single Page Application (React/Vite) e o ecossistema do Google (Search Console & Indexing API) para automação de SEO e visibilidade imediata.

## 🧠 Lições Aprendidas (GSD Workflow)
- **Causa Raiz:** SPAs puras sofrem com indexação lenta pois o Googlebot pode não renderizar o conteúdo dinâmico imediatamente.
- **Regra de Prevenção:** Injeção de metadados dinâmicos via `react-helmet-async` e Dados Estruturados (JSON-LD) são essenciais para Rich Snippets.

## 🛠️ Implementação Técnica
- **Componente SEO:** Centraliza `Title`, `Description`, `OpenGraph` e `Schema Organization`.
- **Backend Automation:** Scripts Node.js para autenticação OAuth2 e comunicação com APIs do Google.
- **Google Indexing API:** Permite solicitar o rastreamento imediato de novas URLs (útil para novos produtos/carros).
- **Search Console API:** Extração de métricas de cliques e impressões via CLI.

## 📜 Comandos Disponíveis
- `npm run seo:auth`: Autenticação e geração de `tokens.json`.
- `npm run seo:list`: Lista propriedades do Search Console.
- `npm run seo:report "[URL]"`: Relatório de top keywords.
- `npm run seo:index "[URL]"`: Solicita indexação prioritária.
- `npm run seo:audit "[URL]"`: Verifica integridade de sitemaps.

## 🛡️ Segurança
- O arquivo `tokens.json` deve estar SEMPRE no `.gitignore`.
- Credenciais OAuth no `.env` não devem ter o prefixo `VITE_` para evitar exposição no client-side.

---
*Vínculo de Inteligência: [[00_Mapa_Mestre]]*
