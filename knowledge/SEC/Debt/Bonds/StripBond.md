---
type: FIBO Class
title: "strip bond"
description: "bond that is part of a series of bonds formed by selling each interest payment and the principal amount of a bond as separate zero coupon bonds."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/StripBond
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/ZeroCouponBond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/Strip.md", provenance: fibo}
  - {type: is-based-on, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
---

bond that is part of a series of bonds formed by selling each interest payment and the principal amount of a bond as separate zero coupon bonds.

### Relationships
- is-a: [ZeroCouponBond](/SEC/Debt/Bonds/ZeroCouponBond.md)
- is-a: [Strip](/SEC/Debt/DebtInstruments/Strip.md)
- is-based-on: [Bond](/SEC/Debt/Bonds/Bond.md)
