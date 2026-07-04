---
type: FIBO Class
title: "correspondent"
description: "A bank, brokerage or other financial institution that is not a direct DTC member. Correspondents rely on direct DTC Participants to perform their DTC settlement services"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Correspondent
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/MuniIssuance/MuniIssuanceProcessParticipant.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractThirdParty.md", provenance: fibo}
  - {type: participates-in, target: "/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md", provenance: fibo}
---

A bank, brokerage or other financial institution that is not a direct DTC member. Correspondents rely on direct DTC Participants to perform their DTC settlement services

### Relationships
- is-a: [MuniIssuanceProcessParticipant](/BP/SecuritiesIssuance/MuniIssuance/MuniIssuanceProcessParticipant.md)
- is-a: [ContractThirdParty](/FND/Agreements/Contracts/ContractThirdParty.md)
- participates-in: [SecuritiesUnderwritingIssuanceProcess](/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md)
