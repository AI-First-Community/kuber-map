---
type: FIBO Class
title: "sovereign state"
description: "non-physical juridical entity that is represented by one centralized government that has sovereignty over a geographic area"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/SovereignState
tags: [BE, Release]
detail: "A legal entity that is represented by one centralized government, has a permanent population, defined territory, and the capacity to enter into relations with other sovereign states."
relations:
  - {type: is-a, target: "/BE/GovernmentEntities/GovernmentEntities/Polity.md", provenance: fibo}
  - {type: has-full-sovereignty-over, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: is-represented-by, target: "/BE/GovernmentEntities/GovernmentEntities/NationalGovernment.md", provenance: fibo}
---

non-physical juridical entity that is represented by one centralized government that has sovereignty over a geographic area

### Relationships
- is-a: [Polity](/BE/GovernmentEntities/GovernmentEntities/Polity.md)
- has-full-sovereignty-over: [Country](/CMNS/Locations/Country.md)
- is-represented-by: [NationalGovernment](/BE/GovernmentEntities/GovernmentEntities/NationalGovernment.md)
