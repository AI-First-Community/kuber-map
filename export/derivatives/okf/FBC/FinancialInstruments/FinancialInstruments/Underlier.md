---
type: FIBO Class
title: "underlier"
description: "something that can be assigned a value in the marketplace that forms the basis for a derivative or pool-backed instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Underlier
tags: [FBC, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "Underlier means any rate (including interest and foreign exchange rates), currency, commodity, security, instrument of indebtedness, index, quantitative measure, occurrence or non-occurrence of an event, or other financial or economic interest, or property of any kind, or any interest therein or based on the value thereof, in or by reference to which any payment or delivery under a transaction is to be made or determined."
examples:
  - "The S&P 500 index underlying an index option."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Undergoer.md", provenance: fibo}
---

something that can be assigned a value in the marketplace that forms the basis for a derivative or pool-backed instrument

### Relationships
- is-a: [Undergoer](/CMNS/PartiesAndSituations/Undergoer.md)
