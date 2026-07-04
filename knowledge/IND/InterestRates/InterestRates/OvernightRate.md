---
type: FIBO Class
title: "overnight rate"
description: "reference rate that is an interest rate at which a depository institution lends funds to another depository institution (short-term), or the interest rate the central bank charges a financial institution to borrow money overnight"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/OvernightRate
tags: [IND, Release]
detail: "The overnight rate is the lowest available interest rate, and as such, it is only available to the most creditworthy institutions. It is the underlying rate for Overnight Interest Rate Swaps (IOS)."
relations:
  - {type: is-a, target: "/IND/InterestRates/InterestRates/ReferenceInterestRate.md", provenance: fibo}
  - {type: has-tenor, target: "/IND/InterestRates/InterestRates/OneDay.md", provenance: fibo}
---

reference rate that is an interest rate at which a depository institution lends funds to another depository institution (short-term), or the interest rate the central bank charges a financial institution to borrow money overnight

### Relationships
- is-a: [ReferenceInterestRate](/IND/InterestRates/InterestRates/ReferenceInterestRate.md)
- has-tenor: [OneDay](/IND/InterestRates/InterestRates/OneDay.md)
