---
type: FIBO Class
title: "notional step amount"
description: "the amount of money that is subtracted from the notional on each step date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepAmount
tags: [DER, Release]
detail: "Note that this is an actual concrete sum of money, which may be specified either as a monetary amount (e.g. dollars and cents) or as a percentage of either the original notional amount or the previous notional amount."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
---

the amount of money that is subtracted from the notional on each step date

### Relationships
- is-a: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
