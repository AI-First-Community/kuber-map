---
type: FIBO Class
title: "notional step change event"
description: "event in which a step change in the notional amount for a given swap leg occurs"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepChangeEvent
tags: [DER, Release]
detail: "The frequency / period length of the steps in the step schedule is a multiple of the calculation period or frequency. For example, if the notional is recalculated on every calculation date, applying a new interest rate to the new notional amount, then the two frequencies are the same. If notional is updated every second calculation period, then the step schedule specifies periods that are twice as long, and so on."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/StepEvent.md", provenance: fibo}
  - {type: specifies, target: "/DER/RateDerivatives/IRSwaps/NotionalStepAmount.md", provenance: fibo}
---

event in which a step change in the notional amount for a given swap leg occurs

### Relationships
- is-a: [ContractLifecycleEventOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md)
- is-a: [StepEvent](/SEC/Debt/DebtInstruments/StepEvent.md)
- specifies: [NotionalStepAmount](/DER/RateDerivatives/IRSwaps/NotionalStepAmount.md)
