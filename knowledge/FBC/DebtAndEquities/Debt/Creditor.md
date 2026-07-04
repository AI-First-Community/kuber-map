---
type: FIBO Class
title: "creditor"
description: "a party to whom an obligation, such as an amount of money, or good, or performance of some service exists"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Creditor
tags: [FBC, Release]
core: true
examples:
  - "The bank owed repayment under a mortgage note."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Obligee.md", provenance: fibo}
  - {type: is-owed, target: "/FBC/DebtAndEquities/Debt/Debt.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
---

a party to whom an obligation, such as an amount of money, or good, or performance of some service exists

### Relationships
- is-a: [Obligee](/FND/Agreements/Agreements/Obligee.md)
- is-owed: [Debt](/FBC/DebtAndEquities/Debt/Debt.md)
- is-played-by: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
