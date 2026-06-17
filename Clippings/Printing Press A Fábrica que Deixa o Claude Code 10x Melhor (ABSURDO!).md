---
title: "Printing Press: A Fábrica que Deixa o Claude Code 10x Melhor (ABSURDO!)"
source: https://www.youtube.com/watch?v=UDTdsLLwGWw&list=WL&index=13&t=93s
author:
published: 2026-06-11
created: 2026-06-17
description: "Printing Press é a fábrica que transforma qualquer site ou API em CLI agent-native pro Claude Code, com workflow até 10x mais rápido que MCP tradicional. Neste vídeo eu mostro a ferramenta completa: i"
tags:
---
![](https://www.youtube.com/watch?v=UDTdsLLwGWw)

Printing Press é a fábrica que transforma qualquer site ou API em CLI agent-native pro Claude Code, com workflow até 10x mais rápido que MCP tradicional. Neste vídeo eu mostro a ferramenta completa: instalação do binário, carregamento das skills, uso de um CLI pronto da biblioteca de 52 disponíveis, e duas gerações do zero ao vivo, uma a partir de uma API documentada brasileira (Asaas) e outra a partir de um site sem API pública (OLX).  
  
⭐ Inscreva-se na Lista de Espera do Curso Pare de Brigar com a IA: https://app.horadecodar.com.br/lp/pare-de-brigar-com-a-ia-claude-code  
  
🔴 Formação Vibe Coding (Antigravity, Claude Code e +): https://app.horadecodar.com.br/lp/formacao-vibe-coding?utm\_source=yt  
  
🟪 Hospedagem que eu indico: https://www.hostinger.com/matheushoradecodar (use o cupom HORADECODAR para ter +10% de desconto)  
  
📘 Guia Engenharia de Prompt: https://app.horadecodar.com.br/ebookpages/guia-engenharia-de-prompt  
  
Entre no nosso servidor de Discord e me siga nas redes:  
  
🟣 Discord Hora de Codar: https://discord.gg/Veq4mvsWwk  
🔴 Instagram: https://www.instagram.com/horadecodar/  
  
O conceito é poderoso: ao invés de carregar um MCP server pesado que consome token só pra existir no contexto, você usa um CLI enxuto que o agente sabe exatamente como chamar via skill.  
  
Se você usa Claude Code todo dia, sente que MCPs estão pesando no contexto e quer parar de gastar token à toa, esse vídeo é pra você. Cubro o problema do MCP tradicional carregando 30 tools de uma vez, a sacada do Printing Press de gerar 4 outputs de uma só geração (binário Go standalone, skill Claude Code, skill OpenClaw e MCP server), e a parte brasileira gerando CLI pra Asaas e OLX em poucos minutos.  
  
A instalação é direta: go install pra baixar o binário, git clone do repo de skills, claude com plugin-dir pra carregar tudo. As 5 slash commands aparecem no help: printing-press, polish, publish, reprint e import. O conjunto cobre o ciclo completo de uma fábrica de CLIs.  
  
A primeira demo é o flight-goat, que junta Google Flights com Kayak nonstop sem precisar de API key. Rodo busca direta GRU para LHR, scan de range de datas pro mais barato, e mostro a flag agent que ativa json compact no-input no-color yes de uma vez. Esse é o argumento literal do vídeo: o CLI nasce desenhado pra agente, não adaptado pra agente. Termino chamando o flight-goat via prompt em PT-BR no Claude Code, que identifica a skill sozinho.  
  
A segunda demo é gerar CLI do zero pro Asaas, gateway de pagamento brasileiro. Disparo o slash command passando só o nome da empresa, e o Claude Code roda 5 fases automaticamente: research lendo docs, discovery mapeando endpoints, code generation criando o Go CLI, verification rodando dogfood contra a spec, polish limpando e gerando README. No final tem quality score, dois binários (asaas-pp-cli e asaas-pp-mcp), e SKILL.md pronta. Crio conta sandbox em um minuto, exporto a API key como variável de ambiente e rodo customers list e payments list no terminal.  
  
A terceira demo é o pulo do gato: gerar CLI pra um site brasileiro sem API pública. Aponto o printing-press pra URL do OLX, e a fábrica abre browser headless, sniffa o tráfego do front, identifica endpoints internos e parâmetros de paginação, gera CLI igual o do Asaas. Rodo busca de iPhone 15 em Santa Catarina, e chamo via Claude Code em PT-BR pedindo os 5 anúncios mais baratos em Florianópolis das últimas 24h. O mesmo padrão funciona pra Mercado Livre, Vagas, Quinto Andar, qualquer site brasileiro.  
  
Mostro também os recursos extras: o modo Codex delega code generation pro Codex CLI mantendo o Claude como cérebro, economizando 60% dos tokens Opus. O polish roda diagnóstico completo e conserta falhas. E o publish empacota e abre PR automático na biblioteca pública, deixando você como autor, com convite pra ser o primeiro brasileiro a publicar.  
  
Os casos de uso pro seu fluxo: transformar seu SaaS em CLI pro Claude Code chamar direto, virar site BR sem API em agente IA, substituir MCPs pesados liberando contexto, padronizar time inteiro com o mesmo CLI. Tudo open source, gratuito, funciona em Claude Code, Codex, OpenClaw e Hermes, e o autor é endossado publicamente pelo Garry Tan da Y Combinator.  
  
E você, qual API ou site brasileiro quer ver virar CLI no Claude Code? Comenta aqui embaixo que o mais pedido eu gero ao vivo no próximo vídeo. Já testou alguma fábrica de CLI ou ainda usa MCP tradicional? Deixa o like, se inscreve no canal e ativa o sininho pra não perder os próximos drops do ecossistema Claude Code.  
  
  
LINKS  
  
Printing Press: https://printingpress.dev  
  
https://github.com/mvanhorn/cli-printing-press

https://github.com/mvanhorn/printing-press-library

