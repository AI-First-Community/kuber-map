---
type: FIBO Class
title: "m b s tranche note"
description: "An individual note of a tranche."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote
tags: [SEC, Provisional]
detail: "A Tranche is made up of e.g. $500m in notes and so on. These may be in different notes, with different denominations. Analytics that would apply to the Tranche would by implication apply to each slice of the tranche."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md", provenance: fibo}
---

An individual note of a tranche.

### Relationships
- is-a: [PromissoryNote](/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md)
