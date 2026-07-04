---
type: FIBO Class
title: "fund bond class unit"
description: "A fund unit which takes the form of debt in that fund."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundBondClassUnit
tags: [SEC, Provisional]
detail: "From EFAMA Review: called denominations e.g. issued in $5000 pieces. You cannot buy fractional amounts in a bond."
relations:
  - {type: is-a, target: "/SEC/Funds/Funds/FundUnit.md", provenance: fibo}
  - {type: has-expected-coupon, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundBondUnitCoupon.md", provenance: fibo}
  - {type: has-strategy, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy.md", provenance: fibo}
---

A fund unit which takes the form of debt in that fund.

### Relationships
- is-a: [FundUnit](/SEC/Funds/Funds/FundUnit.md)
- has-expected-coupon: [FundBondUnitCoupon](/SEC/Funds/CollectiveInvestmentVehicles/FundBondUnitCoupon.md)
- has-strategy: [FundUnitDistributionPolicy](/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy.md)
