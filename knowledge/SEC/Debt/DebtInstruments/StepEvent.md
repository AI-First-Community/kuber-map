---
type: FIBO Class
title: "step event"
description: "event that prescribes a change in a contractual term, such as a rate or notional amount, for a given contract"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepEvent
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/CalculationEvent.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/PrescriptiveEvent.md", provenance: fibo}
---

event that prescribes a change in a contractual term, such as a rate or notional amount, for a given contract

### Relationships
- is-a: [CalculationEvent](/FND/DatesAndTimes/Occurrences/CalculationEvent.md)
- is-a: [PrescriptiveEvent](/SEC/Debt/DebtInstruments/PrescriptiveEvent.md)
