---
type: FIBO Class
title: "authorization"
description: "situation in which a party authorizes someone to act on their behalf or to have specific capabilities under certain conditions for some period of time"
resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/Authorization
tags: [CMNS]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: has-authorized-party, target: "/CMNS/BusinessAuthorizations/AuthorizedParty.md", provenance: fibo}
  - {type: has-authorizing-party, target: "/CMNS/BusinessAuthorizations/AuthorizingParty.md", provenance: fibo}
---

situation in which a party authorizes someone to act on their behalf or to have specific capabilities under certain conditions for some period of time

### Relationships
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- has-authorized-party: [AuthorizedParty](/CMNS/BusinessAuthorizations/AuthorizedParty.md)
- has-authorizing-party: [AuthorizingParty](/CMNS/BusinessAuthorizations/AuthorizingParty.md)
