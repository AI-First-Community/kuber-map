---
type: FIBO Class
title: "median"
description: "value of the variate dividing the total frequency of a data sample, population, or probability distribution, into two halves"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Median
tags: [FND, Release]
detail: "The basic advantage of the median in describing data compared to the mean is that it is not skewed by extremely large or small values, and may provide a better idea of a 'typical' value. This measure represents the middle value (if n is odd) or the average of the two middle values (if n is even) in an ordered list of data values. The median divides the total frequency distribution into two equal parts: one-half of the cases fall below the median and one-half of the cases exceed the median."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/StatisticalMeasure.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-observed-value, target: "/CMNS/Collections/StructuredCollection.md", provenance: fibo}
---

value of the variate dividing the total frequency of a data sample, population, or probability distribution, into two halves

### Relationships
- is-a: [StatisticalMeasure](/FND/Utilities/Analytics/StatisticalMeasure.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-observed-value: [StructuredCollection](/CMNS/Collections/StructuredCollection.md)
