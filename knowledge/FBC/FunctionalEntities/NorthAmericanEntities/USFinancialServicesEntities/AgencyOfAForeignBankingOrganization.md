---
type: FIBO Class
title: "agency of a foreign banking organization"
description: "place of business of a foreign bank, located in any state, at which credit balances are maintained, checks are paid, money is lent, or, to the extent not prohibited by state or federal law, deposits are accepted from a person or entity that is not a citizen or resident of the United States"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/AgencyOfAForeignBankingOrganization
tags: [FBC, Release]
detail: "Obligations shall not be considered credit balances unless they are:  (1) Incidental to, or arise out of the exercise of, other lawful banking powers;  (2) To serve a specific purpose;  (3) Not solicited from the general public;  (4) Not used to pay routine operating expenses in the United States such as salaries, rent, or taxes;  (5) Withdrawn within a reasonable period of time after the specific purpose for which they were placed has been accomplished; and  (6) Drawn upon in a manner reasonable in relation to the size and nature of the account."
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
  - {type: is-controlled-party-of, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank.md", provenance: fibo}
  - {type: is-owned-asset, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank.md", provenance: fibo}
  - {type: is-played-by, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/OfficeOfAForeignBank.md", provenance: fibo}
---

place of business of a foreign bank, located in any state, at which credit balances are maintained, checks are paid, money is lent, or, to the extent not prohibited by state or federal law, deposits are accepted from a person or entity that is not a citizen or resident of the United States

### Relationships
- is-a: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
- is-controlled-party-of: [ForeignBank](/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank.md)
- is-owned-asset: [ForeignBank](/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank.md)
- is-played-by: [OfficeOfAForeignBank](/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/OfficeOfAForeignBank.md)
