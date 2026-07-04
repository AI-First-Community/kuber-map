---
type: FIBO Class
title: "community investment fund"
description: "professionally-managed investment fund with three essential characteristics: capital is sourced from people in the community (ideally from retail/non-accredited investors); capital is invested into local people, projects, and businesses; and capital is deployed by individuals in the community, typically but not necessarily a nonprofit fund"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/CommunityInvestmentFund
tags: [SEC, Release]
detail: "A community investment fund is typically but not necessarily a nonprofit fund."
synonyms:
  - "CIF"
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/PrivateFund.md", provenance: fibo}
  - {type: has-coverage-area, target: "/CMNS/Locations/GeographicRegion.md", provenance: fibo}
  - {type: has-objective, target: "/FND/GoalsAndObjectives/Objectives/LocalInvestmentObjective.md", provenance: fibo}
---

professionally-managed investment fund with three essential characteristics: capital is sourced from people in the community (ideally from retail/non-accredited investors); capital is invested into local people, projects, and businesses; and capital is deployed by individuals in the community, typically but not necessarily a nonprofit fund

### Relationships
- is-a: [PrivateFund](/SEC/Securities/Pools/PrivateFund.md)
- has-coverage-area: [GeographicRegion](/CMNS/Locations/GeographicRegion.md)
- has-objective: [LocalInvestmentObjective](/FND/GoalsAndObjectives/Objectives/LocalInvestmentObjective.md)
