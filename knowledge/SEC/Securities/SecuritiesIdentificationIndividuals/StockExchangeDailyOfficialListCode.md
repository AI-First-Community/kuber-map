---
type: FIBO Class
title: "Stock Exchange Daily Official List (SEDOL) code"
description: "seven-character security identifier, issued by the London Stock Exchange, that is the National Securities Identifying Number (NSIN) for securities issued in the United Kingdom, which is also part of the ISIN for the security it identifies"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListCode
tags: [SEC, Release]
synonyms:
  - "SEDOL code"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListScheme.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange.md", provenance: fibo}
  - {type: is-registered-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/SEDOLMasterFile.md", provenance: fibo}
---

seven-character security identifier, issued by the London Stock Exchange, that is the National Securities Identifying Number (NSIN) for securities issued in the United Kingdom, which is also part of the ISIN for the security it identifies

### Relationships
- is-a: [ListedSecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md)
- is-a: [NationalSecuritiesIdentifyingNumber](/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- is-a: [ProprietarySecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)
- is-defined-in: [StockExchangeDailyOfficialListScheme](/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListScheme.md)
- is-issued-by: [LondonStockExchange](/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange.md)
- is-registered-by: [LondonStockExchange](/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange.md)
- is-registered-in: [SEDOLMasterFile](/SEC/Securities/SecuritiesIdentificationIndividuals/SEDOLMasterFile.md)
