---
type: FIBO Class
title: "trade identifier"
description: "sequence of characters identifying a trade within some context"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md", provenance: fibo}
---

sequence of characters identifying a trade within some context

### Relationships
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [Trade](/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)
