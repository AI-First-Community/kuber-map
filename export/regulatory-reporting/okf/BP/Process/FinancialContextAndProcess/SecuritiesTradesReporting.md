---
type: FIBO Class
title: "securities trades reporting"
description: "Post-trade process of reporting executed securities trades to a trade repository or regulator."
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/SecuritiesTradesReporting
tags: [BP, Provisional]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "Reporting an executed equity trade to a FINRA Trade Reporting Facility within seconds of execution."
examples_provenance: curated
relations:
  - {type: is-a, target: "/BP/Process/FinancialContextAndProcess/SecuritiesPostTrade.md", provenance: fibo}
---

Post-trade process of reporting executed securities trades to a trade repository or regulator.

### Relationships
- is-a: [SecuritiesPostTrade](/BP/Process/FinancialContextAndProcess/SecuritiesPostTrade.md)
