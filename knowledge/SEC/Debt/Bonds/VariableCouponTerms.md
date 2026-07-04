---
type: FIBO Class
title: "variable coupon terms"
description: "contractual terms specifying the calculation of the interest rate for a variable coupon bond"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponTerms
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/CouponPaymentTerms.md", provenance: fibo}
  - {type: has-expression, target: "/SEC/Debt/Bonds/VariableInterestCalculationFormula.md", provenance: fibo}
  - {type: is-based-on, target: "/IND/Indicators/Indicators/MarketRate.md", provenance: fibo}
---

contractual terms specifying the calculation of the interest rate for a variable coupon bond

### Relationships
- is-a: [CouponPaymentTerms](/SEC/Debt/Bonds/CouponPaymentTerms.md)
- has-expression: [VariableInterestCalculationFormula](/SEC/Debt/Bonds/VariableInterestCalculationFormula.md)
- is-based-on: [MarketRate](/IND/Indicators/Indicators/MarketRate.md)
