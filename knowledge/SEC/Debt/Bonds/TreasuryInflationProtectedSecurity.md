---
type: FIBO Class
title: "treasury inflation-protected security"
description: "variable income bond whose principal is indexed to inflation or deflation and thus changes over the life of the security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryInflationProtectedSecurity
tags: [SEC, Release]
detail: "Treasury Inflation-Protected Securities, or TIPS, provide protection against inflation. The principal of a TIPS increases with inflation and decreases with deflation, as measured by the Consumer Price Index. When a TIPS matures, you are paid the adjusted principal or original principal, whichever is greater."
synonyms:
  - "TIPS"
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/InflationLinkedBond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/Bonds/USTreasurySecurity.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/Bonds/VariablePrincipalBond.md", provenance: fibo}
---

variable income bond whose principal is indexed to inflation or deflation and thus changes over the life of the security

### Relationships
- is-a: [InflationLinkedBond](/SEC/Debt/Bonds/InflationLinkedBond.md)
- is-a: [USTreasurySecurity](/SEC/Debt/Bonds/USTreasurySecurity.md)
- is-a: [VariablePrincipalBond](/SEC/Debt/Bonds/VariablePrincipalBond.md)
