---
type: FIBO Class
title: "dispersion"
description: "degree of scatter or variability shown by observations"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Dispersion
tags: [FND, Release]
detail: "A measure of statistical dispersion is a nonnegative real number that is zero if all the data are the same and increases as the data become more diverse. It is usually measured as an average deviation about some central value (e.g. mean deviation, standard deviation) or by an order statistic (e.g. quartile deviation, range) but may also be a mean of deviations of values among themselves (e.g. Gini's mean difference and also standard deviation)."
examples:
  - "Common examples of measures of statistical dispersion are the variance, standard deviation, and interquartile range. The collection size argument, above, represents the number of elements in the set, if known. The collection of values under consideration is represented as a structured collection in FIBO, typically a sample set derived from a finite population."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/StatisticalMeasure.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: applies-to, target: "/FND/Utilities/Analytics/FinitePopulation.md", provenance: fibo}
  - {type: has-observed-value, target: "/CMNS/Collections/StructuredCollection.md", provenance: fibo}
---

degree of scatter or variability shown by observations

### Relationships
- is-a: [StatisticalMeasure](/FND/Utilities/Analytics/StatisticalMeasure.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- applies-to: [FinitePopulation](/FND/Utilities/Analytics/FinitePopulation.md)
- has-observed-value: [StructuredCollection](/CMNS/Collections/StructuredCollection.md)
