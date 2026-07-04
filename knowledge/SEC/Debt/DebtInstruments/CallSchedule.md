---
type: FIBO Class
title: "call schedule"
description: "a schedule of call prices and when they are in effect"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallSchedule
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Debt/DebtInstruments/CallEvent.md", provenance: fibo}
---

a schedule of call prices and when they are in effect

### Relationships
- is-a: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- comprises: [CallEvent](/SEC/Debt/DebtInstruments/CallEvent.md)
