---
type: FIBO Class
title: "asset"
description: "something of monetary value that is owned or provides benefit to some party"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
tags: [FND, Release]
detail: "An asset is something that provides probable future economic benefit obtained or controlled by some party as a result of past transactions or events. An asset has three essential characteristics: (a) it embodies a probable future benefit that involves a capacity, singly or in combination with other assets, to contribute directly or indirectly to future net cash inflows, (b) a party can obtain the benefit and control others' access to it, and (c) the transaction or other event giving rise to the party's right to or control of the benefit has already occurred."
synonyms:
  - "economic resource"
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
