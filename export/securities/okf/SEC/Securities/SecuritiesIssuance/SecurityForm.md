---
type: FIBO Class
title: "security form"
description: "nature of the proof of ownership of a security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityForm
tags: [SEC, Release]
detail: "Securities are typically issued in one of two forms, registered or bearer. Most securities issued today are in registered form, which enables the issuing firm or registrar to keep records of a security's owner and mail them any dividend, coupon, or other payments. Registered securities may be issued in book entry (digital only) or certificate (physical) form, but most today are entirely digital."
examples:
  - "Registered form (the issuer records the holder) versus bearer form (whoever holds the certificate owns it)."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractDocument.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: exemplifies, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
---

nature of the proof of ownership of a security

### Relationships
- is-a: [ContractDocument](/FND/Agreements/Contracts/ContractDocument.md)
- applies-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- exemplifies: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
