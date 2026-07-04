---
type: FIBO Class
title: "swap confirmation"
description: "formal confirmation that codifies the terms and conditions specific to a lifecycle event with respect to the overall transaction between the parties"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapConfirmation
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/SwapLifecycleEvent.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation.md", provenance: fibo}
  - {type: has-contract-party, target: "/DER/DerivativesContracts/Swaps/SwapParty.md", provenance: fibo}
---

formal confirmation that codifies the terms and conditions specific to a lifecycle event with respect to the overall transaction between the parties

### Relationships
- is-a: [SwapLifecycleEvent](/DER/DerivativesContracts/Swaps/SwapLifecycleEvent.md)
- is-a: [TransactionConfirmation](/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation.md)
- has-contract-party: [SwapParty](/DER/DerivativesContracts/Swaps/SwapParty.md)
