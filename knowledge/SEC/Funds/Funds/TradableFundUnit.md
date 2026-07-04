---
type: FIBO Class
title: "tradable fund unit"
description: "security representing a tradable interest in a fund"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/TradableFundUnit
tags: [SEC, Release]
detail: "Tradable fund units typically occur in collective investment schemes such as mutual funds or exchange-traded funds (ETFs), where units are bought and sold on regulated markets."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Funds/Funds/FundUnit.md", provenance: fibo}
---

security representing a tradable interest in a fund

### Relationships
- is-a: [EquityInstrument](/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument.md)
- is-a: [NegotiableSecurity](/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity.md)
- is-a: [FundUnit](/SEC/Funds/Funds/FundUnit.md)
