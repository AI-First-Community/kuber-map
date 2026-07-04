---
type: FIBO Class
title: "Committee on Uniform Securities Identification Procedures (CUSIP) number"
description: "nine-character alphanumeric number that identifies all North American stocks and registered bonds for the purposes of facilitating clearing and settlement of trades, issued by CUSIP Global Services on behalf of the American Bankers' Association, which is a part of Standard and Poor's Capital IQ, that is the National Numbering Agency Identifier for securities issued in North America, which is also part of the ISIN for the security it identifies"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommitteeOnUniformSecuritiesIdentificationProceduresNumber
tags: [SEC, Release]
synonyms:
  - "CUSIP"
  - "CUSIP number"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CommitteeOnUniformSecuritiesIdentificationProceduresScheme.md", provenance: fibo}
  - {type: is-issued-by, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md", provenance: fibo}
  - {type: is-registered-by, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md", provenance: fibo}
  - {type: is-registered-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/CGSCUSIPAccessRepository.md", provenance: fibo}
---

nine-character alphanumeric number that identifies all North American stocks and registered bonds for the purposes of facilitating clearing and settlement of trades, issued by CUSIP Global Services on behalf of the American Bankers' Association, which is a part of Standard and Poor's Capital IQ, that is the National Numbering Agency Identifier for securities issued in North America, which is also part of the ISIN for the security it identifies

### Relationships
- is-a: [NationalSecuritiesIdentifyingNumber](/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- is-a: [ProprietarySecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
- identifies: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- is-defined-in: [CommitteeOnUniformSecuritiesIdentificationProceduresScheme](/SEC/Securities/SecuritiesIdentificationIndividuals/CommitteeOnUniformSecuritiesIdentificationProceduresScheme.md)
- is-issued-by: [CUSIPGlobalServices](/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md)
- is-registered-by: [CUSIPGlobalServices](/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md)
- is-registered-in: [CGSCUSIPAccessRepository](/SEC/Securities/SecuritiesIdentificationIndividuals/CGSCUSIPAccessRepository.md)
