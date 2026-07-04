---
type: FIBO Class
title: "exchange rate structure"
description: "structured collection of quoted or projected exchange rates, such that volatility may be constructed for the structure"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ExchangeRateStructure
tags: [IND, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/FND/Accounting/CurrencyAmount/ExchangeRate.md", provenance: fibo}
---

structured collection of quoted or projected exchange rates, such that volatility may be constructed for the structure

### Relationships
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [ExchangeRate](/FND/Accounting/CurrencyAmount/ExchangeRate.md)
