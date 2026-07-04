---
type: FIBO Class
title: "trade"
description: "situation that realizes an agreement between parties participating in a voluntary action of buying and selling goods and services"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: has-buyer, target: "/FND/ProductsAndServices/ProductsAndServices/Buyer.md", provenance: fibo}
  - {type: has-seller, target: "/FND/ProductsAndServices/ProductsAndServices/Seller.md", provenance: fibo}
  - {type: is-characterized-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md", provenance: fibo}
  - {type: is-embodied-in, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: is-facilitated-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Trader.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md", provenance: fibo}
---

situation that realizes an agreement between parties participating in a voluntary action of buying and selling goods and services

### Relationships
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- has-buyer: [Buyer](/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
- has-seller: [Seller](/FND/ProductsAndServices/ProductsAndServices/Seller.md)
- is-characterized-by: [TradeLifecycle](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)
- is-embodied-in: [Contract](/FND/Agreements/Contracts/Contract.md)
- is-facilitated-by: [Trader](/FBC/ProductsAndServices/FinancialProductsAndServices/Trader.md)
- is-identified-by: [TradeIdentifier](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md)
