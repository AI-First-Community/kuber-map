---
type: FIBO Class
title: "registry"
description: "authoritative record or collection of records relating to something"
resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
tags: [CMNS]
detail: "Electronic registries typically contain a unique identifier for each entry, so that individual records can be referenced from other documents and registries."
relations:
  - {type: is-a, target: "/CMNS/Collections/StructuredCollection.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/Record.md", provenance: fibo}
  - {type: comprises, target: "/CMNS/RegistrationAuthorities/RegistryEntry.md", provenance: fibo}
  - {type: is-managed-by, target: "/CMNS/RegistrationAuthorities/RegistrationAuthority.md", provenance: fibo}
---

authoritative record or collection of records relating to something

### Relationships
- is-a: [StructuredCollection](/CMNS/Collections/StructuredCollection.md)
- is-a: [Record](/CMNS/Documents/Record.md)
- comprises: [RegistryEntry](/CMNS/RegistrationAuthorities/RegistryEntry.md)
- is-managed-by: [RegistrationAuthority](/CMNS/RegistrationAuthorities/RegistrationAuthority.md)
