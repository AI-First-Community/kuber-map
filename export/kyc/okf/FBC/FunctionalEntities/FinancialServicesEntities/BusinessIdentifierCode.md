---
type: FIBO Class
title: "business identifier code"
description: "international identifier for financial and non-financial institutions used to facilitate automated processing of information for financial services"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode
tags: [FBC, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "The BIC is used for addressing messages, routing business transactions and identifying business parties. Note that the use of OrganizationSubUnitIdentifier in FIBO corresponds to the Branch Code in the SWIFT scheme."
examples:
  - "BOFAUS3N, the SWIFT BIC for Bank of America."
examples_provenance: curated
synonyms:
  - "BIC"
  - "SWIFT ID"
  - "SWIFT code"
  - "SWIFT-BIC"
  - "bank identifier code"
  - "business entity identifier"
relations:
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/ContextualIdentifiers/StructuredIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/OrganizationIdentifier.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartyPrefix.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartySuffix.md", provenance: fibo}
  - {type: comprises, target: "/CMNS/Organizations/OrganizationSubUnitIdentifier.md", provenance: fibo}
  - {type: comprises, target: "/LCC/Countries/CountryRepresentation/Alpha2Code.md", provenance: fibo}
  - {type: denotes, target: "/CMNS/Organizations/FormalOrganization.md", provenance: fibo}
  - {type: is-member-of, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md", provenance: fibo}
---

international identifier for financial and non-financial institutions used to facilitate automated processing of information for financial services

### Relationships
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- is-a: [StructuredIdentifier](/CMNS/ContextualIdentifiers/StructuredIdentifier.md)
- is-a: [OrganizationIdentifier](/CMNS/Organizations/OrganizationIdentifier.md)
- comprises: [BusinessPartyPrefix](/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartyPrefix.md)
- comprises: [BusinessPartySuffix](/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartySuffix.md)
- comprises: [OrganizationSubUnitIdentifier](/CMNS/Organizations/OrganizationSubUnitIdentifier.md)
- comprises: [Alpha2Code](/LCC/Countries/CountryRepresentation/Alpha2Code.md)
- denotes: [FormalOrganization](/CMNS/Organizations/FormalOrganization.md)
- is-member-of: [BusinessIdentifierCodeScheme](/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md)
