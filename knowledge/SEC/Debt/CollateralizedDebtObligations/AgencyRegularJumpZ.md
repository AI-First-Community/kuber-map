---
type: FIBO Class
title: "agency regular jump z"
description: "Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyRegularJumpZ
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/AgencyJumpZTranche.md", provenance: fibo}
  - {type: reverts-on, target: "/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEventReversal.md", provenance: fibo}
---

Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.

### Relationships
- is-a: [AgencyJumpZTranche](/SEC/Debt/CollateralizedDebtObligations/AgencyJumpZTranche.md)
- reverts-on: [JumpZTriggerEventReversal](/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEventReversal.md)
