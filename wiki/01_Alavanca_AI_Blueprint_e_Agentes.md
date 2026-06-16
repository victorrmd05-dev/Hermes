---
aliases: [Alavanca AI Blueprint, Estrutura de Agentes, Organograma Alavanca]
tags: [wiki, alavanca-ai, agents, blueprint, paperclip]
---

# 🤖 Alavanca AI: Blueprint e Estrutura de Agentes

## 🌐 Visão Geral
A **Alavanca AI** é uma agência inteligente impulsionada por agentes autônomos operando sobre a plataforma Paperclip. 
- **Foco:** Minerar, validar e escalar ofertas digitais (infoprodutos e dropshipping). 
- **Comunicação:** Ocorre ativamente via banco de dados Supabase compartilhado e protocolo de delegação interna (`agent://`).

---

## 🏢 Hierarquia e Papéis da Equipe

Abaixo está o organograma da agência. Cada agente possui seu próprio `agent.md` configurado, que define seu comportamento.

| Nível | Agente | Responsabilidade Principal |
| :---: | :--- | :--- |
| **00** | **Paperclip CEO** | Orquestrador mestre do sistema; ponte entre o usuário (ou Hermes Agent) e a infraestrutura. |
| **01** | **Alavanca CEO** | Líder operacional. Foca em velocidade, ROI e delegação. Pede relatórios e gerencia as frentes. |
| **02** | **CTO** | Gerencia infraestrutura, banco de dados (Supabase) e APIs (Scrape Creators, etc). Dá suporte técnico. |
| **03** | **Minerador** | Busca ofertas validadas e lucrativas no Meta Ads, preenchendo o banco de dados. |
| **04** | **Copywriting** | Escreve anúncios e páginas focadas em persuasão e gatilhos emocionais. |
| **05** | **Revisor** | Controle rigoroso de qualidade e compliance, evitando bloqueios de anúncio. |
| **06** | **Designer-Webmaster** | Criação de layouts responsivos, design e publicação de landing pages de alta conversão. |
| **07** | **Video-Maker** | Edição de e criativos visuais (utilizando APIs visuais como Higgsfield). |
| **08** | **Gestor-Meta-Ads** | Compra de tráfego pago, análise de dados de campanha e otimização agressiva de ROI. |
| **09** | **SEO** | Otimização orgânica (On-page/Off-page), palavras-chave e ranqueamento técnico. |

---

## 🧠 Arquivos Avançados (Personalidade e Rotina)

Os agentes utilizam três arquivos de extensão adicionais para guiar seu dia a dia e incorporar uma personalidade profunda:

1. **`SOUL.md` (A Alma):** Define tom de voz, estilo de comunicação e valores core. 
   - *Exemplo:* O CEO é direto, executivo, usa termos de mercado e prioriza "velocidade acima de perfeição".
2. **`HEARTBEAT.md` (A Rotina):** O cronograma interno de tarefas recorrentes e proativas do agente. 
   - *Exemplo:* CEO solicita resumos diários às 09:00 BRT; Minerador realiza busca automática de tendências a cada 6 horas.
3. **`TOOLS.md` (Ferramentas Técnicas):** Manual prático sobre como lidar com as ferramentas atreladas àquele cargo (ex: CTO monitorando logs e implementando pausas para evitar Rate Limits de API).

---

## 🔗 Padrões de Comunicação Interna

> [!IMPORTANT] Regra de Ouro (Agent Links)
> SEMPRE referencie outros agentes nos arquivos de instrução usando a notação estrita de link de agente: `[@NomeDoAgente](agent://nome-do-agente)`. NUNCA use caminhos locais ou menções informais.
> 
> *Exemplo correto:* Solicite análise ao `[@Minerador](agent://minerador)`.
