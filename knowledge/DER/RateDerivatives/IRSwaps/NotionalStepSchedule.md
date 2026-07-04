---
type: FIBO Class
title: "notional step schedule"
description: "schedule of changes in the notional amount on which interest is paid, comprising the regular sequence of step events"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepSchedule
tags: [DER, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/StepSchedule.md", provenance: fibo}
  - {type: has-occurrence, target: "/DER/RateDerivatives/IRSwaps/NotionalStepChangeEvent.md", provenance: fibo}
  - {type: has-recurrence-interval, target: "/DER/RateDerivatives/IRSwaps/NotionalStepPeriodLength.md", provenance: fibo}
---

schedule of changes in the notional amount on which interest is paid, comprising the regular sequence of step events

### Relationships
- is-a: [ProjectedContractEventSchedule](/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- is-a: [StepSchedule](/SEC/Debt/DebtInstruments/StepSchedule.md)
- has-occurrence: [NotionalStepChangeEvent](/DER/RateDerivatives/IRSwaps/NotionalStepChangeEvent.md)
- has-recurrence-interval: [NotionalStepPeriodLength](/DER/RateDerivatives/IRSwaps/NotionalStepPeriodLength.md)
