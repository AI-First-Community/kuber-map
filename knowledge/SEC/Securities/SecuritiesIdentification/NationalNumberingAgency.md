---
type: FIBO Class
title: "national numbering agency"
description: "registration authority responsible for issuing and managing National Securities Identifying Numbers for securities in accordance with the ISO 6166 standard in some jurisdiction (typically that of a country)"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency
tags: [SEC, Release]
synonyms:
  - "NNA"
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistrationAuthority.md", provenance: fibo}
  - {type: has-coverage-area, target: "/CMNS/Locations/GeopoliticalEntity.md", provenance: fibo}
  - {type: issues, target: "/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md", provenance: fibo}
  - {type: manages, target: "/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistry.md", provenance: fibo}
  - {type: registers, target: "/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md", provenance: fibo}
---

registration authority responsible for issuing and managing National Securities Identifying Numbers for securities in accordance with the ISO 6166 standard in some jurisdiction (typically that of a country)

### Relationships
- is-a: [RegistrationAuthority](/CMNS/RegistrationAuthorities/RegistrationAuthority.md)
- has-coverage-area: [GeopoliticalEntity](/CMNS/Locations/GeopoliticalEntity.md)
- issues: [NationalSecuritiesIdentifyingNumber](/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- manages: [NationalSecuritiesIdentifyingNumberRegistry](/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistry.md)
- registers: [NationalSecuritiesIdentifyingNumber](/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
