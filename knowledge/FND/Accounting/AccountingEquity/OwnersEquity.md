---
type: FIBO Class
title: "owners' equity"
description: "owners' share in a business plus operating profit"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/AccountingEquity/OwnersEquity
tags: [FND, Release]
detail: "Owner's equity is represented by capital investments and accumulated earnings less any dividends or other financial obligations. It is typically used to talk about equity in a business, but may also refer to the net assets of a pool or special purpose vehicle."
synonyms:
  - "capital"
  - "contributed capital"
  - "equity"
  - "net worth"
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: applies-to, target: "/CMNS/Organizations/FormalOrganization.md", provenance: fibo}
  - {type: has-argument, target: "/FND/Accounting/AccountingEquity/PaidInCapital.md", provenance: fibo}
  - {type: has-argument, target: "/FND/Accounting/AccountingEquity/RetainedEarnings.md", provenance: fibo}
---

owners' share in a business plus operating profit

### Relationships
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- applies-to: [FormalOrganization](/CMNS/Organizations/FormalOrganization.md)
- has-argument: [PaidInCapital](/FND/Accounting/AccountingEquity/PaidInCapital.md)
- has-argument: [RetainedEarnings](/FND/Accounting/AccountingEquity/RetainedEarnings.md)
