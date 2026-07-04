---
type: FIBO Class
title: "identity document"
description: "any legal document which may be used to verify aspects of a person's identity"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "If issued in the form of a small, mostly standard-sized card, it is usually called an identity card (IC). Countries which do not have formal identity documents may require informal documents. In the absence of a formal identity document, driving licenses can be used in many countries as a method of proof of identity, although some countries do not accept driving licenses for identification, often because in those countries they don't expire as documents and can be old and easily forged. Most countries accept passports as a form of identification. Most countries have the rule that foreign citizens need to have their passport or occasionally a national identity card from their country available at any time if they do not have residence permit in the country."
synonyms:
  - "identity card"
relations:
  - {type: is-a, target: "/CMNS/Documents/LegalDocument.md", provenance: fibo}
  - {type: has-date-of-issuance, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-expiration-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: identifies, target: "/FND/AgentsAndPeople/People/Person.md", provenance: fibo}
  - {type: is-evidence-for, target: "/FND/AgentsAndPeople/People/DateOfBirth.md", provenance: fibo}
  - {type: is-evidence-for, target: "/FND/AgentsAndPeople/People/PlaceOfBirth.md", provenance: fibo}
  - {type: is-evidence-for, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: is-identified-by, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: is-issued-by, target: "/BE/GovernmentEntities/GovernmentEntities/Government.md", provenance: fibo}
---

any legal document which may be used to verify aspects of a person's identity

### Relationships
- is-a: [LegalDocument](/CMNS/Documents/LegalDocument.md)
- has-date-of-issuance: [Date](/CMNS/DatesAndTimes/Date.md)
- has-expiration-date: [Date](/CMNS/DatesAndTimes/Date.md)
- identifies: [Person](/FND/AgentsAndPeople/People/Person.md)
- is-evidence-for: [DateOfBirth](/FND/AgentsAndPeople/People/DateOfBirth.md)
- is-evidence-for: [PlaceOfBirth](/FND/AgentsAndPeople/People/PlaceOfBirth.md)
- is-evidence-for: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- is-identified-by: [Identifier](/CMNS/Identifiers/Identifier.md)
- is-issued-by: [Government](/BE/GovernmentEntities/GovernmentEntities/Government.md)
