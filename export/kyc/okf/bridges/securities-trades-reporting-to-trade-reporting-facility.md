---
type: Cross-Domain Relation
title: "securities trades reporting -> trade reporting facility"
description: "Executed off-exchange securities trades are reported to a trade reporting facility."
tags: [bridge, BP, FBC]
relations:
  - {type: submitted-to, target: "/FBC/FunctionalEntities/Markets/TradeReportingFacility.md", provenance: curated}
source_class: "/BP/Process/FinancialContextAndProcess/SecuritiesTradesReporting.md"
kind: "cross-domain (BP->FBC)"
citation: "FINRA Trade Reporting Facility rules; MiFID II APA reporting"
rationale: "Executed off-exchange securities trades are reported to a trade reporting facility. FIBO models the securities-trades-reporting process (BP) and the TradeReportingFacility (FBC) but does not connect the reporting activity to the facility it reports to."
---

**securities trades reporting** --[submitted-to]--> **trade reporting facility**  _(curated bridge — cross-domain (BP->FBC))_

Executed off-exchange securities trades are reported to a trade reporting facility. FIBO models the securities-trades-reporting process (BP) and the TradeReportingFacility (FBC) but does not connect the reporting activity to the facility it reports to.

*Citation:* FINRA Trade Reporting Facility rules; MiFID II APA reporting
