---
type: Cross-Domain Relation
title: "lender -> financial institution"
description: "Lender is modeled as a party role (is-a ContractParty/Creditor); FinancialInstitution is the legal-entity type that plays it."
tags: [bridge, FBC, FBC]
relations:
  - {type: played-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: curated}
source_class: "/FBC/DebtAndEquities/Debt/Lender.md"
kind: "role->entity gap (FBC)"
citation: "FIBO FBC party-role vs entity modeling"
rationale: "Lender is modeled as a party role (is-a ContractParty/Creditor); FinancialInstitution is the legal-entity type that plays it. FIBO leaves the role-to-entity link implicit, blocking resolution of 'the lender' to a regulated institution."
---

**lender** --[played-by]--> **financial institution**  _(curated bridge — role->entity gap (FBC))_

Lender is modeled as a party role (is-a ContractParty/Creditor); FinancialInstitution is the legal-entity type that plays it. FIBO leaves the role-to-entity link implicit, blocking resolution of 'the lender' to a regulated institution.

*Citation:* FIBO FBC party-role vs entity modeling
