---
type: FIBO Class
title: "cross default provision"
description: "contract provision that triggers a default under one contract if the borrower defaults on another related obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/CrossDefaultProvision
tags: [FBC, Release]
detail: "Cross default provisions are commonly found in loans, bond indentures, syndicated loans, and other instruments such as certain master agreements (e.g., derivatives transactions master agreements)."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ConditionPrecedent.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
  - {type: has-default-threshold-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

contract provision that triggers a default under one contract if the borrower defaults on another related obligation

### Relationships
- is-a: [ConditionPrecedent](/FND/Agreements/Contracts/ConditionPrecedent.md)
- applies-to: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- has-default-threshold-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
