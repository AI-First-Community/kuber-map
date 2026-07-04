---
type: FIBO Class
title: "contractually capable entity"
description: "a unique entity that is legally or financially responsible for the performance of financial transactions, or has the legal right in its jurisdiction to enter independently into legal contracts, regardless of whether it is incorporated or constituted in some other way (e.g. trust, partnership, contractual). This excludes natural persons, but includes governmental organizations and supranationals."
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/ContractuallyCapableEntity
tags: [BE, Release]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/AgentRole.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
---

a unique entity that is legally or financially responsible for the performance of financial transactions, or has the legal right in its jurisdiction to enter independently into legal contracts, regardless of whether it is incorporated or constituted in some other way (e.g. trust, partnership, contractual). This excludes natural persons, but includes governmental organizations and supranationals.

### Relationships
- is-a: [AgentRole](/CMNS/PartiesAndSituations/AgentRole.md)
- is-played-by: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
