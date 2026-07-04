---
type: FIBO Class
title: "issued security issue information"
description: "FIBIM: 'Elements relating to issue preparation/bringing to market (also known as primary market or Initial Public Offering (IPO) issuance) through to issue date.'"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/CMNS/Documents/Document.md", provenance: fibo}
  - {type: has-partially-paid-issuance-schedule, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
  - {type: is-about, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

FIBIM: "Elements relating to issue preparation/bringing to market (also known as primary market or Initial Public Offering (IPO) issuance) through to issue date."

### Relationships
- is-a: [Document](/CMNS/Documents/Document.md)
- has-partially-paid-issuance-schedule: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
- is-about: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
