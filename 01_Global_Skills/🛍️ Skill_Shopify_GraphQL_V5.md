---
name: skill-shopify-graphql-v5
description: >
  Integração e consultas avançadas para Shopify Admin API via GraphQL e Remix.
---

# Skill_Shopify_GraphQL_V5.md
> Protocolo de Extração V5.0 | Fonte: skills/api-graphql + app-development + headless-hydrogen

---

## 🔑 AUTENTICAÇÃO

### Admin API (Backend)
```javascript
// Remix App — padrão recomendado
import { authenticate } from "../shopify.server";

export async function loader({ request }) {
  const { admin } = await authenticate.admin(request);
  const response = await admin.graphql(`query { ... }`);
  return response.json();
}
```

### Storefront API (Frontend/Headless)
```javascript
const storefrontClient = new StorefrontApiClient({
  privateAccessToken: process.env.STOREFRONT_ACCESS_TOKEN,
  storeDomain: "your-store.myshopify.com",
  apiVersion: "2025-01",
});
```

### Next.js / Custom Stack
```typescript
export async function shopifyFetch({ query, variables }) {
  const response = await fetch(
    `https://${domain}/api/2025-01/graphql.json`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Shopify-Storefront-Access-Token": storefrontAccessToken,
      },
      body: JSON.stringify({ query, variables }),
    }
  );
  return response.json();
}
```

---

## 📦 QUERIES ESSENCIAIS

### Produtos com Variantes
```graphql
query GetProducts($first: Int!, $after: String) {
  products(first: $first, after: $after) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id title handle status vendor tags
      featuredImage { url altText }
      variants(first: 10) {
        nodes { id title sku price compareAtPrice inventoryQuantity
          selectedOptions { name value }
        }
      }
      priceRange {
        minVariantPrice { amount currencyCode }
        maxVariantPrice { amount currencyCode }
      }
      metafields(first: 10) {
        nodes { namespace key value type }
      }
      seo { title description }
    }
  }
}
```

### Pedidos com Detalhes Completos
```graphql
query GetOrders($first: Int!, $query: String) {
  orders(first: $first, query: $query, sortKey: CREATED_AT, reverse: true) {
    nodes {
      id name email createdAt
      displayFinancialStatus displayFulfillmentStatus
      totalPriceSet { shopMoney { amount currencyCode } }
      customer { id firstName lastName email }
      lineItems(first: 50) {
        nodes {
          id title quantity sku
          variant { id sku product { id title } }
          originalTotalSet { shopMoney { amount currencyCode } }
        }
      }
      shippingAddress { address1 city province country zip }
      fulfillments { status trackingInfo { company number url } }
    }
  }
}
```

### Clientes
```graphql
query GetCustomers($first: Int!, $query: String) {
  customers(first: $first, query: $query) {
    nodes {
      id firstName lastName email phone
      ordersCount totalSpent { amount currencyCode }
      addresses(first: 5) { address1 city country }
      tags createdAt
    }
  }
}
```

### Inventário por Localização
```graphql
query GetInventory($locationId: ID!) {
  location(id: $locationId) {
    inventoryLevels(first: 100) {
      nodes {
        available incoming
        item { id sku variant { id displayName product { title } } }
      }
    }
  }
}
```

---

## ✏️ MUTATIONS ESSENCIAIS

### Criar Produto
```graphql
mutation CreateProduct($input: ProductInput!) {
  productCreate(input: $input) {
    product { id title handle }
    userErrors { field message }
  }
}
```
```json
{
  "input": {
    "title": "Novo Produto",
    "descriptionHtml": "<p>Descrição</p>",
    "vendor": "Minha Marca",
    "tags": ["new", "featured"],
    "variants": [{
      "price": "29.99",
      "sku": "SKU-001",
      "inventoryManagement": "SHOPIFY",
      "inventoryPolicy": "DENY"
    }]
  }
}
```

### Metafields (Ler e Escrever)
```graphql
# Ler
query { product(id: $id) {
  careInstructions: metafield(namespace: "custom", key: "care_instructions") { value }
  metafields(first: 20) { nodes { namespace key value type } }
}}

# Escrever
mutation SetMetafields($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { id key value }
    userErrors { field message }
  }
}
```
```json
{
  "metafields": [{
    "ownerId": "gid://shopify/Product/123456",
    "namespace": "custom",
    "key": "care_instructions",
    "value": "Lavar à mão",
    "type": "single_line_text_field"
  }]
}
```

### Cart (Storefront API)
```graphql
mutation CreateCart($lines: [CartLineInput!]!) {
  cartCreate(input: { lines: $lines }) {
    cart { id checkoutUrl
      lines(first: 10) {
        nodes { id quantity merchandise { ... on ProductVariant { title } } }
      }
    }
  }
}

mutation AddToCart($cartId: ID!, $lines: [CartLineInput!]!) {
  cartLinesAdd(cartId: $cartId, lines: $lines) {
    cart { id lines(first: 10) { nodes { id quantity } } }
  }
}
```

### Webhooks
```graphql
mutation WebhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) {
  webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) {
    webhookSubscription { id topic endpoint { ... on WebhookHttpEndpoint { callbackUrl } } }
    userErrors { field message }
  }
}
```
**Topics principais:** `PRODUCTS_CREATE` `PRODUCTS_UPDATE` `ORDERS_CREATE` `ORDERS_PAID` `CUSTOMERS_CREATE` `INVENTORY_LEVELS_UPDATE`

---

## 📄 PAGINAÇÃO (Cursor-Based)
```javascript
async function getAllProducts(admin) {
  let products = [], hasNextPage = true, cursor = null;
  while (hasNextPage) {
    const data = await admin.graphql(QUERY, { variables: { first: 50, after: cursor } });
    const { nodes, pageInfo } = data.data.products;
    products = [...products, ...nodes];
    hasNextPage = pageInfo.hasNextPage;
    cursor = pageInfo.endCursor;
  }
  return products;
}
```

---

## ⚡ RATE LIMITS + RETRY
```javascript
async function queryWithRetry(admin, query, variables, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    const response = await admin.graphql(query, { variables });
    const data = await response.json();
    if (data.errors?.some(e => e.extensions?.code === "THROTTLED")) {
      await new Promise(r => setTimeout(r, Math.pow(2, attempt) * 1000));
      continue;
    }
    return data;
  }
}
// Custo máximo: 2000 pts | Restore: 100 pts/s
// Extensions.cost.throttleStatus para monitorar
```

---

## 📊 TIPOS DE METAFIELDS
| Tipo | Exemplo |
|------|---------|
| `single_line_text_field` | `"Texto curto"` |
| `multi_line_text_field` | `"Linha 1\nLinha 2"` |
| `number_integer` | `"42"` |
| `number_decimal` | `"19.99"` |
| `boolean` | `"true"` |
| `json` | `"{\"key\": \"value\"}"` |
| `url` | `"https://exemplo.com"` |
| `color` | `"#FF0000"` |

---

## 🔥 BULK OPERATIONS (Grandes Volumes)
```graphql
mutation BulkProducts {
  bulkOperationRunQuery(query: """
    { products { edges { node { id title variants { edges { node { id sku price } } } } } } }
  """) {
    bulkOperation { id status }
    userErrors { field message }
  }
}

query BulkOperationStatus {
  currentBulkOperation { id status objectCount url }
}
```

---

## ✅ REGRAS DE OURO
1. **Solicite apenas os campos que você usa** — reduz custo e payload
2. **Sempre verifique `userErrors`** em mutations
3. **Use paginação cursor-based** — nunca busque tudo de uma vez
4. **Implemente retry com exponential backoff** para rate limits
5. **Use Bulk Operations** para exports de dados grandes
6. **Admin API = backend apenas | Storefront API = frontend seguro**
