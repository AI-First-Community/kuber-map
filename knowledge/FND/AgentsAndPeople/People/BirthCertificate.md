---
type: FIBO Class
title: "birth certificate"
description: "an original document certifying the circumstances of the birth, or a certified copy of or representation of the ensuing registration of that birth"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificate
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/AgentsAndPeople/People/IdentityDocument.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/Certificate.md", provenance: fibo}
  - {type: is-evidence-for, target: "/FND/AgentsAndPeople/People/PlaceOfBirth.md", provenance: fibo}
  - {type: is-identified-by, target: "/FND/AgentsAndPeople/People/BirthCertificateIdentifier.md", provenance: fibo}
---

an original document certifying the circumstances of the birth, or a certified copy of or representation of the ensuing registration of that birth

### Relationships
- is-a: [IdentityDocument](/FND/AgentsAndPeople/People/IdentityDocument.md)
- is-a: [Certificate](/CMNS/Documents/Certificate.md)
- is-evidence-for: [PlaceOfBirth](/FND/AgentsAndPeople/People/PlaceOfBirth.md)
- is-identified-by: [BirthCertificateIdentifier](/FND/AgentsAndPeople/People/BirthCertificateIdentifier.md)
