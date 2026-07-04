---
type: FIBO Class
title: "basket of commodities"
description: "custom basket whose constituents consist of one or more negotiable commodities"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/BasketOfCommodities
tags: [DER, Release]
detail: "A commodity basket may contain constituents from one of the potential underlying assets or from multiple underlying assets."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md", provenance: fibo}
  - {type: has-member, target: "/DER/DerivativesContracts/CommoditiesContracts/CommodityBasketConstituent.md", provenance: fibo}
---

custom basket whose constituents consist of one or more negotiable commodities

### Relationships
- is-a: [WeightedBasket](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- has-member: [CommodityBasketConstituent](/DER/DerivativesContracts/CommoditiesContracts/CommodityBasketConstituent.md)
