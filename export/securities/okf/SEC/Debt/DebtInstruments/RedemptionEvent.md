---
type: FIBO Class
title: "redemption event"
description: "a prescriptive event involving the return of an investor's principal in a fixed-income security, such as a preferred stock or bond, or the sale of units in a mutual fund"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/RedemptionEvent
tags: [SEC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
examples:
  - "A bond reaching maturity and repaying principal to its holders."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/PrescriptiveEvent.md", provenance: fibo}
---

a prescriptive event involving the return of an investor's principal in a fixed-income security, such as a preferred stock or bond, or the sale of units in a mutual fund

### Relationships
- is-a: [PrescriptiveEvent](/SEC/Debt/DebtInstruments/PrescriptiveEvent.md)
