---
type: FIBO Class
title: "insurance policy"
description: "contract that (1) puts an indemnity cover into effect, (2) serves as a legal evidence of the insurance agreement, (3) sets out the exact terms on which the indemnity cover has been provided, and (4) states associated information such as the (a) specific risks and perils covered, (b) duration of coverage, (c) amount of premium, (d) mode of premium payment, and (e) deductibles, if any"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/InsurancePolicy
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-counterparty, target: "/FBC/DebtAndEquities/Guaranty/Policyholder.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/DebtAndEquities/Guaranty/Insurer.md", provenance: fibo}
---

contract that (1) puts an indemnity cover into effect, (2) serves as a legal evidence of the insurance agreement, (3) sets out the exact terms on which the indemnity cover has been provided, and (4) states associated information such as the (a) specific risks and perils covered, (b) duration of coverage, (c) amount of premium, (d) mode of premium payment, and (e) deductibles, if any

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-counterparty: [Policyholder](/FBC/DebtAndEquities/Guaranty/Policyholder.md)
- is-issued-by: [Insurer](/FBC/DebtAndEquities/Guaranty/Insurer.md)
