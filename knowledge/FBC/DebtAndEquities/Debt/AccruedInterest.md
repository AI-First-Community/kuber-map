---
type: FIBO Class
title: "accrued interest"
description: "amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/AccruedInterest
tags: [FBC, Release]
detail: "Accrued interest refers to the interest that has accumulated on a bond or other financial obligation since the last interest payment up to, but not including, the settlement date. This interest is earned over time but not yet paid out to the bondholder, for example. If this is a dirty price, this is the amount of accrued interest that is included in the price. This is therefore passed on to the purchaser of the bond or debt instrument."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/Interest.md", provenance: fibo}
  - {type: has-as-of-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
---

amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out

### Relationships
- is-a: [Interest](/FBC/DebtAndEquities/Debt/Interest.md)
- has-as-of-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
