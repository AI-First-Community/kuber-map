---
type: FIBO Class
title: "payment netting provision"
description: "netting provision that specifies the way in which all payments in a single currency owed between parties will be aggregated for each traded currency per value date and within the larger aggregate obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/PaymentNettingProvision
tags: [FND, Release]
detail: "For each value date and for each traded currency, the parties will aggregate and net all payments owed between them to arrive at a single currency obligation for each currency payable between the parties. The parties calculate net payments at some pre-agreed time, typically the day before value date (although it is possible to agree net payments on the value date, depending on the currency and time zone)."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/NettingProvision.md", provenance: fibo}
---

netting provision that specifies the way in which all payments in a single currency owed between parties will be aggregated for each traded currency per value date and within the larger aggregate obligation

### Relationships
- is-a: [NettingProvision](/FND/Agreements/Contracts/NettingProvision.md)
