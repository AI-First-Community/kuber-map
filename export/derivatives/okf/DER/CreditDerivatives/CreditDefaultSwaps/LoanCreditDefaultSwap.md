---
type: FIBO Class
title: "loan credit default swap"
description: "credit default swap whose underlying reference obligation is limited strictly to syndicated secured loans, rather than any type of corporate debt"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/LoanCreditDefaultSwap
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "A CDS whose reference obligation is a syndicated loan."
examples_provenance: curated
synonyms:
  - "LCDS"
relations:
  - {type: is-a, target: "/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md", provenance: fibo}
---

credit default swap whose underlying reference obligation is limited strictly to syndicated secured loans, rather than any type of corporate debt

### Relationships
- is-a: [CreditDefaultSwap](/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)
