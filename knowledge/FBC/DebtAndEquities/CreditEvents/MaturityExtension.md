---
type: FIBO Class
title: "maturity extension"
description: "credit event involving extension of payments beyond the original maturity date of the obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/MaturityExtension
tags: [FBC, Release]
detail: "As stipulated in the terms and conditions for a bond, for example, the issuer or the bondholder may prolong the maturity date. After extension, the security may differ from original issue (new rate or maturity date). May be subject to bondholder's approval."
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/CorporateAction.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md", provenance: fibo}
---

credit event involving extension of payments beyond the original maturity date of the obligation

### Relationships
- is-a: [CorporateAction](/CAE/CorporateEvents/CorporateActions/CorporateAction.md)
- is-a: [ObligationSpecificCreditEvent](/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md)
