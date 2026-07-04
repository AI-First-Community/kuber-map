---
type: FIBO Class
title: "contact"
description: "role or associated with a party serving as a designated point of communication, typically within a system or process"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Contact
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: is-identified-by, target: "/FND/Parties/Parties/PartyRoleIdentifier.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
  - {type: is-signified-by, target: "/FND/AgentsAndPeople/People/ContactRecord.md", provenance: fibo}
---

role or associated with a party serving as a designated point of communication, typically within a system or process

### Relationships
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- is-identified-by: [PartyRoleIdentifier](/FND/Parties/Parties/PartyRoleIdentifier.md)
- is-played-by: [Party](/CMNS/PartiesAndSituations/Party.md)
- is-signified-by: [ContactRecord](/FND/AgentsAndPeople/People/ContactRecord.md)
