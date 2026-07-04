---
type: FIBO Class
title: "civilian labor force participation rate"
description: "economic indicator representing the rate of participation the labor force of a given economy for some specified period"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForceParticipationRate
tags: [IND, Release]
detail: "The labor force participation rate is the percentage of the population that is either employed or unemployed (that is, either working or actively seeking work)."
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-baseline-population, target: "/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md", provenance: fibo}
  - {type: has-comparison-population, target: "/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md", provenance: fibo}
---

economic indicator representing the rate of participation the labor force of a given economy for some specified period

### Relationships
- is-a: [EconomicIndicator](/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-baseline-population: [CivilianNonInstitutionalPopulation](/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)
- has-comparison-population: [CivilianLaborForce](/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md)
