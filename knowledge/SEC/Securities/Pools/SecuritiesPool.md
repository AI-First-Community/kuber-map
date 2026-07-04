---
type: FIBO Class
title: "securities pool"
description: "pool of securities organized for the purpose of issuing notes against those securities"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/SecuritiesPool
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/InstrumentPool.md", provenance: fibo}
  - {type: has-member, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

pool of securities organized for the purpose of issuing notes against those securities

### Relationships
- is-a: [InstrumentPool](/SEC/Securities/Pools/InstrumentPool.md)
- has-member: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
