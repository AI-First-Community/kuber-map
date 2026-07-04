---
type: FIBO Class
title: "open-end credit"
description: "credit agreement that may be extended up to an agreed credit limit and paid down at any time within the period of the line, if any, and on which interest is charged only on the outstanding balance"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OpenEndCredit
tags: [LOAN, Release]
detail: "There is a credit limit most of the time, with exceptions including reverse mortgages with tenure payment. The borrower has the option of paying off the outstanding balance, without penalty, or making installment payments."
examples:
  - "Credit card and overdraft lines of credit are among the most widely used forms of open-end credit."
synonyms:
  - "charge account credit"
  - "revolving credit"
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
  - {type: has-credit-limit, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

credit agreement that may be extended up to an agreed credit limit and paid down at any time within the period of the line, if any, and on which interest is charged only on the outstanding balance

### Relationships
- is-a: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- has-credit-limit: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
