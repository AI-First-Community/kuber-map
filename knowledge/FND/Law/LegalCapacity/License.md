---
type: FIBO Class
title: "license"
description: "grant of permission needed to do something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/License
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/Documents/LegalDocument.md", provenance: fibo}
  - {type: confers, target: "/FND/Law/LegalCapacity/LegalCapacity.md", provenance: fibo}
  - {type: is-issued-by, target: "/FND/Law/LegalCapacity/Licensor.md", provenance: fibo}
  - {type: holds-during, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: has-party-role, target: "/FND/Law/LegalCapacity/Licensee.md", provenance: fibo}
---

grant of permission needed to do something

### Relationships
- is-a: [LegalDocument](/CMNS/Documents/LegalDocument.md)
- confers: [LegalCapacity](/FND/Law/LegalCapacity/LegalCapacity.md)
- is-issued-by: [Licensor](/FND/Law/LegalCapacity/Licensor.md)
- holds-during: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- has-party-role: [Licensee](/FND/Law/LegalCapacity/Licensee.md)
