---
type: FIBO Class
title: "share issuer"
description: "issuer of securities that represent an ownership interest in something"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ShareIssuer
tags: [SEC, Release]
detail: "This includes shares that represent equity ownership in a corporation, or ownership in a mutual fund, or an interest in a general or limited partnership, or ownership in a structured product, such as a real estate investment trust."
examples:
  - "A corporation that issues common shares to raise equity capital."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Issuer.md", provenance: fibo}
  - {type: issues, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
---

issuer of securities that represent an ownership interest in something

### Relationships
- is-a: [Issuer](/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)
- issues: [Share](/SEC/Equities/EquityInstruments/Share.md)
