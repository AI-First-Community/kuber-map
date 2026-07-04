---
type: FIBO Class
title: "loan participation note"
description: "credit facility and fixed-income security that may be distributed across a group of lenders"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/LoanParticipationNote
tags: [SEC, Release]
detail: "The main difference between a loan participation and a loan syndication is that in a loan participation, one lender sells ownership interests in a loan to other lenders, while in a loan syndication, the lenders work together to originate and lend on the loan. With an LPN, a lead bank underwrites and issues the loan. This lending institution then recruits other banks to participate and share the risks and profits on a pro rata basis. The lead lender keeps a partial interest in the loan and is responsible for servicing it."
synonyms:
  - "LPN"
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditFacility.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md", provenance: fibo}
  - {type: has-actor, target: "/SEC/Debt/DistributedLoans/LeadArranger.md", provenance: fibo}
---

credit facility and fixed-income security that may be distributed across a group of lenders

### Relationships
- is-a: [CreditFacility](/FBC/DebtAndEquities/Debt/CreditFacility.md)
- is-a: [CommercialLoan](/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md)
- is-a: [FixedIncomeSecurity](/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)
- has-actor: [LeadArranger](/SEC/Debt/DistributedLoans/LeadArranger.md)
