---
type: FIBO Class
title: "currency swap"
description: "foreign exchange agreement between two parties to exchange a given amount of one currency for another currency for spot delivery or for forward delivery at an agreed rate after a specified period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
  - {type: has-leg, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencyForward.md", provenance: fibo}
---

foreign exchange agreement between two parties to exchange a given amount of one currency for another currency for spot delivery or for forward delivery at an agreed rate after a specified period of time

### Relationships
- is-a: [CurrencyDerivative](/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md)
- is-a: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
- has-leg: [CurrencyForward](/DER/DerivativesContracts/CurrencyContracts/CurrencyForward.md)
