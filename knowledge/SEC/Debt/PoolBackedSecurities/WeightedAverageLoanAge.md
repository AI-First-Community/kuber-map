---
type: FIBO Class
title: "weighted average loan age"
description: "dollar-weighted average measuring the age of the individual loans in a mortgage pass-through or pooled security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageLoanAge
tags: [SEC, Release]
detail: "A weighted average loan age (WALA) may apply to pool-backed securities such as Ginnie Mae or Freddie Mac securities. The WALA is measured as the time in months since the origination of the loans, with the weighting based on each loan's size in proportion to the aggregate total of the pool. This is defined by the issuer. WALA is more official, not an analysis from a vendor. This changes but the values are relayed by the issuer on an ongoing basis. Investopedia explains Weighted Average Loan Age - WALA The weighted average age will change over time as some mortgages get paid off faster than others. Based on the issuer of the mortgage-backed securities (MBS), the WALA may be weighted on the remaining principal balance dollar figure, or the beginning notional value of the loan. The flip side of the WALA is the weighted average maturity (WAM), which is a dollar-weighted measure of the months remaining until the principal amounts are completely repaid on each loan in the pool."
synonyms:
  - "WALA"
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/ArithmeticMean.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
---

dollar-weighted average measuring the age of the individual loans in a mortgage pass-through or pooled security

### Relationships
- is-a: [ArithmeticMean](/FND/Utilities/Analytics/ArithmeticMean.md)
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
