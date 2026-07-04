---
type: FIBO Class
title: "weighted basket"
description: "basket whose constituents have some relative importance with respect to one another"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Collections/StructuredCollection.md", provenance: fibo}
  - {type: has-expression, target: "/FND/Utilities/Analytics/WeightingFunction.md", provenance: fibo}
  - {type: has-member, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md", provenance: fibo}
---

basket whose constituents have some relative importance with respect to one another

### Relationships
- is-a: [Basket](/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md)
- is-a: [StructuredCollection](/CMNS/Collections/StructuredCollection.md)
- has-expression: [WeightingFunction](/FND/Utilities/Analytics/WeightingFunction.md)
- has-member: [WeightedBasketConstituent](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md)
