---
type: FIBO Class
title: "securities underwriting issuance process"
description: "The process by which debt instruments are offered to the market by a syndicate of underwriters who underwrite the issue."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md", provenance: fibo}
  - {type: has-agent, target: "/BP/SecuritiesIssuance/MuniIssuance/IssuanceAgent.md", provenance: fibo}
  - {type: has-financial-advisor, target: "/BP/SecuritiesIssuance/MuniIssuance/IssuanceFinancialAdvisor.md", provenance: fibo}
  - {type: has-issuer-counsel, target: "/BP/SecuritiesIssuance/MuniIssuance/IssuerCounsel.md", provenance: fibo}
  - {type: has-obligor, target: "/BP/SecuritiesIssuance/MuniIssuance/Obligor.md", provenance: fibo}
  - {type: has-paying-agent, target: "/BP/SecuritiesIssuance/MuniIssuance/PayingAgent.md", provenance: fibo}
  - {type: has-printer, target: "/BP/SecuritiesIssuance/MuniIssuance/IssuancePrinter.md", provenance: fibo}
  - {type: has-remarketing-agent, target: "/BP/SecuritiesIssuance/MuniIssuance/RemarketingAgent.md", provenance: fibo}
  - {type: has-servicer, target: "/BP/SecuritiesIssuance/MuniIssuance/Servicer.md", provenance: fibo}
  - {type: has-subscriber, target: "/BP/SecuritiesIssuance/IssuanceProcess/Subscriber.md", provenance: fibo}
  - {type: has-transfer-agent, target: "/BP/SecuritiesIssuance/MuniIssuance/TransferAgent.md", provenance: fibo}
  - {type: has-trustee, target: "/BP/SecuritiesIssuance/MuniIssuance/Trustee.md", provenance: fibo}
  - {type: produces, target: "/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails.md", provenance: fibo}
  - {type: requested-by, target: "/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceRequestor.md", provenance: fibo}
  - {type: underwritten-by, target: "/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter.md", provenance: fibo}
---

The process by which debt instruments are offered to the market by a syndicate of underwriters who underwrite the issue.

### Relationships
- is-a: [SecuritiesIssuanceProcess](/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md)
- has-agent: [IssuanceAgent](/BP/SecuritiesIssuance/MuniIssuance/IssuanceAgent.md)
- has-financial-advisor: [IssuanceFinancialAdvisor](/BP/SecuritiesIssuance/MuniIssuance/IssuanceFinancialAdvisor.md)
- has-issuer-counsel: [IssuerCounsel](/BP/SecuritiesIssuance/MuniIssuance/IssuerCounsel.md)
- has-obligor: [Obligor](/BP/SecuritiesIssuance/MuniIssuance/Obligor.md)
- has-paying-agent: [PayingAgent](/BP/SecuritiesIssuance/MuniIssuance/PayingAgent.md)
- has-printer: [IssuancePrinter](/BP/SecuritiesIssuance/MuniIssuance/IssuancePrinter.md)
- has-remarketing-agent: [RemarketingAgent](/BP/SecuritiesIssuance/MuniIssuance/RemarketingAgent.md)
- has-servicer: [Servicer](/BP/SecuritiesIssuance/MuniIssuance/Servicer.md)
- has-subscriber: [Subscriber](/BP/SecuritiesIssuance/IssuanceProcess/Subscriber.md)
- has-transfer-agent: [TransferAgent](/BP/SecuritiesIssuance/MuniIssuance/TransferAgent.md)
- has-trustee: [Trustee](/BP/SecuritiesIssuance/MuniIssuance/Trustee.md)
- produces: [UnderwritingProcessDetails](/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails.md)
- requested-by: [UnderwritingIssuanceRequestor](/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceRequestor.md)
- underwritten-by: [PotentialMuniUnderwriter](/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter.md)
