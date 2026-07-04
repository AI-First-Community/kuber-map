---
type: FIBO Class
title: "securities issuance process"
description: "The process by which a financial security is issued."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess
tags: [BP, Provisional]
relations:
  - {type: has-issuance-guarantor, target: "/BP/SecuritiesIssuance/IssuanceProcess/SecurityIssuanceGuarantor.md", provenance: fibo}
  - {type: has-potential-issuer, target: "/BP/SecuritiesIssuance/IssuanceProcess/PotentialIssuer.md", provenance: fibo}
  - {type: produces, target: "/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md", provenance: fibo}
  - {type: subscriber, target: "/BP/SecuritiesIssuance/IssuanceProcess/Subscriber.md", provenance: fibo}
---

The process by which a financial security is issued.

### Relationships
- has-issuance-guarantor: [SecurityIssuanceGuarantor](/BP/SecuritiesIssuance/IssuanceProcess/SecurityIssuanceGuarantor.md)
- has-potential-issuer: [PotentialIssuer](/BP/SecuritiesIssuance/IssuanceProcess/PotentialIssuer.md)
- produces: [TradedInstrumentIssuanceProcessInformation](/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md)
- subscriber: [Subscriber](/BP/SecuritiesIssuance/IssuanceProcess/Subscriber.md)
