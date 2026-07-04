---
type: FIBO Class
title: "product lifecycle stage"
description: "phase in a product lifecycle"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStage.md", provenance: fibo}
  - {type: classifies, target: "/FND/ProductsAndServices/ProductsAndServices/Product.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleEvent.md", provenance: fibo}
  - {type: is-defined-in, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md", provenance: fibo}
  - {type: is-stage-of, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md", provenance: fibo}
---

phase in a product lifecycle

### Relationships
- is-a: [LifecycleStage](/FND/Arrangements/Lifecycles/LifecycleStage.md)
- classifies: [Product](/FND/ProductsAndServices/ProductsAndServices/Product.md)
- comprises: [ProductLifecycleEvent](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleEvent.md)
- is-defined-in: [ProductLifecycle](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md)
- is-stage-of: [ProductLifecycle](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md)
