---
type: FIBO Class
title: "business party suffix"
description: "two-character (2 alphanumeric) code associated with the organization for the purposes of banking telecommunications"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartySuffix
tags: [FBC, Release]
detail: "In the prior version of the standard, position 7 of the BIC determined the location of the BIC in a particular country. In a country spanning over multiple time zones, each character may have been used to define a different time zone. If an organization moved location to a different time zone within the same country, the existing BIC would normally have been deleted and replaced by a new BIC with the appropriate location code. With the revision of the standard [and transition period ending November 2018], the location code has been re-defined as a 'party suffix' without any specific meaning. A new reference data attribute has been introduced in the SWIFTRef directories to indicate where the institution is located and to which time zone it refers."
relations:
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: is-defined-in, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md", provenance: fibo}
  - {type: is-included-in, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode.md", provenance: fibo}
---

two-character (2 alphanumeric) code associated with the organization for the purposes of banking telecommunications

### Relationships
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- is-defined-in: [BusinessIdentifierCodeScheme](/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md)
- is-included-in: [BusinessIdentifierCode](/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode.md)
