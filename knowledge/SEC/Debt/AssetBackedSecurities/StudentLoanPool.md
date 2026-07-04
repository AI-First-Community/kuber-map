---
type: FIBO Class
title: "student loan pool"
description: "debt pool consisting of student loans"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/StudentLoanPool
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
  - {type: has-part, target: "/LOAN/LoansSpecific/StudentLoans/StudentLoan.md", provenance: fibo}
---

debt pool consisting of student loans

### Relationships
- is-a: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
- has-part: [StudentLoan](/LOAN/LoansSpecific/StudentLoans/StudentLoan.md)
