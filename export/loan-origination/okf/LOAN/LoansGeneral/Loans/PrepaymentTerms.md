---
type: FIBO Class
title: "pre-payment terms"
description: "principal repayment terms related to payment of the loan prior to maturity"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PrepaymentTerms
tags: [LOAN, Release]
core: true
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md", provenance: fibo}
  - {type: has-pre-payment-penalty-term, target: "/CMNS/DatesAndTimes/ExplicitDuration.md", provenance: fibo}
---

principal repayment terms related to payment of the loan prior to maturity

### Relationships
- is-a: [PrincipalRepaymentTerms](/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md)
- has-pre-payment-penalty-term: [ExplicitDuration](/CMNS/DatesAndTimes/ExplicitDuration.md)
