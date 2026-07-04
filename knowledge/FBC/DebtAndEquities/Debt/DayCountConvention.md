---
type: FIBO Class
title: "day-count convention"
description: "a business recurrence interval convention that is used to calculate the number of days in an interest payment, which applies to the amount of accrued interest or the present value for debt instruments"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention
tags: [FBC, Release]
detail: "Day-count conventions apply to swaps, mortgages and forward rate agreements as well as bonds, each of which has its own day-count convention, which varies depending on the type of instrument, whether the interest rate is fixed or floating, and the country of issuance. Among the most common conventions are 30/360 or 365, actual/360 or 365, and actual/actual. A 30/360 convention assumes 30 days in a month and 360 days in a year. An actual/360 convention assumes the actual number of days in the given month and 360 days in the year. An actual/ actual convention uses the actual number of days in the given interest period and year."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
---

a business recurrence interval convention that is used to calculate the number of days in an interest payment, which applies to the amount of accrued interest or the present value for debt instruments

### Relationships
- is-a: [BusinessRecurrenceIntervalConvention](/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
