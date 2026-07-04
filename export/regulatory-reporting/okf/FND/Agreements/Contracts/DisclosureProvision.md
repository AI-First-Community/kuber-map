---
type: FIBO Class
title: "disclosure provision"
description: "contractual provision that outlines the requirements and responsibilities of one or both parties to reveal certain information to each other"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision
tags: [FND, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "Disclosure provisions are crucial in ensuring transparency, mitigating risks, and maintaining trust between the parties. Typical elements of a disclosure provision include (1) scope - defining the kind of information that must be disclosed, (2) materiality - which usually states that only information material to the agreement must be disclosed, (3) timing - specifying when such disclosures must be made, (4) ongoing requirements - outlining whether or not disclosures any time significant changes or new information must be made available over some period of time, (5) method - specifying how such disclosures must be made, for example, in writing, (6) exclusions - information that is explicitly out of scope with respect to disclosure requirements, (7) confidentiality - restrictions related to whether or not the information is confidential and on how it may be used, and (8) penalities - specifying consequences for failing to disclose relevant information. With respect to contracts, failure to disclose key details can lead to breaches of contract or claims of misrepresentation. Disclosure requirements are typically specific to the nature of the contract and jurisdiction."
examples:
  - "A loan-agreement clause requiring the APR to be disclosed to the borrower."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractualCommitment.md", provenance: fibo}
---

contractual provision that outlines the requirements and responsibilities of one or both parties to reveal certain information to each other

### Relationships
- is-a: [ContractualCommitment](/FND/Agreements/Contracts/ContractualCommitment.md)
