---
type: FIBO Class
title: "disclosure action"
description: "corporate action involving a request for holders or beneficial owners to disclose their name, location and holdings of any issue to the issuer"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/DisclosureAction
tags: [CAE, Release]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "A company's disclosure of a material event to the market."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md", provenance: fibo}
---

corporate action involving a request for holders or beneficial owners to disclose their name, location and holdings of any issue to the issuer

### Relationships
- is-a: [VoluntaryCorporateAction](/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)
