---
type: FIBO Class
title: "fully paid share"
description: "share whose payment status indicates that no additional money is owed to the company by shareholders on the value of the shares"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/FullyPaidShare
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
  - {type: has-share-payment-status, target: "/SEC/Equities/EquityInstruments/FullyPaidShareStatus.md", provenance: fibo}
---

share whose payment status indicates that no additional money is owed to the company by shareholders on the value of the shares

### Relationships
- is-a: [Share](/SEC/Equities/EquityInstruments/Share.md)
- has-share-payment-status: [FullyPaidShareStatus](/SEC/Equities/EquityInstruments/FullyPaidShareStatus.md)
