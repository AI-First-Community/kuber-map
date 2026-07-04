---
type: FIBO Class
title: "option"
description: "derivative instrument that grants to the holder either the privilege to purchase or the privilege to sell the assets specified at a predetermined price or formula at or within a time period in the future"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
tags: [FBC, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "A contract giving the right to buy 100 Apple shares at $200 by December."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md", provenance: fibo}
  - {type: has-calculated-market-value, target: "/DER/DerivativesContracts/Options/OptionPremium.md", provenance: fibo}
  - {type: has-exercise-price, target: "/DER/DerivativesContracts/Options/StrikePrice.md", provenance: fibo}
  - {type: has-exercise-schedule, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: has-exercise-style, target: "/SEC/Debt/ExerciseConventions/ExerciseConvention.md", provenance: fibo}
  - {type: has-expiration-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-option-holder, target: "/DER/DerivativesContracts/Options/OptionHolder.md", provenance: fibo}
  - {type: has-option-writer, target: "/DER/DerivativesContracts/Options/OptionIssuer.md", provenance: fibo}
---

derivative instrument that grants to the holder either the privilege to purchase or the privilege to sell the assets specified at a predetermined price or formula at or within a time period in the future

### Relationships
- is-a: [DerivativeInstrument](/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)
- has-calculated-market-value: [OptionPremium](/DER/DerivativesContracts/Options/OptionPremium.md)
- has-exercise-price: [StrikePrice](/DER/DerivativesContracts/Options/StrikePrice.md)
- has-exercise-schedule: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- has-exercise-style: [ExerciseConvention](/SEC/Debt/ExerciseConventions/ExerciseConvention.md)
- has-expiration-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-option-holder: [OptionHolder](/DER/DerivativesContracts/Options/OptionHolder.md)
- has-option-writer: [OptionIssuer](/DER/DerivativesContracts/Options/OptionIssuer.md)
