---
type: FIBO Class
title: "pre-approval request"
description: "request from a potential borrower that a lender commit to pre-approving the borrower for a loan of up to a specified amount of money"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest
tags: [LOAN, Provisional]
core: true
detail: "This may also include limits on the region where to purchase."
examples:
  - "A buyer asking a lender to pre-approve them for a $400k mortgage."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Reporting/RequestActivity.md", provenance: fibo}
  - {type: has-borrower, target: "/FBC/DebtAndEquities/Debt/Borrower.md", provenance: fibo}
  - {type: has-requested-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

request from a potential borrower that a lender commit to pre-approving the borrower for a loan of up to a specified amount of money

### Relationships
- is-a: [RequestActivity](/FND/Arrangements/Reporting/RequestActivity.md)
- has-borrower: [Borrower](/FBC/DebtAndEquities/Debt/Borrower.md)
- has-requested-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
