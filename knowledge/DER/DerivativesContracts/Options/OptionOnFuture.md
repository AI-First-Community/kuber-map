---
type: FIBO Class
title: "option on future"
description: "option that gives the holder the right, but not the obligation, to buy or sell a specific futures contract at a specified price on or before the option's expiration date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionOnFuture
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/VanillaOption.md", provenance: fibo}
  - {type: has-exercise-terms, target: "/SEC/Debt/ExerciseConventions/AmericanExerciseTerms.md", provenance: fibo}
---

option that gives the holder the right, but not the obligation, to buy or sell a specific futures contract at a specified price on or before the option's expiration date

### Relationships
- is-a: [VanillaOption](/DER/DerivativesContracts/Options/VanillaOption.md)
- has-exercise-terms: [AmericanExerciseTerms](/SEC/Debt/ExerciseConventions/AmericanExerciseTerms.md)
