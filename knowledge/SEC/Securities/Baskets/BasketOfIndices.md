---
type: FIBO Class
title: "market basket"
description: "basket composed of market indices"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfIndices
tags: [SEC, Release]
examples:
  - "For example, certain equities derivatives have an underlying basket which is a basket of more than one index, not a basket of securities."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Securities/Baskets/BasketOfIndicesConstituent.md", provenance: fibo}
---

basket composed of market indices

### Relationships
- is-a: [WeightedBasket](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [BasketOfIndicesConstituent](/SEC/Securities/Baskets/BasketOfIndicesConstituent.md)
