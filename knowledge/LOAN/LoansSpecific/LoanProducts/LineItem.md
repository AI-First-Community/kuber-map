---
type: FIBO Class
title: "line item"
description: "description of a product or service including its unit cost, number of units and total cost"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LineItem
tags: [LOAN, Provisional]
relations:
  - {type: is-a, target: "/CMNS/Collections/Constituent.md", provenance: fibo}
  - {type: has-cost, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-unit-cost, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

description of a product or service including its unit cost, number of units and total cost

### Relationships
- is-a: [Constituent](/CMNS/Collections/Constituent.md)
- has-cost: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-unit-cost: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
