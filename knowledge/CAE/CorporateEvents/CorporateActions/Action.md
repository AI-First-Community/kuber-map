---
type: FIBO Class
title: "action"
description: "event announced, initiated or carried out by an organization that affects a legal entity or the securities it issues and may have a material impact on that entity's stakeholders, such as shareholders and creditors"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/Action
tags: [CAE, Release]
detail: "Actions initiated by an issuer are typically approved by that company's board of directors and authorized by their shareholders."
examples:
  - "Actions that impact an entity may be initiated by an issuer, exchange, regulator, creditor, or other third party."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: is-classified-by, target: "/CAE/CorporateEvents/CorporateActions/ActionClassifier.md", provenance: fibo}
---

event announced, initiated or carried out by an organization that affects a legal entity or the securities it issues and may have a material impact on that entity's stakeholders, such as shareholders and creditors

### Relationships
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- is-classified-by: [ActionClassifier](/CAE/CorporateEvents/CorporateActions/ActionClassifier.md)
