---
type: FIBO Class
title: "debt issuance process information"
description: "information specific to the issuance of a debt security"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/DebtIssuanceProcessInformation
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md", provenance: fibo}
  - {type: has-debt-issuance-purpose, target: "/BP/SecuritiesIssuance/DebtIssuance/DebtIssuancePurpose.md", provenance: fibo}
---

information specific to the issuance of a debt security

### Relationships
- is-a: [TradedInstrumentIssuanceProcessInformation](/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md)
- has-debt-issuance-purpose: [DebtIssuancePurpose](/BP/SecuritiesIssuance/DebtIssuance/DebtIssuancePurpose.md)
