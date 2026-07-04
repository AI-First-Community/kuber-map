---
type: FIBO Class
title: "income"
description: "revenue received during a period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/AccountingEquity/Income
tags: [FND, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Income includes cash or cash equivalent(s) received during some period of time in exchange for labor or services, from the sale of goods or property, or as receipts from financial investments."
examples:
  - "Wages"
  - "Self-employment income"
  - "Rental income used to qualify a borrower"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-date-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

revenue received during a period of time

### Relationships
- is-a: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-date-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
