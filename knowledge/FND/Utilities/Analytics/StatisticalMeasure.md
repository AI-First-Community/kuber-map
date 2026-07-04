---
type: FIBO Class
title: "statistical measure"
description: "summary (means, mode, total, index, etc.) of the individual quantitative variable values for the statistical units in a specific group (study domain)"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
tags: [FND, Release]
detail: "Statistical measures may consist of several orthogonal characteristics, including (a) whether they reflect an estimate or variable, (b) the datatype, or from a FIBO perspective, nature of the measure (e.g., index, total, ratio, percent, percent change, mean, others), (c) the population (or the universe that applies to the highest level if defined in general) to which the measure applies, and (d) any relevant aspects used to subset or stratify a measure, (i.e., make them apply to a smaller universe)."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Measure.md", provenance: fibo}
  - {type: is-characterized-by, target: "/CMNS/Classifiers/Aspect.md", provenance: fibo}
---

summary (means, mode, total, index, etc.) of the individual quantitative variable values for the statistical units in a specific group (study domain)

### Relationships
- is-a: [Measure](/CMNS/QuantitiesAndUnits/Measure.md)
- is-characterized-by: [Aspect](/CMNS/Classifiers/Aspect.md)
