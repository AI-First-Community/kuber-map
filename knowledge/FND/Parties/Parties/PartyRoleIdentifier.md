---
type: FIBO Class
title: "party role identifier"
description: "sequence of characters, capable of uniquely identifying a party based on a specific role that they play in some context"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentifier
tags: [FND, Release]
relations:
  - {type: is-member-of, target: "/FND/Parties/Parties/PartyRoleIdentificationScheme.md", provenance: fibo}
  - {type: is-defined-in, target: "/FND/Parties/Parties/PartyRoleIdentificationScheme.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
---

sequence of characters, capable of uniquely identifying a party based on a specific role that they play in some context

### Relationships
- is-member-of: [PartyRoleIdentificationScheme](/FND/Parties/Parties/PartyRoleIdentificationScheme.md)
- is-defined-in: [PartyRoleIdentificationScheme](/FND/Parties/Parties/PartyRoleIdentificationScheme.md)
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
