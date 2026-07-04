---
type: FIBO Class
title: "secured loan"
description: "loan in which the borrower pledges some asset via a security agreement as collateral for the loan, or that is secured via third-party guarantee"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/SecuredLoan
tags: [LOAN, Release]
core: true
detail: "Backed by pledged assets or a guarantee, which lowers the lender's risk relative to an unsecured loan and usually the borrower's rate as well."
detail_provenance: curated
examples:
  - "A mortgage (secured by a home)"
  - "A pawn loan (secured by an item)"
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/Loan.md", provenance: fibo}
---

loan in which the borrower pledges some asset via a security agreement as collateral for the loan, or that is secured via third-party guarantee

### Relationships
- is-a: [Loan](/LOAN/LoansGeneral/Loans/Loan.md)
