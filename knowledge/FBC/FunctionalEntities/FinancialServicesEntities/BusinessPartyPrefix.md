---
type: FIBO Class
title: "business party prefix"
description: "four-character (4 alphanumeric) code associated with an organization for the purposes of banking telecommunications"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartyPrefix
tags: [FBC, Release]
detail: "For new BIC registration by an organization already identified with a BIC or an affiliated organization [after the transition period ending November 2018], SWIFT will still reserve the usage of an existing party prefix to these organizations. This legacy rule will be reserved to existing BIC owners. If they wish to preserve this value, no other organization will be allowed to use the same code For new BIC registration from an organization not yet identified by a BIC, the party prefix will be allocated at the discretion of the RA. The code will not have a mnemonic or acronym value anymore."
synonyms:
  - "bank code"
  - "institution code"
relations:
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/OrganizationIdentifier.md", provenance: fibo}
  - {type: is-defined-in, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md", provenance: fibo}
  - {type: is-included-in, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode.md", provenance: fibo}
---

four-character (4 alphanumeric) code associated with an organization for the purposes of banking telecommunications

### Relationships
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- is-a: [OrganizationIdentifier](/CMNS/Organizations/OrganizationIdentifier.md)
- is-defined-in: [BusinessIdentifierCodeScheme](/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md)
- is-included-in: [BusinessIdentifierCode](/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode.md)
