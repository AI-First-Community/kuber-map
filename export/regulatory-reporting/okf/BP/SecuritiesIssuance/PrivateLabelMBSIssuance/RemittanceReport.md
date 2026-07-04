---
type: FIBO Class
title: "remittance report"
description: "Report containing a specific and limited set of information about the Deal. Term origin:MBS PoC Reviews"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/RemittanceReport
tags: [BP, Provisional]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "A monthly servicer remittance report on payments collected for a mortgage pool."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Reporting/Report.md", provenance: fibo}
---

Report containing a specific and limited set of information about the Deal. Term origin:MBS PoC Reviews

### Relationships
- is-a: [Report](/FND/Arrangements/Reporting/Report.md)
