---
name: skill-frontend-design-elite
description: >
  Diretrizes técnicas e design systems para SaaS, Dashboards e apps AI-Native.
---

# 🎨 Skill: Frontend Design & UI/UX Elite

> **Status:** Ativa | **Foco:** SaaS, Dashboards e Interfaces de IA

## 🧠 Core Reasoning (O Cérebro do Design)

Sempre que gerar interfaces, siga este processo de raciocínio:

1. **Contexto do Produto:** Identifique se é B2B (Sério/Limpo), B2C (Emocional/Vibrante) ou AI-Native (Futurista/Minimalista).
    
2. **Hierarquia 60-30-10:** 60% Cor Dominante (Fundo), 30% Cor Secundária (Cards/Inputs), 10% Cor de Ação (Botões/Destaques).
    
3. **Padrão de Densidade:** Use alta densidade (compacto) para Dashboards e baixa densidade (espaçoso) para Landing Pages.
    

## 🛠️ Stack & Componentes (Diretrizes Técnicas)

- **Framework:** Next.js + Tailwind CSS + Lucide Icons.
    
- **Biblioteca Base:** `shadcn/ui` para estrutura, `Magic UI` ou `Aceternity` para efeitos visuais.
    
- **Animações (Framer Motion):** * _Hovers:_ 200ms `ease-out`.
    
    - _Entradas:_ Opacidade 0 para 1 com leve subida (Y: 20 -> 0).
        
- **Grid:** Use exclusivamente o sistema de 8px para `gap`, `padding` e `margin`.
    

## 📐 Regras de UX "Inegociáveis"

- **Botões:** O botão primário deve ter contraste máximo. Nunca use emojis como ícones em botões de ação.
    
- **Tipografia:** * Títulos: Sem serifa, peso `bold` ou `semibold`, tracking `-0.02em`.
    
    - Corpo: `Inter` ou `Geist Sans`, `leading-relaxed`.
        
- **Inputs:** Sempre inclua estados de `:focus-visible` e `:disabled`. Bordas com `rounded-lg` por padrão.
    
- **Empty States:** Nunca deixe uma tela vazia. Use skeletons ou ilustrações minimalistas com um CTA claro.
    

## 🚫 Anti-Patterns (O que NÃO fazer)

- **NÃO** use gradientes genéricos de IA (Roxo/Rosa) em produtos financeiros ou médicos.
    
- **NÃO** use sombras pesadas. Use `shadow-sm` ou bordas finas (`border-[1px] border-white/10`) para dark mode.
    
- **NÃO** use "Pure Black" (`#000000`) para fundos Dark. Use cinzas profundos (`#09090b` ou `#0a0a0a`).
    

## ✅ Pre-delivery Checklist

1. A interface é responsiva (Mobile-first)?
    
2. O contraste atende ao padrão WCAG AA?
    
3. Todos os interativos têm feedback visual (hover/click)?
    
4. As imagens/ícones têm `alt` text e carregamento otimizado?