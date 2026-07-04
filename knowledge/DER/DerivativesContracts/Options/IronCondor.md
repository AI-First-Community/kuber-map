---
type: FIBO Class
title: "iron condor"
description: "condor strategy consisting of two puts (one long and one short) and two calls (one long and one short), and four strike prices, all with the same expiration date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/IronCondor
tags: [DER, Release]
detail: "The iron condor earns the maximum profit when the underlying asset closes between the middle strike prices at expiration. In other words, the goal is to profit from low volatility in the underlying asset."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/CondorSpread.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
  - {type: has-exercise-price, target: "/DER/DerivativesContracts/Options/StrikePrice.md", provenance: fibo}
---

condor strategy consisting of two puts (one long and one short) and two calls (one long and one short), and four strike prices, all with the same expiration date

### Relationships
- is-a: [CondorSpread](/DER/DerivativesContracts/Options/CondorSpread.md)
- comprises: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- comprises: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
- has-exercise-price: [StrikePrice](/DER/DerivativesContracts/Options/StrikePrice.md)
