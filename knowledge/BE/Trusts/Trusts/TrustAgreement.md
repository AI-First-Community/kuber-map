---
type: FIBO Class
title: "trust agreement"
description: "formal agreement that establishes a trust, whereby the trustor(s) gives the trustee(s) the responsibility to hold and manage assets for the beneficiary(ies)"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustAgreement
tags: [BE, Release]
detail: "A trust agreement typically states the (1) purpose for which the trust was established and fulfillment of which will terminate the trust, (2) details of the assets placed in the trust, (3) powers and limitations of the trustees, their reporting requirements, and other associated provisions, and (4) may also specify the trustees' compensation, if any. A trust agreement involving real estate requires its exact description and the trustor's express, written consent to create the trust to be valid."
synonyms:
  - "trust deed"
  - "trust document"
  - "trust instrument"
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
