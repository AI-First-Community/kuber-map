---
type: FIBO Class
title: "entitlement"
description: "financial instrument that provides the holder an interest in, or the privilege to subscribe to, or to receive specific assets under terms specified"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
tags: [FBC, Release]
detail: "Note that certain fund units, including but not limited to units in pension funds and other non-public investment structures may be considered entitlements but not securities. They may or may not be identified using traditional financial instrument identifiers. Some entitlements, such as warrants, whose value changes based on the value of some underlier, are considered derivative instruments."
synonyms:
  - "right"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md", provenance: fibo}
  - {type: is-issued-in-form, target: "/SEC/Securities/SecuritiesIssuance/SecurityForm.md", provenance: fibo}
---

financial instrument that provides the holder an interest in, or the privilege to subscribe to, or to receive specific assets under terms specified

### Relationships
- is-a: [FinancialInstrument](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- is-issued-in-form: [SecurityForm](/SEC/Securities/SecuritiesIssuance/SecurityForm.md)
