---
type: FIBO Class
title: "court judgment"
description: "decision by a court or other tribunal that resolves a controversy and determines the rights and obligations of the parties"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CourtJudgment
tags: [LOAN, Provisional]
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/LoanEvents/LegalProceeding.md", provenance: fibo}
  - {type: has-judgement-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-delivered-by, target: "/FND/Law/LegalCore/CourtOfLaw.md", provenance: fibo}
---

decision by a court or other tribunal that resolves a controversy and determines the rights and obligations of the parties

### Relationships
- is-a: [LegalProceeding](/LOAN/LoansGeneral/LoanEvents/LegalProceeding.md)
- has-judgement-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-delivered-by: [CourtOfLaw](/FND/Law/LegalCore/CourtOfLaw.md)
