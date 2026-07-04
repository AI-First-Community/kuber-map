---
type: FIBO Class
title: "rates swap"
description: "swap in two counterparties each agree to pay the other cash flows on defined dates during an agreed period, based on a specified notional amount and a floating interest, floating inflation or fixed interest rate"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RatesSwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
  - {type: has-leg, target: "/DER/DerivativesContracts/Swaps/RateBasedLeg.md", provenance: fibo}
---

swap in two counterparties each agree to pay the other cash flows on defined dates during an agreed period, based on a specified notional amount and a floating interest, floating inflation or fixed interest rate

### Relationships
- is-a: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
- has-leg: [RateBasedLeg](/DER/DerivativesContracts/Swaps/RateBasedLeg.md)
