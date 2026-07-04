---
type: FIBO Class
title: "lookback strike terms"
description: "terms specifying the value of the underlying asset based on analysis during a specific period, typically ending in the maturity of the option, whereby the payoff is determined by comparing the strike price with the value of the selected price"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms
tags: [DER, Release]
detail: "In the case of a fixed strike, the terms depend on whether the option is a call or put. If it is a call, the calculated payout reflects the difference between a running maximum value of the observable during the lookback period, and the pre-agreed strike. The payoff may either be the difference between a fixed, pre-agreed Strike Price and the observable, or the difference between the best or worst valuable of the observable and the value of that same observable at maturity of the contract (these are the Fixed and Floating lookback terms respectively). This (per review at Nordea) is not mutually exclusive with the terms for Fixed Strike and Resettable Strike, that is, either of those kinds of strike terms may apply, and Lookback strike terms may also apply."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md", provenance: fibo}
  - {type: has-argument, target: "/IND/Indicators/Indicators/PriceStructure.md", provenance: fibo}
  - {type: has-expression, target: "/DER/DerivativesContracts/ExoticOptions/FixedLookbackStrikeExpression.md", provenance: fibo}
  - {type: has-expression, target: "/DER/DerivativesContracts/ExoticOptions/FloatingLookbackStrikeExpression.md", provenance: fibo}
  - {type: has-lookback-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

terms specifying the value of the underlying asset based on analysis during a specific period, typically ending in the maturity of the option, whereby the payoff is determined by comparing the strike price with the value of the selected price

### Relationships
- is-a: [DerivativeTerms](/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- has-argument: [PriceStructure](/IND/Indicators/Indicators/PriceStructure.md)
- has-expression: [FixedLookbackStrikeExpression](/DER/DerivativesContracts/ExoticOptions/FixedLookbackStrikeExpression.md)
- has-expression: [FloatingLookbackStrikeExpression](/DER/DerivativesContracts/ExoticOptions/FloatingLookbackStrikeExpression.md)
- has-lookback-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
