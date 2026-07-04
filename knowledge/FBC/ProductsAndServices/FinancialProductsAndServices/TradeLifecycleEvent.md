---
type: FIBO Class
title: "trade lifecycle event"
description: "kind of event that occurs during one or more stages of the lifecycle of a trade"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleEvent.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md", provenance: fibo}
  - {type: classifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEventOccurrence.md", provenance: fibo}
---

kind of event that occurs during one or more stages of the lifecycle of a trade

### Relationships
- is-a: [LifecycleEvent](/FND/Arrangements/Lifecycles/LifecycleEvent.md)
- applies-to: [TradeLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)
- classifies: [TradeLifecycleEventOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEventOccurrence.md)
