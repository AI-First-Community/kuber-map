---
type: FIBO Class
title: "bond default event"
description: "corporate action which indicates a failure by the issuer to perform obligations defined as default events under the bond agreement and that have not been remedied"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/BondDefaultAction
tags: [CAE, Provisional]
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/CreditEvents/ObligationDefault.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
---

corporate action which indicates a failure by the issuer to perform obligations defined as default events under the bond agreement and that have not been remedied

### Relationships
- is-a: [MandatoryCorporateAction](/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)
- is-a: [ObligationDefault](/FBC/DebtAndEquities/CreditEvents/ObligationDefault.md)
- applies-to: [Bond](/SEC/Debt/Bonds/Bond.md)
