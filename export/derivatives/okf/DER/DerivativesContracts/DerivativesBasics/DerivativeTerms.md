---
type: FIBO Class
title: "derivative terms"
description: "contractual terms specific to derivative contracts, including terms related to payments and delivery between parties"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "The strike, expiry, and notional recorded in an option's contract terms."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractualCommitment.md", provenance: fibo}
---

contractual terms specific to derivative contracts, including terms related to payments and delivery between parties

### Relationships
- is-a: [ContractualCommitment](/FND/Agreements/Contracts/ContractualCommitment.md)
