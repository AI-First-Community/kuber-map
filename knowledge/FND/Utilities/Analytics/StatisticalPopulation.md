---
type: FIBO Class
title: "statistical population"
description: "statistical universe filtered by time and region"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalPopulation
tags: [FND, Release]
detail: "A common aim of statistical analysis is to produce information about some chosen population. In statistical inference, a subset of the population (a statistical sample) is chosen to represent the population in a statistical analysis. If a sample is chosen properly, characteristics of the entire population that the sample is drawn from can be estimated from corresponding characteristics of the sample."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/FinitePopulation.md", provenance: fibo}
  - {type: is-a, target: "/FND/Utilities/Analytics/StatisticalUniverse.md", provenance: fibo}
  - {type: is-characterized-by, target: "/FND/Utilities/Analytics/StatisticalArea.md", provenance: fibo}
  - {type: is-characterized-by, target: "/CMNS/DatesAndTimes/ExplicitDatePeriod.md", provenance: fibo}
---

statistical universe filtered by time and region

### Relationships
- is-a: [FinitePopulation](/FND/Utilities/Analytics/FinitePopulation.md)
- is-a: [StatisticalUniverse](/FND/Utilities/Analytics/StatisticalUniverse.md)
- is-characterized-by: [StatisticalArea](/FND/Utilities/Analytics/StatisticalArea.md)
- is-characterized-by: [ExplicitDatePeriod](/CMNS/DatesAndTimes/ExplicitDatePeriod.md)
