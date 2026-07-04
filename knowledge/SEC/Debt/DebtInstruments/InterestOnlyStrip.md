---
type: FIBO Class
title: "interest-only strip"
description: "a strip that represents the non-principal portion of the monthly payments on the underlying debt instrument, such as a bond"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/InterestOnlyStrip
tags: [SEC, Release]
detail: "An interest-only strip holder is interested in rising rates and no prepayment, as prepayment would cause them forfeit future interest payments and receive nothing from the return of the principal."
examples:
  - "An interest-only strip can be reintegrated into other synthetic or engineered products. For example, interest-only strips can be pooled to create or make up a portion of a larger collateralized mortgage obligation (CMO), asset-backed security (ABS) or collateralized debt obligation (CDO) structure."
synonyms:
  - "IO strip"
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/Strip.md", provenance: fibo}
---

a strip that represents the non-principal portion of the monthly payments on the underlying debt instrument, such as a bond

### Relationships
- is-a: [Strip](/SEC/Debt/DebtInstruments/Strip.md)
