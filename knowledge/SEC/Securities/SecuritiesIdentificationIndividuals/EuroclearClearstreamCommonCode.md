---
type: FIBO Class
title: "Euroclear Clearstream common code"
description: "nine-character alphanumeric securities identifier, issued in Luxembourg, jointly by Euroclear and Clearstream"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCode
tags: [SEC, Release]
synonyms:
  - "common code"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCodeScheme.md", provenance: fibo}
  - {type: is-registered-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository.md", provenance: fibo}
---

nine-character alphanumeric securities identifier, issued in Luxembourg, jointly by Euroclear and Clearstream

### Relationships
- is-a: [ProprietarySecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
- identifies: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- is-defined-in: [EuroclearClearstreamCommonCodeScheme](/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCodeScheme.md)
- is-registered-in: [CommonCodeRepository](/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository.md)
