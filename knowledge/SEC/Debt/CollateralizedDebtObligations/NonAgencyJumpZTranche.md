---
type: FIBO Class
title: "non agency jump z tranche"
description: "A Jump Z tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpZTranche
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/NonAgencyZTranche.md", provenance: fibo}
---

A Jump Z tranche is like a Z tranche but if there is some sort of trigger event reached then the holders of the Jump Z tranche will begin to receive payments. Regular non-Sticky Jump Z tranches maintain their changed status only while the trigger event is in effect, and revert to their old payment status once the trigger event has passed.

### Relationships
- is-a: [NonAgencyJumpTranche](/SEC/Debt/CollateralizedDebtObligations/NonAgencyJumpTranche.md)
- is-a: [NonAgencyZTranche](/SEC/Debt/CollateralizedDebtObligations/NonAgencyZTranche.md)
