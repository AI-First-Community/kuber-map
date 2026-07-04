---
type: FIBO Class
title: "loan pool"
description: "debt pool whose consituents are loans"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/LoanPool
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
  - {type: has-member, target: "/LOAN/LoansGeneral/Loans/Loan.md", provenance: fibo}
---

debt pool whose consituents are loans

### Relationships
- is-a: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
- has-member: [Loan](/LOAN/LoansGeneral/Loans/Loan.md)
