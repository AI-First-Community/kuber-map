---
type: FIBO Class
title: "non agency jump tranche"
description: "A tranche where if there is some sort of trigger event reached then the holders of the tranche will begin to receive payments."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md", provenance: fibo}
  - {type: specifies-trigger, target: "/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent.md", provenance: fibo}
---

A tranche where if there is some sort of trigger event reached then the holders of the tranche will begin to receive payments.

### Relationships
- is-a: [TranchedMBSInstrument](/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)
- specifies-trigger: [JumpZTriggerEvent](/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent.md)
