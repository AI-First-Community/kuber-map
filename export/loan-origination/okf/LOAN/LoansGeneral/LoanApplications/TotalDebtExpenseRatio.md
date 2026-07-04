---
type: FIBO Class
title: "total debt expense ratio"
description: "ratio of all monthly debt payments of all borrowers, including proposed expenses, with respect to the income of the borrowers as relied upon to make a credit decision"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "The debt-to-income (DTI) ratio; under US ability-to-repay / Qualified Mortgage rules it is commonly capped around 43%."
detail_provenance: curated
examples:
  - "All monthly debt ÷ income = 43% DTI used in the credit decision."
examples_provenance: curated
synonyms:
  - "back end ratio"
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
---

ratio of all monthly debt payments of all borrowers, including proposed expenses, with respect to the income of the borrowers as relied upon to make a credit decision

### Relationships
- is-a: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
