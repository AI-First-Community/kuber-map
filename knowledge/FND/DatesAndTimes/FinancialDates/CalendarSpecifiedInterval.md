---
type: FIBO Class
title: "calendar-specified interval"
description: "recurrence interval that is defined as the nth day of some calendar period (such as a calendar month), and a time direction (forward from the beginning of the month, or backwards from the end)"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalendarSpecifiedInterval
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
  - {type: has-calendar-period, target: "/FND/DatesAndTimes/FinancialDates/CalendarPeriod.md", provenance: fibo}
  - {type: has-time-direction, target: "/FND/DatesAndTimes/FinancialDates/TimeDirection.md", provenance: fibo}
---

recurrence interval that is defined as the nth day of some calendar period (such as a calendar month), and a time direction (forward from the beginning of the month, or backwards from the end)

### Relationships
- is-a: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- has-calendar-period: [CalendarPeriod](/FND/DatesAndTimes/FinancialDates/CalendarPeriod.md)
- has-time-direction: [TimeDirection](/FND/DatesAndTimes/FinancialDates/TimeDirection.md)
