---
type: FIBO Class
title: "national identification number"
description: "number or text which appears on an identity document issued by a country or jurisdiction"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/NationalIdentificationNumber
tags: [FND, Release]
detail: "A national identification number, national identity number, or national insurance number is used by the governments of many countries as a means of tracking their citizens, permanent residents, and temporary residents for the purposes of work, taxation, government benefits, health care, and other governmentally-related functions. The number will appear on an identity document issued by a country.  The ways in which such a system is implemented are dependent on the country, but in most cases, a citizen is issued an identification number at birth or when they reach a legal age (typically the age of 18). Non-citizens may be issued such numbers when they enter the country, or when granted a temporary or permanent residence permit.  Many countries issued such numbers ostensibly for a singular purpose, but over time, they become a de facto national identification number. For example, the United States originally developed its Social Security number system as a means of disbursing Social Security benefits. However, due to function creep, the number has become utilized for other purposes to the point where it is almost essential to have one to, among other things, open a bank account, obtain a credit card, or drive a car."
synonyms:
  - "national identity number"
relations:
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/FND/AgentsAndPeople/People/Person.md", provenance: fibo}
  - {type: is-defined-in, target: "/FND/AgentsAndPeople/People/NationalIdentificationNumberScheme.md", provenance: fibo}
  - {type: is-issued-by, target: "/BE/GovernmentEntities/GovernmentEntities/Government.md", provenance: fibo}
---

number or text which appears on an identity document issued by a country or jurisdiction

### Relationships
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [Person](/FND/AgentsAndPeople/People/Person.md)
- is-defined-in: [NationalIdentificationNumberScheme](/FND/AgentsAndPeople/People/NationalIdentificationNumberScheme.md)
- is-issued-by: [Government](/BE/GovernmentEntities/GovernmentEntities/Government.md)
