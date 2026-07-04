---
type: FIBO Class
title: "cash flow structure"
description: "the structure related to one or more cash flows"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlowStructure
tags: [FND, Provisional]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/FND/Accounting/CashFlows/CashFlow.md", provenance: fibo}
  - {type: has-schedule, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: specifies, target: "/FND/Accounting/CashFlows/TriggeringEvent.md", provenance: fibo}
---

the structure related to one or more cash flows

### Relationships
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [CashFlow](/FND/Accounting/CashFlows/CashFlow.md)
- has-schedule: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- specifies: [TriggeringEvent](/FND/Accounting/CashFlows/TriggeringEvent.md)
