---
type: FIBO Class
title: "commodity basket constituent"
description: "component of a custom commodity basket whose relative importance with respect to other basket constituents is known"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityBasketConstituent
tags: [DER, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md", provenance: fibo}
  - {type: has-as-of-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-commodity-value-as-of-date, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-quantity-value, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
  - {type: involves, target: "/FND/ProductsAndServices/ProductsAndServices/Commodity.md", provenance: fibo}
---

component of a custom commodity basket whose relative importance with respect to other basket constituents is known

### Relationships
- is-a: [WeightedBasketConstituent](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md)
- has-as-of-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-commodity-value-as-of-date: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-quantity-value: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
- involves: [Commodity](/FND/ProductsAndServices/ProductsAndServices/Commodity.md)
