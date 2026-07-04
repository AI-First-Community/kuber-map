---
type: FIBO Class
title: "non agency regular jump z tranche"
description: "Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyRegularJumpZTranche
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpZTranche.md", provenance: fibo}
  - {type: reverts, target: "/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEventReversal.md", provenance: fibo}
---

Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.

### Relationships
- is-a: [NonAgencyJumpZTranche](/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpZTranche.md)
- reverts: [JumpZTriggerEventReversal](/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEventReversal.md)
