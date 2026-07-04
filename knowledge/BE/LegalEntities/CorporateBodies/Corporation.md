---
type: FIBO Class
title: "corporation"
description: "formal organization that is a legal entity (artificial person) distinct from its owners, created under the jurisdiction of the laws of a state or nation"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
tags: [BE, Release]
relations:
  - {type: is-a, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
  - {type: is-constituted-by, target: "/BE/LegalEntities/CorporateBodies/InstrumentOfIncorporation.md", provenance: fibo}
  - {type: is-incorporated-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

formal organization that is a legal entity (artificial person) distinct from its owners, created under the jurisdiction of the laws of a state or nation

### Relationships
- is-a: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
- is-constituted-by: [InstrumentOfIncorporation](/BE/LegalEntities/CorporateBodies/InstrumentOfIncorporation.md)
- is-incorporated-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
