---
type: FIBO Class
title: "swaption"
description: "over-the-counter option that confers the right but not the obligation, to enter into a swap transaction at some time in the future"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/Swaption
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "A swaption, also known as a swap option, refers to an option to enter into an interest rate swap or some other type of swap. In exchange for an options premium, the buyer gains the right but not the obligation to enter into a specified swap agreement with the issuer on a specified future date."
examples:
  - "An option to enter a 5-year interest-rate swap one year from now."
examples_provenance: curated
synonyms:
  - "swap option"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
---

over-the-counter option that confers the right but not the obligation, to enter into a swap transaction at some time in the future

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
