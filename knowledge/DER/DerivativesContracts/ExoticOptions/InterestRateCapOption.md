---
type: FIBO Class
title: "interest rate cap option"
description: "interest rate derivative in which the buyer receives payments at the end of each period in which the interest rate exceeds the agreed strike price"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/InterestRateCapOption
tags: [DER, Release]
detail: "The interest in each period is effectively capped by the strike rate. That is, the rate of interest may not go above the strike rate because the holder is expected to exercise the option to take the strike as the rate of interest instead."
examples:
  - "An example of a cap would be an agreement to receive a payment for each month the LIBOR rate exceeds 2.5%."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/InterestRateOption.md", provenance: fibo}
---

interest rate derivative in which the buyer receives payments at the end of each period in which the interest rate exceeds the agreed strike price

### Relationships
- is-a: [InterestRateOption](/DER/DerivativesContracts/Options/InterestRateOption.md)
