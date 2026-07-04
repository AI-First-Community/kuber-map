---
type: FIBO Class
title: "low exercise price option"
description: "exotic option that is a European-style call option with an exercise price of one cent that mimics a futures contract"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LowExercisePriceOption
tags: [DER, Release]
detail: "LEPOs function as deep-in-the-money options similar to the stock itself. Both buyer and seller of a LEPO operate on margin. LEPO options are not available on any U.S. exchanges. Since the strike price is so close to zero, the investor purchasing the LEPO gains most of the features of owning the share directly with the major exceptions of dividends and voting rights. They are only available with European style expirations."
synonyms:
  - "LEPO"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
  - {type: has-exercise-style, target: "/SEC/Debt/ExerciseConventions/EuropeanExerciseConvention.md", provenance: fibo}
---

exotic option that is a European-style call option with an exercise price of one cent that mimics a futures contract

### Relationships
- is-a: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
- has-exercise-style: [EuropeanExerciseConvention](/SEC/Debt/ExerciseConventions/EuropeanExerciseConvention.md)
