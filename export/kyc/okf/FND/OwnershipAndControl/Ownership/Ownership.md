---
type: FIBO Class
title: "ownership"
description: "situation in which some party holds the legal title to something (explicitly or implicitly) and has the right to transfer that title and/or possession"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "Ownership is the right to possess, use, sell, donate or give as a gift any asset or property belonging to a person known as the 'owner'. An owner can be either a beneficial owner or a legal owner."
examples:
  - "A shareholder's ownership of 100 shares in a company."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: has-owned-asset, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
  - {type: has-owning-party, target: "/FND/OwnershipAndControl/Ownership/Owner.md", provenance: fibo}
---

situation in which some party holds the legal title to something (explicitly or implicitly) and has the right to transfer that title and/or possession

### Relationships
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- has-owned-asset: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
- has-owning-party: [Owner](/FND/OwnershipAndControl/Ownership/Owner.md)
