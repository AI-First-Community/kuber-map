---
type: FIBO Class
title: "register with regulatory authority"
description: "Process step in which an issuer registers a securities offering with the relevant regulatory authority before it can be listed or sold."
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/RegisterWithRegulatoryAuthority
tags: [BP, Provisional]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "Filing a registration statement with the SEC before an initial public offering."
examples_provenance: curated
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/EquitiesIPOIssuance/InitialPublicOfferingProcessStep.md", provenance: fibo}
  - {type: is-provided-by, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
---

Process step in which an issuer registers a securities offering with the relevant regulatory authority before it can be listed or sold.

### Relationships
- is-a: [InitialPublicOfferingProcessStep](/BP/SecuritiesIssuance/EquitiesIPOIssuance/InitialPublicOfferingProcessStep.md)
- is-provided-by: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
