---
type: FIBO Class
title: "mean"
description: "most common measure of central tendency; the average of a set of numbers"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Mean
tags: [FND, Release]
detail: "When unqualified, the mean usually refers to the expectation of a variate, or to the arithmetic mean of a sample used as an estimate of the expectation."
synonyms:
  - "expected value"
  - "first (raw) moment"
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/StatisticalMeasure.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-observed-value, target: "/CMNS/Collections/StructuredCollection.md", provenance: fibo}
---

most common measure of central tendency; the average of a set of numbers

### Relationships
- is-a: [StatisticalMeasure](/FND/Utilities/Analytics/StatisticalMeasure.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-observed-value: [StructuredCollection](/CMNS/Collections/StructuredCollection.md)
