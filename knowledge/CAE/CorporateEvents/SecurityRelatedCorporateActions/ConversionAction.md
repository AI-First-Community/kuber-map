---
type: FIBO Class
title: "conversion action"
description: "corporate action involving conversion of securities (generally convertible bonds or preferred shares) into another form of securities (usually common shares) at a pre-stated price/ratio"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/ConversionAction
tags: [CAE, Provisional]
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md", provenance: fibo}
  - {type: converts-from, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: converts-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

corporate action involving conversion of securities (generally convertible bonds or preferred shares) into another form of securities (usually common shares) at a pre-stated price/ratio

### Relationships
- is-a: [VoluntaryCorporateAction](/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)
- converts-from: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- converts-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
