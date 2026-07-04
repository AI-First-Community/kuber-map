---
type: FIBO Class
title: "prepayment speed"
description: "estimated rate at which a debt or part of a debt is paid off ahead of schedule"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed
tags: [SEC, Release]
detail: "A prepayment model is used to estimate the level of prepayments (speed) on a loan portfolio that will occur in a set period of time, given possible changes in interest rates. Understanding prepayment speed is critical in assessing the value of mortgage pass-through securities. Prepayment models are based on mathematical equations and usually involve the analysis of historical prepayment trends to predict what will happen in the future. Prepayment models are often used to value mortgage pools such as GNMA securities or other securitized debt products, including mortgage-backed securities (MBS)."
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
  - {type: is-based-on, target: "/MD/DebtTemporal/DebtAnalytics/LoanPoolPrepaymentModel.md", provenance: fibo}
---

estimated rate at which a debt or part of a debt is paid off ahead of schedule

### Relationships
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
- is-based-on: [LoanPoolPrepaymentModel](/MD/DebtTemporal/DebtAnalytics/LoanPoolPrepaymentModel.md)
