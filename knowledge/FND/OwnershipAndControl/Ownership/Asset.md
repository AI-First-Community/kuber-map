---
type: FIBO Class
title: "asset"
description: "something of monetary value that is owned or provides benefit to some party"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Undergoer.md", provenance: fibo}
  - {type: is-asset-of, target: "/FND/OwnershipAndControl/Ownership/Owner.md", provenance: fibo}
  - {type: is-owned-asset, target: "/FND/OwnershipAndControl/Ownership/Ownership.md", provenance: fibo}
---

something of monetary value that is owned or provides benefit to some party

### Relationships
- is-a: [Undergoer](/CMNS/PartiesAndSituations/Undergoer.md)
- is-asset-of: [Owner](/FND/OwnershipAndControl/Ownership/Owner.md)
- is-owned-asset: [Ownership](/FND/OwnershipAndControl/Ownership/Ownership.md)
