---
type: FIBO Class
title: "equity conversion terms"
description: "conversion terms specifying the details regarding conversion of shares into other securities"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityConversionTerms
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIssuance/ConversionTerms.md", provenance: fibo}
  - {type: specifies-conversion-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: specifies-conversion-into, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

conversion terms specifying the details regarding conversion of shares into other securities

### Relationships
- is-a: [ConversionTerms](/SEC/Securities/SecuritiesIssuance/ConversionTerms.md)
- specifies-conversion-date: [Date](/CMNS/DatesAndTimes/Date.md)
- specifies-conversion-into: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
