---
type: FIBO Class
title: "general partnership"
description: "partnership that has at least two general partners that agree to share in all assets, profits, and financial and legal liabilities of the business"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartnership
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "General partnerships are the most basic and common form of partnership world-wide."
examples:
  - "A partnership in which all partners share unlimited liability for the firm's debts."
examples_provenance: curated
synonyms:
  - "GP"
relations:
  - {type: is-a, target: "/BE/Partnerships/Partnerships/Partnership.md", provenance: fibo}
  - {type: has-general-partner, target: "/BE/Partnerships/Partnerships/GeneralPartner.md", provenance: fibo}
---

partnership that has at least two general partners that agree to share in all assets, profits, and financial and legal liabilities of the business

### Relationships
- is-a: [Partnership](/BE/Partnerships/Partnerships/Partnership.md)
- has-general-partner: [GeneralPartner](/BE/Partnerships/Partnerships/GeneralPartner.md)
