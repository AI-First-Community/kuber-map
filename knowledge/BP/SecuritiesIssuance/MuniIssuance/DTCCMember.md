---
type: FIBO Class
title: "d t c c member"
description: "A firm which is a member of DTCC. Note: this Actor may perform any of the Roles described elsewhere in this Issuance model, i.e. the DTCC Member may also be any of the Actors defined. REVIEW: does this apply to ALL the defined Actor types?"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/DTCCMember
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/MuniIssuance/MuniIssuanceProcessParticipant.md", provenance: fibo}
  - {type: participates-in, target: "/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md", provenance: fibo}
---

A firm which is a member of DTCC. Note: this Actor may perform any of the Roles described elsewhere in this Issuance model, i.e. the DTCC Member may also be any of the Actors defined. REVIEW: does this apply to ALL the defined Actor types?

### Relationships
- is-a: [MuniIssuanceProcessParticipant](/BP/SecuritiesIssuance/MuniIssuance/MuniIssuanceProcessParticipant.md)
- participates-in: [SecuritiesUnderwritingIssuanceProcess](/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md)
