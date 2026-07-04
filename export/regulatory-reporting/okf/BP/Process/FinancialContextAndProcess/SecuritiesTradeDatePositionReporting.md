---
type: FIBO Class
title: "securities trade date position reporting"
description: "Reporting of a party's securities positions as of a given trade date, used for regulatory position and transparency reporting."
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/SecuritiesTradeDatePositionReporting
tags: [BP, Provisional]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "Reporting a fund's securities positions as of the trade date for regulatory transparency."
examples_provenance: curated
relations:
  - {type: is-a, target: "/BP/Process/FinancialContextAndProcess/SecuritiesTrade.md", provenance: fibo}
---

Reporting of a party's securities positions as of a given trade date, used for regulatory position and transparency reporting.

### Relationships
- is-a: [SecuritiesTrade](/BP/Process/FinancialContextAndProcess/SecuritiesTrade.md)
