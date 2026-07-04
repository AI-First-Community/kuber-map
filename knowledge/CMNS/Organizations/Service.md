---
type: FIBO Class
title: "service"
description: "intangible activity performed by some party for the benefit of another party"
resource: https://www.omg.org/spec/Commons/Organizations/Service
tags: [CMNS]
detail: "Sometimes services are difficult to identify because they are closely associated with a good; such as the combination of a diagnosis with the administration of a medicine. No transfer of possession or ownership takes place when services are sold, and they (1) cannot be stored or transported, (2) are instantly perishable, and (3) come into existence at the time they are bought and consumed. The OECD defines services as outputs produced to order and which cannot be traded separately from their production; ownership rights cannot be established over services and by the time their production is completed they must have been provided to the consumers. As an exception to this rule there is a group of industries, generally classified as service industries, some of whose outputs have characteristics of goods, i.e. those concerned with the provision, storage, communication and dissemination of information, advice and entertainment in the broadest sense of those terms; the products of these industries, where ownership rights can be established, may be classified either as goods or services depending on the medium by which these outputs are supplied."
examples:
  - "Services include intangible products, such as accounting, banking, cleaning, consultancy, education, insurance, expertise, medical treatment, or transportation services."
relations:
  - {type: is-provided-by, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
  - {type: is-provisioned-by, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
  - {type: provides, target: "/CMNS/Organizations/Capability.md", provenance: fibo}
---

intangible activity performed by some party for the benefit of another party

### Relationships
- is-provided-by: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
- is-provisioned-by: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
- provides: [Capability](/CMNS/Organizations/Capability.md)
