---
type: FIBO Class
title: "fixed coupon bond"
description: "bond whose coupon rate and principal amount are fixed at the time of origination or sale and remain constant while the security is outstanding"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponBond
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md", provenance: fibo}
  - {type: has-interest-payment-terms, target: "/SEC/Debt/Bonds/FixedCouponTerms.md", provenance: fibo}
---

bond whose coupon rate and principal amount are fixed at the time of origination or sale and remain constant while the security is outstanding

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- is-a: [FixedIncomeSecurity](/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)
- has-interest-payment-terms: [FixedCouponTerms](/SEC/Debt/Bonds/FixedCouponTerms.md)
