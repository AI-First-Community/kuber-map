---
type: FIBO Class
title: "trade lifecycle occurrence"
description: "realization of the lifecycle for a specific trade"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleOccurrence
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleOccurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md", provenance: fibo}
  - {type: has-stage, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence.md", provenance: fibo}
---

realization of the lifecycle for a specific trade

### Relationships
- is-a: [LifecycleOccurrence](/FND/Arrangements/Lifecycles/LifecycleOccurrence.md)
- exemplifies: [TradeLifecycle](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)
- has-stage: [TradeLifecycleStageOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence.md)
