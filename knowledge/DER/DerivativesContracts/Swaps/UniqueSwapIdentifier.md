---
type: FIBO Class
title: "unique swap identifier"
description: "identifier for a swap that is used in recordkeeping and swap data reporting"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier
tags: [DER, Release]
synonyms:
  - "USI"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
---

identifier for a swap that is used in recordkeeping and swap data reporting

### Relationships
- is-a: [FinancialInstrumentIdentifier](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)
- identifies: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
