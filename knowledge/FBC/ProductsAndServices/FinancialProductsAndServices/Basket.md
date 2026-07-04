---
type: FIBO Class
title: "basket"
description: "collection of goods, services, or other things (e.g., financial contracts) that can be purchased and sold in some marketplace"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Basket
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/Collections/Collection.md", provenance: fibo}
  - {type: has-member, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/BasketConstituent.md", provenance: fibo}
  - {type: has-selecting-party, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
---

collection of goods, services, or other things (e.g., financial contracts) that can be purchased and sold in some marketplace

### Relationships
- is-a: [Collection](/CMNS/Collections/Collection.md)
- has-member: [BasketConstituent](/FBC/ProductsAndServices/FinancialProductsAndServices/BasketConstituent.md)
- has-selecting-party: [Party](/CMNS/PartiesAndSituations/Party.md)
