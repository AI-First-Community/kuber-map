---
type: FIBO Class
title: "entity owner"
description: "owner (person, group of people, or other business entity) that owns, or holds an ownership interest in, a formal business organization"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwner
tags: [BE, Release]
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Owner.md", provenance: fibo}
  - {type: holds, target: "/FND/Accounting/AccountingEquity/OwnersEquity.md", provenance: fibo}
---

owner (person, group of people, or other business entity) that owns, or holds an ownership interest in, a formal business organization

### Relationships
- is-a: [Owner](/FND/OwnershipAndControl/Ownership/Owner.md)
- holds: [OwnersEquity](/FND/Accounting/AccountingEquity/OwnersEquity.md)
