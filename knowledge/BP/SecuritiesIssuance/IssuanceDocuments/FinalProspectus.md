---
type: FIBO Class
title: "final prospectus"
description: "The final Prospectus for an issue describes the Offer Issue, including facts about the issue itself such as closing dates, and known facts about the securities that will form part of that issue."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/FinalProspectus
tags: [BP, Provisional]
detail: "Anticipated facts might include expected issue price, yields, pool parameters as appropriate for the type of instrument being issued. Term origin:SMER"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIssuance/Prospectus.md", provenance: fibo}
  - {type: has-contractual-element, target: "/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md", provenance: fibo}
  - {type: succeeds, target: "/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md", provenance: fibo}
---

The final Prospectus for an issue describes the Offer Issue, including facts about the issue itself such as closing dates, and known facts about the securities that will form part of that issue.

### Relationships
- is-a: [Prospectus](/SEC/Securities/SecuritiesIssuance/Prospectus.md)
- has-contractual-element: [OfferingDocumentTerms](/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md)
- succeeds: [PreliminaryProspectus](/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md)
