---
type: FIBO Class
title: "non-tradable fund unit"
description: "security representing an interest in a fund that cannot be traded ontside of the fund itself"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/NonTradableFundUnit
tags: [SEC, Release]
detail: "Non-tradable fund units are commonly found in pension funds, insurance pools, or internal benefit plans, where units serve as accounting or entitlement mechanisms without market transferability."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Funds/Funds/FundUnit.md", provenance: fibo}
---

security representing an interest in a fund that cannot be traded ontside of the fund itself

### Relationships
- is-a: [NonNegotiableSecurity](/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity.md)
- is-a: [FundUnit](/SEC/Funds/Funds/FundUnit.md)
