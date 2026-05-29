# 📥 Caixa de Entrada Bruta (.raw/)

Esta e a **pasta de ingestao** do motor de conhecimento do Nexus.AI.

## Como Usar

Jogue aqui qualquer material bruto que queira que a IA processe:

- PDFs de trafego (Meta Ads, Google Ads, TikTok Ads)
- Planilhas `.xlsx` e `.csv` (Shopify, relatorios de vendas)
- Relatorios de estrategia e textos copiados
- Prints de resultados e screenshots (colados como texto)

## Apos Jogar o Arquivo

Diga para a IA no chat:
> "Ingest o arquivo [nome-do-arquivo]"

ou

> "Ingira este documento e crie notas em wiki/"

## O que a IA Faz

- Le o arquivo completo
- Cria um resumo em `wiki/sources/`
- Extrai conceitos para `wiki/concepts/`
- Mapeia entidades (pessoas, marcas, metricas) em `wiki/entities/`
- Detecta contradicoes com conhecimento anterior e cria alertas

## Comando Rapido

```
/wiki-ingest [nome-do-arquivo]
```

---

> Esta pasta e **ignorada pelo .gitignore** — seus dados brutos nunca saem do seu computador.
