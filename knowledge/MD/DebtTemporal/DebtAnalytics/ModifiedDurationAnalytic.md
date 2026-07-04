---
type: FIBO Class
title: "modified duration analytic"
description: "The percentage price change of a security for a given change in yield. The higher the modified duration of a security, the higher its risk. Ad/ModDuration = [duration / {1 + (IRR/M)}]; where IRR is the internal rate of return and M is the number of compounding periods per year."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/ModifiedDurationAnalytic
tags: [MD, Provisional]
detail: "The higher the MD the greater the change in price for a given change in yield."
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/DurationAnalytic.md", provenance: fibo}
  - {type: refers-to, target: "/MD/DebtTemporal/DebtAnalytics/MacCaulaysDurationAnalytic.md", provenance: fibo}
---

The percentage price change of a security for a given change in yield. The higher the modified duration of a security, the higher its risk. Ad/ModDuration = [duration / {1 + (IRR/M)}]; where IRR is the internal rate of return and M is the number of compounding periods per year.

### Relationships
- is-a: [DurationAnalytic](/MD/DebtTemporal/DebtAnalytics/DurationAnalytic.md)
- refers-to: [MacCaulaysDurationAnalytic](/MD/DebtTemporal/DebtAnalytics/MacCaulaysDurationAnalytic.md)
