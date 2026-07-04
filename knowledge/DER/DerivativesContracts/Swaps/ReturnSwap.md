---
type: FIBO Class
title: "return swap"
description: "swap in which one leg, the return leg, is based on income generated from some underlier"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnSwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
  - {type: has-funding-leg, target: "/DER/DerivativesContracts/Swaps/FixedPaymentLeg.md", provenance: fibo}
  - {type: has-return-leg, target: "/DER/DerivativesContracts/Swaps/ReturnLeg.md", provenance: fibo}
---

swap in which one leg, the return leg, is based on income generated from some underlier

### Relationships
- is-a: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
- has-funding-leg: [FixedPaymentLeg](/DER/DerivativesContracts/Swaps/FixedPaymentLeg.md)
- has-return-leg: [ReturnLeg](/DER/DerivativesContracts/Swaps/ReturnLeg.md)
