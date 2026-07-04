---
type: FIBO Class
title: "borrower identifier"
description: "sequence of characters, capable of uniquely identifying a borrower"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowerIdentifier
tags: [FBC, Release]
detail: "A given identifier identifies a particular borrower with respect to at least some number of notes/facilities inside a particular institution according to some policy for minting identifiers. Optimally, there would be a single identifier for a given borrower, but due to operational issues, this is often not the case. A CIF number, or Customer Information File number, is used to link accounts across an institution to all notes/facilities owed by a given borrower."
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
