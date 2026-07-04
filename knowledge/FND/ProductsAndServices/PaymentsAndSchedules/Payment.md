---
type: FIBO Class
title: "payment"
description: "delivery of money in fulfillment of an obligation, such as to satisfy a claim or debt"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment
tags: [FND, Release]
relations:
  - {type: has-payment-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
---

delivery of money in fulfillment of an obligation, such as to satisfy a claim or debt

### Relationships
- has-payment-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
