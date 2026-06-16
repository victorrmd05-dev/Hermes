---
name: monitoramento-de-custos-claude
description: >
  🎯 Objetivo
---

## 🎯 Objetivo

Rastrear e limitar o consumo de tokens e o custo financeiro das chamadas de API durante as sessões de codificação.

## 🛠️ Pré-requisitos

- Acesso à API da Anthropic.
    
- Variáveis de ambiente de precificação configuradas.
    

## 📝 Workflow (Passo a Passo)

1. **Captura de Input/Output:** O sistema lê a quantidade de tokens enviados e recebidos em cada mensagem.
    
2. **Cálculo de Preço:** Multiplica os tokens pelo valor atual do modelo (ex: Claude 3.5 Sonnet).
    
3. **Acúmulo de Sessão:** Soma o custo total desde o início da execução do CLI.
    
4. **Alerta de Limite:** Se o custo ultrapassar o limite definido no `config`, o sistema emite um aviso no terminal.
    

## ⚠️ Regras e Restrições

- Não interromper processos críticos de escrita de arquivo, apenas avisar o usuário.
    
- O rastreador deve ser resetado a cada nova sessão iniciada pelo comando `claude`.
    

## 🔗 Links Relacionados

- [[00_Mapa_Mestre]]
- [[🪨 Skill Caveman Token Optimizer]]
