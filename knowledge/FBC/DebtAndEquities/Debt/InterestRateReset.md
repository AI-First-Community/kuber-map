---
type: FIBO Class
title: "interest rate reset"
description: "event reflecting a potential adjustment to an interest rate, typically corresponding to a change in the underlying benchmark interest rate or index specified in the contract"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateReset
tags: [FBC, Release]
detail: "Note that depending on the contract, a rate reset can occur daily or on some other timetable, and depending on the underlying benchmark, the actual rate may or may not change. Rate resets may be associated with variable interest rate loans, scheduled reset dates for loans and other debt instruments, for example, interest rate swaps, certain kinds of bonds, and the like. The date on which interest is (re)calculated may be an explicit or date relative."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/InterestCalculation.md", provenance: fibo}
---

event reflecting a potential adjustment to an interest rate, typically corresponding to a change in the underlying benchmark interest rate or index specified in the contract

### Relationships
- is-a: [InterestCalculation](/FBC/DebtAndEquities/Debt/InterestCalculation.md)
