---
type: FIBO Class
title: "regulation"
description: "a rule used to carry out a law"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Regulation
tags: [FND, Release]
detail: "Many government agencies issue regulations to administer laws."
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LegalConstruct.md", provenance: fibo}
  - {type: is-applicable-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-conferred-by, target: "/FND/Law/LegalCore/Law.md", provenance: fibo}
  - {type: is-issued-by, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
---

a rule used to carry out a law

### Relationships
- is-a: [LegalConstruct](/FND/Law/LegalCapacity/LegalConstruct.md)
- is-applicable-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-conferred-by: [Law](/FND/Law/LegalCore/Law.md)
- is-issued-by: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
