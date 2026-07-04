---
type: FIBO Class
title: "open-end credit"
description: "credit agreement that may be extended up to an agreed credit limit and paid down at any time within the period of the line, if any, and on which interest is charged only on the outstanding balance"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OpenEndCredit
tags: [LOAN, Release]
relations:
  - {type: has-credit-limit, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
---

credit agreement that may be extended up to an agreed credit limit and paid down at any time within the period of the line, if any, and on which interest is charged only on the outstanding balance

### Relationships
- has-credit-limit: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-a: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
