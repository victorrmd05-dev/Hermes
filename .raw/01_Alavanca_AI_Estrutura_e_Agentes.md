# Alavanca AI: Blueprint e Estrutura de Agentes

## 1. Visão Geral
A **Alavanca AI** é uma agência impulsionada por agentes autônomos operando sobre a plataforma Paperclip, focada em minerar, validar e escalar ofertas digitais (infoprodutos e dropshipping). A comunicação acontece via Supabase compartilhado e protocolo de delegação interna (`agent://`).

## 2. Hierarquia e Papéis da Equipe
Cada agente tem seu `agent.md` que define o seu comportamento. A hierarquia se organiza assim:

- **00 - Paperclip CEO**: Orquestrador mestre do sistema, ponte entre o usuário (ou Hermes Agent) e a infraestrutura.
- **01 - Alavanca CEO**: Líder operacional. Foca em velocidade, ROI e delegação. Pede relatórios e gerencia as frentes.
- **02 - CTO**: Gerencia infraestrutura, banco de dados (Supabase) e APIs (Scrape Creators, etc). Dá suporte técnico.
- **03 - Minerador**: Busca ofertas validadas no Meta Ads, preenchendo o banco de dados.
- **04 - Copywriting**: Escreve anúncios e páginas focadas em persuasão e gatilhos emocionais.
- **05 - Revisor**: Controle de qualidade e compliance, evitando bloqueios de anúncio.
- **06 - Designer-Webmaster**: Criação de layouts, páginas responsivas e landing pages de alta conversão.
- **07 - Video-Maker**: Edição de e criativos visuais (usa APIs como Higgsfield).
- **08 - Gestor-Meta-Ads**: Compra de tráfego pago, análise de dados e otimização de ROI.
- **09 - SEO**: Otimização orgânica de palavras-chave e ranqueamento técnico.

## 3. Arquivos Avançados (Personalidade e Rotina)
Os agentes utilizam arquivos de extensão para guiar seu dia a dia e personalidade de maneira profunda:
- **SOUL.md (A Alma):** Define tom de voz e valores core. Exemplo: O CEO é direto, usa termos de mercado e prioriza "velocidade acima de perfeição".
- **HEARTBEAT.md (A Rotina):** Cronograma de tarefas do agente. Exemplo: CEO pede resumos diários às 09:00 BRT; Minerador realiza busca automática de ofertas a cada 6 horas.
- **TOOLS.md (Ferramentas):** Manual técnico sobre como lidar com as ferramentas daquele cargo (ex: CTO monitorando logs e evitando Rate Limits).

## 4. Padrões de Comunicação
**Regra de Ouro:** SEMPRE referencie outros agentes nos arquivos usando a notação estrita de link de agente: `[@NomeDoAgente](agent://nome-do-agente)`. (Ex: `[@Minerador](agent://minerador)`). NUNCA use caminhos locais de arquivo.
