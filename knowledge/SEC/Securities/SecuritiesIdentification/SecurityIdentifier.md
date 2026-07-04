---
type: FIBO Class
title: "security identifier"
description: "any publicly available identifier that is used to identify a security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentifier
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md", provenance: fibo}
---

any publicly available identifier that is used to identify a security

### Relationships
- is-a: [FinancialInstrumentIdentifier](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)
- identifies: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- is-defined-in: [SecurityIdentificationScheme](/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md)
