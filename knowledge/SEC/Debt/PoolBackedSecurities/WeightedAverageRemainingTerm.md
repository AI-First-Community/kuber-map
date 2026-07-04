---
type: FIBO Class
title: "weighted average remaining term"
description: "weighted average time to maturity of a portfolio of asset-backed securities (ABS) or mortgage-backed (MBS) securities"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageRemainingTerm
tags: [SEC, Release]
detail: "The longer the WART, the longer the portfolio's assets will take to mature, on average. WART is often used in relation to mortgage-backed securities (MBS) but can also be applied to any portfolio of fixed-income securities. WART is closely related to weighted average loan age (WALA), which is its inverse."
synonyms:
  - "WART"
  - "weighted average remaining maturity"
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/ArithmeticMean.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
---

weighted average time to maturity of a portfolio of asset-backed securities (ABS) or mortgage-backed (MBS) securities

### Relationships
- is-a: [ArithmeticMean](/FND/Utilities/Analytics/ArithmeticMean.md)
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
