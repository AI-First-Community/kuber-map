---
type: FIBO Class
title: "corporate action obligation"
description: "An obligation related to the holding of a Security."
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CorporateActionObligation
tags: [CAE, Provisional]
detail: "Delivery of a security. Not defining direction at this level of the model - one party may have an obligation to deliver security or to pay; other party may have an obligation to deliver or to pay. Or there may be just one."
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/CorporateAction.md", provenance: fibo}
  - {type: is-a, target: "/FND/Law/LegalCapacity/Duty.md", provenance: fibo}
---

An obligation related to the holding of a Security.

### Relationships
- is-a: [CorporateAction](/CAE/CorporateEvents/CorporateActions/CorporateAction.md)
- is-a: [Duty](/FND/Law/LegalCapacity/Duty.md)
