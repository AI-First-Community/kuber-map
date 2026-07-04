---
type: FIBO Class
title: "pre-approval contract"
description: "written commitment to lend when specified conditions are met, such as finding suitable property, and unchanged creditworthiness"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalContract
tags: [LOAN, Provisional]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-approved-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-interest-rate, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
---

written commitment to lend when specified conditions are met, such as finding suitable property, and unchanged creditworthiness

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-approved-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-interest-rate: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
