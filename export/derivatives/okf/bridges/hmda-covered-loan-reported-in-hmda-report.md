---
type: Cross-Domain Relation
title: "HMDA covered loan contract -> HMDA report"
description: "HMDA requires every covered loan/application to be recorded on the institution's Loan/Application Register that constitutes the HMDA report."
tags: [bridge, LOAN, LOAN]
relations:
  - {type: reported-in, target: "/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report.md", provenance: curated}
source_class: "/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-CoveredLoanContract.md"
kind: "intra-domain gap"
citation: "12 CFR 1003.4 (Regulation C — compilation of reportable data)"
rationale: "HMDA requires every covered loan/application to be recorded on the institution's Loan/Application Register that constitutes the HMDA report. FIBO models both HMDA-CoveredLoanContract and HMDA-Report but does not connect the reported loan to the report that reports it."
---

**HMDA covered loan contract** --[reported-in]--> **HMDA report**  _(curated bridge — intra-domain gap)_

HMDA requires every covered loan/application to be recorded on the institution's Loan/Application Register that constitutes the HMDA report. FIBO models both HMDA-CoveredLoanContract and HMDA-Report but does not connect the reported loan to the report that reports it.

*Citation:* 12 CFR 1003.4 (Regulation C — compilation of reportable data)
