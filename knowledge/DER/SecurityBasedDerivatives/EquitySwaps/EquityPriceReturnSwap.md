---
type: FIBO Class
title: "equity price return swap"
description: "return swap whose return leg underlier is based on equities"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityPriceReturnSwap
tags: [DER, Release]
detail: "A price return equity swap is similar to a total return swap, except that dividends are not passed through to the buyer)."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/ReturnSwap.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md", provenance: fibo}
  - {type: has-return-leg, target: "/DER/SecurityBasedDerivatives/EquitySwaps/EquityReturnLeg.md", provenance: fibo}
---

return swap whose return leg underlier is based on equities

### Relationships
- is-a: [ReturnSwap](/DER/DerivativesContracts/Swaps/ReturnSwap.md)
- is-a: [EquitySwap](/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)
- has-return-leg: [EquityReturnLeg](/DER/SecurityBasedDerivatives/EquitySwaps/EquityReturnLeg.md)
