---
type: FIBO Class
title: "service provider"
description: "role of an agent that provides some service, including but not limited to commercial or professional services"
resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
tags: [CMNS]
examples:
  - "Example services may include consulting, financial, legal, real estate, education, communications, registration, regulatory, manufacturing, storage, processing, or other services."
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/PartiesAndSituations/AgentRole.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RolesAndCompositions/FunctionalRole.md", provenance: fibo}
  - {type: provides, target: "/CMNS/Organizations/Service.md", provenance: fibo}
  - {type: provisions, target: "/CMNS/Organizations/Service.md", provenance: fibo}
  - {type: provisions, target: "/CMNS/SitesAndFacilities/Facility.md", provenance: fibo}
---

role of an agent that provides some service, including but not limited to commercial or professional services

### Relationships
- is-a: [FunctionalEntity](/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md)
- is-a: [AgentRole](/CMNS/PartiesAndSituations/AgentRole.md)
- is-a: [FunctionalRole](/CMNS/RolesAndCompositions/FunctionalRole.md)
- provides: [Service](/CMNS/Organizations/Service.md)
- provisions: [Service](/CMNS/Organizations/Service.md)
- provisions: [Facility](/CMNS/SitesAndFacilities/Facility.md)
