---
type: FIBO Class
title: "mortgage indemnity guarantee"
description: "insurance-backed guarantee that protects lenders if the mortgage repayments cease for some reason, perhaps due to death or a homeowner being made redundant at work"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantee
tags: [LOAN, Provisional]
relations:
  - {type: is-exemplified-by, target: "/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityInsurancePolicy.md", provenance: fibo}
  - {type: is-guaranteed-by, target: "/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/Guaranty/InsuranceBackedGuaranty.md", provenance: fibo}
---

insurance-backed guarantee that protects lenders if the mortgage repayments cease for some reason, perhaps due to death or a homeowner being made redundant at work

### Relationships
- is-exemplified-by: [MortgageIndemnityInsurancePolicy](/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityInsurancePolicy.md)
- is-guaranteed-by: [MortgageIndemnityGuarantor](/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor.md)
- is-a: [InsuranceBackedGuaranty](/FBC/DebtAndEquities/Guaranty/InsuranceBackedGuaranty.md)
