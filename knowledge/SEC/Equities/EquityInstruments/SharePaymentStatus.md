---
type: FIBO Class
title: "share payment status"
description: "classifier that specifies the overall payment status for shares issued"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SharePaymentStatus
tags: [SEC, Release]
detail: "When a company issues shares upon incorporation or through an initial or secondary issuance, shareholders are required to pay a set amount for those shares. Once the company has received the full amount from shareholders, the shares become fully paid shares."
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStatus.md", provenance: fibo}
  - {type: classifies, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
---

classifier that specifies the overall payment status for shares issued

### Relationships
- is-a: [LifecycleStatus](/FND/Arrangements/Lifecycles/LifecycleStatus.md)
- classifies: [Share](/SEC/Equities/EquityInstruments/Share.md)
