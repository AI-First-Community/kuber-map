---
type: FIBO Class
title: "regulatory report"
description: "document required to support operational transparency that demonstrates compliance with some specification, law, policy, restriction, or other rule specified by a regulatory agency"
resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryReport
tags: [CMNS]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "Such a report may be needed for licensing, monitoring, taxation, or for other purposes that demonstrate the integrity, fairness, safety, or other capacity of a given industry, organization, or product."
examples:
  - "A HMDA loan/application register filed with the CFPB, or a MiFID II transaction report."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Reporting/Report.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/Record.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/ReferenceDocument.md", provenance: fibo}
---

document required to support operational transparency that demonstrates compliance with some specification, law, policy, restriction, or other rule specified by a regulatory agency

### Relationships
- is-a: [Report](/FND/Arrangements/Reporting/Report.md)
- is-a: [Record](/CMNS/Documents/Record.md)
- is-a: [ReferenceDocument](/CMNS/Documents/ReferenceDocument.md)
