---
type: FIBO Class
title: "debt pool statistical measure"
description: "qualified measure of some aspect of the behavior of one or more debt instrument(s) that may vary over time"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/QualifiedMeasure.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
  - {type: has-applicable-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

qualified measure of some aspect of the behavior of one or more debt instrument(s) that may vary over time

### Relationships
- is-a: [QualifiedMeasure](/FND/Utilities/Analytics/QualifiedMeasure.md)
- applies-to: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
- has-applicable-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
