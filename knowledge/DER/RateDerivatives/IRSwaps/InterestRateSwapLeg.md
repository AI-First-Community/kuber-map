---
type: FIBO Class
title: "interest rate swap leg"
description: "swap leg that has an interest rate payment stream, including both a parametric and cashflow representation for the stream of payments"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg
tags: [DER, Release]
synonyms:
  - "interest rate swap stream"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/RateBasedLeg.md", provenance: fibo}
  - {type: has-business-recurrence-interval-convention, target: "/FBC/DebtAndEquities/Debt/DayCountConvention.md", provenance: fibo}
  - {type: has-payment-schedule, target: "/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md", provenance: fibo}
  - {type: has-schedule, target: "/DER/RateDerivatives/IRSwaps/NotionalStepSchedule.md", provenance: fibo}
  - {type: specifies, target: "/FBC/DebtAndEquities/Debt/InterestCalculationSchedule.md", provenance: fibo}
  - {type: specifies, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

swap leg that has an interest rate payment stream, including both a parametric and cashflow representation for the stream of payments

### Relationships
- is-a: [RateBasedLeg](/DER/DerivativesContracts/Swaps/RateBasedLeg.md)
- has-business-recurrence-interval-convention: [DayCountConvention](/FBC/DebtAndEquities/Debt/DayCountConvention.md)
- has-payment-schedule: [InterestPaymentSchedule](/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md)
- has-schedule: [NotionalStepSchedule](/DER/RateDerivatives/IRSwaps/NotionalStepSchedule.md)
- specifies: [InterestCalculationSchedule](/FBC/DebtAndEquities/Debt/InterestCalculationSchedule.md)
- specifies: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
