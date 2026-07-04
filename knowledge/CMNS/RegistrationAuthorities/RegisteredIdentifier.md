---
type: FIBO Class
title: "registered identifier"
description: "contextual identifier that is registered in a registry by, or on behalf of, a registration authority according to some registration scheme"
resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
tags: [CMNS]
relations:
  - {type: is-a, target: "/CMNS/ContextualIdentifiers/ContextualIdentifier.md", provenance: fibo}
  - {type: complies-with, target: "/CMNS/RegistrationAuthorities/RegistrationScheme.md", provenance: fibo}
  - {type: is-registered-by, target: "/CMNS/RegistrationAuthorities/Registrar.md", provenance: fibo}
  - {type: is-registered-in, target: "/CMNS/RegistrationAuthorities/Registry.md", provenance: fibo}
---

contextual identifier that is registered in a registry by, or on behalf of, a registration authority according to some registration scheme

### Relationships
- is-a: [ContextualIdentifier](/CMNS/ContextualIdentifiers/ContextualIdentifier.md)
- complies-with: [RegistrationScheme](/CMNS/RegistrationAuthorities/RegistrationScheme.md)
- is-registered-by: [Registrar](/CMNS/RegistrationAuthorities/Registrar.md)
- is-registered-in: [Registry](/CMNS/RegistrationAuthorities/Registry.md)
