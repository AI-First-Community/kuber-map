---
type: FIBO Class
title: "business day convention"
description: "convention that enumerates the possible ways to handle a date that falls on a weekend or holiday"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
tags: [FND, Release]
detail: "Business day conventions are linked to a calendar. Calendars have working and non-working days. In the ACTUS dictionary, the rules related to business day conventions (BDCs) state that a BDC value other than N means that cash flows cannot fall on non-working days, they must be shifted to the next business day (following) or the previous on (preceding). These two simple rules get refined twofold: (1) Following modified (preceding): Same like following (preceding), however if a cash flow gets shifted into a new month, then it is shifted to preceding (following) business day; (2) Shift/calculate (SC) and calculate/shift (CS). Accrual, principal, and possibly other calculations are affected by this choice. In the case of SC first the dates are shifted and after the shift cash flows are calculated. In the case of CS it is the other way round. Business day conventions commonly include: - Following business day: Moves the date to the next business day - Modified following business day: Moves the date to the next business day, unless it would fall in the next calendar month - Preceding business day: Moves the date to the previous business day - Modified preceding business day: Moves the date to the previous business day, unless it would fall in the previous calendar month The 2006 IDSA Definitions Section 4.11, provide the following examples: FRN Convention; Eurodollar Convention. - If a payment date or period end date falls on a non-business day, it is moved to the next business day. - If there is no numerically corresponding day in a calendar month, the payment date or period end date is moved to the last business day in that month."
synonyms:
  - "business day adjustment"
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md", provenance: fibo}
  - {type: has-business-center, target: "/CMNS/Locations/BusinessCenter.md", provenance: fibo}
---

convention that enumerates the possible ways to handle a date that falls on a weekend or holiday

### Relationships
- is-a: [BusinessRecurrenceIntervalConvention](/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)
- has-business-center: [BusinessCenter](/CMNS/Locations/BusinessCenter.md)
