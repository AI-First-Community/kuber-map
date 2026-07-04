---
type: FIBO Class
title: "power of attorney"
description: "legal authorization given by one party (the principal) to another (the agent or attorney-in-fact) to perform certain acts on the principal's behalf"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/PowerOfAttorney
tags: [BE, Release]
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LegalCapacity.md", provenance: fibo}
  - {type: has-effective-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: is-conferred-on, target: "/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md", provenance: fibo}
---

legal authorization given by one party (the principal) to another (the agent or attorney-in-fact) to perform certain acts on the principal's behalf

### Relationships
- is-a: [LegalCapacity](/FND/Law/LegalCapacity/LegalCapacity.md)
- has-effective-date: [Date](/CMNS/DatesAndTimes/Date.md)
- is-conferred-on: [LegallyCompetentNaturalPerson](/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
