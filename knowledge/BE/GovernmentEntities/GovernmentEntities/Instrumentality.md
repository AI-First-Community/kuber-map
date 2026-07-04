---
type: FIBO Class
title: "instrumentality"
description: "organization that serves a public purpose and is closely tied to a government, but is not a government agency"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Instrumentality
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
  - {type: is-an-instrument-of, target: "/BE/GovernmentEntities/GovernmentEntities/Government.md", provenance: fibo}
  - {type: is-mandated-by, target: "/FND/Law/LegalCore/StatuteLaw.md", provenance: fibo}
---

organization that serves a public purpose and is closely tied to a government, but is not a government agency

### Relationships
- is-a: [GovernmentBody](/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)
- is-a: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
- is-an-instrument-of: [Government](/BE/GovernmentEntities/GovernmentEntities/Government.md)
- is-mandated-by: [StatuteLaw](/FND/Law/LegalCore/StatuteLaw.md)
