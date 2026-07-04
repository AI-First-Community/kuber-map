---
type: FIBO Class
title: "automated underwriting system"
description: "software system that collects the information necessary to approve a loan application and supports a mortgage lender's analysis of a new loan application"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/AutomatedUnderwritingSystem
tags: [LOAN, Provisional]
core: true
detail: "In the United States, automated underwriting systems review the applicant's credit history and ability to repay the loan, and determine whether the price the applicant is offering to pay is supported by the property value."
examples:
  - "Fannie Mae Desktop Underwriter (DU)"
  - "Freddie Mac Loan Product Advisor (LPA)"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/AgentsAndPeople/Agents/AutomatedSystem.md", provenance: fibo}
---

software system that collects the information necessary to approve a loan application and supports a mortgage lender's analysis of a new loan application

### Relationships
- is-a: [AutomatedSystem](/FND/AgentsAndPeople/Agents/AutomatedSystem.md)
