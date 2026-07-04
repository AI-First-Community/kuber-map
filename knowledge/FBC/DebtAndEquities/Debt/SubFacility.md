---
type: FIBO Class
title: "sub-facility"
description: "portion of a credit facility extended to the borrower for some purpose, possibly per some schedule specified in the facility"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SubFacility
tags: [FBC, Release]
detail: "Each sub-facility may have separate terms, and may be or include individual promissory notes, depending on the facility. The amount of associated with the individual sub-facilities sums to the total credit facility amount. Sub-facilities may, individually, have a stated purpose, such as to cover inventory, equipment, accounts receivable, working capital, letters of credit, and so forth."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-constituent-of, target: "/FBC/DebtAndEquities/Debt/CreditFacility.md", provenance: fibo}
---

portion of a credit facility extended to the borrower for some purpose, possibly per some schedule specified in the facility

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-constituent-of: [CreditFacility](/FBC/DebtAndEquities/Debt/CreditFacility.md)
