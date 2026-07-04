---
type: FIBO Class
title: "credit index constituent"
description: "constituent of a basket of credit risks"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndexConstituent
tags: [IND, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/DebtAndEquities/CreditEvents/CreditEvent.md", provenance: fibo}
---

constituent of a basket of credit risks

### Relationships
- is-a: [WeightedBasketConstituent](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md)
- is-a: [DatedCollectionConstituent](/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- refers-to: [CreditEvent](/FBC/DebtAndEquities/CreditEvents/CreditEvent.md)
