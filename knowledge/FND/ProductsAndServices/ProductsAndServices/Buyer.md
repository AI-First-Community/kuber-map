---
type: FIBO Class
title: "buyer"
description: "party that purchases something in exchange for money or other consideration under a contract of sale"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: buys, target: "/FND/ProductsAndServices/ProductsAndServices/Product.md", provenance: fibo}
---

party that purchases something in exchange for money or other consideration under a contract of sale

### Relationships
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- buys: [Product](/FND/ProductsAndServices/ProductsAndServices/Product.md)
