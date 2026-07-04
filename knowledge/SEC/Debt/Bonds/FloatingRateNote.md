---
type: FIBO Class
title: "floating rate note"
description: "bond with a variable interest rate based on a published reference interest rate"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FloatingRateNote
tags: [SEC, Release]
core: true
detail: "The adjustments to the interest rate (coupon) are made periodically, usually on a quarterly or monthly basis, and are tied to a certain money-market index. Also known as a 'floater'. For example six months USD LIBOR + 0.20%."
examples:
  - "A 3-year note paying SOFR + 0.50%, resetting quarterly."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/VariableCouponBond.md", provenance: fibo}
  - {type: has-interest-rate, target: "/IND/InterestRates/InterestRates/ReferenceInterestRate.md", provenance: fibo}
---

bond with a variable interest rate based on a published reference interest rate

### Relationships
- is-a: [VariableCouponBond](/SEC/Debt/Bonds/VariableCouponBond.md)
- has-interest-rate: [ReferenceInterestRate](/IND/InterestRates/InterestRates/ReferenceInterestRate.md)
