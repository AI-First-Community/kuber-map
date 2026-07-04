---
type: FIBO Class
title: "sovereign debt instrument"
description: "debt security issued by the government of a country"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignDebtInstrument
tags: [SEC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
examples:
  - "A Japanese Government Bond (JGB) issued by the government of Japan."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity.md", provenance: fibo}
---

debt security issued by the government of a country

### Relationships
- is-a: [GovernmentIssuedDebtSecurity](/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity.md)
