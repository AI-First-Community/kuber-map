---
type: FIBO Class
title: "counterparty"
description: "party to a contract with whom one negotiates on a given agreement"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
tags: [FND, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "The counterparty is usually the party 'on the other side' of a contract from the perspective of the issuer or holder. The term 'counterparty' can refer to any party to an agreement, depending on context."
examples:
  - "The bank on the other side of your interest-rate swap."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
---

party to a contract with whom one negotiates on a given agreement

### Relationships
- is-a: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
