---
type: FIBO Class
title: "real property identifier"
description: "unique identifier given to identify a specific real property in some jurisidiction"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealPropertyIdentifier
tags: [FND, Release]
relations:
  - {type: is-applicable-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/ContextualIdentifiers/ContextualIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FND/Places/RealProperty/RealProperty.md", provenance: fibo}
---

unique identifier given to identify a specific real property in some jurisidiction

### Relationships
- is-applicable-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-a: [ContextualIdentifier](/CMNS/ContextualIdentifiers/ContextualIdentifier.md)
- identifies: [RealProperty](/FND/Places/RealProperty/RealProperty.md)
