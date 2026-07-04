---
type: FIBO Class
title: "product lifecycle occurrence"
description: "realization of the lifecycle of a specific product"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleOccurrence
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleOccurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md", provenance: fibo}
  - {type: has-stage, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStageOccurrence.md", provenance: fibo}
---

realization of the lifecycle of a specific product

### Relationships
- is-a: [LifecycleOccurrence](/FND/Arrangements/Lifecycles/LifecycleOccurrence.md)
- exemplifies: [ProductLifecycle](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md)
- has-stage: [ProductLifecycleStageOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStageOccurrence.md)
