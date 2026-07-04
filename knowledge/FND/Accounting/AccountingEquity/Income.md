---
type: FIBO Class
title: "income"
description: "revenue received during a period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/AccountingEquity/Income
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-date-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

revenue received during a period of time

### Relationships
- is-a: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-date-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
