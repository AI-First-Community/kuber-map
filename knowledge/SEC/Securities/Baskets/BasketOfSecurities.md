---
type: FIBO Class
title: "basket of securities"
description: "basket composed of securities, typically of a particular asset class such as equities or bonds"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfSecurities
tags: [SEC, Release]
core: true
examples:
  - "The basket of 500 stocks underlying an S&P 500 index fund."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Securities/Baskets/SecuritiesBasketConstituent.md", provenance: fibo}
---

basket composed of securities, typically of a particular asset class such as equities or bonds

### Relationships
- is-a: [WeightedBasket](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [SecuritiesBasketConstituent](/SEC/Securities/Baskets/SecuritiesBasketConstituent.md)
