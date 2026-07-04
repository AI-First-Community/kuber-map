---
type: FIBO Class
title: "step schedule"
description: "schedule specifying the date(s) and change in a contractual term(s), e.g., rate or notional amount, for a contract that has a feature where stipulated changes occur at specified intervals or on specified dates"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepSchedule
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Debt/DebtInstruments/StepEvent.md", provenance: fibo}
---

schedule specifying the date(s) and change in a contractual term(s), e.g., rate or notional amount, for a contract that has a feature where stipulated changes occur at specified intervals or on specified dates

### Relationships
- is-a: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- comprises: [StepEvent](/SEC/Debt/DebtInstruments/StepEvent.md)
