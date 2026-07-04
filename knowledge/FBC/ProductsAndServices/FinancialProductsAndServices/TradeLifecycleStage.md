---
type: FIBO Class
title: "trade lifecycle stage"
description: "phase in the lifecycle of a trade"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStage.md", provenance: fibo}
  - {type: classifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent.md", provenance: fibo}
  - {type: is-defined-in, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md", provenance: fibo}
  - {type: is-stage-of, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md", provenance: fibo}
---

phase in the lifecycle of a trade

### Relationships
- is-a: [LifecycleStage](/FND/Arrangements/Lifecycles/LifecycleStage.md)
- classifies: [Trade](/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)
- comprises: [TradeLifecycleEvent](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent.md)
- is-defined-in: [TradeLifecycle](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)
- is-stage-of: [TradeLifecycle](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)
