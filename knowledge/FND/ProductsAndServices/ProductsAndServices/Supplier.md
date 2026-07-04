---
type: FIBO Class
title: "supplier"
description: "party that provides goods or services that some party wants or needs, especially over a long period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Supplier
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: supplies, target: "/FND/ProductsAndServices/ProductsAndServices/Product.md", provenance: fibo}
---

party that provides goods or services that some party wants or needs, especially over a long period of time

### Relationships
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- supplies: [Product](/FND/ProductsAndServices/ProductsAndServices/Product.md)
