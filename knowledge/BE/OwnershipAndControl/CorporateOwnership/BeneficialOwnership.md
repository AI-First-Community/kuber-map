---
type: FIBO Class
title: "beneficial ownership"
description: "situation linking party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner) to the asset that they own"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwnership
tags: [BE, Release]
detail: "Beneficial ownership may be shared among a group of individuals. If a beneficial owner acquires a position of more than 5 percent in the United States, it must file Schedule 13D or 13G under Section 12 of the Securities Exchange Act of 1934."
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Ownership.md", provenance: fibo}
  - {type: has-owned-asset, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
  - {type: has-owning-party, target: "/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md", provenance: fibo}
---

situation linking party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner) to the asset that they own

### Relationships
- is-a: [Ownership](/FND/OwnershipAndControl/Ownership/Ownership.md)
- has-owned-asset: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
- has-owning-party: [BeneficialOwner](/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md)
