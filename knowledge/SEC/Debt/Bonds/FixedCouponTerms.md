---
type: FIBO Class
title: "fixed coupon terms"
description: "terms for payment of interest on a bond with a fixed interest rate"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponTerms
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/CouponPaymentTerms.md", provenance: fibo}
  - {type: has-interest-rate, target: "/FBC/DebtAndEquities/Debt/FixedInterestRate.md", provenance: fibo}
---

terms for payment of interest on a bond with a fixed interest rate

### Relationships
- is-a: [CouponPaymentTerms](/SEC/Debt/Bonds/CouponPaymentTerms.md)
- has-interest-rate: [FixedInterestRate](/FBC/DebtAndEquities/Debt/FixedInterestRate.md)
