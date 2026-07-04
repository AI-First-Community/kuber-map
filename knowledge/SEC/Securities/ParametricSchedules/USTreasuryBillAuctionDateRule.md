---
type: FIBO Class
title: "US Treasury bill auction date rule"
description: "rule for setting auction dates for US Treasury bills"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/USTreasuryBillAuctionDateRule
tags: [SEC, Release]
detail: "To finance the public debt, the U.S. Treasury sells bills, notes, bonds, Floating Rate Notes (FRNs), and Treasury Inflation-Protected Securities (TIPS) to institutional and individual investors through public auctions. Treasury auctions occur regularly and have a set schedule. Rules and other information are available via announcements of pending auctions."
relations:
  - {type: is-a, target: "/SEC/Securities/ParametricSchedules/AuctionDateRule.md", provenance: fibo}
  - {type: has-business-day-convention, target: "/FND/DatesAndTimes/BusinessDates/BusinessDayFollowing.md", provenance: fibo}
---

rule for setting auction dates for US Treasury bills

### Relationships
- is-a: [AuctionDateRule](/SEC/Securities/ParametricSchedules/AuctionDateRule.md)
- has-business-day-convention: [BusinessDayFollowing](/FND/DatesAndTimes/BusinessDates/BusinessDayFollowing.md)
