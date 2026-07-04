---
type: FIBO Class
title: "unemployed population"
description: "subset of the civilian labor force that is considered to have had no employment but was available for work, except for temporary illness, and had made specific efforts to find employment sometime during a specified period, during the reporting period"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemployedPopulation
tags: [IND, Release]
detail: "Persons who were waiting to be recalled to a job from which they had been laid off need not have been looking for work to be classified as unemployed."
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md", provenance: fibo}
  - {type: has-duration-of-unemployment, target: "/CMNS/DatesAndTimes/Duration.md", provenance: fibo}
---

subset of the civilian labor force that is considered to have had no employment but was available for work, except for temporary illness, and had made specific efforts to find employment sometime during a specified period, during the reporting period

### Relationships
- is-a: [CivilianLaborForce](/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md)
- has-duration-of-unemployment: [Duration](/CMNS/DatesAndTimes/Duration.md)
