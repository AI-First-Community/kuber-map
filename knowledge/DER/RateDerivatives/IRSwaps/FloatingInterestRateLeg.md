---
type: FIBO Class
title: "floating interest rate leg"
description: "floating leg in which variable interest is paid on some notional amount, linked to some underlying interest reference rate"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg
tags: [DER, Release]
detail: "Instead of an absolute rate you have either a variable reference rate or fixed reference rate and an offset that varies in some way, called a spread (same as margin in floating rate notes)."
synonyms:
  - "floating interest rate swap stream"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/FloatingLeg.md", provenance: fibo}
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md", provenance: fibo}
  - {type: has-schedule, target: "/FBC/DebtAndEquities/Debt/InterestCalculationSchedule.md", provenance: fibo}
  - {type: has-schedule, target: "/FBC/DebtAndEquities/Debt/InterestRateResetSchedule.md", provenance: fibo}
  - {type: specifies, target: "/FBC/DebtAndEquities/Debt/InterestRateReset.md", provenance: fibo}
  - {type: specifies, target: "/FBC/DebtAndEquities/Debt/InterestRateSettingEvent.md", provenance: fibo}
---

floating leg in which variable interest is paid on some notional amount, linked to some underlying interest reference rate

### Relationships
- is-a: [FloatingLeg](/DER/DerivativesContracts/Swaps/FloatingLeg.md)
- is-a: [InterestRateSwapLeg](/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md)
- has-schedule: [InterestCalculationSchedule](/FBC/DebtAndEquities/Debt/InterestCalculationSchedule.md)
- has-schedule: [InterestRateResetSchedule](/FBC/DebtAndEquities/Debt/InterestRateResetSchedule.md)
- specifies: [InterestRateReset](/FBC/DebtAndEquities/Debt/InterestRateReset.md)
- specifies: [InterestRateSettingEvent](/FBC/DebtAndEquities/Debt/InterestRateSettingEvent.md)
