---
type: FIBO Class
title: "security registry"
description: "registry used to manage security identifiers and related information"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistry
tags: [SEC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
detail: "Securities registries may be managed by an exchange, clearing house, custodian, bank, or other financial services provider."
examples:
  - "A registrar maintaining the register of a company's shareholders."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/Registry.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md", provenance: fibo}
  - {type: is-characterized-by, target: "/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md", provenance: fibo}
  - {type: is-managed-by, target: "/CMNS/RegistrationAuthorities/RegistrationAuthority.md", provenance: fibo}
---

registry used to manage security identifiers and related information

### Relationships
- is-a: [Registry](/CMNS/RegistrationAuthorities/Registry.md)
- comprises: [SecurityRegistryEntry](/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md)
- is-characterized-by: [SecurityIdentificationScheme](/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md)
- is-managed-by: [RegistrationAuthority](/CMNS/RegistrationAuthorities/RegistrationAuthority.md)
