---
type: FIBO Class
title: "registration authority"
description: "service provider that is officially responsible for maintaining a registry and providing registration services and/or for delegating of some or all of these roles to a registrar"
resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
tags: [CMNS]
synonyms:
  - "RA"
relations:
  - {type: is-a, target: "/CMNS/BusinessAuthorizations/AuthorizingParty.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
  - {type: manages, target: "/CMNS/RegistrationAuthorities/Registry.md", provenance: fibo}
---

service provider that is officially responsible for maintaining a registry and providing registration services and/or for delegating of some or all of these roles to a registrar

### Relationships
- is-a: [AuthorizingParty](/CMNS/BusinessAuthorizations/AuthorizingParty.md)
- is-a: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
- manages: [Registry](/CMNS/RegistrationAuthorities/Registry.md)
