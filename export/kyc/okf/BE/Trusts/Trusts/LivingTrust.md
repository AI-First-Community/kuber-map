---
type: FIBO Class
title: "living trust"
description: "trust created during an individual's lifetime where a designated person, the trustee, is given responsibility for managing that individual's assets for the benefit of the eventual beneficiary"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/LivingTrust
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "A living trust is designed to allow for the easy transfer of the trust creator or settlor's assets while bypassing the often complex and expensive legal process of probate. Living trust agreements designate a trustee who holds legal possession of assets and property that flow into the trust."
examples:
  - "A revocable living trust created to hold a person's assets during their lifetime."
examples_provenance: curated
relations:
  - {type: is-a, target: "/BE/Trusts/Trusts/Trust.md", provenance: fibo}
---

trust created during an individual's lifetime where a designated person, the trustee, is given responsibility for managing that individual's assets for the benefit of the eventual beneficiary

### Relationships
- is-a: [Trust](/BE/Trusts/Trusts/Trust.md)
