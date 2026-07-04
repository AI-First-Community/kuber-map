---
type: FIBO Class
title: "instrumentality"
description: "organization that serves a public purpose and is closely tied to a government, but is not a government agency"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Instrumentality
tags: [BE, Release]
detail: "An instrumentality is a non-governmental agency that acts independently but whose obligations are backed by a government because of its role in providing a public service. Many instrumentalities are private companies, and some are chartered directly by government. Instrumentalities are subject to a unique set of laws that shape their activities. Certain organizations, such as Sallie Mae in the United States, may be considered instrumentalities from some perspectives but not others. Sallie Mae's status was changed in 2004, when it was privatized, and since that time it is no longer considered a government-sponsored enterprise (GSE)."
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
