---
type: FIBO Class
title: "statistical swap"
description: "swap that depends on some statistical measure of the performance of the underlier"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StatisticalSwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
  - {type: has-leg, target: "/DER/DerivativesContracts/Swaps/FixedLeg.md", provenance: fibo}
  - {type: has-leg, target: "/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md", provenance: fibo}
---

swap that depends on some statistical measure of the performance of the underlier

### Relationships
- is-a: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
- has-leg: [FixedLeg](/DER/DerivativesContracts/Swaps/FixedLeg.md)
- has-leg: [PerformanceBasedVariableLeg](/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md)
