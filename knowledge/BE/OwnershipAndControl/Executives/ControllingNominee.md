---
type: FIBO Class
title: "controlling nominee"
description: "party that holds legal title to an asset (e.g., stocks, bonds, or property) on behalf of the beneficial owner"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ControllingNominee
tags: [BE, Release]
detail: "The nominee is typically the registered owner of an asset, named in official records."
relations:
  - {type: is-a, target: "/CMNS/BusinessAuthorizations/LegallyDelegatedAuthority.md", provenance: fibo}
  - {type: has-delegated-control-of, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
---

party that holds legal title to an asset (e.g., stocks, bonds, or property) on behalf of the beneficial owner

### Relationships
- is-a: [LegallyDelegatedAuthority](/CMNS/BusinessAuthorizations/LegallyDelegatedAuthority.md)
- has-delegated-control-of: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
