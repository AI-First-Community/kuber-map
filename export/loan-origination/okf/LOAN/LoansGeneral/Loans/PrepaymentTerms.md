---
type: FIBO Class
title: "pre-payment terms"
description: "principal repayment terms related to payment of the loan prior to maturity"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PrepaymentTerms
tags: [LOAN, Release]
core: true
detail: "Prepayment may or may not involve refinancing with the same lender. Prepayment terms include any prepayment penalty period, penalty amount and whether or not there is provision for waiver of the penalty, and any conditions related to making additional payments or payments over and above the expected installment payment over the lifetime of the loan."
examples:
  - "A 2% prepayment penalty if repaid within 3 years"
  - "Penalty-free prepayment"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md", provenance: fibo}
  - {type: has-pre-payment-penalty-term, target: "/CMNS/DatesAndTimes/ExplicitDuration.md", provenance: fibo}
---

principal repayment terms related to payment of the loan prior to maturity

### Relationships
- is-a: [PrincipalRepaymentTerms](/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md)
- has-pre-payment-penalty-term: [ExplicitDuration](/CMNS/DatesAndTimes/ExplicitDuration.md)
