---
type: FIBO Class
title: "currency"
description: "medium of exchange value, defined by reference to the geographical location of the monetary authorities responsible for it"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
tags: [FND, Release]
synonyms:
  - "currency unit"
  - "monetary unit"
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/MeasurementUnit.md", provenance: fibo}
  - {type: is-used-by, target: "/CMNS/Locations/GeopoliticalEntity.md", provenance: fibo}
---

medium of exchange value, defined by reference to the geographical location of the monetary authorities responsible for it

### Relationships
- is-a: [MeasurementUnit](/CMNS/QuantitiesAndUnits/MeasurementUnit.md)
- is-used-by: [GeopoliticalEntity](/CMNS/Locations/GeopoliticalEntity.md)
