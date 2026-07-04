---
type: FIBO Class
title: "trade lifecycle stage occurrence"
description: "realization of a phase in the lifecycle of a specific trade"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEventOccurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md", provenance: fibo}
  - {type: is-stage-of, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleOccurrence.md", provenance: fibo}
---

realization of a phase in the lifecycle of a specific trade

### Relationships
- is-a: [LifecycleStageOccurrence](/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md)
- comprises: [TradeLifecycleEventOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEventOccurrence.md)
- exemplifies: [TradeLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)
- is-stage-of: [TradeLifecycleOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleOccurrence.md)
