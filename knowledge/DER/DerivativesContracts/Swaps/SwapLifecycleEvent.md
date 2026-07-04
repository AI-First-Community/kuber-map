---
type: FIBO Class
title: "swap lifecycle event"
description: "event that occurs during the lifecycle of a swap, where the overall set of events includes those specific to the issuer, front office, middle office, and/or back office processes"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLifecycleEvent
tags: [DER, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleEvent.md", provenance: fibo}
  - {type: applies-to, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
  - {type: has-party-role, target: "/DER/DerivativesContracts/Swaps/SwapParty.md", provenance: fibo}
  - {type: has-swap-identifier, target: "/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier.md", provenance: fibo}
  - {type: is-identified-by, target: "/DER/DerivativesContracts/Swaps/SwapLifecycleEventIdentifier.md", provenance: fibo}
---

event that occurs during the lifecycle of a swap, where the overall set of events includes those specific to the issuer, front office, middle office, and/or back office processes

### Relationships
- is-a: [LifecycleEvent](/FND/Arrangements/Lifecycles/LifecycleEvent.md)
- applies-to: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
- has-party-role: [SwapParty](/DER/DerivativesContracts/Swaps/SwapParty.md)
- has-swap-identifier: [UniqueSwapIdentifier](/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier.md)
- is-identified-by: [SwapLifecycleEventIdentifier](/DER/DerivativesContracts/Swaps/SwapLifecycleEventIdentifier.md)
