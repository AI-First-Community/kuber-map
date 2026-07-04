---
type: FIBO Class
title: "next call"
description: "The next call of the issue, as at the current time."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NextCall
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/CallEvent.md", provenance: fibo}
  - {type: has-date, target: "/MD/DebtTemporal/DebtAnalytics/NextCallDate.md", provenance: fibo}
---

The next call of the issue, as at the current time.

### Relationships
- is-a: [CallEvent](/SEC/Debt/DebtInstruments/CallEvent.md)
- has-date: [NextCallDate](/MD/DebtTemporal/DebtAnalytics/NextCallDate.md)
