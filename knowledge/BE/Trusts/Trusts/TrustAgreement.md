---
type: FIBO Class
title: "trust agreement"
description: "formal agreement that establishes a trust, whereby the trustor(s) gives the trustee(s) the responsibility to hold and manage assets for the beneficiary(ies)"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustAgreement
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md", provenance: fibo}
  - {type: has-party-role, target: "/BE/Trusts/Trusts/TrustBeneficiary.md", provenance: fibo}
  - {type: has-party-role, target: "/BE/Trusts/Trusts/Trustee.md", provenance: fibo}
  - {type: has-party-role, target: "/BE/Trusts/Trusts/Trustor.md", provenance: fibo}
---

formal agreement that establishes a trust, whereby the trustor(s) gives the trustee(s) the responsibility to hold and manage assets for the beneficiary(ies)

### Relationships
- is-a: [OrganizationCoveringAgreement](/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md)
- has-party-role: [TrustBeneficiary](/BE/Trusts/Trusts/TrustBeneficiary.md)
- has-party-role: [Trustee](/BE/Trusts/Trusts/Trustee.md)
- has-party-role: [Trustor](/BE/Trusts/Trusts/Trustor.md)
