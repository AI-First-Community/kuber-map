---
type: FIBO Class
title: "merchant identifier"
description: "unique identifier for a merchant that is used, for example, for transaction interchange purposes"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantIdentifier
tags: [BE, Release]
relations:
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/BE/FunctionalEntities/FunctionalEntities/Merchant.md", provenance: fibo}
---

unique identifier for a merchant that is used, for example, for transaction interchange purposes

### Relationships
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [Merchant](/BE/FunctionalEntities/FunctionalEntities/Merchant.md)
