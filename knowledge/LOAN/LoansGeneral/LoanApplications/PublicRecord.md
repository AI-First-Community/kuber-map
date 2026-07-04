---
type: FIBO Class
title: "public record"
description: "record about an action involving a party that is publicly available from a court or other government agency"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PublicRecord
tags: [LOAN, Provisional]
detail: "This can include court actions such as bankruptcy and foreclosure, as well as liens and other events that have been recorded."
relations:
  - {type: is-a, target: "/CMNS/Documents/Record.md", provenance: fibo}
  - {type: is-classified-by, target: "/LOAN/LoansGeneral/LoanApplications/PublicRecordCategory.md", provenance: fibo}
  - {type: is-evidenced-by, target: "/CMNS/Documents/LegalDocument.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
---

record about an action involving a party that is publicly available from a court or other government agency

### Relationships
- is-a: [Record](/CMNS/Documents/Record.md)
- is-classified-by: [PublicRecordCategory](/LOAN/LoansGeneral/LoanApplications/PublicRecordCategory.md)
- is-evidenced-by: [LegalDocument](/CMNS/Documents/LegalDocument.md)
- refers-to: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
