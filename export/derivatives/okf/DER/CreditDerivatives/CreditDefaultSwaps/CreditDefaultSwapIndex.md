---
type: FIBO Class
title: "credit default swap index"
description: "index whose underlying reference obligations are credit default swap instruments"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwapIndex
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "The CDX North America Investment Grade index of CDS."
examples_provenance: curated
relations:
  - {type: is-a, target: "/IND/MarketIndices/BasketIndices/ReferenceIndex.md", provenance: fibo}
  - {type: is-based-on, target: "/DER/CreditDerivatives/CreditDefaultSwaps/BasketOfCreditDefaultSwaps.md", provenance: fibo}
---

index whose underlying reference obligations are credit default swap instruments

### Relationships
- is-a: [ReferenceIndex](/IND/MarketIndices/BasketIndices/ReferenceIndex.md)
- is-based-on: [BasketOfCreditDefaultSwaps](/DER/CreditDerivatives/CreditDefaultSwaps/BasketOfCreditDefaultSwaps.md)
