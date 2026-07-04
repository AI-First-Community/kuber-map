---
type: FIBO Class
title: "fund bond unit coupon"
description: "A fixed coupon paid out to holders of the Fund Bond Unit."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundBondUnitCoupon
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
  - {type: has-policy-terms, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundCouponPolicy.md", provenance: fibo}
---

A fixed coupon paid out to holders of the Fund Bond Unit.

### Relationships
- is-a: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
- has-policy-terms: [FundCouponPolicy](/SEC/Funds/CollectiveInvestmentVehicles/FundCouponPolicy.md)
