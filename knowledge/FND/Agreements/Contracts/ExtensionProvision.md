---
type: FIBO Class
title: "extension provision"
description: "contract terms that specify the conditions under which a contract can be extended"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ExtensionProvision
tags: [FND, Release]
detail: "In the case of a debt instrument, an extension may include extending the time allowed for repayment of the principal, the maturity date, and so forth."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractualCommitment.md", provenance: fibo}
  - {type: has-extendable-period, target: "/CMNS/DatesAndTimes/ExplicitDatePeriod.md", provenance: fibo}
---

contract terms that specify the conditions under which a contract can be extended

### Relationships
- is-a: [ContractualCommitment](/FND/Agreements/Contracts/ContractualCommitment.md)
- has-extendable-period: [ExplicitDatePeriod](/CMNS/DatesAndTimes/ExplicitDatePeriod.md)
