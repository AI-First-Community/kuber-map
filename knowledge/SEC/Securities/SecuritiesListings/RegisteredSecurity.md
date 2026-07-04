---
type: FIBO Class
title: "registered security"
description: "security that is registered with some registration authority"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/RegisteredSecurity
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: has-registration-date, target: "/CMNS/DatesAndTimes/CombinedDateTime.md", provenance: fibo}
  - {type: is-registered, target: "/CMNS/RegistrationAuthorities/RegistrationAuthority.md", provenance: fibo}
---

security that is registered with some registration authority

### Relationships
- is-a: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- has-registration-date: [CombinedDateTime](/CMNS/DatesAndTimes/CombinedDateTime.md)
- is-registered: [RegistrationAuthority](/CMNS/RegistrationAuthorities/RegistrationAuthority.md)
