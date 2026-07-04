---
type: FIBO Class
title: "condor spread"
description: "non-directional options strategy that limits both gains and losses while seeking to profit from either low or high volatility"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CondorSpread
tags: [DER, Release]
detail: "There are two types of condor spreads. A long condor seeks to profit from low volatility and little to no movement in the underlying asset. A short condor seeks to profit from high volatility and a sizable move in the underlying asset in either direction. A Condor Spread uses either all calls or all puts."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/OptionTradingStrategy.md", provenance: fibo}
---

non-directional options strategy that limits both gains and losses while seeking to profit from either low or high volatility

### Relationships
- is-a: [OptionTradingStrategy](/DER/DerivativesContracts/Options/OptionTradingStrategy.md)
