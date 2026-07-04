---
type: FIBO Class
title: "identity document"
description: "any legal document which may be used to verify aspects of a person's identity"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument
tags: [FND, Release]
relations:
  - {type: is-evidence-for, target: "/FND/AgentsAndPeople/People/PlaceOfBirth.md", provenance: fibo}
  - {type: is-evidence-for, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: is-evidence-for, target: "/FND/AgentsAndPeople/People/DateOfBirth.md", provenance: fibo}
  - {type: is-identified-by, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: has-expiration-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/LegalDocument.md", provenance: fibo}
  - {type: identifies, target: "/FND/AgentsAndPeople/People/Person.md", provenance: fibo}
  - {type: has-date-of-issuance, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
---

any legal document which may be used to verify aspects of a person's identity

### Relationships
- is-evidence-for: [PlaceOfBirth](/FND/AgentsAndPeople/People/PlaceOfBirth.md)
- is-evidence-for: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- is-evidence-for: [DateOfBirth](/FND/AgentsAndPeople/People/DateOfBirth.md)
- is-identified-by: [Identifier](/CMNS/Identifiers/Identifier.md)
- has-expiration-date: [Date](/CMNS/DatesAndTimes/Date.md)
- is-a: [LegalDocument](/CMNS/Documents/LegalDocument.md)
- identifies: [Person](/FND/AgentsAndPeople/People/Person.md)
- has-date-of-issuance: [Date](/CMNS/DatesAndTimes/Date.md)
