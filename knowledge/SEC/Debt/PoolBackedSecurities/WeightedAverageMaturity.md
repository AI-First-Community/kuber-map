---
type: FIBO Class
title: "weighted average maturity"
description: "weighted average amount of time until the maturities on mortgages in a mortgage-backed security (MBS)"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageMaturity
tags: [SEC, Release]
core: true
detail: "The measure is calculated by totaling each mortgage value represented by the MBS. The weights of each mortgage is found by dividing the value of each into the total of all. To arrive at the WAM number the weight of each security is multiplied by the time until maturity of each mortgage, and then all the values are added together. For example say an MBS has three mortgages valued at $1,000, $2,000 and $3,000 (a total of $6,000) and mature in one, two and three years respectively. The weights of these are 1/6 (1,000/6,000), 1/3 (2,000/6,000) and 1/2 (3,000/6,000). The WAM is 2 1/3 years (1/6 x 1 year + 1/3 x 2 years + 1/2 x 3 years). Note that this calculation would need to be adjusted if there are multiple pools behind the MBS. This term is used more broadly to describe maturities in a portfolio of debt securities, including corporate debt and municipal bonds. The higher the WAM, the longer it takes for all of the mortgages or bonds in the portfolio to mature. WAM is used to manage debt portfolios and to assess the performance of debt portfolio managers."
examples:
  - "The 18-month weighted-average maturity of a money-market fund's holdings."
examples_provenance: curated
synonyms:
  - "WAM"
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/ArithmeticMean.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
---

weighted average amount of time until the maturities on mortgages in a mortgage-backed security (MBS)

### Relationships
- is-a: [ArithmeticMean](/FND/Utilities/Analytics/ArithmeticMean.md)
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
