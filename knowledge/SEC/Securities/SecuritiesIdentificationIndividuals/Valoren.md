---
type: FIBO Class
title: "Valoren"
description: "identification number assigned to financial instruments in Switzerland, Liechtenstein and Belgium, issued by SIX Financial Information, that is the National Securities Identifying Number (NSIN) for securities issued in those countries and is also part of the ISIN for the security it identifies"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/Valoren
tags: [SEC, Release]
detail: "A VALOR code is between six and nine characters in length and like other securities identification codes (like ISIN, CUSIPs etc). A VALOR is utilized for identification purposes as well as clearing and settlement, similar to an ISIN code, and identifies debt and equity securities."
synonyms:
  - "Valor"
  - "Valor Code"
  - "Valor Nummer"
  - "Valoren Code"
  - "Valoren Number"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/ValorenScheme.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md", provenance: fibo}
---

identification number assigned to financial instruments in Switzerland, Liechtenstein and Belgium, issued by SIX Financial Information, that is the National Securities Identifying Number (NSIN) for securities issued in those countries and is also part of the ISIN for the security it identifies

### Relationships
- is-a: [ListedSecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md)
- is-a: [NationalSecuritiesIdentifyingNumber](/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- is-a: [ProprietarySecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)
- is-defined-in: [ValorenScheme](/SEC/Securities/SecuritiesIdentificationIndividuals/ValorenScheme.md)
- is-issued-by: [SIXFinancialInformation](/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md)
- is-registered-by: [SIXFinancialInformation](/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md)
