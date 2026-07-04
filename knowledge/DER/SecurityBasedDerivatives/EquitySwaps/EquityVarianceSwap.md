---
type: FIBO Class
title: "equity variance swap"
description: "dispersion swap in which the parties agree to exchange payments based on the difference between (i) the realized variance of the price changes of a specified equity underlier over a stated observation period and (ii) a fixed amount of variance that is agreed when the contract is executed"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityVarianceSwap
tags: [DER, Release]
detail: "An equity variance swap is a forward swap that uses the variance (being the volatility squared) of an underlying's price movement over a period as the basis for the payoff calculation."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/DispersionSwap.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md", provenance: fibo}
---

dispersion swap in which the parties agree to exchange payments based on the difference between (i) the realized variance of the price changes of a specified equity underlier over a stated observation period and (ii) a fixed amount of variance that is agreed when the contract is executed

### Relationships
- is-a: [DispersionSwap](/DER/DerivativesContracts/Swaps/DispersionSwap.md)
- is-a: [EquitySwap](/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)
