---
type: FIBO Class
title: "swap"
description: "derivative instrument whereby counterparties agree to exchange periodic streams of cash flows or liabilities from two different financial instruments with each other"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "The notional amount, effective date and termination date are some of the properties that each swap leg has that are taken from the swap contract. The underlying instruments can be almost anything, representing various asset classes, but most swaps involve cash flows (streams of payments or other commitments over time) based on a notional principal amount that both parties agree to. Usually, the principal does not change hands. Each cash flow comprises one leg of the swap. One cash flow is generally fixed, while the other is variable, that is, based on a a benchmark interest rate, floating currency exchange rate or index price."
examples:
  - "A contract in which two parties exchange fixed for floating interest payments."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md", provenance: fibo}
  - {type: exchanges, target: "/DER/DerivativesContracts/Swaps/SwapLeg.md", provenance: fibo}
  - {type: has-contract-party, target: "/DER/DerivativesContracts/Swaps/SwapParty.md", provenance: fibo}
  - {type: has-contractual-element, target: "/DER/DerivativesContracts/Swaps/SwapTerms.md", provenance: fibo}
  - {type: is-identified-by, target: "/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier.md", provenance: fibo}
---

derivative instrument whereby counterparties agree to exchange periodic streams of cash flows or liabilities from two different financial instruments with each other

### Relationships
- is-a: [DerivativeInstrument](/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)
- exchanges: [SwapLeg](/DER/DerivativesContracts/Swaps/SwapLeg.md)
- has-contract-party: [SwapParty](/DER/DerivativesContracts/Swaps/SwapParty.md)
- has-contractual-element: [SwapTerms](/DER/DerivativesContracts/Swaps/SwapTerms.md)
- is-identified-by: [UniqueSwapIdentifier](/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier.md)
