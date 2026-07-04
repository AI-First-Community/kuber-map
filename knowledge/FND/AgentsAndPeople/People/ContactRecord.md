---
type: FIBO Class
title: "contact record"
description: "record about a party in a specific communicative or liaison role"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/ContactRecord
tags: [FND, Release]
detail: "Contact records may include attributes such as name, role, communication channel, and affiliation, They may be found in registries, schemas, systems such as those designed for customer relationship management (CRM), enterprise resource planning (ERP), health information, legal and regulatory compliance and others, as well as personal address books, to support communications, coordination, support, or compliance."
relations:
  - {type: is-a, target: "/CMNS/Documents/Record.md", provenance: fibo}
  - {type: comprises, target: "/FND/Parties/Parties/PartyRoleIdentifier.md", provenance: fibo}
  - {type: denotes, target: "/FND/AgentsAndPeople/People/Contact.md", provenance: fibo}
---

record about a party in a specific communicative or liaison role

### Relationships
- is-a: [Record](/CMNS/Documents/Record.md)
- comprises: [PartyRoleIdentifier](/FND/Parties/Parties/PartyRoleIdentifier.md)
- denotes: [Contact](/FND/AgentsAndPeople/People/Contact.md)
