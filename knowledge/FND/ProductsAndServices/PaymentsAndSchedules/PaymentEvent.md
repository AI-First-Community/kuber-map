---
type: FIBO Class
title: "payment event"
description: "an event that involves delivery of money in fulfillment of an obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentEvent
tags: [FND, Release]
relations:
  - {type: involves, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md", provenance: fibo}
  - {type: applies-to, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md", provenance: fibo}
---

an event that involves delivery of money in fulfillment of an obligation

### Relationships
- involves: [Payment](/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md)
- applies-to: [PaymentObligation](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md)
- is-a: [TransactionEvent](/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md)
