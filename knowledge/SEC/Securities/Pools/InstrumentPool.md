---
type: FIBO Class
title: "instrument pool"
description: "pool consisting of financial instruments that may be included in the same investment vehicle"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/InstrumentPool
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/Pool.md", provenance: fibo}
  - {type: has-member, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md", provenance: fibo}
---

pool consisting of financial instruments that may be included in the same investment vehicle

### Relationships
- is-a: [Pool](/SEC/Securities/Pools/Pool.md)
- has-member: [FinancialInstrument](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
