---
name: skill-shopify-functions-v5
description: >
  Skill_Shopify_Functions_V5.md
---

# Skill_Shopify_Functions_V5.md
> Protocolo de Extração V5.0 | Fonte: skills/shopify-functions + checkout-customization

---

## 🧠 O QUE SÃO SHOPIFY FUNCTIONS?

Módulos **WebAssembly serverless** que rodam na infraestrutura da Shopify.
- ✅ Executam em milissegundos | Escaláveis automaticamente
- ✅ Upgrade-safe (funcionam com Shop Pay e novas features)
- ✅ Suportam Rust (recomendado) e JavaScript

### Tipos de Function
| API | Finalidade |
|-----|------------|
| **Discounts** | Descontos em produto, pedido, frete |
| **Delivery Customization** | Renomear, reordenar, ocultar opções de envio |
| **Payment Customization** | Filtrar e reordenar métodos de pagamento |
| **Cart & Checkout Validation** | Bloquear checkout com erros |
| **Cart Transform** | Modificar conteúdo do carrinho |
| **Order Routing** | Controlar localização de fulfillment |

---

## 🚀 CRIANDO UMA FUNCTION

```bash
shopify app generate extension
# → Selecionar tipo de function desejado

shopify app function run --path extensions/my-function  # Testar local
shopify app function typegen                             # Gerar types
shopify app deploy                                       # Deploy
```

### Estrutura
```
extensions/my-discount/
├── src/
│   └── run.rs (ou run.js)
├── input.graphql       ← Define quais dados você recebe
├── shopify.extension.toml
└── Cargo.toml (Rust)
```

### shopify.extension.toml
```toml
api_version = "2025-01"

[[extensions]]
name = "Volume Discount"
handle = "volume-discount"
type = "function"

[[extensions.targeting]]
target = "purchase.product-discount.run"
input_query = "src/run.graphql"
export = "run"

[extensions.build]
command = "cargo wasi build --release"
path = "target/wasm32-wasi/release/volume-discount.wasm"
```

---

## 📥 INPUT QUERY (input.graphql)

```graphql
query RunInput {
  cart {
    lines {
      id quantity
      merchandise {
        ... on ProductVariant {
          id
          product {
            id title
            hasAnyTag(tags: ["discount-eligible"])
          }
        }
      }
      cost { amountPerQuantity { amount currencyCode } }
    }
    cost { totalAmount { amount } }
  }
  discountNode {
    metafield(namespace: "volume-discount", key: "config") { value }
  }
}
```

---

## 🔖 DESCONTO POR VOLUME — JavaScript
```javascript
// src/run.js
import { DiscountApplicationStrategy } from "../generated/api";

export function run(input) {
  const config = JSON.parse(
    input.discountNode.metafield?.value ?? '{"minimumQuantity": 5, "percentage": "10"}'
  );

  const discounts = input.cart.lines
    .filter(line =>
      line.quantity >= config.minimumQuantity &&
      line.merchandise.__typename === "ProductVariant" &&
      line.merchandise.product.hasAnyTag
    )
    .map(line => ({
      targets: [{ productVariant: { id: line.merchandise.id } }],
      value: { percentage: { value: config.percentage } },
      message: `${config.percentage}% desconto por volume`,
    }));

  return {
    discounts,
    discountApplicationStrategy: DiscountApplicationStrategy.First,
  };
}
```

---

## 🔖 DESCONTO POR VOLUME — Rust
```rust
use shopify_function::prelude::*;
use shopify_function::Result;

#[shopify_function_target(query_path = "src/run.graphql", schema_path = "schema.graphql")]
fn run(input: input::ResponseData) -> Result<output::FunctionRunResult> {
    let config: Config = input.discount_node.metafield
        .as_ref()
        .map(|m| serde_json::from_str(&m.value).unwrap())
        .unwrap_or_default();

    let discounts = input.cart.lines.iter()
        .filter_map(|line| {
            let variant = match &line.merchandise {
                input::InputCartLinesMerchandise::ProductVariant(v) => v,
                _ => return None,
            };
            if line.quantity >= config.minimum_quantity && variant.product.has_any_tag {
                Some(output::Discount {
                    targets: vec![output::Target::ProductVariant(
                        output::ProductVariantTarget { id: variant.id.clone(), quantity: None }
                    )],
                    value: output::Value::Percentage(output::Percentage {
                        value: Decimal::from_str(&config.discount_percentage).unwrap(),
                    }),
                    message: Some(format!("{}% desconto por volume", config.discount_percentage)),
                })
            } else { None }
        })
        .collect();

    Ok(output::FunctionRunResult {
        discounts,
        discount_application_strategy: output::DiscountApplicationStrategy::FIRST,
    })
}

#[derive(Default, serde::Deserialize)]
struct Config { minimum_quantity: i64, discount_percentage: String }
```

---

## 🚢 DELIVERY CUSTOMIZATION

```rust
fn run(input: input::ResponseData) -> Result<output::FunctionRunResult> {
    let mut operations = vec![];
    for method in input.cart.delivery_groups[0].delivery_options.iter() {
        // Ocultar express para pedidos pesados
        if method.title.contains("Express") && cart_weight_exceeds_limit(&input) {
            operations.push(output::Operation::Hide(output::HideOperation {
                delivery_option_handle: method.handle.clone(),
            }));
        }
        // Renomear opção
        if method.title.contains("Standard") {
            operations.push(output::Operation::Rename(output::RenameOperation {
                delivery_option_handle: method.handle.clone(),
                title: Some("Entrega Econômica (5-7 dias)".to_string()),
            }));
        }
    }
    Ok(output::FunctionRunResult { operations })
}
```

---

## 💳 PAYMENT CUSTOMIZATION

```javascript
export function run(input) {
  const total = parseFloat(input.cart.cost.totalAmount.amount);
  const operations = [];

  // Ocultar COD para pedidos > R$500
  if (total > 500) {
    const cod = input.paymentMethods.find(m => m.name.includes("Cash on Delivery"));
    if (cod) operations.push({ hide: { paymentMethodId: cod.id } });
  }

  // Reordenar métodos
  operations.push({ move: { paymentMethodId: input.paymentMethods[0].id, index: 2 } });

  return { operations };
}
```

---

## 🛑 CART & CHECKOUT VALIDATION

```rust
fn run(input: input::ResponseData) -> Result<output::FunctionRunResult> {
    let mut errors = vec![];

    // Valor mínimo de pedido
    let total: f64 = input.cart.cost.total_amount.amount.parse().unwrap();
    if total < 25.0 {
        errors.push(output::FunctionError {
            localized_message: "Pedido mínimo de R$25,00".to_string(),
            target: output::Target::Cart,
        });
    }

    // Restrição por região
    for line in &input.cart.lines {
        if let input::InputCartLinesMerchandise::ProductVariant(variant) = &line.merchandise {
            if is_restricted_product(&variant, &input.cart.buyer_identity) {
                errors.push(output::FunctionError {
                    localized_message: format!("{} não disponível nesta região", variant.product.title),
                    target: output::Target::CartLine(output::CartLineTarget { id: line.id.clone() }),
                });
            }
        }
    }

    Ok(output::FunctionRunResult { errors })
}
```

---

## 🛒 CART TRANSFORM (Brinde Automático)

```javascript
export function run(input) {
  const operations = input.cart.lines
    .filter(line => line.merchandise.product.hasAnyTag && line.quantity >= 3)
    .map(line => ({
      expand: {
        cartLineId: line.id,
        expandedCartItems: [
          { merchandiseId: line.merchandise.id, quantity: line.quantity },
          { merchandiseId: "gid://shopify/ProductVariant/FREE_GIFT_ID", quantity: 1 },
        ],
      },
    }));
  return { operations };
}
```

---

## 🖥️ CHECKOUT UI EXTENSION (React)

### Estrutura
```
extensions/checkout-ui/
├── src/Checkout.jsx
├── locales/en.default.json
└── shopify.extension.toml
```

### Extension Básica
```jsx
import { reactExtension, Banner, useTranslate } from "@shopify/ui-extensions-react/checkout";

export default reactExtension("purchase.checkout.block.render", () => <Extension />);

function Extension() {
  const translate = useTranslate();
  return <Banner title={translate("welcomeMessage")}>Obrigado por comprar conosco!</Banner>;
}
```

### Targets Principais
```javascript
"purchase.checkout.shipping-option-list.render-before"  // Antes do frete
"purchase.checkout.payment-method-list.render-before"   // Antes do pagamento
"purchase.checkout.cart-line-list.render-after"         // Após itens
"purchase.checkout.block.render"                        // Bloco livre
"purchase.checkout.delivery-address.render-before"      // Antes do endereço
```

### Hooks Úteis
```jsx
import { useCartLines, useTotalAmount, useShippingAddress, useCustomer } from "@shopify/ui-extensions-react/checkout";

const cartLines = useCartLines();
const totalAmount = useTotalAmount();
const customer = useCustomer();
const itemCount = cartLines.reduce((sum, line) => sum + line.quantity, 0);
```

### Salvar com Metafield
```jsx
import { useApplyMetafieldsChange } from "@shopify/ui-extensions-react/checkout";

const applyMetafieldsChange = useApplyMetafieldsChange();
await applyMetafieldsChange({
  type: "updateMetafield",
  namespace: "custom", key: "gift_message",
  valueType: "string", value: "Mensagem de presente",
});
```

### Bloquear Checkout (Intercept)
```jsx
import { useBuyerJourneyIntercept } from "@shopify/ui-extensions-react/checkout";

useBuyerJourneyIntercept(({ canBlockProgress }) => {
  if (!verified && canBlockProgress) {
    return {
      behavior: "block",
      reason: "Verificação necessária",
      errors: [{ message: "Por favor, confirme sua idade" }],
    };
  }
  return { behavior: "allow" };
});
```

---

## 🧪 TESTAR FUNCTION LOCALMENTE

```bash
# Input via stdin
cat input.json | shopify app function run --path extensions/my-function

# Sample input.json
{
  "cart": {
    "lines": [{
      "id": "gid://shopify/CartLine/1",
      "quantity": 5,
      "merchandise": {
        "__typename": "ProductVariant",
        "id": "gid://shopify/ProductVariant/123",
        "product": { "id": "gid://shopify/Product/456", "title": "Produto Teste", "hasAnyTag": true }
      },
      "cost": { "amountPerQuantity": { "amount": "10.00", "currencyCode": "BRL" } }
    }]
  },
  "discountNode": { "metafield": { "value": "{\"minimumQuantity\": 3, \"percentage\": \"15\"}" } }
}
```

---

## ✅ REGRAS DE OURO
1. **Use Rust para carrinhos grandes** — JS pode dar timeout com muitos itens
2. **Minimize o input query** — solicite apenas dados necessários
3. **Parse metafields uma vez** — configure no início, não em cada linha
4. **Use `hasAnyTag`** no input.graphql para evitar loops extras
5. **Sempre retorne `userErrors`** em mutations de configuração
6. **Shopify Plus** necessário para Checkout UI Extensions comercialmente

### CLI Rápida
| Comando | Ação |
|---------|------|
| `shopify app generate extension` | Criar function |
| `shopify app function run` | Testar local |
| `shopify app function typegen` | Gerar types |
| `shopify app deploy` | Fazer deploy |
