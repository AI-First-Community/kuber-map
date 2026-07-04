---
type: FIBO Class
title: "dividend swap"
description: "equity swap that has at least one leg whose underlier is a dividend stream"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/DividendSwap
tags: [DER, Release]
detail: "Dividend swaps include those that are fixed-term contracts between two parties where one party makes an interest rate payment for each interval and the other party pays the total dividends received as pay-out by a selected underlying asset."
relations:
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md", provenance: fibo}
  - {type: has-leg, target: "/DER/SecurityBasedDerivatives/EquitySwaps/DividendLeg.md", provenance: fibo}
---

equity swap that has at least one leg whose underlier is a dividend stream

### Relationships
- is-a: [EquitySwap](/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)
- has-leg: [DividendLeg](/DER/SecurityBasedDerivatives/EquitySwaps/DividendLeg.md)
