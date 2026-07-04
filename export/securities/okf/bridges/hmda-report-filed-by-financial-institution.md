---
type: Cross-Domain Relation
title: "HMDA report -> financial institution"
description: "A HMDA report is filed by a covered financial institution."
tags: [bridge, LOAN, FBC]
relations:
  - {type: filed-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: curated}
source_class: "/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report.md"
kind: "cross-domain (LOAN->FBC)"
citation: "12 CFR 1003.2 (covered institution); 12 CFR 1003.5 (reporting)"
rationale: "A HMDA report is filed by a covered financial institution. FIBO links HMDA-Report to the RegulatoryAgency it is submitted-to, but not to the filing institution — leaving the filer unresolved."
---

**HMDA report** --[filed-by]--> **financial institution**  _(curated bridge — cross-domain (LOAN->FBC))_

A HMDA report is filed by a covered financial institution. FIBO links HMDA-Report to the RegulatoryAgency it is submitted-to, but not to the filing institution — leaving the filer unresolved.

*Citation:* 12 CFR 1003.2 (covered institution); 12 CFR 1003.5 (reporting)
