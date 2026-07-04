---
type: FIBO Class
title: "issued and securitized agency mortage pool"
description: "An agency mortgage pool which has been securitized as part of an agency Mortgage Backed Security."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/IssuedAndSecuritizedAgencyMortagePool
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool.md", provenance: fibo}
  - {type: has-stage, target: "/BP/SecuritiesIssuance/DebtIssuance/Issued.md", provenance: fibo}
---

An agency mortgage pool which has been securitized as part of an agency Mortgage Backed Security.

### Relationships
- is-a: [AgencyMortgagePool](/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool.md)
- has-stage: [Issued](/BP/SecuritiesIssuance/DebtIssuance/Issued.md)
