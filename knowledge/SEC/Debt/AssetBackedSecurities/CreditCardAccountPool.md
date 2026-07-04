---
type: FIBO Class
title: "credit card account pool"
description: "pool of credit card receivables associated with designated accounts"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/CreditCardAccountPool
tags: [SEC, Release]
detail: "In a credit card securitization transaction only the receivables are sold, not the accounts that generate the receivables. The financial institution retains legal ownership of the credit card accounts and can continue to change the terms on the accounts. Accounts corresponding to securitized loans are typically referred to as the designated accounts (or sometimes trust accounts). The initial outstanding balances on the designated accounts are sold to the trust as are the rights to any new charges on the designated accounts. Subsequently, as cardholder purchase activity generates more receivables on the designated accounts, these new receivables are purchased by the trust from the originating institution/seller/transferor. The trust uses the monthly principal payments received from the cardholders to acquire these new charges or receivables. When the securitization is initially set up, the originating institution/seller adds sufficient receivables to support the principal balance of the certificates plus an additional amount (seller's interest) that serves to absorb fluctuations in the outstanding balance of the receivables. The originating institution/seller will make subsequent additions to the trust in order to keep the seller's interest at the required level."
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
  - {type: has-part, target: "/LOAN/LoansSpecific/CardAccounts/CreditCardAccount.md", provenance: fibo}
---

pool of credit card receivables associated with designated accounts

### Relationships
- is-a: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
- has-part: [CreditCardAccount](/LOAN/LoansSpecific/CardAccounts/CreditCardAccount.md)
