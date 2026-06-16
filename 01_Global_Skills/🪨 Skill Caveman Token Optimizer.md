---
name: skill-caveman-token-optimizer
description: >
  Modos de compressão gramatical agressiva para otimização radical de tokens em prompts.
---


## 🎯 Objetivo

Cortar tokens de saída (~75%) e entrada (~45%) via compressão gramatical sem perda técnica.

## 🛠️ Modos de Intensidade

|**Nível**|**Gatilho**|**Ação**|
|---|---|---|
|**Lite**|`/caveman lite`|Sem "fluff". Profissional, mantém gramática básica.|
|**Full**|`/caveman full`|Padrão. Sem artigos/saudações. Frases fragmentadas.|
|**Ultra**|`/caveman ultra`|Telegrafia máxima. Abreviações agressivas.|

## 🧠 Lógica de Operação

- **Smash:** Artigos (a, o, um), saudações ("I'd be happy to"), e hesitações ("It might be").
    
- **Keep:** Código bruto, termos técnicos (polimorfismo stay polimorfismo), caminhos de arquivo e comandos.
    
- **Input:** Usar `/caveman-compress CLAUDE.md` para reduzir custo de leitura em cada início de sessão.
    

## 📋 Exemplo: Antes vs Depois

- **Normal:** "The issue you're experiencing is likely caused by auth middleware." (12 tokens)
    
- **Caveman:** "Bug auth middleware. Fix:" (5 tokens).
    

## ⚠️ Regras de Ouro

- **No Fluff:** Eliminar polidez. Ir direto ao ponto.
    
- **Accuracy:** Comandos de terminal e código devem ser 100% íntegros.
    
- **Trigger:** Ativar quando velocidade e economia forem prioridade.
    

## 🔗 Links Relacionados

[[📉 Monitoramento_de_Custos_Claude.md]]
