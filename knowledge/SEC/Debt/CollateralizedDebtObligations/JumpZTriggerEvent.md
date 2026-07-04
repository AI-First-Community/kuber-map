---
type: FIBO Class
title: "jump z trigger event"
description: "The event which triggers the Jump Z"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/JumpZTriggerEvent
tags: [SEC, Provisional]
detail: "If this trigger event is reached then the holders of the Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed. The event may be a market event or an event relating to the deal."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/TriggerEvent.md", provenance: fibo}
---

The event which triggers the Jump Z

### Relationships
- is-a: [TriggerEvent](/SEC/Debt/CollateralizedDebtObligations/TriggerEvent.md)
