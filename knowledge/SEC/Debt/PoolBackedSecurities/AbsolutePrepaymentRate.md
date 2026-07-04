---
type: FIBO Class
title: "absolute prepayment rate"
description: "measure of the monthly rate of loan prepayments as a percentage of the original pool balance"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AbsolutePrepaymentRate
tags: [SEC, Release]
detail: "ABS is defined by the following formula where SMM refers to Single Monthly Mortality, which measures the percentage of dollars prepaid in a given month expressed as a percentage of the scheduled loan balance. ABS = (100 * SMM)/100 + (SMM X (Age - 1). The ABS measurement differs from conditional prepayment rate (CPR) used in the mortgage industry, which measures prepayment as an annualized percentage of the current pool balance."
synonyms:
  - "ABS"
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
---

measure of the monthly rate of loan prepayments as a percentage of the original pool balance

### Relationships
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
