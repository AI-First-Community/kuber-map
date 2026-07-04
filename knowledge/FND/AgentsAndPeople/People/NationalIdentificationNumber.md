---
type: FIBO Class
title: "national identification number"
description: "number or text which appears on an identity document issued by a country or jurisdiction"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/NationalIdentificationNumber
tags: [FND, Release]
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
