---
type: FIBO Class
title: "price structure"
description: "structured collection of prices, such as market prices for some index or security, such that volatility or other analyses may be performed over the structure"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceStructure
tags: [IND, Release]
detail: "Historical prices are needed not only for various statistical analyses but for determining best prices for certain kinds of options, for example. Note that prices may be quoted or calculated."
synonyms:
  - "price history"
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
---

structured collection of prices, such as market prices for some index or security, such that volatility or other analyses may be performed over the structure

### Relationships
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
