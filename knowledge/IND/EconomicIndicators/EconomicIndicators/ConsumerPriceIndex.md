---
type: FIBO Class
title: "consumer price index"
description: "economic indicator representing measure of the change over time in the prices of consumer goods and services that households consume"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex
tags: [IND, Release]
synonyms:
  - "CPI"
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-baseline-population, target: "/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md", provenance: fibo}
  - {type: has-input, target: "/IND/EconomicIndicators/EconomicIndicators/FixedBasket.md", provenance: fibo}
---

economic indicator representing measure of the change over time in the prices of consumer goods and services that households consume

### Relationships
- is-a: [EconomicIndicator](/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-baseline-population: [CivilianNonInstitutionalPopulation](/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)
- has-input: [FixedBasket](/IND/EconomicIndicators/EconomicIndicators/FixedBasket.md)
