---
type: FIBO Class
title: "trustor"
description: "party that establishes a trust and places property under the protection and management of one or more trustees for the benefit of at least one beneficiary"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustor
tags: [BE, Release]
detail: "It is not always necessary to identify the trustor who may be also be a trustee and/or one of the beneficiaries. In legal parlance, a trustor is called a settlor in the UK and a grantor in the US, whereas in common usage he or she may also be called a creator, donor, initiator, owner, or trust maker."
synonyms:
  - "grantor"
  - "settlor"
relations:
  - {type: is-a, target: "/CMNS/Organizations/OrganizationMember.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
---

party that establishes a trust and places property under the protection and management of one or more trustees for the benefit of at least one beneficiary

### Relationships
- is-a: [OrganizationMember](/CMNS/Organizations/OrganizationMember.md)
- is-played-by: [Party](/CMNS/PartiesAndSituations/Party.md)
