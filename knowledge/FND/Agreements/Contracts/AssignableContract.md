---
type: FIBO Class
title: "assignable contract"
description: "contract in which contract holder (assignor) may transfer some or all of their rights and obligations to another party (assignee)"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/AssignableContract
tags: [FND, Release]
detail: "Note that while the assignor may divest themselves of some rights, that assignment does not necessarily eliminate performance obligations of the assignor to the third party. Characteristics that are important to understand with respect to an assignment include the circumstances in which the assignor remains obligated and any remedies available if the assignor does not perform."
examples:
  - "Many, though not all, futures contracts are assignable. This means that the original contract holder can sell the contract to another party in return for cash, and that party then assumes the rights, responsibilities, and benefits of that contract from that point onwards."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/TransferableContract.md", provenance: fibo}
---

contract in which contract holder (assignor) may transfer some or all of their rights and obligations to another party (assignee)

### Relationships
- is-a: [TransferableContract](/FND/Agreements/Contracts/TransferableContract.md)
