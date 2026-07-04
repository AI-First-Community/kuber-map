---
type: FIBO Class
title: "trader"
description: "party that engages in the transfer of financial assets in any financial market on behalf of a client or the financial services provider"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trader
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
  - {type: facilitates, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md", provenance: fibo}
---

party that engages in the transfer of financial assets in any financial market on behalf of a client or the financial services provider

### Relationships
- is-a: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
- facilitates: [Trade](/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)
