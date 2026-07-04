---
type: FIBO Class
title: "receiver"
description: "party appointed by some court for the purposes of winding up the affairs of some entity which is no longer solvent"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/Receiver
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md", provenance: fibo}
  - {type: is-controlling-party-in, target: "/BE/OwnershipAndControl/ControlParties/CourtAppointedControl.md", provenance: fibo}
---

party appointed by some court for the purposes of winding up the affairs of some entity which is no longer solvent

### Relationships
- is-a: [DeJureControllingInterestParty](/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)
- is-controlling-party-in: [CourtAppointedControl](/BE/OwnershipAndControl/ControlParties/CourtAppointedControl.md)
