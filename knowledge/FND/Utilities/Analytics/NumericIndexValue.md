---
type: FIBO Class
title: "numeric index value"
description: "numeric value of some aggregate relative to the value of that aggregate as of some date"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/NumericIndexValue
tags: [FND, Release]
detail: "A mathematical device or number which is used to express the observation (e.g., price level, volume of trade, relative amount etc.) of a given period, in comparison with that of a prior period."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
  - {type: is-value-of, target: "/FND/Utilities/Analytics/QualifiedMeasure.md", provenance: fibo}
---

numeric value of some aggregate relative to the value of that aggregate as of some date

### Relationships
- is-a: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
- is-value-of: [QualifiedMeasure](/FND/Utilities/Analytics/QualifiedMeasure.md)
