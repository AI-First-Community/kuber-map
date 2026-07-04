---
type: FIBO Class
title: "legal person"
description: "party that is recognized as having rights and obligations under the law, including but not limited to the right to sue and be sued, enter into contracts, own property, and incur financial and other obligations"
resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
tags: [CMNS]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "To have legal personality means to be capable of having legal rights and duties within a certain legal system, such as to enter into contracts, sue, and be sued. Legal personality is a prerequisite to legal capacity, the ability of any legal person to amend (enter into, transfer, etc.) rights and obligations."
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
  - {type: is-identified-by, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: fibo}
  - {type: is-recognized-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

party that is recognized as having rights and obligations under the law, including but not limited to the right to sue and be sued, enter into contracts, own property, and incur financial and other obligations

### Relationships
- is-a: [Party](/CMNS/PartiesAndSituations/Party.md)
- is-identified-by: [LegalEntityIdentifier](/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
- is-recognized-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
