---
type: FIBO Class
title: "pool"
description: "combination of resources for a common purpose or benefit"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/Pool
tags: [SEC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
examples:
  - "A pool of residential mortgages underlying a mortgage-backed security."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Collections/Collection.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Securities/Pools/PoolConstituent.md", provenance: fibo}
---

combination of resources for a common purpose or benefit

### Relationships
- is-a: [Collection](/CMNS/Collections/Collection.md)
- has-member: [PoolConstituent](/SEC/Securities/Pools/PoolConstituent.md)
