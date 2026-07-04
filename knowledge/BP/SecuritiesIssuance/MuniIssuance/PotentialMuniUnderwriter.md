---
type: FIBO Class
title: "potential muni underwriter"
description: "An intermediary between an issuer of a security and the investing public. An underwriter can either be DTC Participant or Correspondent who would clear the underwriting deal using the Crediting Participant."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceProcess/PotentialUnderwriter.md", provenance: fibo}
  - {type: underwrites, target: "/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md", provenance: fibo}
---

An intermediary between an issuer of a security and the investing public. An underwriter can either be DTC Participant or Correspondent who would clear the underwriting deal using the Crediting Participant.

### Relationships
- is-a: [PotentialUnderwriter](/BP/SecuritiesIssuance/IssuanceProcess/PotentialUnderwriter.md)
- underwrites: [SecuritiesUnderwritingIssuanceProcess](/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md)
