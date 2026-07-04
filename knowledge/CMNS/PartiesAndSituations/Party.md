---
type: FIBO Class
title: "party"
description: "person or organization"
resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
tags: [CMNS]
core: true
synonyms:
  - "independent party"
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Agent.md", provenance: fibo}
  - {type: has-address, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: has-mailing-address, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
---

person or organization

### Relationships
- is-a: [Agent](/CMNS/PartiesAndSituations/Agent.md)
- has-address: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- has-mailing-address: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
