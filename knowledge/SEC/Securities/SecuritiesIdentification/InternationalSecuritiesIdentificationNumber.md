---
type: FIBO Class
title: "international securities identification number"
description: "security identifier that is defined as specified in ISO 6166, Securities and related financial instruments -- International securities identification numbering system (ISIN)"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/InternationalSecuritiesIdentificationNumber
tags: [SEC, Release]
detail: "ISINs consist of two alphabetic characters, which are the ISO 3166-1 alpha-2 code for the issuing country, nine alpha-numeric characters (the National Securities Identifying Number, or NSIN, which identifies the security, padded as necessary with leading zeros), and one numerical check digit. The ISIN is specified as a class of identifiers because although there is a scheme associated with the structure of an ISIN, there are many country-specific variations issued by national numbering agencies."
synonyms:
  - "ISIN"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/ContextualIdentifiers/StructuredIdentifier.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md", provenance: fibo}
  - {type: comprises, target: "/LCC/Countries/CountryRepresentation/Alpha2Code.md", provenance: fibo}
---

security identifier that is defined as specified in ISO 6166, Securities and related financial instruments -- International securities identification numbering system (ISIN)

### Relationships
- is-a: [SecurityIdentifier](/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md)
- is-a: [StructuredIdentifier](/CMNS/ContextualIdentifiers/StructuredIdentifier.md)
- comprises: [NationalSecuritiesIdentifyingNumber](/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- comprises: [Alpha2Code](/LCC/Countries/CountryRepresentation/Alpha2Code.md)
