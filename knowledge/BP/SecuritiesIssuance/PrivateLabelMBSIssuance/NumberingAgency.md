---
type: FIBO Class
title: "numbering agency"
description: "The agency which will provide the primary securitiy identifier for the security. Term origin:MBS PoC Reviews"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/NumberingAgency
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcessActor.md", provenance: fibo}
  - {type: allocates-identifier, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/AllocatePrimaryIdentifier.md", provenance: fibo}
  - {type: allocates-identifier, target: "/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AllocatePrimaryIdentifier.md", provenance: fibo}
---

The agency which will provide the primary securitiy identifier for the security. Term origin:MBS PoC Reviews

### Relationships
- is-a: [SecuritiesIssuanceProcessActor](/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcessActor.md)
- allocates-identifier: [AllocatePrimaryIdentifier](/BP/SecuritiesIssuance/AgencyMBSIssuance/AllocatePrimaryIdentifier.md)
- allocates-identifier: [AllocatePrimaryIdentifier](/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AllocatePrimaryIdentifier.md)
