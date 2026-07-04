---
type: FIBO Class
title: "employment-population ratio"
description: "economic indicator representing the ratio of the employed population with respect to the overall civilian non-institutional population of a given economy for some specified period"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmploymentPopulationRatio
tags: [IND, Release]
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-baseline-population, target: "/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md", provenance: fibo}
  - {type: has-comparison-population, target: "/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md", provenance: fibo}
---

economic indicator representing the ratio of the employed population with respect to the overall civilian non-institutional population of a given economy for some specified period

### Relationships
- is-a: [EconomicIndicator](/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-baseline-population: [CivilianNonInstitutionalPopulation](/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)
- has-comparison-population: [EmployedPopulation](/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md)
