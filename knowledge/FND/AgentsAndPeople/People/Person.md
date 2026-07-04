---
type: FIBO Class
title: "person"
description: "individual human being, with consciousness of self"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
synonyms:
  - "natural person"
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
  - {type: has-age, target: "/FND/DatesAndTimes/FinancialDates/Age.md", provenance: fibo}
  - {type: has-citizenship, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: has-date-of-birth, target: "/FND/AgentsAndPeople/People/DateOfBirth.md", provenance: fibo}
  - {type: has-date-of-death, target: "/FND/AgentsAndPeople/People/DateOfDeath.md", provenance: fibo}
  - {type: has-name, target: "/FND/AgentsAndPeople/People/PersonName.md", provenance: fibo}
  - {type: has-place-of-birth, target: "/FND/AgentsAndPeople/People/PlaceOfBirth.md", provenance: fibo}
  - {type: has-residence, target: "/FND/Places/Addresses/ConventionalStreetAddress.md", provenance: fibo}
---

individual human being, with consciousness of self

### Relationships
- is-a: [Party](/CMNS/PartiesAndSituations/Party.md)
- has-age: [Age](/FND/DatesAndTimes/FinancialDates/Age.md)
- has-citizenship: [Country](/CMNS/Locations/Country.md)
- has-date-of-birth: [DateOfBirth](/FND/AgentsAndPeople/People/DateOfBirth.md)
- has-date-of-death: [DateOfDeath](/FND/AgentsAndPeople/People/DateOfDeath.md)
- has-name: [PersonName](/FND/AgentsAndPeople/People/PersonName.md)
- has-place-of-birth: [PlaceOfBirth](/FND/AgentsAndPeople/People/PlaceOfBirth.md)
- has-residence: [ConventionalStreetAddress](/FND/Places/Addresses/ConventionalStreetAddress.md)
