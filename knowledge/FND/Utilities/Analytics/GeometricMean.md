---
type: FIBO Class
title: "geometric mean"
description: "mean that indicates the central tendency or typical value of a set of numbers by using the product of their values (as opposed to the arithmetic mean which uses their sum)"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/GeometricMean
tags: [FND, Release]
detail: "The geometric mean is defined as the nth root of the product of n numbers. A geometric mean is often used when comparing different items - finding a single 'figure of merit' for these items - when each item has multiple properties that have different numeric ranges. For example, the geometric mean can give a meaningful 'average' to compare two companies which are each rated at 0 to 5 for their environmental sustainability, and are rated at 0 to 100 for their financial viability. If an arithmetic mean were used instead of a geometric mean, the financial viability is given more weight because its numeric range is larger - so a small percentage change in the financial rating (e.g. going from 80 to 90) makes a much larger difference in the arithmetic mean than a large percentage change in environmental sustainability (e.g. going from 2 to 5)."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/Mean.md", provenance: fibo}
---

mean that indicates the central tendency or typical value of a set of numbers by using the product of their values (as opposed to the arithmetic mean which uses their sum)

### Relationships
- is-a: [Mean](/FND/Utilities/Analytics/Mean.md)
