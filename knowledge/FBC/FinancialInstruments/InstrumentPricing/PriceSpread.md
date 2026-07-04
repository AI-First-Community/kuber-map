---
type: FIBO Class
title: "price spread"
description: "difference between two prices"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceSpread
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/Difference.md", provenance: fibo}
  - {type: has-applicable-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: has-argument, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
---

difference between two prices

### Relationships
- is-a: [Difference](/FND/Utilities/Analytics/Difference.md)
- has-applicable-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- has-argument: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
