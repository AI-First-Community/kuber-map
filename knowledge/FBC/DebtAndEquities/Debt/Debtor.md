---
type: FIBO Class
title: "debtor"
description: "a party that owes a debt or other obligation to another party"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debtor
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Obligor.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: owes, target: "/FBC/DebtAndEquities/Debt/Debt.md", provenance: fibo}
---

a party that owes a debt or other obligation to another party

### Relationships
- is-a: [Obligor](/FND/Agreements/Agreements/Obligor.md)
- is-played-by: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- owes: [Debt](/FBC/DebtAndEquities/Debt/Debt.md)
