---
type: FIBO Class
title: "stepped coupon terms"
description: "coupon payment terms for securities with a coupon that increases (steps up) while the bond is outstanding"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SteppedCouponTerms
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/CouponPaymentTerms.md", provenance: fibo}
  - {type: has-schedule, target: "/SEC/Debt/DebtInstruments/StepSchedule.md", provenance: fibo}
---

coupon payment terms for securities with a coupon that increases (steps up) while the bond is outstanding

### Relationships
- is-a: [CouponPaymentTerms](/SEC/Debt/Bonds/CouponPaymentTerms.md)
- has-schedule: [StepSchedule](/SEC/Debt/DebtInstruments/StepSchedule.md)
