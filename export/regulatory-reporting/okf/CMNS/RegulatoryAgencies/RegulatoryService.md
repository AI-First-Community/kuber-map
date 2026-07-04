---
type: FIBO Class
title: "regulatory service"
description: "service provided by a regulatory agency, which may include, but not be limited to, examination, monitoring, supervision, testing, or other capabilities required to ensure the integrity, fairness, safety, or other capacity of a given industry, organization, or product"
resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryService
tags: [CMNS]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "A supervisory service provided by a regulator, such as reviewing registration filings."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Organizations/Service.md", provenance: fibo}
  - {type: is-provided-by, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
---

service provided by a regulatory agency, which may include, but not be limited to, examination, monitoring, supervision, testing, or other capabilities required to ensure the integrity, fairness, safety, or other capacity of a given industry, organization, or product

### Relationships
- is-a: [Service](/CMNS/Organizations/Service.md)
- is-provided-by: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
