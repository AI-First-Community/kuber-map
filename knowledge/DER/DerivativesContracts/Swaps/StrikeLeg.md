---
type: FIBO Class
title: "strike leg"
description: "swap leg that specifies a fixed amount, 'the strike', quoted at the time of execution"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StrikeLeg
tags: [DER, Release]
detail: "The fixed amount may be with respect to some variable or a monetary amount. The realization of a strike leg is not a cashflow per se, but a netting out against the terms defined in the other leg of a statistical swap."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/FixedLeg.md", provenance: fibo}
---

swap leg that specifies a fixed amount, 'the strike', quoted at the time of execution

### Relationships
- is-a: [FixedLeg](/DER/DerivativesContracts/Swaps/FixedLeg.md)
