---
type: FIBO Class
title: "shareholder"
description: "party that owns shares in and has rights and responsibilities with respect to some asset, provided in exchange for investment"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholder
tags: [BE, Release]
detail: "The shares represent an ownership interest in a corporation, mutual fund, or partnership, or a unit of ownership in a structured product, such as a real estate investment trust."
synonyms:
  - "stockholder"
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/Counterparty.md", provenance: fibo}
---

party that owns shares in and has rights and responsibilities with respect to some asset, provided in exchange for investment

### Relationships
- is-a: [ConstitutionalOwner](/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner.md)
- is-a: [Counterparty](/FND/Agreements/Contracts/Counterparty.md)
