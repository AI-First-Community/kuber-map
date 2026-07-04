---
type: FIBO Class
title: "variable principal bond"
description: "bond whose principal adjusts over time with changes in an index"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariablePrincipalBond
tags: [SEC, Release]
detail: "The principal on variable principal bonds adjusts line with an index such as inflation or GDP. For example, for a bond linked to the CPI, if inflation rises two percent the principal increases by 2 percent. The coupon rate is typically fixed. The best-known example is TIPS or Treasury Inflation Protected Bonds, which are linked to the CPI. TIPs offer a real or inflation adjusted rate of return."
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/VariableIncomeBond.md", provenance: fibo}
  - {type: defines-terms-for, target: "/SEC/Debt/Bonds/VariableDebtPrincipal.md", provenance: fibo}
---

bond whose principal adjusts over time with changes in an index

### Relationships
- is-a: [VariableIncomeBond](/SEC/Debt/Bonds/VariableIncomeBond.md)
- defines-terms-for: [VariableDebtPrincipal](/SEC/Debt/Bonds/VariableDebtPrincipal.md)
