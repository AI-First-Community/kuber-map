---
type: FIBO Class
title: "National Securities Identifying Number registry"
description: "registry used by a national numbering agency to manage the financial instrument identifiers and related information that it registers"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistry
tags: [SEC, Release]
synonyms:
  - "NSIN registry"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/SecurityRegistry.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistryEntry.md", provenance: fibo}
  - {type: is-characterized-by, target: "/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme.md", provenance: fibo}
  - {type: is-managed-by, target: "/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency.md", provenance: fibo}
---

registry used by a national numbering agency to manage the financial instrument identifiers and related information that it registers

### Relationships
- is-a: [SecurityRegistry](/SEC/Securities/SecuritiesIdentification/SecurityRegistry.md)
- comprises: [NationalSecuritiesIdentifyingNumberRegistryEntry](/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistryEntry.md)
- is-characterized-by: [NationalSecurityIdentificationScheme](/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme.md)
- is-managed-by: [NationalNumberingAgency](/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency.md)
