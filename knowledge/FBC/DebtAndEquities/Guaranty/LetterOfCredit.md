---
type: FIBO Class
title: "letter of credit"
description: "letter from a bank or other creditworthy institution guaranteeing that a buyer's payment to a seller will be received on time and for the correct amount"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/LetterOfCredit
tags: [FBC, Release]
detail: "In some states in the U.S., the issuer is not limited to financial institutions -- it is simply a written instrument, addressed by one person to another, requesting the latter to give credit to the person in whose favor it is drawn. In the event that the buyer is unable to make payment, the bank or other issuer is required to cover the full or remaining amount."
synonyms:
  - "L/C"
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md", provenance: fibo}
  - {type: is-issued-by, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: plays-role, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
---

letter from a bank or other creditworthy institution guaranteeing that a buyer's payment to a seller will be received on time and for the correct amount

### Relationships
- is-a: [CommittedCreditFacility](/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md)
- is-issued-by: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- plays-role: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
