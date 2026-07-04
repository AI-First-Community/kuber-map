---
type: FIBO Class
title: "bullet bond"
description: "bond whose entire principal value is paid on the maturity date, rather than amortized over its lifetime"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BulletBond
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: has-repayment-terms, target: "/SEC/Debt/Bonds/BulletPrincipalRepaymentTerms.md", provenance: fibo}
---

bond whose entire principal value is paid on the maturity date, rather than amortized over its lifetime

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- has-repayment-terms: [BulletPrincipalRepaymentTerms](/SEC/Debt/Bonds/BulletPrincipalRepaymentTerms.md)
