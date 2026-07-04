---
type: FIBO Class
title: "single monthly mortality"
description: "estimated per-month percentage of mortgages in an MBS pool that will be paid off early"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/SingleMonthlyMortality
tags: [SEC, Release]
detail: "Single monthly mortality (SMM) is a way to gauge the prepayment risk of a mortgage-backed security."
synonyms:
  - "SMM"
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Percentage.md", provenance: fibo}
---

estimated per-month percentage of mortgages in an MBS pool that will be paid off early

### Relationships
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
- is-a: [Percentage](/CMNS/QuantitiesAndUnits/Percentage.md)
