---
type: FIBO Class
title: "pre-approval contract"
description: "written commitment to lend when specified conditions are met, such as finding suitable property, and unchanged creditworthiness"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalContract
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "A commitment from a lender to a borrower to extend a home purchase loan up to a certain amount, and subject to certain non-credit related conditions.  This commitment is entered into after a comprehensive analysis of the credit worthiness of the borrower is carried out. This may also include limits on the region where to purchase."
examples:
  - "A lender's written commitment to lend up to $400k subject to conditions."
examples_provenance: curated
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
