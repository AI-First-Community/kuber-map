---
type: FIBO Class
title: "equity option"
description: "option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying equity assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/EquityOption
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "For an Equity Option, one contract represents 100 shares of stock. Equity options settle in 'American style'."
examples:
  - "A listed call option on Tesla shares."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/VanillaOption.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md", provenance: fibo}
  - {type: has-exercise-style, target: "/SEC/Debt/ExerciseConventions/AmericanExerciseConvention.md", provenance: fibo}
---

option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying equity assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)

### Relationships
- is-a: [VanillaOption](/DER/DerivativesContracts/Options/VanillaOption.md)
- is-a: [EquityDerivative](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md)
- has-exercise-style: [AmericanExerciseConvention](/SEC/Debt/ExerciseConventions/AmericanExerciseConvention.md)
