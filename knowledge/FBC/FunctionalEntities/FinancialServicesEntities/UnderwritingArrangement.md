---
type: FIBO Class
title: "underwriting arrangement"
description: "written contract between parties that commits the underwriter to assuming risk"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/UnderwritingArrangement
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-party-role, target: "/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md", provenance: fibo}
---

written contract between parties that commits the underwriter to assuming risk

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-party-role: [Underwriter](/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md)
