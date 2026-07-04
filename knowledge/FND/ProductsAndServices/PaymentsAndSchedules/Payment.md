---
type: FIBO Class
title: "payment"
description: "delivery of money in fulfillment of an obligation, such as to satisfy a claim or debt"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment
tags: [FND, Release]
core: true
examples:
  - "A $1,800 monthly mortgage payment of principal and interest."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: has-payment-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

delivery of money in fulfillment of an obligation, such as to satisfy a claim or debt

### Relationships
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- has-payment-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
