---
type: FIBO Class
title: "calculation"
description: "actual execution of some computation, computational process, or operation that was scheduled or triggered by something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Calculation
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: has-quantity-value, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
  - {type: has-quantity-value-range, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValueRange.md", provenance: fibo}
  - {type: exemplifies, target: "/FND/DatesAndTimes/Occurrences/CalculationEvent.md", provenance: fibo}
  - {type: has-expression, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
---

actual execution of some computation, computational process, or operation that was scheduled or triggered by something

### Relationships
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- has-quantity-value: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
- has-quantity-value-range: [ScalarQuantityValueRange](/CMNS/QuantitiesAndUnits/ScalarQuantityValueRange.md)
- exemplifies: [CalculationEvent](/FND/DatesAndTimes/Occurrences/CalculationEvent.md)
- has-expression: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
