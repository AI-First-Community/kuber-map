---
type: FIBO Class
title: "offering document"
description: "legal document that states the objectives, risks and terms of an investment"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
tags: [SEC, Release]
detail: "There are many variations, including offering memorandum, which is typically used in the context of a private placement, offering statement, which has slightly different meanings depending on the context (for securities, for bonds, etc.) and so forth. This concept is intended to act as a more abstract parent for these more nuanced concepts."
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/Publishers/Publication.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/LegalDocument.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: has-contractual-element, target: "/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md", provenance: fibo}
  - {type: has-date-of-issuance, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-expiration-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: is-evidence-for, target: "/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md", provenance: fibo}
---

legal document that states the objectives, risks and terms of an investment

### Relationships
- is-a: [Publication](/BE/FunctionalEntities/Publishers/Publication.md)
- is-a: [LegalDocument](/CMNS/Documents/LegalDocument.md)
- applies-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- has-contractual-element: [OfferingDocumentTerms](/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md)
- has-date-of-issuance: [Date](/CMNS/DatesAndTimes/Date.md)
- has-expiration-date: [Date](/CMNS/DatesAndTimes/Date.md)
- is-evidence-for: [SecuritiesOffering](/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)
