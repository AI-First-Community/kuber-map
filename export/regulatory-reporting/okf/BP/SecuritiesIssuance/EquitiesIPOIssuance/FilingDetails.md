---
type: FIBO Class
title: "filing details"
description: "Document capturing the particulars of a regulatory filing, such as what was filed, when, and with which authority."
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/FilingDetails
tags: [BP, Provisional]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "The particulars of a filing: the form type, the filing date, and the receiving authority."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Documents/Document.md", provenance: fibo}
---

Document capturing the particulars of a regulatory filing, such as what was filed, when, and with which authority.

### Relationships
- is-a: [Document](/CMNS/Documents/Document.md)
