---
type: FIBO Class
title: "CUSIP International Numbering System (CINS) number"
description: "9-character alphanumeric identifier that employs the same 9 characters as CUSIP, but also contains a letter of the alphabet in the first position signifying the issuer's country or geographic region, issued by CUSIP Global Services"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPInternationalNumberingSystemNumber
tags: [SEC, Release]
synonyms:
  - "CINS"
  - "CINS number"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPInternationalNumberingSystemScheme.md", provenance: fibo}
  - {type: is-issued-by, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md", provenance: fibo}
  - {type: is-registered-by, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md", provenance: fibo}
  - {type: is-registered-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CGSCUSIPAccessRepository.md", provenance: fibo}
---

9-character alphanumeric identifier that employs the same 9 characters as CUSIP, but also contains a letter of the alphabet in the first position signifying the issuer's country or geographic region, issued by CUSIP Global Services

### Relationships
- is-a: [ProprietarySecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
- identifies: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- is-defined-in: [CUSIPInternationalNumberingSystemScheme](/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPInternationalNumberingSystemScheme.md)
- is-issued-by: [CUSIPGlobalServices](/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md)
- is-registered-by: [CUSIPGlobalServices](/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md)
- is-registered-in: [CGSCUSIPAccessRepository](/SEC/Securities/SecuritiesIdentificationIndividuals/CGSCUSIPAccessRepository.md)
