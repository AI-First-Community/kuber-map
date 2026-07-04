---
type: FIBO Class
title: "de facto control"
description: "control that exists informally and is accepted, although not formally recognized"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeFactoControl
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "For example, de facto acquisition or change of control means the acquisition, directly or indirectly, by any person or group of persons acting jointly or in concert, of beneficial ownership of, or control or direction over, sufficient voting shares of some legal entity to permit such person or persons to exercise, or to control or direct the voting of, 50 percent or more of the total number of votes in that entity."
examples:
  - "Control exercised in practice, e.g. directing a company despite holding under 50% of its shares."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/Control.md", provenance: fibo}
---

control that exists informally and is accepted, although not formally recognized

### Relationships
- is-a: [Control](/FND/OwnershipAndControl/Control/Control.md)
