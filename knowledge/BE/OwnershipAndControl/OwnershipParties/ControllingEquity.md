---
type: FIBO Class
title: "controlling equity"
description: "shareholders's equity that formally confers control in the entity, either by law or as explicitly stated in a corresponding equity instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ControllingEquity
tags: [BE, Release]
core: true
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/ShareholdersEquity.md", provenance: fibo}
  - {type: confers, target: "/FND/OwnershipAndControl/Control/DeJureControl.md", provenance: fibo}
---

shareholders's equity that formally confers control in the entity, either by law or as explicitly stated in a corresponding equity instrument

### Relationships
- is-a: [ShareholdersEquity](/FND/Accounting/AccountingEquity/ShareholdersEquity.md)
- confers: [DeJureControl](/FND/OwnershipAndControl/Control/DeJureControl.md)
