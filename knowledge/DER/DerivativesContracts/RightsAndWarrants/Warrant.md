---
type: FIBO Class
title: "warrant"
description: "entitlement that permits the holder to purchase a specified amount of a financial instrument, commodity, currency or other asset during a specified period at a specified price"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
tags: [DER, Release]
detail: "Warrants are for any kind of instrument. Warrants may be privately issued and may not necessarily be traded on an exchange."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md", provenance: fibo}
  - {type: has-exercise-terms, target: "/SEC/Debt/ExerciseConventions/ExerciseTerms.md", provenance: fibo}
---

entitlement that permits the holder to purchase a specified amount of a financial instrument, commodity, currency or other asset during a specified period at a specified price

### Relationships
- is-a: [Entitlement](/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)
- has-exercise-terms: [ExerciseTerms](/SEC/Debt/ExerciseConventions/ExerciseTerms.md)
