---
type: FIBO Class
title: "equity volatility swap"
description: "dispersion swap that is a forward contract on the variability of movements in the price of its underlying equities"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityVolatilitySwap
tags: [DER, Release]
detail: "An equity volatility swap is a measure of the amount by which an asset's price is expected to fluctuate over a given period of time; it is normally measured by the annual standard deviation of daily price changes."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/DispersionSwap.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md", provenance: fibo}
---

dispersion swap that is a forward contract on the variability of movements in the price of its underlying equities

### Relationships
- is-a: [DispersionSwap](/DER/DerivativesContracts/Swaps/DispersionSwap.md)
- is-a: [EquitySwap](/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)
