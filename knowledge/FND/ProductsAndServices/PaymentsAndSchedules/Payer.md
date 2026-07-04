---
type: FIBO Class
title: "payer"
description: "a party who pays a bill or fees, or who makes payments to a payee in partial or complete fulfillment of an obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payer
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Obligor.md", provenance: fibo}
  - {type: has-obligation, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md", provenance: fibo}
---

a party who pays a bill or fees, or who makes payments to a payee in partial or complete fulfillment of an obligation

### Relationships
- is-a: [Obligor](/FND/Agreements/Agreements/Obligor.md)
- has-obligation: [PaymentObligation](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md)
