---
type: FIBO Class
title: "underwriter takedown"
description: "Infomation on Takedown quantity of the security handled by the underwriter (that will be brought into DTC)."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/UnderwriterTakedown
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails.md", provenance: fibo}
  - {type: taken-down-by, target: "/BP/SecuritiesIssuance/DebtIssuance/MuniIssueUnderwriter.md", provenance: fibo}
---

Infomation on Takedown quantity of the security handled by the underwriter (that will be brought into DTC).

### Relationships
- is-a: [UnderwritingProcessDetails](/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails.md)
- taken-down-by: [MuniIssueUnderwriter](/BP/SecuritiesIssuance/DebtIssuance/MuniIssueUnderwriter.md)
