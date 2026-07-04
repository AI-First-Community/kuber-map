---
type: FIBO Class
title: "fixed basket"
description: "basket of goods and services whose quantity and quality are held fixed for some period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/FixedBasket
tags: [IND, Release]
synonyms:
  - "basket of goods"
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/IND/EconomicIndicators/EconomicIndicators/FixedBasketConstituent.md", provenance: fibo}
---

basket of goods and services whose quantity and quality are held fixed for some period of time

### Relationships
- is-a: [Basket](/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md)
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [FixedBasketConstituent](/IND/EconomicIndicators/EconomicIndicators/FixedBasketConstituent.md)
