---
type: FIBO Class
title: "preferred share"
description: "share that pays dividends at a specified rate and has preference over common shares in the payment of dividends and liquidation of corporate assets"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
tags: [SEC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
examples:
  - "A 5% preferred share paying a fixed dividend ahead of common shareholders."
examples_provenance: curated
synonyms:
  - "preference share"
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
  - {type: has-maturity-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-senior-to, target: "/SEC/Equities/EquityInstruments/CommonShare.md", provenance: fibo}
---

share that pays dividends at a specified rate and has preference over common shares in the payment of dividends and liquidation of corporate assets

### Relationships
- is-a: [Share](/SEC/Equities/EquityInstruments/Share.md)
- has-maturity-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-senior-to: [CommonShare](/SEC/Equities/EquityInstruments/CommonShare.md)
