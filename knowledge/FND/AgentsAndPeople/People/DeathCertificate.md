---
type: FIBO Class
title: "death certificate"
description: "original document certifying the circumstances of the death (such as how and when it occurred), or a certified copy of or representation of the ensuing registration of that death"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DeathCertificate
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/AgentsAndPeople/People/IdentityDocument.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/Certificate.md", provenance: fibo}
  - {type: is-evidence-for, target: "/FND/AgentsAndPeople/People/DateOfDeath.md", provenance: fibo}
  - {type: is-identified-by, target: "/FND/AgentsAndPeople/People/DeathCertificateIdentifier.md", provenance: fibo}
---

original document certifying the circumstances of the death (such as how and when it occurred), or a certified copy of or representation of the ensuing registration of that death

### Relationships
- is-a: [IdentityDocument](/FND/AgentsAndPeople/People/IdentityDocument.md)
- is-a: [Certificate](/CMNS/Documents/Certificate.md)
- is-evidence-for: [DateOfDeath](/FND/AgentsAndPeople/People/DateOfDeath.md)
- is-identified-by: [DeathCertificateIdentifier](/FND/AgentsAndPeople/People/DeathCertificateIdentifier.md)
