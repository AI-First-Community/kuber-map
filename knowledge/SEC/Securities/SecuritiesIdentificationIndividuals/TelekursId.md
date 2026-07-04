---
type: FIBO Class
title: "Telekurs Id"
description: "identifier used to identify financial instruments owned, managed, and distributed by SIX Financial Information (formerly Telekurs AG and subsequently SIX Telekurs Ltd.)"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/TelekursId
tags: [SEC, Release]
detail: "The Telekurs Id was phased out in favor of the Valoren (Valor Nummer in Swiss German) in 2013."
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentificationIndividuals/TelekursSecurityIdentifierScheme.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md", provenance: fibo}
---

identifier used to identify financial instruments owned, managed, and distributed by SIX Financial Information (formerly Telekurs AG and subsequently SIX Telekurs Ltd.)

### Relationships
- is-a: [ProprietarySecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)
- is-defined-in: [TelekursSecurityIdentifierScheme](/SEC/Securities/SecuritiesIdentificationIndividuals/TelekursSecurityIdentifierScheme.md)
- is-issued-by: [SIXFinancialInformation](/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md)
- is-registered-by: [SIXFinancialInformation](/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md)
