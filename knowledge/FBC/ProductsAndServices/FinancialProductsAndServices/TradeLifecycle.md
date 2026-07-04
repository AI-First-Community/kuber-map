---
type: FIBO Class
title: "trade lifecycle"
description: "lifecycle that defines the evolution of a trade, from initiation through settlement"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle
tags: [FBC, Release]
examples:
  - "The trade life cycle covers the period of time over which a trade is initiated, typically as a part of a broader deal, is consumated, processed and executed, is settled or closed for other reasons, and is reported. Parts of a trade lifecycle may include or overlap with the lifecycle of one or more contracts."
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/Lifecycle.md", provenance: fibo}
  - {type: defines, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md", provenance: fibo}
  - {type: has-stage, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md", provenance: fibo}
  - {type: is-lifecycle-of, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md", provenance: fibo}
---

lifecycle that defines the evolution of a trade, from initiation through settlement

### Relationships
- is-a: [Lifecycle](/FND/Arrangements/Lifecycles/Lifecycle.md)
- defines: [TradeLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)
- has-stage: [TradeLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)
- is-lifecycle-of: [Trade](/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)
