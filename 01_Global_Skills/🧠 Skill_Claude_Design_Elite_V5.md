---
name: skill-claude-design-elite-v5
description: >
  Padrões de ritmo visual e hierarquia extraídos diretamente do Claude Design System.
---

# 🧠 Skill: Claude Design Elite — V5
> **Padrão:** Hermes Standard · **Versão:** 5.0 · **Data:** 2026-04-21
> **Fonte:** Destilação do Claude Design System (design_raw.md · 464 linhas · 73 KB)
> **Classificação:** 🔒 Interno — Uso Estratégico

---

## ⚡ TL;DR — O que esta Skill entrega

Um conjunto de lógicas de elite extraídas diretamente do engine de design do Claude (claude.ai). Cobre:
- **Ritmo visual** — como criar variância intencional, não caos.
- **Layering (camadas)** — composição em profundidade, não em planura.
- **Anti-clichês** — o que corta a credibilidade do design instantaneamente.
- **localStorage persistence** — padrões técnicos para estado sobreviver a refresh.

---

## 🎼 I. RITMO VISUAL (Visual Rhythm)

> *"Introduza variedade visual intencional e ritmo: use cores de fundo diferentes para aberturas de seção; use layouts full-bleed quando a imagem é central."*

### Princípios Ativos

| Lei | Aplicação Prática |
|---|---|
| **Sistema Primeiro** | Antes de qualquer tela, declare o sistema. Escolha layout para cabeçalhos, títulos, imagens. Só então construa. |
| **Variância Controlada** | Máx. 1–2 cores de fundo por deck. Variância vem de **layout**, não de paleta aleatória. |
| **Contraste de Densidade** | Alterne slides/telas densas em texto com telas de impacto visual. O olho precisa de respiro. |
| **Tipografia como Ritmo** | Use escalas tipográficas para criar hierarquia. Nada abaixo de 24px em 1920×1080. 12pt mínimo em print. |
| **Escala de Toque** | Em mockups mobile: nenhum alvo de toque menor que 44px. |

### Padrão de Aplicação
```
1. Vocalizar o sistema antes de codificar: "Vou usar X para headers, Y para corpo, Z para blocos de destaque."
2. Aberturas de seção → cor de fundo diferente do restante.
3. Quando imagem é o conteúdo → layout full-bleed (sem margens internas).
4. Slides pesados em texto → comprometer-se com uma imagem placeholder real.
5. Variações devem começar básicas e escalar para avançadas/criativas.
```

---

## 🗂️ II. LAYERING (Camadas Visuais)

> *"Brinque com escala, preenchimentos, textura, ritmo visual, layering, layouts novos, tratamentos de tipo."*

### O Conceito
Layering é a prática de criar **profundidade perceptual** — a sensação de que elementos existem em planos distintos, não todos na mesma superfície plana.

### Dimensões de Layering

```
┌─────────────────────────────────────────────────┐
│  PLANO FRONT    → Tipo principal, CTA, dados    │
│  PLANO MIDDLE   → Cards, containers, UI chrome  │
│  PLANO BACK     → Background, texturas, grids   │
└─────────────────────────────────────────────────┘
```

### Técnicas Extraídas do Engine

| Técnica | Implementação |
|---|---|
| **Scale Contrast** | Elementos grandes no plano back criam profundidade sem z-index. |
| **Texture** | Ruído sutil, grains, ou padrões geométricos no fundo ancoram o plano back. |
| **CSS avançado** | `text-wrap: pretty`, CSS Grid, `mix-blend-mode`, `backdrop-filter` são permitidos e incentivados. |
| **oklch para harmonia** | Quando o design system é restritivo, use `oklch()` para derivar cores harmônicas sem inventar do zero. |
| **Fills vs. Strokes** | Varie entre elementos preenchidos e de contorno no mesmo plano para criar respiração. |

### Regra de Ouro
> Se todos os elementos parecem estar na mesma distância do olho, o design está **plano**. Layering = ilusão de distância focal.

---

## 🚫 III. ANTI-CLICHÊS — O Que Destrói a Credibilidade

> *"Evitar AI slop tropes"* — as marcas registradas de design gerado por IA sem critério.

### Lista Negra Oficial (Extraída Verbatim)

| ❌ Clichê | 💡 Alternativa Elite |
|---|---|
| Gradient backgrounds agressivos | Fundos sólidos, sutis; gradiente APENAS como acento |
| Emoji como decoração de UI | Ícones SVG personalizados, ou placeholder honesto |
| Container com `border-radius` + `border-left` colorida | Cards com profundidade real (sombra, escala, cor de fundo) |
| SVG tentando ser ilustração fotorrealista | Placeholder limpo + pedir material real ao usuário |
| Inter, Roboto, Arial, Fraunces, fontes de sistema | Fontes com caráter: Syne, DM Serif, Instrument, etc. |
| Seções de padding genéricas para "preencher" | **Zero filler content** — cada elemento ganha seu lugar |
| Stats/ícones/números decorativos ("data slop") | Só dados que têm função semântica real |

### Regra da Adição
> Antes de adicionar qualquer seção, ícone ou elemento novo: **perguntar ao usuário**. Ele conhece melhor o objetivo do que a IA.

### Filosofia Minimalista
> *"One thousand no's for every yes. Less is more."*

---

## 💾 IV. localStorage — PERSISTÊNCIA DE ESTADO

> *"Para conteúdo como decks e vídeos, torne a posição de reprodução persistente; armazene no localStorage sempre que mudar, e releia ao carregar."*

### Por Que Isso Importa
O `localStorage` resolve o problema do **refresh inconveniente** — o usuário recarrega a página durante iteração de design e perde o slide/posição. Eliminar isso é um sinal de design de produção.

### Padrão Básico (Posição de Playback)

```javascript
// SALVAR posição ao mudar
function onSlideChange(index) {
  localStorage.setItem('deck_slide_position', index);
  // notificar host se em iframe
  window.parent.postMessage({ slideIndexChanged: index }, '*');
}

// RESTAURAR ao carregar
window.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('deck_slide_position');
  if (saved !== null) goToSlide(parseInt(saved, 10));
});
```

### Padrão Avançado (Tweaks/Preferências de Design)

```javascript
// Defina defaults com markers especiais para reescrita automática pelo host
const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "primaryColor": "#D97757",
  "fontSize": 16,
  "dark": false
}/*EDITMODE-END*/;

// Merge com localStorage
const saved = JSON.parse(localStorage.getItem('tweaks') || '{}');
const config = { ...TWEAK_DEFAULTS, ...saved };

// Persistir ao mudar
function applyTweak(key, value) {
  config[key] = value;
  localStorage.setItem('tweaks', JSON.stringify(config));
  // Sincronizar com host (para reescrita em disco)
  window.parent.postMessage({
    type: '__edit_mode_set_keys',
    edits: { [key]: value }
  }, '*');
}
```

### O Protocolo de Tweaks (Ordem É Crítica)

```
⚠️ ORDEM IMPORTA — registrar listener ANTES de anunciar disponibilidade

1. window.addEventListener('message', handler)  ← PRIMEIRO
   - 'activate_edit_mode'   → mostrar painel Tweaks
   - 'deactivate_edit_mode' → ocultar painel Tweaks

2. window.parent.postMessage({ type: '__edit_mode_available' }, '*')  ← DEPOIS
   → Faz o toggle do toolbar aparecer
```

### Regras de Tweaks

- Painel pequeno: floating `bottom-right`, não uma barra lateral inteira.
- Ocultar completamente quando Tweaks está desligado — o design deve parecer **final**.
- Adicionar 2–3 tweaks por padrão, mesmo sem pedido — expõe possibilidades ao usuário.
- Usar para ciclagem de variantes: ao invés de múltiplos arquivos, um arquivo com toggle.

---

## 🔩 V. PADRÕES TÉCNICOS CRÍTICOS

### React + Babel (Versões Pinadas com Integridade)

```html
<script
  src="https://unpkg.com/react@18.3.1/umd/react.development.js"
  integrity="sha384-hD6/rw4ppMLGNu3tX5cjIb+uRZ7UkRJ6BPkLpg4hAu/6onKUg4lLsHAs9EBPT82L"
  crossorigin="anonymous"
></script>
<script
  src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js"
  integrity="sha384-u6aeetuaXnQ38mYT8rp6sbXaQe3NL9t+IBXmnYxwkUI2Hw4bsp2Wvmx4yRQF1uAm"
  crossorigin="anonymous"
></script>
<script
  src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js"
  integrity="sha384-m08KidiNqLdpJqLq95G/LEi8Qvjl/xUYll3QILypMoQ65QorJ9Lvtp2RXYGBFj1y"
  crossorigin="anonymous"
></script>
```

> ⚠️ **NUNCA** usar versões sem pin (ex: `react@18`). Sem `integrity` = risco de supply chain.

### Style Objects — Conflito de Escopo Global

```javascript
// ❌ PROIBIDO — causa colisão de escopo entre componentes
const styles = { container: { ... } }

// ✅ CORRETO — nome único baseado no componente
const terminalStyles = { container: { ... } }
const heroStyles = { wrapper: { ... } }
```

### Compartilhamento entre Arquivos Babel

```javascript
// Ao final de components.jsx — exportar para window
Object.assign(window, {
  Terminal, Line, Spacer,
  Gray, Blue, Green, Bold,
});
// Outros arquivos .jsx podem consumir via window.Terminal, etc.
```

### Fixed-Size Content (Decks/Vídeos)

```
Canvas fixo (padrão: 1920×1080 · 16:9)
  → Envolto em stage full-viewport
  → Letterboxed via transform: scale()
  → Controles FORA do elemento escalado
  → Gerenciamento via deck_stage.js (starter component)
```

---

## 🎯 VI. PROCESSO DE DESIGN — O Fluxo Correto

```
(1) Perguntar → Mínimo 10 perguntas para projetos novos
(2) Contexto → UI kit, design system, codebase, screenshot. SEM contexto = design ruim.
(3) Plano + Placeholder → Arquivo HTML com estrutura e placeholders. MOSTRAR CEDO.
(4) Componentes → Escrever React e embutir. MOSTRAR DE NOVO.
(5) Iterar → Verificar, corrigir, iterar.
```

### Regras de Variações
- Entregar **3+ variações** por exploração de design.
- Começar básico → escalar para criativo/avançado.
- Expor como **Tweaks** (não arquivos separados).
- Misturar: by-the-book + novel UX + interações avançadas.

### Contexto é Não-Negociável
> *"Mockar um produto do zero é ÚLTIMO RECURSO e leva a design ruim."*
> Sempre buscar: UI kit → codebase → screenshots → perguntar ao usuário.

---

## 🌈 VII. COR — Filosofia e Técnica

| Situação | Abordagem |
|---|---|
| Design system existente | Usar as cores do sistema. Ponto. |
| Sistema restritivo | Derivar com `oklch()` para harmonia automática. |
| Sem sistema | Invocar skill "Frontend design" antes de inventar. |
| Emoji | Somente se o design system usar. Caso contrário: **jamais**. |

### oklch para Derivação Harmônica
```css
/* Exemplo: criar variante mais clara de uma cor existente */
:root {
  --brand-primary: oklch(55% 0.18 240);
  --brand-light:   oklch(75% 0.12 240);  /* L+20, C-0.06 */
  --brand-dark:    oklch(35% 0.22 240);  /* L-20, C+0.04 */
}
```

---

## 📐 VIII. SLIDES/DECKS — Checklist de Produção

- [ ] Canvas 1920×1080, escalonado via JS para qualquer viewport
- [ ] `deck_stage.js` starter component (nunca hand-roll)
- [ ] `data-screen-label` em cada slide (1-indexed: "01 Title", "02 Agenda")
- [ ] Posição do slide salva no localStorage ao mudar
- [ ] `window.postMessage({ slideIndexChanged: N })` a cada mudança
- [ ] Speaker notes APENAS se explicitamente pedido
- [ ] Controles de navegação FORA do elemento escalado
- [ ] Print-to-PDF via deck_stage (uma página por slide)
- [ ] Fontes mínimas: 24px (nunca abaixo disso em slides)

---

## 🧩 IX. STARTER COMPONENTS — Referência Rápida

| Arquivo | Uso |
|---|---|
| `deck_stage.js` | Shell para qualquer apresentação de slides |
| `design_canvas.jsx` | Grid para apresentar 2+ opções estáticas lado a lado |
| `ios_frame.jsx` | Bezel iOS com status bar e teclado |
| `android_frame.jsx` | Bezel Android |
| `macos_window.jsx` | Chrome de janela macOS com traffic lights |
| `browser_window.jsx` | Chrome de browser com tab bar |
| `animations.jsx` | Engine de animação: Stage + Sprite + Easing + scrubber |

> 💡 **Regra:** Sempre preferir starter components a hand-roll. O componente retorna seu conteúdo completo para slots imediatos.

---

## ⚠️ X. ARMADILHAS E GOTCHAS

| Armadilha | Solução |
|---|---|
| `scrollIntoView()` | **Nunca usar** — quebra o web app. Usar outros métodos DOM. |
| `type="module"` em scripts | **Evitar** — pode quebrar imports. Usar `text/babel` ou script clássico. |
| Múltiplos `const styles` | Nomear especificamente por componente (ver seção V). |
| Títulos em protótipos | Resistir. Protótipo centered no viewport, sem tela de título. |
| Conteúdo filler | Zero tolerance. Cada elemento justifica sua existência. |
| Design sem contexto | Sempre buscar antes de inventar. |
| Slide 0-indexed no label | Labels são 1-indexed. "Slide 5" = label "05", não array[4]. |

---

## 📎 Metadados da Skill

```yaml
skill_id: claude-design-elite-v5
version: 5.0
created: 2026-04-21
source: design_raw.md (Claude Design System · 464 linhas)
extraction_method: full-read + thematic distillation
themes_extracted:
  - ritmo_visual
  - layering
  - anti_cliches
  - localStorage_persistence
  - technical_patterns
  - design_process
aplicação:
  - Protótipos HTML de alta fidelidade
  - Decks de apresentação
  - UI kits e design systems
  - Mockups interativos com Tweaks
tags: [design, html, react, localStorage, slides, ritmo-visual, layering, anti-ai-slop]
status: integrado-ao-cofre
```

---

> *"CSS, HTML, JS e SVG são incríveis. Os usuários geralmente não sabem o que eles podem fazer. Surpreenda o usuário."*
> — Claude Design System
