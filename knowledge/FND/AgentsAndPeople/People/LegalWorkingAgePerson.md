---
type: FIBO Class
title: "legal working age person"
description: "person whose age is greater than the minimum legal working age specified in a jurisdiction in which they work"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/LegalWorkingAgePerson
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/AgentsAndPeople/People/Person.md", provenance: fibo}
  - {type: has-minimum-legal-working-age, target: "/FND/AgentsAndPeople/People/LegalWorkingAge.md", provenance: fibo}
---

person whose age is greater than the minimum legal working age specified in a jurisdiction in which they work

### Relationships
- is-a: [Person](/FND/AgentsAndPeople/People/Person.md)
- has-minimum-legal-working-age: [LegalWorkingAge](/FND/AgentsAndPeople/People/LegalWorkingAge.md)
