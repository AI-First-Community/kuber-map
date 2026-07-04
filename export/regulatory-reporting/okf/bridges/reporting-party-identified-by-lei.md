---
type: Cross-Domain Relation
title: "reporting party -> legal entity identifier"
description: "In supervisory and transaction reporting the party that submits a report is identified by its Legal Entity Identifier."
tags: [bridge, FND, BE]
relations:
  - {type: identified-by, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: curated}
source_class: "/FND/Arrangements/Reporting/ReportingParty.md"
kind: "cross-domain (FND->BE)"
citation: "ISO 17442 (LEI); MiFID II / ESMA transaction reporting; CFTC swap reporting"
rationale: "In supervisory and transaction reporting the party that submits a report is identified by its Legal Entity Identifier. FIBO defines the ReportingParty role (FND) and the LegalEntityIdentifier (BE) but does not connect a reporting party to its LEI."
---

**reporting party** --[identified-by]--> **legal entity identifier**  _(curated bridge — cross-domain (FND->BE))_

In supervisory and transaction reporting the party that submits a report is identified by its Legal Entity Identifier. FIBO defines the ReportingParty role (FND) and the LegalEntityIdentifier (BE) but does not connect a reporting party to its LEI.

*Citation:* ISO 17442 (LEI); MiFID II / ESMA transaction reporting; CFTC swap reporting
