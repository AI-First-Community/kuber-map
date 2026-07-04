---
type: FIBO Class
title: "National Securities Identifying Number"
description: "generic, nine-digit alpha numeric code which identifies a fungible security, assigned by a national numbering agency under the ISO 6166 standard"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
tags: [SEC, Release]
synonyms:
  - "NSIN"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme.md", provenance: fibo}
  - {type: is-registered-by, target: "/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency.md", provenance: fibo}
---

generic, nine-digit alpha numeric code which identifies a fungible security, assigned by a national numbering agency under the ISO 6166 standard

### Relationships
- is-a: [SecurityIdentifier](/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md)
- is-defined-in: [NationalSecurityIdentificationScheme](/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme.md)
- is-registered-by: [NationalNumberingAgency](/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency.md)
