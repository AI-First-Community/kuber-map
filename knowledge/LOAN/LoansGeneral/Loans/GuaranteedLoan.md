---
type: FIBO Class
title: "guaranteed loan"
description: "loan that is secured with respect to repayment of principal and interest by guaranty"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/GuaranteedLoan
tags: [LOAN, Release]
detail: "A loan guarantee is a promise by one party to assume the debt obligation of a borrower if that borrower defaults. A guarantee can be limited or unlimited, making the guarantor liable for only a portion or all of the debt. In the U.S., the term 'guaranteed loan' typically refers to a loan that is backed by a federal agency, such as the Department of Veterans Affairs or the Small Business Administration. Student loans may be guaranteed by the Student Loan Marketing Association."
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
