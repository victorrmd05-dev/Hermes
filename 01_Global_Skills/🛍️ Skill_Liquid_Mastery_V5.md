---
name: skill-liquid-mastery-v5
description: >
  Skill_Liquid_Mastery_V5.md
---

# Skill_Liquid_Mastery_V5.md
> Protocolo de Extração V5.0 | Fonte: skills/liquid-templating + theme-development

---

## 🏗️ ARQUITETURA DO TEMA

### Hierarquia de Componentes
```
Layout (theme.liquid) → Template (product.json) → Sections → Blocks → Snippets
```

### Estrutura de Diretórios
```
theme/
├── assets/      # CSS, JS, imagens, fontes (.css, .js, .svg)
├── config/      # settings_schema.json + settings_data.json
├── layout/      # theme.liquid (OBRIGATÓRIO), password.liquid
├── locales/     # en.default.json, fr.json, pt-BR.json
├── sections/    # Módulos customizáveis (com {% schema %})
├── snippets/    # Reutilizáveis via {% render %}
└── templates/   # JSON ou Liquid por tipo de página
```

### Layout Base (theme.liquid)
```liquid
<!DOCTYPE html>
<html lang="{{ request.locale.iso_code }}">
<head>
  <title>{{ page_title }}</title>
  {{ content_for_header }}
  {{ 'style.css' | asset_url | stylesheet_tag }}
</head>
<body>
  {% sections 'header-group' %}
  <main>{{ content_for_layout }}</main>
  {% sections 'footer-group' %}
</body>
</html>
```

---

## 🌍 OBJETOS GLOBAIS

### Shop & Request
```liquid
{{ shop.name }} {{ shop.email }} {{ shop.domain }}
{{ shop.currency }} {{ shop.money_format }}
{{ request.locale.iso_code }} {{ request.page_type }} {{ request.path }}
{{ settings.primary_color }}  {# settings_schema.json #}
```

### Produto
```liquid
{{ product.title }} {{ product.description }} {{ product.vendor }}
{{ product.price | money }} {{ product.compare_at_price | money }}
{{ product.available }} {{ product.url }} {{ product.tags | join: ', ' }}
{{ product.featured_image | image_url: width: 500 | image_tag }}
{{ product.metafields.custom.care_instructions }}

{% for variant in product.variants %}
  {{ variant.title }} — {{ variant.price | money }} (SKU: {{ variant.sku }})
{% endfor %}
{% for image in product.images %}
  {{ image | image_url: width: 300 | image_tag }}
{% endfor %}
```

### Collection
```liquid
{{ collection.title }} {{ collection.products_count }}
{% paginate collection.products by 12 %}
  {% for product in collection.products %}
    {% render 'product-card', product: product %}
  {% endfor %}
  {{ paginate | default_pagination }}
{% endpaginate %}
```

### Cart
```liquid
{{ cart.item_count }} {{ cart.total_price | money }}
{% for item in cart.items %}
  {{ item.product.title }} × {{ item.quantity }} = {{ item.line_price | money }}
{% endfor %}
{{ cart.attributes.gift_message }}
```

### Customer
```liquid
{% if customer %}
  Olá, {{ customer.first_name }}! | {{ customer.orders_count }} pedidos
  {{ customer.total_spent | money }}
{% else %}
  <a href="/account/login">Entrar</a>
{% endif %}
```

---

## 🔧 FILTROS ESSENCIAIS

### String
```liquid
{{ 'hello' | upcase }}        → HELLO
{{ 'HELLO' | downcase }}      → hello
{{ 'hello world' | truncate: 8 }} → hello...
{{ 'hello' | append: ' world' }} → hello world
{{ 'hello' | replace: 'e', 'a' }} → hallo
{{ 'hello world' | split: ' ' | first }} → hello
```

### Número / Dinheiro
```liquid
{{ 4.567 | round: 2 }}       → 4.57
{{ product.price | money }}                    → R$ 19,99
{{ product.price | money_with_currency }}      → R$ 19,99 BRL
{{ product.price | money_without_trailing_zeros }} → R$ 20
{{ 5 | plus: 3 }} | {{ 10 | divided_by: 2 }} | {{ 10 | modulo: 3 }}
```

### Array
```liquid
{{ array | first }} | {{ array | last }} | {{ array | size }}
{{ products | map: 'title' | join: ', ' }}
{{ products | where: 'available', true }}
{{ array | sort: 'price' | reverse }}
{{ array | concat: other_array | uniq | compact }}
```

### Imagem (Moderna — Recomendada)
```liquid
{{ image | image_url: width: 800 }}
{{ image | image_url: width: 800, height: 600, crop: 'center' }}

{# Responsiva com lazy load #}
{{ image | image_url: width: 1200 | image_tag:
  loading: 'lazy',
  widths: '300, 600, 900, 1200',
  sizes: '(max-width: 600px) 100vw, 50vw',
  alt: product.title
}}
```

### URL
```liquid
{{ 'style.css' | asset_url | stylesheet_tag }}
{{ 'app.js' | asset_url | script_tag }}
{{ product.url | within: collection }}
{{ 'general.cart' | t }}  {# tradução #}
```

---

## 🔀 CONTROLE DE FLUXO

### Condicionais
```liquid
{% if product.available %}
  Em Estoque
{% elsif product.compare_at_price %}
  Em Promoção
{% else %}
  Esgotado
{% endif %}

{% unless product.available %}Esgotado{% endunless %}

{% case product.type %}
  {% when 'Camisa' %} É uma camisa!
  {% when 'Calça' %} São calças!
  {% else %} Tipo desconhecido
{% endcase %}
```

### Operadores
```liquid
{% if product.price > 1000 and product.available %}
{% if product.tags contains 'sale' %}
{% if product.title == blank %}    {# verifica vazio #}
```

### For Loop
```liquid
{% for product in collection.products limit: 4 offset: 2 %}
  {{ forloop.index }} / {{ forloop.length }}  {# 1, 2... / total #}
  {% if forloop.first %}Primeiro!{% endif %}
  {% if forloop.last %}Último!{% endif %}
{% else %}
  Nenhum produto encontrado.
{% endfor %}

{# Cycle para classes alternadas #}
{% for product in collection.products %}
  <div class="{% cycle 'odd', 'even' %}">{{ product.title }}</div>
{% endfor %}
```

---

## 🧩 SNIPPETS & SECTIONS

### Render (Use SEMPRE em vez de include)
```liquid
{% render 'product-card' %}
{% render 'product-card', product: product, show_price: true %}
{% render 'product-card' for collection.products as product %}
```

### Section com Schema
```liquid
{% schema %}
{
  "name": "Coleção em Destaque",
  "settings": [
    { "type": "collection", "id": "collection", "label": "Coleção" },
    { "type": "range", "id": "products_to_show", "min": 2, "max": 12, "default": 4, "label": "Qtd. produtos" }
  ],
  "presets": [{ "name": "Coleção em Destaque" }]
}
{% endschema %}

<section>
  {% for product in section.settings.collection.products limit: section.settings.products_to_show %}
    {% render 'product-card', product: product %}
  {% endfor %}
</section>
```

### Blocks (Drag & Drop no Editor)
```liquid
{% schema %}
{
  "blocks": [{
    "type": "slide", "name": "Slide",
    "settings": [
      { "type": "image_picker", "id": "image", "label": "Imagem" },
      { "type": "text", "id": "heading", "label": "Título" }
    ]
  }]
}
{% endschema %}

{% for block in section.blocks %}
  <div {{ block.shopify_attributes }}>
    <img src="{{ block.settings.image | image_url: width: 1920 }}">
    <h2>{{ block.settings.heading }}</h2>
  </div>
{% endfor %}
```

---

## ⚡ PADRÕES AVANÇADOS

### Badge de Promoção
```liquid
{% if product.compare_at_price > product.price %}
  {% assign savings = product.compare_at_price | minus: product.price %}
  {% assign percent_off = savings | times: 100.0 | divided_by: product.compare_at_price | round %}
  <span class="badge-sale">{{ percent_off }}% OFF</span>
{% endif %}
```

### Seletor de Variante
```liquid
{% unless product.has_only_default_variant %}
  {% for option in product.options_with_values %}
    <label>{{ option.name }}</label>
    <select name="options[{{ option.name }}]">
      {% for value in option.values %}
        <option value="{{ value }}">{{ value }}</option>
      {% endfor %}
    </select>
  {% endfor %}
{% endunless %}
```

### Classes Condicionais
```liquid
{% assign classes = 'product' %}
{% if product.available == false %}{% assign classes = classes | append: ' sold-out' %}{% endif %}
{% if product.compare_at_price > product.price %}{% assign classes = classes | append: ' on-sale' %}{% endif %}
<div class="{{ classes }}">
```

### Formulário de Produto (Rápido)
```liquid
{% form 'product', product %}
  <select name="id">
    {% for variant in product.variants %}
      <option value="{{ variant.id }}">{{ variant.title }}</option>
    {% endfor %}
  </select>
  <input type="number" name="quantity" value="1" min="1">
  <button type="submit">Adicionar ao Carrinho</button>
{% endform %}
```

### Tradução com Fallback
```liquid
{{ 'products.add_to_cart' | t | default: 'Adicionar ao Carrinho' }}
```

### Metafield Acesso
```liquid
{{ product.metafields.custom.care_instructions }}
{{ product.metafields.custom.dimensions.value | json }}
```

### Whitespace Control
```liquid
{%- if condition -%}
  {# sem espaços extras #}
{%- endif -%}
```

---

## 🚫 LIMITES DO TEMA
| Recurso | Limite |
|---------|--------|
| Arquivo único | 256 KB |
| Tema total | 50 MB |
| Liquid / JSON / CSS | 256 KB cada |

---

## ✅ REGRAS DE OURO
1. **Use `{% render %}` não `{% include %}`** — escopo isolado, mais rápido
2. **Imagens: sempre `image_url` + `image_tag`** — CDN otimizado automaticamente
3. **Lógica complexa → JavaScript** — Liquid é para render, não lógica pesada
4. **Sempre trate estados vazios** — `{% else %}` nos `{% for %}` loops
5. **Adicione `presets` no schema** — seção aparece no Theme Editor
6. **Use `{%- -%}` para whitespace control** em snippets críticos
7. **Theme Check obrigatório** — `shopify theme check --fail-level error`
