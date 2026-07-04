---
type: FIBO Class
title: "step up bond"
description: "bond with a coupon that increases (steps up) while the bond is outstanding"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/StepUpBond
tags: [SEC, Release]
detail: "The step change may be one time, or occur according to a schedule or at regular intervals."
synonyms:
  - "step down bond"
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md", provenance: fibo}
  - {type: has-interest-payment-terms, target: "/SEC/Debt/Bonds/SteppedCouponTerms.md", provenance: fibo}
---

bond with a coupon that increases (steps up) while the bond is outstanding

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- is-a: [FixedIncomeSecurity](/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)
- has-interest-payment-terms: [SteppedCouponTerms](/SEC/Debt/Bonds/SteppedCouponTerms.md)
