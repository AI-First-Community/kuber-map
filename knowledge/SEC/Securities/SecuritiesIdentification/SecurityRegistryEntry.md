---
type: FIBO Class
title: "security registry entry"
description: "record for a security in a securities registry"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistryEntry.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Securities/SecuritiesListings/RegisteredSecurity.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md", provenance: fibo}
---

record for a security in a securities registry

### Relationships
- is-a: [RegistryEntry](/CMNS/RegistrationAuthorities/RegistryEntry.md)
- applies-to: [RegisteredSecurity](/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)
- comprises: [SecurityIdentifier](/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md)
