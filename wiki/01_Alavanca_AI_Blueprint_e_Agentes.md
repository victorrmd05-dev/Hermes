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
| **00** | **CEO (Paperclip)** | O orquestrador principal de todo o ecossistema do Paperclip. |
| **01** | **CEO Alavanca AI** | O CEO e líder da agência de inteligência artificial. Fornece diretrizes e aprovações de alto nível. (Representa o usuário do sistema). |
| **02** | **CTO** | Diretor de infraestrutura técnica, responsável pelo gerenciamento de chaves de API e configuração das conexões. Dá suporte técnico aos outros agentes. |
| **03** | **Minerador** | Focado na mineração de infoprodutos e ofertas validadas através da análise de dados usando scrapers de meta ads. Alimenta o banco de dados inicial (`workflow_mineracao`). |
| **04** | **Copywriting** | Especialista em escrita persuasiva. Responsável por criar as copys para as páginas de vendas e anúncios, usando os produtos aprovados no dashboard. Escreve os resultados na tabela `workflow_copywriting`. |
| **05** | **Revisor** | Controle de qualidade. Responsável pela revisão rigorosa das copys geradas, garantindo aderência aos padrões da Alavanca AI e validando a versão final junto com o CEO Alavanca AI. |
| **06** | **Designer-Webmaster** | Especialista em criação web. Responsável por traduzir as copys aprovadas no desenvolvimento e no deploy de landing pages funcionais e de alta conversão. |
| **07** | **Video-Maker** | Especialista em criativos visuais. Usa a API do Higgsfield para a criação de vídeos para os anúncios com base nos ganchos emocionais da copy aprovada. |
| **08** | **Gestor-Meta-Ads** | Especialista em tráfego pago. Responsável pela gestão, criação e otimização das campanhas de tráfego utilizando os criativos e as landing pages produzidas pelos outros agentes. |

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
