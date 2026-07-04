---
type: FIBO Class
title: "fixed leg"
description: "swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated by reference to a fixed annual rate or consisting of at least one payment of a fixed amount"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedLeg
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/SwapLeg.md", provenance: fibo}
  - {type: has-payment-schedule, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
---

swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated by reference to a fixed annual rate or consisting of at least one payment of a fixed amount

### Relationships
- is-a: [SwapLeg](/DER/DerivativesContracts/Swaps/SwapLeg.md)
- has-payment-schedule: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
