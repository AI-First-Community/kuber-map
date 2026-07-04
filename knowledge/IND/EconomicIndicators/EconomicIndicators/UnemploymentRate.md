---
type: FIBO Class
title: "unemployment rate"
description: "economic indicator representing the ratio of the unemployed population with respect to the civilian labor force of a given economy for some specified period"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate
tags: [IND, Release]
detail: "Persons are classified as unemployed if they do not have a job, have actively looked for work in the prior 4 weeks, and are currently available for work. Workers expecting to be recalled from layoff are counted as unemployed, whether or not they have engaged in a specific jobseeking activity. In all other cases, the individual must have been engaged in at least one active job search activity in the 4 weeks preceding the interview and be available for work (except for temporary illness)."
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-baseline-population, target: "/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md", provenance: fibo}
  - {type: has-comparison-population, target: "/IND/EconomicIndicators/EconomicIndicators/UnemployedPopulation.md", provenance: fibo}
---

economic indicator representing the ratio of the unemployed population with respect to the civilian labor force of a given economy for some specified period

### Relationships
- is-a: [EconomicIndicator](/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-baseline-population: [CivilianLaborForce](/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md)
- has-comparison-population: [UnemployedPopulation](/IND/EconomicIndicators/EconomicIndicators/UnemployedPopulation.md)
