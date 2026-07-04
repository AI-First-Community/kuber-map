---
type: FIBO Class
title: "product lifecycle"
description: "lifecycle specific to a product or product family"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/Lifecycle.md", provenance: fibo}
  - {type: defines, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md", provenance: fibo}
  - {type: has-stage, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md", provenance: fibo}
  - {type: is-lifecycle-of, target: "/FND/ProductsAndServices/ProductsAndServices/Product.md", provenance: fibo}
---

lifecycle specific to a product or product family

### Relationships
- is-a: [Lifecycle](/FND/Arrangements/Lifecycles/Lifecycle.md)
- defines: [ProductLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md)
- has-stage: [ProductLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md)
- is-lifecycle-of: [Product](/FND/ProductsAndServices/ProductsAndServices/Product.md)
