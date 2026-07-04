---
type: FIBO Class
title: "triggering event"
description: "event that relates to or triggers some aspect of a credit default swap"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "A triggering event is typically a credit event, but could be anything that happens in the marketplace. For example, a weather-specific contract could be triggered by a hurricane - which wouldn't be considered a credit event per se."
examples:
  - "A bond issuer's bankruptcy that triggers a CDS payout."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
---

event that relates to or triggers some aspect of a credit default swap

### Relationships
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
