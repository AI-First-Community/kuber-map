---
type: FIBO Class
title: "variable coupon bond"
description: "bond that has a floating interest rate"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponBond
tags: [SEC, Release]
detail: "The rate adjusts according to a predetermined formula outlined in the bond's prospectus or official statement."
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/VariableIncomeBond.md", provenance: fibo}
  - {type: has-interest-rate, target: "/SEC/Debt/Bonds/BondVariableCoupon.md", provenance: fibo}
---

bond that has a floating interest rate

### Relationships
- is-a: [VariableIncomeBond](/SEC/Debt/Bonds/VariableIncomeBond.md)
- has-interest-rate: [BondVariableCoupon](/SEC/Debt/Bonds/BondVariableCoupon.md)
