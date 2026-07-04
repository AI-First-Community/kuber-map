---
type: FIBO Class
title: "early termination provision"
description: "termination of an agreement for any reason prior to its expiration date"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/EarlyTerminationProvision
tags: [FND, Release]
detail: "Early termination date refers to the date set within an agreement for the parties to exercise the option to terminate the contract prior to its original expiration, typically subject to predefined terms such as notice periods or specific conditions. Early termination may be automatically triggered by an event of default with respect to any contract obligation, due to corporate action, or for other reasons. An early termination date may be calculated per the terms of the agreement or specified explicitly at the time the termination event occurs."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/TerminationProvision.md", provenance: fibo}
  - {type: has-expiration-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
---

termination of an agreement for any reason prior to its expiration date

### Relationships
- is-a: [TerminationProvision](/FND/Agreements/Contracts/TerminationProvision.md)
- has-expiration-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
