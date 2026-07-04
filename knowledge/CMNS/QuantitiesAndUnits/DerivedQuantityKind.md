---
type: FIBO Class
title: "derived quantity kind"
description: "quantity, in a system of quantities, defined in terms of the base quantities of that system"
resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/DerivedQuantityKind
tags: [CMNS]
examples:
  - "In a system of quantities having the base quantities length and mass, mass density is a derived quantity defined as the quotient of mass and volume (length to the power three)."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/QuantityKind.md", provenance: fibo}
  - {type: has-factor, target: "/CMNS/QuantitiesAndUnits/QuantityKindPowerFactor.md", provenance: fibo}
  - {type: is-derived-from, target: "/CMNS/QuantitiesAndUnits/QuantityKind.md", provenance: fibo}
---

quantity, in a system of quantities, defined in terms of the base quantities of that system

### Relationships
- is-a: [QuantityKind](/CMNS/QuantitiesAndUnits/QuantityKind.md)
- has-factor: [QuantityKindPowerFactor](/CMNS/QuantitiesAndUnits/QuantityKindPowerFactor.md)
- is-derived-from: [QuantityKind](/CMNS/QuantitiesAndUnits/QuantityKind.md)
