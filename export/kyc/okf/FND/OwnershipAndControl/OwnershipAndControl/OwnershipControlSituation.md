---
type: FIBO Class
title: "ownership control situation"
description: "situation in which some party owns and controls something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/OwnershipControlSituation
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "An individual owning 40% of a company's shares and also holding board control."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
---

situation in which some party owns and controls something

### Relationships
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
