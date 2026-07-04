---
type: FIBO Class
title: "m b s pool"
description: "A pool investment consisting of a collection of MBS instruments."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MBSPool
tags: [SEC, Provisional]
examples:
  - "The pool of conforming 30-year mortgages backing a Fannie Mae MBS."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
---

A pool investment consisting of a collection of MBS instruments.

### Relationships
- is-a: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
