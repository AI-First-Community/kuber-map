---
type: FIBO Class
title: "zero coupon terms"
description: "terms for payment of interest on a zero coupon bond"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponTerms
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/Bonds/FixedCouponTerms.md", provenance: fibo}
  - {type: has-interest-rate, target: "/SEC/Debt/Bonds/ZeroInterestRate.md", provenance: fibo}
---

terms for payment of interest on a zero coupon bond

### Relationships
- is-a: [BondAmortizationPaymentTerms](/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)
- is-a: [FixedCouponTerms](/SEC/Debt/Bonds/FixedCouponTerms.md)
- has-interest-rate: [ZeroInterestRate](/SEC/Debt/Bonds/ZeroInterestRate.md)
