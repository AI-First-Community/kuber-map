---
type: FIBO Class
title: "securities basket constituent"
description: "security identified as a component of a basket of securities"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/SecuritiesBasketConstituent
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: has-date-added, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
---

security identified as a component of a basket of securities

### Relationships
- is-a: [WeightedBasketConstituent](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md)
- is-a: [DatedCollectionConstituent](/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- comprises: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- has-date-added: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
