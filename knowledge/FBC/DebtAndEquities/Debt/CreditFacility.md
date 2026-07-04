---
type: FIBO Class
title: "credit facility"
description: "credit agreement that allows the borrower to periodically take out money over an extended period of time rather than reapplying for a loan every time they need funds"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility
tags: [FBC, Release]
detail: "Credit facilities include revolving loans/lines of credit, committed facilities, letters of credit, and most retail credit accounts. They may define sub-facilities to which the lender is prepared to commit for specific purposes."
synonyms:
  - "master commitment"
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/ConditionPrecedent.md", provenance: fibo}
  - {type: has-member, target: "/FBC/DebtAndEquities/Debt/SubFacility.md", provenance: fibo}
  - {type: has-member, target: "/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

credit agreement that allows the borrower to periodically take out money over an extended period of time rather than reapplying for a loan every time they need funds

### Relationships
- is-a: [CreditAgreementRepaidPeriodically](/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)
- has-contractual-element: [ConditionPrecedent](/FND/Agreements/Contracts/ConditionPrecedent.md)
- has-member: [SubFacility](/FBC/DebtAndEquities/Debt/SubFacility.md)
- has-member: [PromissoryNote](/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
