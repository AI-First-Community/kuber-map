---
type: FIBO Class
title: "m b s issuer"
description: "The issuer of a Mortgage Backed Security."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MBSIssuer
tags: [SEC, Provisional]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
detail: "This can be an agency that exists for this purpose or it may be the issuer of the original mortgages in the pool."
examples:
  - "A government-sponsored enterprise such as Fannie Mae issuing mortgage-backed securities."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Issuer.md", provenance: fibo}
---

The issuer of a Mortgage Backed Security.

### Relationships
- is-a: [Issuer](/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)
