---
type: FIBO Class
title: "all borrowers' monthly income"
description: "total monthly qualifying income for all borrowers on the loan"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome
tags: [LOAN, Provisional]
relations:
  - {type: is-based-on, target: "/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md", provenance: fibo}
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/Income.md", provenance: fibo}
---

total monthly qualifying income for all borrowers on the loan

### Relationships
- is-based-on: [BorrowerMonthlyIncome](/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md)
- is-a: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-a: [Income](/FND/Accounting/AccountingEquity/Income.md)
