---
type: FIBO Class
title: "borrower identifier"
description: "sequence of characters, capable of uniquely identifying a borrower"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowerIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Parties/Parties/PartyRoleIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/DebtAndEquities/Debt/Borrower.md", provenance: fibo}
  - {type: is-defined-in, target: "/FBC/DebtAndEquities/Debt/BorrowerIdentificationScheme.md", provenance: fibo}
---

sequence of characters, capable of uniquely identifying a borrower

### Relationships
- is-a: [PartyRoleIdentifier](/FND/Parties/Parties/PartyRoleIdentifier.md)
- identifies: [Borrower](/FBC/DebtAndEquities/Debt/Borrower.md)
- is-defined-in: [BorrowerIdentificationScheme](/FBC/DebtAndEquities/Debt/BorrowerIdentificationScheme.md)
