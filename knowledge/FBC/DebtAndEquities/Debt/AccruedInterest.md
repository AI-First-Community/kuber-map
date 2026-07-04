---
type: FIBO Class
title: "accrued interest"
description: "amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/AccruedInterest
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/Interest.md", provenance: fibo}
  - {type: has-as-of-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
---

amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out

### Relationships
- is-a: [Interest](/FBC/DebtAndEquities/Debt/Interest.md)
- has-as-of-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
