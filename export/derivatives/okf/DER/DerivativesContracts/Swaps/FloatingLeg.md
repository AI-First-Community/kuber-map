---
type: FIBO Class
title: "floating leg"
description: "swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated by reference to some variable rate, calculated based on the change in value of some underlying asset, or consisting of at least one payment of some floating amount"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FloatingLeg
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "The leg paying SOFR + 0.4% on the notional."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/SwapLeg.md", provenance: fibo}
  - {type: has-payment-schedule, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
---

swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated by reference to some variable rate, calculated based on the change in value of some underlying asset, or consisting of at least one payment of some floating amount

### Relationships
- is-a: [SwapLeg](/DER/DerivativesContracts/Swaps/SwapLeg.md)
- has-payment-schedule: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
