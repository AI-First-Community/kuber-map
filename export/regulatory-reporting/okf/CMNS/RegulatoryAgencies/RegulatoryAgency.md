---
type: FIBO Class
title: "regulatory agency"
description: "public authority or government agency responsible for exercising authority over something in a regulatory or supervisory capacity"
resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
tags: [CMNS]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "Typically, a regulatory agency is chartered to protect some constituancy, (e.g., investors in the financial industry, consumers with respect to product safety), to ensure the fairness and integrity of some market, and fair and safe business practices among the service providers in that market."
examples:
  - "See http://www.finra.org/AboutFINRA/ for an example describing a regulatory agency."
synonyms:
  - "regulator"
  - "regulatory authority"
  - "regulatory body"
relations:
  - {type: is-a, target: "/CMNS/BusinessAuthorizations/AuthorizingParty.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
  - {type: has-jurisdiction, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/FormalOrganization.md", provenance: fibo}
  - {type: issues, target: "/FBC/FunctionalEntities/RegulatoryAgencies/GovernmentIssuedLicense.md", provenance: fibo}
  - {type: provides, target: "/CMNS/RegulatoryAgencies/RegulatoryService.md", provenance: fibo}
---

public authority or government agency responsible for exercising authority over something in a regulatory or supervisory capacity

### Relationships
- is-a: [AuthorizingParty](/CMNS/BusinessAuthorizations/AuthorizingParty.md)
- is-a: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
- has-jurisdiction: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-played-by: [FormalOrganization](/CMNS/Organizations/FormalOrganization.md)
- issues: [GovernmentIssuedLicense](/FBC/FunctionalEntities/RegulatoryAgencies/GovernmentIssuedLicense.md)
- provides: [RegulatoryService](/CMNS/RegulatoryAgencies/RegulatoryService.md)
