---
type: FIBO Class
title: "weighting function"
description: "expression or function that determines the relative importance or influence of a given element of a set with respect to the whole"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/WeightingFunction
tags: [FND, Release]
detail: "For certain indices, one of the most common weighting factor is by market capitalization. In that case, each of the elements in the basket is multiplied by its market cap to determine its relative importance to the basket overall. With respect to discrete calculations, weighting functions are positive functions defined on discrete sets, such as weighted sums and weighted averages."
examples:
  - "Given a sample size of 1000, and a population of 300M, then the chance that any individual is selected is 1 in 300K. In that case, 300K is the weight assigned to each of the elements in the sample."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/StatisticalMeasure.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
---

expression or function that determines the relative importance or influence of a given element of a set with respect to the whole

### Relationships
- is-a: [StatisticalMeasure](/FND/Utilities/Analytics/StatisticalMeasure.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
