---
type: Cross-Domain Relation
title: "regulatory report -> regulation"
description: "A regulatory report exists because a regulation mandates it."
tags: [bridge, CMNS, FND]
relations:
  - {type: required-by, target: "/FND/Law/LegalCapacity/Regulation.md", provenance: curated}
source_class: "/CMNS/RegulatoryAgencies/RegulatoryReport.md"
kind: "cross-domain (CMNS->FND)"
citation: "Reporting obligations arise from regulations, e.g. HMDA report required by Regulation C"
rationale: "A regulatory report exists because a regulation mandates it. FIBO models RegulatoryReport (CMNS) and Regulation (FND) separately but leaves the report-to-mandating-regulation link implicit."
---

**regulatory report** --[required-by]--> **regulation**  _(curated bridge — cross-domain (CMNS->FND))_

A regulatory report exists because a regulation mandates it. FIBO models RegulatoryReport (CMNS) and Regulation (FND) separately but leaves the report-to-mandating-regulation link implicit.

*Citation:* Reporting obligations arise from regulations, e.g. HMDA report required by Regulation C
