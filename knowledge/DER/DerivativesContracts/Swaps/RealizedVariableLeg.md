---
type: FIBO Class
title: "realized variable leg"
description: "performance-based leg wherein the payment is netted at maturity rather than periodically"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RealizedVariableLeg
tags: [DER, Release]
detail: "In this case there is a single payment at maturity/settlement and so there is no stream of cashflows either way. The other leg of these swaps is implied, and is simply the strike price."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md", provenance: fibo}
---

performance-based leg wherein the payment is netted at maturity rather than periodically

### Relationships
- is-a: [PerformanceBasedVariableLeg](/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md)
