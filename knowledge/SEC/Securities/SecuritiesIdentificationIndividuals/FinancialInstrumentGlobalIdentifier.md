---
type: FIBO Class
title: "financial instrument global identifier"
description: "financial instrument identifier that is defined as specified in the Object Management Group (OMG) Financial Instrument Global Identifier (FIGI) Specification"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifier
tags: [SEC, Release]
detail: "The development of the Financial Instrument Global Identifier (FIGI) originated from a need for a standard methodology to bridge across multiple identification systems for financial instruments. Without prejudice against any existing symbol-based solutions, or any question of the validity of one system over the other, the FIGI standard utilizes a metadata driven approach to enable the unique and persistent identification of financial instruments. While in most cases, a FIGI uniquely identifies a security, there are situations outside of the U.S. where it instead identifies a listing for a security, similar to a ticker symbol."
synonyms:
  - "FIGI"
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierScheme.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md", provenance: fibo}
  - {type: is-registered-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry.md", provenance: fibo}
---

financial instrument identifier that is defined as specified in the Object Management Group (OMG) Financial Instrument Global Identifier (FIGI) Specification

### Relationships
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
- is-defined-in: [FinancialInstrumentGlobalIdentifierScheme](/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierScheme.md)
- is-issued-by: [BloombergLP](/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md)
- is-registered-by: [BloombergLP](/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md)
- is-registered-in: [FinancialInstrumentGlobalIdentifierRegistry](/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry.md)
