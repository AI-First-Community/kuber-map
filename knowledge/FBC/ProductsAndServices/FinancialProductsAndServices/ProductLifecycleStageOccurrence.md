---
type: FIBO Class
title: "product lifecycle stage occurrence"
description: "realization of a specific stage in the lifecycle of a given product"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStageOccurrence
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleEventOccurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md", provenance: fibo}
  - {type: is-stage-of, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleOccurrence.md", provenance: fibo}
---

realization of a specific stage in the lifecycle of a given product

### Relationships
- is-a: [LifecycleStageOccurrence](/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md)
- comprises: [ProductLifecycleEventOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleEventOccurrence.md)
- exemplifies: [ProductLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md)
- is-stage-of: [ProductLifecycleOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleOccurrence.md)
