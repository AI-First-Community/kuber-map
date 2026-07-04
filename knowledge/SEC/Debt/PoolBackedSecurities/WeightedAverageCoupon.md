---
type: FIBO Class
title: "weighted average coupon"
description: "weighted-average gross interest rates of the pool of mortgages that underlie a mortgage-backed security (MBS) weighed by their balances at the time the securities were issued"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon
tags: [SEC, Release]
detail: "The weighted average coupon (WAC) is calculated by taking the gross of the interest rates owed on the underlying mortgages of the MBS and weighting them according to the percentage of the security that each mortgage represents. The WAC represents the average interest rate of different pools of mortgages with varying interest rates. In the weighted average calculation, the principal balance of each underlying mortgage is used as the weighting factor. To calculate the WAC, the coupon rate of each mortgage or MBS is multiplied by its remaining principal balance. The results are added together, and the sum total is divided by the remaining balance. A mortgage-backed security's current WAC can differ from its original WAC as the underlying mortgages pay down at different speeds. In the weighted-average calculation, the principal balance of each underlying mortgage is used as the weighting factor."
synonyms:
  - "WAC"
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/ArithmeticMean.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
---

weighted-average gross interest rates of the pool of mortgages that underlie a mortgage-backed security (MBS) weighed by their balances at the time the securities were issued

### Relationships
- is-a: [ArithmeticMean](/FND/Utilities/Analytics/ArithmeticMean.md)
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
