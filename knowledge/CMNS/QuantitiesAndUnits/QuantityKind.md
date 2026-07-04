---
type: FIBO Class
title: "quantity kind"
description: "aspect common to mutually comparable quantities"
resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/QuantityKind
tags: [CMNS]
examples:
  - "The quantities diameter, circumference, and wavelength are generally considered to be quantities of the same kind, namely, of the kind of quantity called length."
  - "The quantities heat, kinetic energy, and potential energy are generally considered to be quantities of the same kind, namely, of the kind of quantity called energy."
  - "The quantities moment of force and energy are, by convention, not regarded as being of the same kind, although they have the same dimension. Similarly for heat capacity and entropy, as well as for number of entities, relative permeability, and mass fraction."
synonyms:
  - "kind of quantity"
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: has-dimension, target: "/CMNS/QuantitiesAndUnits/QuantityDimension.md", provenance: fibo}
  - {type: has-measurement-unit, target: "/CMNS/QuantitiesAndUnits/MeasurementUnit.md", provenance: fibo}
  - {type: is-defined-in, target: "/CMNS/QuantitiesAndUnits/SystemOfQuantities.md", provenance: fibo}
---

aspect common to mutually comparable quantities

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- has-dimension: [QuantityDimension](/CMNS/QuantitiesAndUnits/QuantityDimension.md)
- has-measurement-unit: [MeasurementUnit](/CMNS/QuantitiesAndUnits/MeasurementUnit.md)
- is-defined-in: [SystemOfQuantities](/CMNS/QuantitiesAndUnits/SystemOfQuantities.md)
