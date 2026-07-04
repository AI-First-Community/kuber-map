---
type: FIBO Class
title: "listed security identifier"
description: "security identifier issued in the public domain and referred to in listings and other relevant publications"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/SEC/Securities/SecuritiesListings/ListedSecurity.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
  - {type: is-registered-in, target: "/SEC/Securities/SecuritiesIdentification/SecurityRegistry.md", provenance: fibo}
---

security identifier issued in the public domain and referred to in listings and other relevant publications

### Relationships
- is-a: [SecurityIdentifier](/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md)
- identifies: [ListedSecurity](/SEC/Securities/SecuritiesListings/ListedSecurity.md)
- is-defined-in: [SecurityIdentificationScheme](/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md)
- is-registered-by: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
- is-registered-in: [SecurityRegistry](/SEC/Securities/SecuritiesIdentification/SecurityRegistry.md)
