---
type: FIBO Class
title: "trust"
description: "fiduciary relationship and legal entity in which one party, known as a trustor, gives another party, the trustee, the right to hold title to and manage assets for the benefit of a third party, the beneficiary"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
tags: [BE, Release]
core: true
relations:
  - {type: is-a, target: "/BE/LegalEntities/LegalPersons/BusinessEntity.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
  - {type: has-party-role, target: "/BE/Trusts/Trusts/TrustBeneficiary.md", provenance: fibo}
  - {type: has-party-role, target: "/BE/Trusts/Trusts/Trustee.md", provenance: fibo}
  - {type: has-party-role, target: "/BE/Trusts/Trusts/Trustor.md", provenance: fibo}
  - {type: is-governed-by, target: "/BE/Trusts/Trusts/TrustAgreement.md", provenance: fibo}
---

fiduciary relationship and legal entity in which one party, known as a trustor, gives another party, the trustee, the right to hold title to and manage assets for the benefit of a third party, the beneficiary

### Relationships
- is-a: [BusinessEntity](/BE/LegalEntities/LegalPersons/BusinessEntity.md)
- is-a: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
- has-party-role: [TrustBeneficiary](/BE/Trusts/Trusts/TrustBeneficiary.md)
- has-party-role: [Trustee](/BE/Trusts/Trusts/Trustee.md)
- has-party-role: [Trustor](/BE/Trusts/Trusts/Trustor.md)
- is-governed-by: [TrustAgreement](/BE/Trusts/Trusts/TrustAgreement.md)
