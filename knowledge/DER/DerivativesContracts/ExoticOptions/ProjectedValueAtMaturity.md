---
type: FIBO Class
title: "projected value at maturity"
description: "expected value of the underlying asset at maturity calculated as of some date during the lookback period"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ProjectedValueAtMaturity
tags: [DER, Release]
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/CalculatedPrice.md", provenance: fibo}
  - {type: has-observed-date-and-time, target: "/CMNS/DatesAndTimes/CombinedDateTime.md", provenance: fibo}
---

expected value of the underlying asset at maturity calculated as of some date during the lookback period

### Relationships
- is-a: [CalculatedPrice](/FND/Accounting/CurrencyAmount/CalculatedPrice.md)
- has-observed-date-and-time: [CombinedDateTime](/CMNS/DatesAndTimes/CombinedDateTime.md)
