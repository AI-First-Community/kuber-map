---
type: FIBO Class
title: "agency jump z tranche"
description: "A Jump Z tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyJumpZTranche
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/AgencyJumpTranche.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/AgencyZTranche.md", provenance: fibo}
---

A Jump Z tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.

### Relationships
- is-a: [AgencyJumpTranche](/SEC/Debt/CollateralizedDebtObligations/AgencyJumpTranche.md)
- is-a: [AgencyZTranche](/SEC/Debt/CollateralizedDebtObligations/AgencyZTranche.md)
