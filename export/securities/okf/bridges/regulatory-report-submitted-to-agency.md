---
type: Cross-Domain Relation
title: "regulatory report -> regulatory agency"
description: "A regulatory report is submitted to the regulatory agency that requires it."
tags: [bridge, CMNS, CMNS]
relations:
  - {type: submitted-to, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: curated}
source_class: "/CMNS/RegulatoryAgencies/RegulatoryReport.md"
kind: "intra-domain gap (CMNS)"
citation: "General supervisory-reporting practice; e.g. HMDA filing to the CFPB, MiFID II reporting to national competent authorities"
rationale: "A regulatory report is submitted to the regulatory agency that requires it. FIBO defines both RegulatoryReport and RegulatoryAgency in Commons but does not draw the edge from a report to the agency it is filed with."
---

**regulatory report** --[submitted-to]--> **regulatory agency**  _(curated bridge — intra-domain gap (CMNS))_

A regulatory report is submitted to the regulatory agency that requires it. FIBO defines both RegulatoryReport and RegulatoryAgency in Commons but does not draw the edge from a report to the agency it is filed with.

*Citation:* General supervisory-reporting practice; e.g. HMDA filing to the CFPB, MiFID II reporting to national competent authorities
