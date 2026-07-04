---
type: FIBO Class
title: "cash flow"
description: "the movement of money from some source to some sink"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlow
tags: [FND, Provisional]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

the movement of money from some source to some sink

### Relationships
- is-a: [DatedCollectionConstituent](/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
