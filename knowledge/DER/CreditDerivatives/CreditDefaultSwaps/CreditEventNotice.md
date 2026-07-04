---
type: FIBO Class
title: "credit event notice"
description: "irrevocable written or verbal notice that states that a triggering event has occurred"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditEventNotice
tags: [DER, Release]
detail: "Notices of certain kinds of credit events are required as a condition of a credit default swap. Such notices are sent from a notifying party (either the buyer or the seller) to the counterparty. They provide information that assists the contract parties in determining whether a triggering credit event has occurred."
relations:
  - {type: is-a, target: "/CMNS/Documents/Notice.md", provenance: fibo}
  - {type: is-about, target: "/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md", provenance: fibo}
  - {type: is-provided-by, target: "/DER/CreditDerivatives/CreditDefaultSwaps/NotifyingParty.md", provenance: fibo}
---

irrevocable written or verbal notice that states that a triggering event has occurred

### Relationships
- is-a: [Notice](/CMNS/Documents/Notice.md)
- is-about: [TriggeringEvent](/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md)
- is-provided-by: [NotifyingParty](/DER/CreditDerivatives/CreditDefaultSwaps/NotifyingParty.md)
