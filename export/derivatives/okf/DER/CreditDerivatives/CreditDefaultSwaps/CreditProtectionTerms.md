---
type: FIBO Class
title: "credit protection terms"
description: "legal terms that define triggering events and associated conditions related to settlement"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "Note that there may be additional payment schedules or a more complex calculation formula required depending on the terms of the contract."
examples:
  - "The terms defining which credit events trigger a CDS payout."
examples_provenance: curated
synonyms:
  - "contingent leg"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md", provenance: fibo}
  - {type: has-buyer, target: "/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationBuyer.md", provenance: fibo}
  - {type: has-scheduled-termination-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-seller, target: "/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationSeller.md", provenance: fibo}
  - {type: specifies, target: "/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation.md", provenance: fibo}
  - {type: specifies, target: "/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md", provenance: fibo}
---

legal terms that define triggering events and associated conditions related to settlement

### Relationships
- is-a: [DerivativeTerms](/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- has-buyer: [DeliverableObligationBuyer](/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationBuyer.md)
- has-scheduled-termination-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-seller: [DeliverableObligationSeller](/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationSeller.md)
- specifies: [DeliverableObligation](/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation.md)
- specifies: [TriggeringEvent](/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md)
