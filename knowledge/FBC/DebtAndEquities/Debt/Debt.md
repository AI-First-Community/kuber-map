---
type: FIBO Class
title: "debt"
description: "obligation to pay something, such as an amount of money, good, service, or instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
  - {type: is-owed-by, target: "/FBC/DebtAndEquities/Debt/Debtor.md", provenance: fibo}
  - {type: is-owed-to, target: "/FBC/DebtAndEquities/Debt/Creditor.md", provenance: fibo}
---

obligation to pay something, such as an amount of money, good, service, or instrument

### Relationships
- is-a: [Commitment](/FND/Agreements/Agreements/Commitment.md)
- is-owed-by: [Debtor](/FBC/DebtAndEquities/Debt/Debtor.md)
- is-owed-to: [Creditor](/FBC/DebtAndEquities/Debt/Creditor.md)
