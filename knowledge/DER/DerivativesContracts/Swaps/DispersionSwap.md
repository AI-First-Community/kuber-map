---
type: FIBO Class
title: "dispersion swap"
description: "statistical derivative used to hedge on the magnitude of a price movement of an underlying asset"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionSwap
tags: [DER, Release]
detail: "A variance swap is an instrument that allows investors to trade future realized (or historical) volatility against current implied volatility. Some strategies involve selling a variance swap on an index and buying the variance swaps on the individual constituents; this particular kind of spread trade is called a variance dispersion trade."
synonyms:
  - "variance swap"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/StatisticalSwap.md", provenance: fibo}
  - {type: has-leg, target: "/DER/DerivativesContracts/Swaps/DispersionLeg.md", provenance: fibo}
---

statistical derivative used to hedge on the magnitude of a price movement of an underlying asset

### Relationships
- is-a: [StatisticalSwap](/DER/DerivativesContracts/Swaps/StatisticalSwap.md)
- has-leg: [DispersionLeg](/DER/DerivativesContracts/Swaps/DispersionLeg.md)
