---
type: FIBO Class
title: "coupon payment terms"
description: "terms for payment of interest on a bond"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-interest-rate, target: "/SEC/Debt/Bonds/BondCoupon.md", provenance: fibo}
  - {type: has-schedule, target: "/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md", provenance: fibo}
---

terms for payment of interest on a bond

### Relationships
- is-a: [InterestPaymentTerms](/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-interest-rate: [BondCoupon](/SEC/Debt/Bonds/BondCoupon.md)
- has-schedule: [InterestPaymentSchedule](/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md)
