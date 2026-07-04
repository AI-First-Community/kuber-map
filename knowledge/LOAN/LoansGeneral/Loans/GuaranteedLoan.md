---
type: FIBO Class
title: "guaranteed loan"
description: "loan that is secured with respect to repayment of principal and interest by guaranty"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/GuaranteedLoan
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/SecuredLoan.md", provenance: fibo}
  - {type: comprises, target: "/FBC/DebtAndEquities/Guaranty/Guaranty.md", provenance: fibo}
  - {type: has-guarantor, target: "/FBC/DebtAndEquities/Guaranty/Guarantor.md", provenance: fibo}
---

loan that is secured with respect to repayment of principal and interest by guaranty

### Relationships
- is-a: [SecuredLoan](/LOAN/LoansGeneral/Loans/SecuredLoan.md)
- comprises: [Guaranty](/FBC/DebtAndEquities/Guaranty/Guaranty.md)
- has-guarantor: [Guarantor](/FBC/DebtAndEquities/Guaranty/Guarantor.md)
