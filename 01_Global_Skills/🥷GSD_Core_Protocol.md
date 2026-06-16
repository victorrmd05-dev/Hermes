---
name: gsd-core-protocol
description: >
  Protocolos do sistema GSD para gestão autônoma de projetos e workflow ágil.
---

# ⚡ Protocolo GSD (Get Shit Done) - Nexus Core OS

Este documento define como o assistente deve utilizar os comandos globais do GSD para iniciar e gerenciar projetos.

## 🚀 Início de Novos Projetos
Sempre que um novo diretório de projeto for aberto e não contiver uma estrutura de codebase, o assistente deve:
1. Executar `/gsd-new-project` para iniciar a arquitetura.
2. Responder às perguntas de configuração focando em: **React, Tailwind, Supabase e Node.js** (Stack Padrão Fernando).
3. Garantir a criação do `PROJECT.md` e da pasta `.planning/`.

## 🛡️ Regra de Ouro de Segurança (NÃO ENVIAR AO GITHUB)
**É TERMINANTEMENTE PROIBIDO** subir a pasta de configuração do codebase ou arquivos sensíveis gerados pelo GSD para o GitHub.
* O assistente deve garantir que `.planning/`, `PROJECT.md` e arquivos de log do GSD estejam no `.gitignore` local do projeto.

## 📂 Integração com Nexus
* O `PROJECT.md` gerado pelo GSD deve sempre conter um link para o `[[00_Mapa_Mestre]]` do Nexus para manter o alinhamento de contexto.