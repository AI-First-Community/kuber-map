---
type: FIBO Class
title: "c d o pool"
description: "A pool of CDO securities. The underlying of the CDO Squared is a pool of CDO instruments."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPool
tags: [SEC, Provisional]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
examples:
  - "The portfolio of leveraged loans backing a collateralized loan obligation."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
---

A pool of CDO securities. The underlying of the CDO Squared is a pool of CDO instruments.

### Relationships
- is-a: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
