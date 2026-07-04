---
type: FIBO Class
title: "seller"
description: "party that makes, offers or contracts to make a sale to an actual or potential buyer"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Seller
tags: [FND, Release]
relations:
  - {type: sells, target: "/FND/ProductsAndServices/ProductsAndServices/Product.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
---

party that makes, offers or contracts to make a sale to an actual or potential buyer

### Relationships
- sells: [Product](/FND/ProductsAndServices/ProductsAndServices/Product.md)
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
