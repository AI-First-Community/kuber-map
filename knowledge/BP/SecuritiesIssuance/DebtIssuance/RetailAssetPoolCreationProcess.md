---
type: FIBO Class
title: "retail asset pool creation process"
description: "The process by which pools of assets are created. These may then be used in the issue of securities based on those asset pools as underlying."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/RetailAssetPoolCreationProcess
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/DebtIssuance/AssetPoolCreationProcess.md", provenance: fibo}
  - {type: is-produced-by, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
  - {type: precedes, target: "/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcess.md", provenance: fibo}
---

The process by which pools of assets are created. These may then be used in the issue of securities based on those asset pools as underlying.

### Relationships
- is-a: [AssetPoolCreationProcess](/BP/SecuritiesIssuance/DebtIssuance/AssetPoolCreationProcess.md)
- is-produced-by: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
- precedes: [PoolBackedSecuritySecuritizationProcess](/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcess.md)
