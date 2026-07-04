---
type: FIBO Class
title: "borrower monthly income"
description: "total monthly qualifying income of a potential borrower"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome
tags: [LOAN, Provisional]
core: true
detail: "A key underwriting input; combined with monthly debt obligations it yields the debt-to-income ratio that drives the credit decision."
detail_provenance: curated
examples:
  - "$8,000/month gross qualifying income from salary plus bonus."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/Income.md", provenance: fibo}
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-party-role, target: "/FBC/DebtAndEquities/Debt/Borrower.md", provenance: fibo}
---

total monthly qualifying income of a potential borrower

### Relationships
- is-a: [Income](/FND/Accounting/AccountingEquity/Income.md)
- is-a: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-party-role: [Borrower](/FBC/DebtAndEquities/Debt/Borrower.md)
