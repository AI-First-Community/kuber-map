---
type: FIBO Class
title: "straddle"
description: "neutral option trading strategy that involves simultaneously buying both a put option and a call option for the underlying security with the same strike price and the same expiration date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Straddle
tags: [DER, Release]
detail: "The strategy is profitable only when the value of the underlier varies (rises or falls) from the strike price by more than the total premium paid."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/OptionTradingStrategy.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
---

neutral option trading strategy that involves simultaneously buying both a put option and a call option for the underlying security with the same strike price and the same expiration date

### Relationships
- is-a: [OptionTradingStrategy](/DER/DerivativesContracts/Options/OptionTradingStrategy.md)
- comprises: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- comprises: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
