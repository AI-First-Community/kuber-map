---
type: FIBO Class
title: "constitutional owner"
description: "entity owner that holds an equity stake in said entity, in the form of shareholders' equity"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner
tags: [BE, Release]
detail: "Typically this would be share ownership or the holding of partnership equity. Ownership in this 'constitutional' sense means that the owner is in some way a member of the organization, such as an employee or director, as distinct from some outside investor."
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md", provenance: fibo}
  - {type: holds, target: "/FND/Accounting/AccountingEquity/ShareholdersEquity.md", provenance: fibo}
---

entity owner that holds an equity stake in said entity, in the form of shareholders' equity

### Relationships
- is-a: [EntityOwner](/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md)
- holds: [ShareholdersEquity](/FND/Accounting/AccountingEquity/ShareholdersEquity.md)
