---
type: FIBO Class
title: "derived unit"
description: "measurement unit for a derived quantity, i.e., one that is defined with respect to one or more base units, such as as a product of powers of one or more other measurement units"
resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/DerivedUnit
tags: [CMNS]
examples:
  - "The meter per second, symbol m/s, and the centimeter per second, symbol cm/s, are derived units of speed in the SI. The kilometer per hour, symbol km/h, is a measurement unit of speed outside the SI but accepted for use with the SI. The knot, equal to one nautical mile per hour, is a measurement unit of speed outside the SI."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/PhysicalUnit.md", provenance: fibo}
  - {type: has-factor, target: "/CMNS/QuantitiesAndUnits/UnitPowerFactor.md", provenance: fibo}
  - {type: is-derived-from, target: "/CMNS/QuantitiesAndUnits/BaseUnit.md", provenance: fibo}
---

measurement unit for a derived quantity, i.e., one that is defined with respect to one or more base units, such as as a product of powers of one or more other measurement units

### Relationships
- is-a: [PhysicalUnit](/CMNS/QuantitiesAndUnits/PhysicalUnit.md)
- has-factor: [UnitPowerFactor](/CMNS/QuantitiesAndUnits/UnitPowerFactor.md)
- is-derived-from: [BaseUnit](/CMNS/QuantitiesAndUnits/BaseUnit.md)
