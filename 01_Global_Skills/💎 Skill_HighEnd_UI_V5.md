# 💎 Skill_HighEnd_UI_V5 — Elite Design Language Extraction
> **Sandbox:** `_SANDBOX_DESIGN/` | **Origem:** `awesome-design-md` (getdesign.md)
> **Marcas mineradas:** Airbnb · Apple · BMW · Ferrari · Lamborghini · Lovable · Minimax · Nvidia · Renault · Replicate · Resend · SpaceX · Spotify · Supabase · Tesla · Uber · Vercel · Wise
> **Data de extração:** 2026-04-12 | **Versão:** V5.0 — Nexus Edition

---

## 📑 ÍNDICE RÁPIDO

| # | Pilar | Marcas-âncora | Aplicação-alvo |
|---|-------|---------------|----------------|
| 1 | [Visual Luxo](#1-visual-luxo) | BMW · Ferrari · Lamborghini · SpaceX · Tesla | Nexus Luxury |
| 2 | [Minimalismo Tech](#2-minimalismo-tech) | Apple · Vercel · Resend · Replicate | Dashboard Ads |
| 3 | [UX de Engajamento](#3-ux-de-engajamento) | Spotify · Airbnb · Uber · Lovable | Ambos |
| 4 | [Trust & Clarity](#4-trust--clarity) | Wise · Supabase · Minimax · Nvidia · Renault | Dashboard Ads |

---

## 1. VISUAL LUXO
> **Essência:** Pretos profundos + tipografia técnica + grids amplos + fotografia cinematográfica

### 🏎️ Ferrari
- **Identidade:** Chiaroscuro editorial — contraste dramatico luz/sombra no layout
- **Cor-âncora:** `#CC0000` (Ferrari Red) sobre fundos `#0A0A0A` (cinematic black)
- **Tipografia:** Serifas condensadas para headlines + fonte sans técnica para dados
- **Grid:** Assimétrico — imagem ocupa 60–70% da viewport; texto flutua sobre a foto
- **Micro-padrão:** Linha vermelho-fino como divisor horizontal (`border-top: 1px solid #CC0000`)
- **Aplicação:** Hero sections com overlay gradiente `rgba(0,0,0,0.65)` sobre foto full-bleed

### 🐂 Lamborghini
- **Identidade:** Brutalismo de luxo — preto absoluto (`#000000`) sem concessões
- **Cor-âncora:** Gold `#D4AF37` / `#C9A227` como único acento cromático
- **Tipografia:** **TODAS LETRAS MAIÚSCULAS** — tracking wide (`letter-spacing: 0.15em`)
- **Grid:** Colunas ultra-amplas (12-col) com gutters generosos (`gap: 80px+`)
- **Micro-padrão:** Bordas gold com `1–2px` de espessura; sem gradientes suaves
- **CSS Token:**
  ```css
  --bg-primary: #000000;
  --accent-gold: #D4AF37;
  --text-hero: uppercase, tracking: 0.15em;
  --border-luxury: 1px solid #D4AF37;
  ```

### 🚗 BMW
- **Identidade:** Engenharia alemã — precisão visual, superfícies escuras premium
- **Paleta:** `#1C1C1C` (surface) · `#2D2D2D` (card) · `#0066CC` (BMW blue accent)
- **Tipografia:** Sem-serif geométrica (BMW Type / alternativa: `Neue Haas Grotesk`)
- **Grid:** Espaçamento rigoroso — múltiplos de 8px; nunca pixels arbitrários
- **Padrão:** Hero em duplo painel — produto à direita, especificações técnicas à esquerda
- **Detalhe premium:** Uso de `backdrop-filter: blur(20px)` em overlays sobre foto de carro

### 🚀 SpaceX
- **Identidade:** Minimalismo extremo do espaço — preto/branco absolutos, sem cor
- **Paleta:** `#000000` + `#FFFFFF` — zero tons intermediários no brand primário
- **Tipografia:** `font-family: 'D-DIN', 'Inter', sans-serif` — técnica, condensada, caps
- **Grid:** Full-viewport — `height: 100vh` em cada seção; scroll snap entre painéis
- **Micro-padrão:** Texto aparece sobre imagem com `mix-blend-mode: difference` ou overlay puro
- **Fotografia:** Full-bleed sem cropping — a imagem **é** o design; UI fica acima com z-index
- **CSS Token:**
  ```css
  --bg: #000000;
  --text: #FFFFFF;
  --section-height: 100vh;
  --font-hero-size: clamp(3rem, 8vw, 7rem);
  scroll-snap-type: y mandatory;
  ```

### ⚡ Tesla
- **Identidade:** Radical subtração — o produto fala; a UI desaparece
- **Princípio:** "Near-zero UI" — apenas CTA e headline visíveis; tudo mais some no scroll
- **Paleta:** Quase monocromático; `#171A20` para dark mode; branco puro para light
- **Tipografia:** `font-weight: 300` (ultralight) para headlines — elegância por leveza
- **Grid:** `100vw × 100vh` por seção; padding lateral mínimo (`5vw`)
- **Padrão-chave:** Dois CTAs lado a lado (`Encomendar agora` | `Saiba mais`) — sempre no bottom da hero
- **Micro-animação:** Fade-in suave do texto ao entrar no viewport (`opacity: 0 → 1, 0.8s ease`)

---

## 2. MINIMALISMO TECH
> **Essência:** Sombras suaves + micro-bordas + tipografia funcional como hero visual

### 🍎 Apple
- **Identidade:** Premium white space — o espaço vazio é um elemento de design
- **Paleta:** `#FFFFFF` (hero) · `#F5F5F7` (section bg) · `#1D1D1F` (text) · `#0071E3` (blue CTA)
- **Tipografia:** `SF Pro Display` → fallback: `'Inter', system-ui` | `font-weight: 600–700` para headline; `300` para suporte
- **Grid:** Centralizado, max-width `980px`; nada toca as bordas — padding lateral `5–8%`
- **Sombra padrão:**
  ```css
  box-shadow: 0 4px 24px rgba(0,0,0,0.08);
  border-radius: 18px; /* Apple card radius */
  ```
- **Micro-padrão:** Sticky nav com `backdrop-filter: saturate(180%) blur(20px)` + fundo semi-transparente
- **Regra de ouro:** Uma única imagem de produto, centrada, sem distrações. Texto acima ou abaixo, nunca sobreposto.

### ▲ Vercel
- **Identidade:** Frontend precision — preto/branco como filosofia, não paleta
- **Fonte:** `Geist` (própria) → fallback: `'Inter', 'Helvetica Neue'`
- **Paleta dark:** `#000000` base · `#111111` card · `#333333` border · `#FFFFFF` texto
- **Paleta light:** `#FFFFFF` base · `#F2F2F2` section · `#EBEBEB` border
- **Micro-borda:** `border: 1px solid rgba(255,255,255,0.1)` — quase invisível, mas presente
- **Hover state:** `background: rgba(255,255,255,0.05)` — transição `150ms ease`
- **Padrão code-block:** Monospace com fundo `#0A0A0A`, syntax highlighting minimalista
- **CTA primário:**
  ```css
  background: #FFFFFF; color: #000000;
  padding: 10px 20px; border-radius: 6px;
  font-weight: 500; font-size: 14px;
  ```

### 📧 Resend
- **Identidade:** Developer-first dark — ferramenta poderosa com face clean
- **Paleta:** `#0A0A0A` bg · `#161616` card · `#262626` border · `#EDEDED` text primário
- **Tipografia:** Monospace para código (`'JetBrains Mono'`, `'Fira Code'`); sans para prosa
- **Micro-acento:** `#FFFFFF` puro — sem cores de acento; hierarquia = contraste de peso
- **Padrão:** Cards com código ao lado direito — split layout `50/50`
- **Border-radius:** `8px` para cards, `4px` para inputs — nunca `0px`, nunca `>12px`

### 🔄 Replicate
- **Identidade:** API-primeiro, canvas limpo — deixa o output falar
- **Paleta:** `#FFFFFF` dominante; acento `#000000`; cinza `#F0F0F0` para sections
- **Padrão:** Dashboard de modelo com preview à direita + controles à esquerda
- **Tipografia:** Sans-serif neutra — foco total no conteúdo gerado, não no chrome
- **Grid:** `prose-max-width: 680px` para conteúdo técnico; sem linhas desnecessárias

---

## 3. UX DE ENGAJAMENTO
> **Essência:** Cards visuais + navegação contextual + feedback visual imediato

### 🎵 Spotify
- **Identidade:** Imersão sonora — dark com cor vibrante emergindo do conteúdo
- **Paleta:** `#121212` bg · `#1DB954` (Spotify Green) · `#282828` card · `#B3B3B3` text-secondary
- **Card pattern:**
  ```css
  .card {
    background: #282828;
    border-radius: 6px;
    padding: 16px;
    transition: background 0.2s ease;
  }
  .card:hover { background: #3E3E3E; }
  ```
- **Navegação:** Sidebar fixa + conteúdo scrollável à direita (split layout permanente)
- **Hierarchy visual:** Artwork/imagem grande → título bold → metadados pequenos
- **Feedback:** Play button aparece no hover do card (opacity: 0 → 1 + translateY(-8px))
- **Grid:** `auto-fill` com `minmax(180px, 1fr)` para grid de cards

### 🏠 Airbnb
- **Identidade:** Warmth photography-driven — a foto vende, o UI suporta
- **Paleta:** `#FF5A5F` (Rausch/coral) · `#FFFFFF` · `#717171` (gray) · `#222222` (text)
- **Card pattern:** Imagem full-width com `border-radius: 12px` + info embaixo
- **Tipografia:** `Circular` (própria) → fallback: `'Inter', sans-serif` — peso `400/600`
- **Filtros/tabs:** Pills horizontais scrolláveis — `overflow-x: auto; scroll-snap-type: x mandatory`
- **Trust signal:** Avatar + rating + review count sempre visíveis no card
- **Micro-animação:** Coração (save) faz pulse ao clicar — `animation: heartbeat 0.3s ease`

### 🚕 Uber
- **Identidade:** Urban monochrome — energia da cidade em preto e branco absolutos
- **Paleta:** `#000000` · `#FFFFFF` · `#276EF1` (Uber blue para CTAs) · `#F6F6F6` (bg-light)
- **Tipografia:** `UberMove` → fallback: `'Inter', sans-serif` — tracking tight (-0.02em)
- **Hero:** Headline ultra-bold (`font-weight: 900`) + fundo branco + bottom CTA
- **Cards de serviço:** Ícone + label + preço estimado — layout limpo, sem ornamentos
- **Padrão de mapa:** Semi-opaco sobre fundo — dados surgem em tooltips contextuais
- **CTA pattern:** Botão preto full-width no mobile; pair de botões no desktop

### 💜 Lovable
- **Identidade:** Friendly gradient SaaS — acessível sem ser infantil
- **Paleta:** Gradiente `#7C3AED → #DB2777` · bg `#FAFAFA` · text `#111827`
- **Estilo de UI:** Glassmorphism suave — `backdrop-filter: blur(16px)` + `background: rgba(255,255,255,0.7)`
- **Bordas:** `border: 1px solid rgba(124,58,237,0.2)` — purple tint
- **Hero:** Gradiente animado no background (`@keyframes gradient-shift`) + headline bold
- **CTA primário:** Gradiente `linear-gradient(135deg, #7C3AED, #DB2777)` com `box-shadow` colorido

---

## 4. TRUST & CLARITY
> **Essência:** Paletas sólidas + hierarquia de dados + feedback financeiro imediato

### 💚 Wise
- **Identidade:** Fintech amigável — clareza como luxo; verde que transmite crescimento e segurança
- **Paleta:** `#00B9A7` (Wise Teal/Green) · `#FFFFFF` · `#163300` (dark text) · `#F8F8F8` (bg)
- **Tipografia:** `'Inter'`, `font-size: 16px` base, `line-height: 1.6` — máxima legibilidade
- **Data display:**
  ```css
  .exchange-rate {
    font-size: 2.5rem;
    font-weight: 700;
    color: #163300;
  }
  .fee-highlight {
    color: #00B9A7;
    font-weight: 600;
  }
  ```
- **Trust signals:** Ícone de escudo + texto de garantia — sempre visíveis acima do CTA
- **Padrão de comparação:** Tabela lado a lado COM vs SEM — verde para ganho do usuário
- **Progress step:** Indicador horizontal de passos numerados — sempre mostra onde o user está

### 🟢 Supabase
- **Identidade:** Dark emerald dev-tool — código como estética, não como necessidade
- **Paleta:** `#1C1C1C` bg · `#3ECF8E` (emerald accent) · `#252525` card · `#EDEDED` text
- **Code highlight:**
  ```css
  pre { background: #1A1A1A; border: 1px solid #2E2E2E; border-radius: 8px; }
  .token-string { color: #3ECF8E; }
  .token-keyword { color: #61AFEF; }
  ```
- **Dashboard layout:** Left nav escura + conteúdo principal claro — alto contraste de zona
- **Tabela de dados:**
  - Header: `background: #1E1E1E; color: #A1A1AA`
  - Row hover: `background: rgba(62,207,142,0.05)`
  - Zebra: alternância sutil `#1C1C1C / #202020`
- **Padrão de status:** Badge colorido — `green/yellow/red` com fundo `rgba` + texto bold

### ⚡ Nvidia
- **Identidade:** GPU power aesthetic — energia verde-preta que comunica performance
- **Paleta:** `#000000` · `#76B900` (Nvidia Green) · `#1A1A1A` card · `#E2E2E2` text
- **Hero pattern:** Imagem de hardware + overlay verde-escuro `rgba(118,185,0,0.15)` + specs em grid
- **Dado técnico:**
  ```css
  .spec-number {
    font-size: 3rem; font-weight: 800;
    color: #76B900; /* o número GRITA */
  }
  .spec-label {
    font-size: 0.75rem; text-transform: uppercase;
    letter-spacing: 0.1em; color: #A0A0A0;
  }
  ```
- **Grid de specs:** 3–4 colunas com números grandes — comparações visuais por tamanho de fonte

### 🌊 Minimax
- **Identidade:** AI neon-on-dark — capacidade do modelo como espetáculo visual
- **Paleta:** `#0D0D0D` bg · neon `#00D2FF` / `#7B2FFF` · `#1A1A2E` surface
- **Efeito neon:**
  ```css
  .neon-text {
    color: #00D2FF;
    text-shadow: 0 0 20px rgba(0,210,255,0.7), 0 0 40px rgba(0,210,255,0.3);
  }
  ```
- **Padrão de showcase:** Demo interativo de output do modelo — ocupa 50%+ da viewport

### 🌊 Renault
- **Identidade:** Aurora gradients — energia francesa vibrante e dinâmica
- **Paleta:** Gradiente `#FF6B35 → #FF1B6D → #45CAFF` (aurora) em fundos hero
- **Tipografia:** `NouvelR` (custom) → fallback: `'Outfit', 'Inter'` — geométrico bold
- **Padrão de cor:** Monocromático no corpo do texto; aurora apenas em hero e CTAs
- **Hover de CTA:** Gradiente animado `background-size: 200%` com `background-position` em transição

---

## 5. TOKENS UNIVERSAIS DE ELITE
> Destilados dos 18 design systems — aplicação cross-projeto

### Paletas Extraídas por Categoria

```css
/* ── LUXO AUTOMOTIVO ── */
--luxury-true-black: #000000;       /* Lamborghini */
--luxury-ferrari-red: #CC0000;      /* Ferrari */
--luxury-cinematic-bg: #0A0A0A;    /* Ferrari/SpaceX */
--luxury-gold: #D4AF37;             /* Lamborghini */
--luxury-bmw-blue: #0066CC;         /* BMW */
--luxury-bmw-surface: #1C1C1C;     /* BMW */

/* ── TECH MINIMAL ── */
--tech-bg-dark: #000000;            /* Vercel/SpaceX */
--tech-surface: #111111;            /* Vercel */
--tech-border: rgba(255,255,255,0.1); /* Vercel */
--tech-apple-bg: #F5F5F7;          /* Apple */
--tech-apple-blue: #0071E3;         /* Apple CTA */
--tech-resend-surface: #161616;    /* Resend */

/* ── ENGAJAMENTO ── */
--engage-spotify-green: #1DB954;   /* Spotify */
--engage-spotify-card: #282828;    /* Spotify */
--engage-airbnb-coral: #FF5A5F;    /* Airbnb */
--engage-uber-blue: #276EF1;       /* Uber */
--engage-lovable-purple: #7C3AED;  /* Lovable */

/* ── TRUST / DADOS ── */
--trust-wise-teal: #00B9A7;        /* Wise */
--trust-supabase-green: #3ECF8E;   /* Supabase */
--trust-nvidia-green: #76B900;     /* Nvidia */
--trust-minimax-neon: #00D2FF;     /* Minimax */
```

### Tipografia de Elite por Categoria

| Categoria | Fonte primária | Fallback seguro | Peso hero | Peso corpo |
|-----------|----------------|-----------------|-----------|------------|
| Luxo | custom serifada | `Playfair Display` | 700 | 300 |
| Tech minimal | `Geist` / `SF Pro` | `Inter` | 600 | 400 |
| Engajamento | `Circular` | `Inter` | 700 | 400 |
| Trust/Dados | `Inter` | `system-ui` | 600 | 400 |

### Sombras e Elevação Padrão

```css
/* Nível 1 — sutil (Apple, Wise) */
--shadow-1: 0 2px 8px rgba(0,0,0,0.06);

/* Nível 2 — card hover (Airbnb, Spotify) */
--shadow-2: 0 8px 24px rgba(0,0,0,0.12);

/* Nível 3 — modal/premium (BMW, Vercel) */
--shadow-3: 0 20px 60px rgba(0,0,0,0.25);

/* Luxo — glow de acento (Lamborghini, Minimax) */
--shadow-luxury: 0 0 30px rgba(212,175,55,0.3);
--shadow-neon: 0 0 20px rgba(0,210,255,0.5);
```

### Border Radius por Personalidade

```css
--radius-zero:    0px;       /* SpaceX, Tesla — zero concessão */
--radius-micro:   4px;       /* Resend, Vercel — developer precision */
--radius-standard: 8px;      /* Supabase, BMW — balanced */
--radius-friendly: 12px;     /* Airbnb, Wise — approachable */
--radius-bold:    18px;      /* Apple — signature premium */
--radius-pill:    9999px;    /* Spotify pills, Uber CTAs */
```

---

## 6. PADRÕES DE COMPONENTE EXTRAÍDOS

### Hero Section — 3 Arquétipos

```
ARQUÉTIPO 1: CINEMATIC (Ferrari/SpaceX/Tesla)
┌─────────────────────────────────────────┐
│  [FOTO FULL-BLEED 100vh]                │
│                                          │
│                                          │
│  H1: TEXTO SOBRE IMAGEM                 │
│  Subtítulo leve                          │
│  [CTA 1]  [CTA 2]                       │
└─────────────────────────────────────────┘

ARQUÉTIPO 2: PRODUCT FOCUS (Apple/Tesla)
┌─────────────────────────────────────────┐
│  H1 centrado bold                        │
│  Subtítulo cinza claro                  │
│  [CTA primário]  [link secundário]      │
│                                          │
│  [PRODUTO FOTO CENTRALIZADA]            │
└─────────────────────────────────────────┘

ARQUÉTIPO 3: SPLIT LAYOUT (BMW/Vercel/Resend)
┌──────────────┬──────────────────────────┐
│ Texto +      │  Foto / Demo / Code      │
│ specs +      │  Preview                 │
│ CTAs         │                          │
└──────────────┴──────────────────────────┘
```

### Card Pattern — DNA de Cada Marca

```css
/* Spotify card — dark immersive */
.card-spotify {
  background: #282828; border-radius: 6px;
  padding: 16px; cursor: pointer;
  transition: background 0.2s ease;
}
.card-spotify:hover { background: #3E3E3E; }

/* Airbnb card — warm photography */
.card-airbnb {
  border-radius: 12px; overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card-airbnb:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

/* Vercel card — precision dark */
.card-vercel {
  background: #111; border: 1px solid #333;
  border-radius: 8px; padding: 24px;
  transition: border-color 0.15s ease;
}
.card-vercel:hover { border-color: #555; }

/* Supabase card — emerald trust */
.card-supabase {
  background: #252525; border: 1px solid #2E2E2E;
  border-radius: 8px; padding: 20px;
}
.card-supabase:hover { border-color: #3ECF8E; }
```

---

## 7. 🎯 AUDITOR TÉCNICO — Aplicabilidade nos Projetos

### 📊 Pontuação por Projeto

#### Nexus Luxury (E-commerce de Moda Masculina Premium)

| Pilar Design | Marca-referência | Score | Recomendação |
|---|---|---|---|
| Paleta de Luxo | Lamborghini + Ferrari | **10/10** | **Adotar imediatamente** — preto `#000` + gold `#D4AF37` |
| Tipografia | BMW + SpaceX | **9/10** | Uppercase tracking wide para headlines + serifada fina para corpo |
| Hero Cinematográfico | Tesla + Ferrari | **10/10** | Full-viewport foto do produto; UI mínima |
| Cards de Produto | Airbnb (adaptado dark) | **8/10** | Card escuro com hover translateY + imagem full-width |
| Trust Signal | Wise (adaptado) | **7/10** | Stars + avaliações + badge "verificado" — adaptar paleta para gold |
| Navegação | Uber (adaptado) | **8/10** | Navbar minimal sticky com backdrop-blur sobre foto |

**Nota Geral — Nexus Luxury:** `⭐ 9.0/10 — ALTAMENTE APLICÁVEL`

> **Estratégia recomendada:** Stack Ferrari (chiaroscuro editorial) + Lamborghini (gold accent + uppercase) + Tesla (near-zero UI) = identidade "Ultra-Luxo Editorial" que posiciona o produto como investimento, não compra.

---

#### DASHBOARD DE ADS (Facebook Ads Analytics)

| Pilar Design | Marca-referência | Score | Recomendação |
|---|---|---|---|
| Layout de Dados | Supabase + Nvidia | **10/10** | **Adotar como base** — emerald accent para KPIs positivos |
| Tabelas/Grids | Supabase | **10/10** | Header escuro + row hover rgba(verde, 0.05) |
| KPI Numbers | Nvidia | **9/10** | Número grande verde + label uppercase tracking |
| Sidebar Nav | Spotify | **9/10** | Sidebar fixa escura + conteúdo scrollável |
| Filtros/Tabs | Airbnb pills | **8/10** | Pill scrollável horizontal para seleção de período |
| CTAs | Vercel | **9/10** | CTA branco em fundo preto — máximo contraste |
| Status Badges | Supabase | **10/10** | Verde/Amarelo/Vermelho com fundo rgba — ROAS positive/neutral/negative |
| Alertas/Insights | MiniMax (neon adaptado) | **7/10** | Neon highlight para insights críticos — usar com moderação |
| Comparações | Wise (tabela side-by-side) | **9/10** | Linha "vs período anterior" verde para gain, vermelho para loss |

**Nota Geral — Dashboard de Ads:** `⭐ 9.3/10 — EXCEPCIONAL FIT`

> **Estratégia recomendada:** Stack Supabase (dark emerald base) + Nvidia (números de poder) + Spotify (layout sidebar+conteúdo) + Wise (comparações claras de dados financeiros) = Dashboard que comunica performance de forma visceral e confiável.

---

### 🔁 Matriz de Cruzamento — O Que Usar Onde

```
                    Nexus Luxury    DASHBOARD ADS
Ferrari chiaroscuro      ████████░░          ░░░░░░░░░░
Lamborghini gold         █████████░          ░░░░░░░░░░
BMW dark surfaces        ███████░░░          ███████░░░
SpaceX full-bleed        ████████░░          ░░░░░░░░░░
Tesla minimal CTA        ████████░░          ██████░░░░
Apple white space        ░░░░░░░░░░          ██████░░░░
Vercel B&W precision     ████░░░░░░          █████████░
Resend dark minimal      ░░░░░░░░░░          ████████░░
Replicate clean canvas   ░░░░░░░░░░          ██████░░░░
Spotify sidebar          ██░░░░░░░░          █████████░
Airbnb cards warm        ████░░░░░░          ██████░░░░
Uber monochrome          ██████░░░░          ████░░░░░░
Lovable gradients        ░░░░░░░░░░          ███░░░░░░░
Wise trust/clarity       ██████░░░░          █████████░
Supabase emerald data    ░░░░░░░░░░          █████████░
Nvidia power numbers     ░░░░░░░░░░          █████████░
Minimax neon             ░░░░░░░░░░          ████░░░░░░
Renault aurora           ░░░░░░░░░░          ███░░░░░░░
```

---

## 8. CSS QUICK-START — IMPLEMENTAÇÃO IMEDIATA

### Para Nexus Luxury (Luxo Editorial)

```css
:root {
  /* === PALETA LUXO === */
  --bg-void: #000000;
  --bg-surface: #0A0A0A;
  --bg-card: #141414;
  --accent-gold: #D4AF37;
  --accent-red: #CC0000;
  --text-primary: #F5F5F0;
  --text-muted: #888888;
  --border-luxury: rgba(212,175,55,0.25);

  /* === TIPOGRAFIA === */
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --tracking-luxury: 0.12em;
  --tracking-brand: 0.2em;

  /* === SPACING === */
  --section-pad: clamp(60px, 10vw, 120px);
  --max-width: 1280px;

  /* === ELEVAÇÃO === */
  --shadow-gold: 0 0 40px rgba(212,175,55,0.15);
  --shadow-card: 0 20px 60px rgba(0,0,0,0.5);
}

/* Hero cinematográfico */
.hero {
  height: 100vh;
  background: var(--bg-void);
  position: relative;
  overflow: hidden;
}
.hero img {
  width: 100%; height: 100%;
  object-fit: cover;
  opacity: 0.7;
}
.hero-text {
  position: absolute; bottom: 8vh; left: 6vw;
  color: var(--text-primary);
}
.hero-title {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 6vw, 5.5rem);
  font-weight: 700;
  letter-spacing: var(--tracking-luxury);
  text-transform: uppercase;
}
```

### Para Dashboard de Ads (Emerald Dark Data)

```css
:root {
  /* === PALETA DATA === */
  --bg-app: #0F0F0F;
  --bg-sidebar: #141414;
  --bg-surface: #1A1A1A;
  --bg-card: #222222;
  --accent-emerald: #3ECF8E;
  --accent-positive: #3ECF8E;
  --accent-negative: #F97066;
  --accent-neutral: #F0B429;
  --text-primary: #EDEDED;
  --text-secondary: #A1A1AA;
  --border-subtle: rgba(255,255,255,0.06);
  --border-accent: rgba(62,207,142,0.3);

  /* === KPI CONFIG === */
  --kpi-number-size: clamp(2rem, 4vw, 3.5rem);
  --kpi-label-size: 0.7rem;
  --kpi-label-tracking: 0.1em;
}

/* KPI Card — estilo Nvidia/Supabase */
.kpi-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: 20px 24px;
  transition: border-color 0.2s ease;
}
.kpi-card:hover { border-color: var(--border-accent); }
.kpi-number {
  font-size: var(--kpi-number-size);
  font-weight: 800;
  color: var(--accent-emerald);
  line-height: 1;
}
.kpi-label {
  font-size: var(--kpi-label-size);
  text-transform: uppercase;
  letter-spacing: var(--kpi-label-tracking);
  color: var(--text-secondary);
  margin-top: 6px;
}

/* Status badge pattern — Supabase */
.badge-positive { background: rgba(62,207,142,0.1); color: #3ECF8E; }
.badge-negative { background: rgba(249,112,102,0.1); color: #F97066; }
.badge-neutral  { background: rgba(240,180,41,0.1);  color: #F0B429; }
```

---

## 9. FONTES & REFERÊNCIAS

| Marca | URL Fonte | Padrão-chave extraído |
|-------|-----------|----------------------|
| Airbnb | getdesign.md/airbnb | Warm coral, photography-driven, rounded |
| Apple | getdesign.md/apple | White space + SF Pro + cinematic |
| BMW | getdesign.md/bmw | Dark premium + German precision |
| Ferrari | getdesign.md/ferrari | Chiaroscuro + Ferrari Red + cinematic black |
| Lamborghini | getdesign.md/lamborghini | True black + gold + dramatic uppercase |
| Lovable | getdesign.md/lovable | Playful gradients + friendly dev |
| Minimax | getdesign.md/minimax | Bold dark + neon accents |
| Nvidia | getdesign.md/nvidia | Green-black energy + power numbers |
| Renault | getdesign.md/renault | Aurora gradients + NouvelR + bold |
| Replicate | getdesign.md/replicate | Clean white canvas + code-forward |
| Resend | getdesign.md/resend | Minimal dark + monospace accents |
| SpaceX | getdesign.md/spacex | Stark B&W + full-bleed + futuristic |
| Spotify | getdesign.md/spotify | Vibrant green-on-dark + album-art |
| Supabase | getdesign.md/supabase | Dark emerald + code-first |
| Tesla | getdesign.md/tesla | Radical subtraction + full-viewport |
| Uber | getdesign.md/uber | Bold B&W + tight type + urban |
| Vercel | getdesign.md/vercel | B&W precision + Geist font |
| Wise | getdesign.md/wise | Bright green + friendly + clear data |

---

*💎 Skill_HighEnd_UI_V5 — Nexus Edition | Extração


