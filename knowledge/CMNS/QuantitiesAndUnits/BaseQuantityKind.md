---
type: FIBO Class
title: "base quantity kind"
description: "quantity in a conventionally chosen subset of a given system of quantities, where no quantity in the subset can be expressed in terms of the other quantities within that subset"
resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/BaseQuantityKind
tags: [CMNS]
examples:
  - "The International System of Quantities (ISQ) comprises these base quantities (with their SI base measurement units): length (meter), mass (kilogram), duration (second), electric current (ampere), thermodynamic temperature (kelvin), amount of substance (mole), and luminous intensity (candela). These base quantities are not mutually comparable. All quantities of any one of these kinds are, however, mutually comparable."
synonyms:
  - "base quantity"
  - "simple quantity kind"
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/QuantityKind.md", provenance: fibo}
  - {type: is-defined-in, target: "/CMNS/QuantitiesAndUnits/SystemOfQuantities.md", provenance: fibo}
---

quantity in a conventionally chosen subset of a given system of quantities, where no quantity in the subset can be expressed in terms of the other quantities within that subset

### Relationships
- is-a: [QuantityKind](/CMNS/QuantitiesAndUnits/QuantityKind.md)
- is-defined-in: [SystemOfQuantities](/CMNS/QuantitiesAndUnits/SystemOfQuantities.md)
