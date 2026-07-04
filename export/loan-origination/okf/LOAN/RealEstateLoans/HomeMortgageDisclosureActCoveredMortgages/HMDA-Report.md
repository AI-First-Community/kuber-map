---
type: FIBO Class
title: "HMDA report"
description: "a report prepared to satisfy HMDA regulatory reporting requirements as described US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report
tags: [LOAN, Provisional]
core: true
detail: "The Loan/Application Register (LAR) a covered institution files annually with the CFPB; regulators use it to detect discriminatory or risky lending patterns."
detail_provenance: curated
examples:
  - "A bank's annual Loan/Application Register (LAR) filed with the CFPB."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Reporting/Report.md", provenance: fibo}
  - {type: is-submitted-to, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
---

a report prepared to satisfy HMDA regulatory reporting requirements as described US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015

### Relationships
- is-a: [Report](/FND/Arrangements/Reporting/Report.md)
- is-submitted-to: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
