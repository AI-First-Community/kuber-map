#!/usr/bin/env python3
"""
Nominate a curated `core:` concept set for a use case, GROUNDED in the extracted data.

Every id in the seed spec is resolved against out/intermediate.json. If any id does not
resolve to a real FIBO class (wrong name, wrong cluster, not-yet-loaded domain), the tool
reports it as UNRESOLVED and exits non-zero — this is the anti-hallucination gate for curation:
you cannot nominate a concept that does not exist in FIBO.

Emits: curation/<use-case>.json (verified core list with real IRIs) + a nomination table.

Usage:
    python etl/nominate_core.py --in out/intermediate.json --out curation/loan-origination.json
"""
import argparse
import json
import os
from collections import Counter

# ---- Use-case seed spec: Residential Mortgage Origination & Underwriting --------------------
# Each entry is (local-id, expected-cluster). Ids are grounded in the extracted LOAN/FND/FBC/BE
# data (see `make extract`); the resolver verifies each one exists.
USE_CASE = "Loan Origination & Underwriting (residential mortgage)"
FACETS = {
    "Instrument": [
        ("Loan", "LOAN"), ("SecuredLoan", "LOAN"), ("CollateralizedLoan", "LOAN"),
        ("LoanSecuredByRealEstate", "LOAN"), ("Mortgage", "LOAN"),
        ("ClosedEndMortgageLoan", "LOAN"), ("OpenEndMortgageLoan", "LOAN"),
        ("ReverseMortgageLoan", "LOAN"), ("HomeEquityLineOfCredit", "LOAN"),
        ("LoanProduct", "LOAN"), ("MortgageProduct", "LOAN"), ("LoanProductOffering", "LOAN"),
    ],
    "Application & process": [
        ("LoanApplication", "LOAN"), ("LoanApplicationStatus", "LOAN"),
        ("LoanApplicationPhase", "LOAN"), ("PreApprovalRequest", "LOAN"),
        ("PreApprovalContract", "LOAN"), ("LoanPhase", "LOAN"), ("RepaymentPhase", "LOAN"),
    ],
    "Underwriting & assessment": [
        ("UnderwritingDecision", "LOAN"), ("AutomatedUnderwritingSystem", "LOAN"),
        ("CreditRiskAssessment", "LOAN"), ("BorrowerAssessment", "LOAN"),
        ("CollateralValuation", "LOAN"), ("IncomeVerificationReport", "LOAN"),
        ("IndividualPersonCreditRating", "LOAN"), ("PaymentHistory", "LOAN"),
    ],
    "Amounts, ratios & terms": [
        ("LoanToValueRatio", "LOAN"), ("CombinedLoanToValueRatio", "LOAN"),
        ("TotalDebtExpenseRatio", "LOAN"), ("TotalOutstandingPrincipal", "LOAN"),
        ("BorrowerMonthlyIncome", "LOAN"), ("AmortizationType", "LOAN"),
        ("LoanPaymentSchedule", "LOAN"), ("PrepaymentTerms", "LOAN"), ("GoodFaithEstimate", "LOAN"),
        ("MonetaryAmount", "FND"), ("Income", "FND"),
    ],
    "Parties & roles": [
        ("Borrower", "FBC"), ("Lender", "FBC"), ("Creditor", "FBC"),
        ("FinancialInstitution", "FBC"), ("Guarantor", "FBC"), ("Servicer", "LOAN"),
        ("MortgageIndemnityGuarantor", "LOAN"), ("Comaker", "LOAN"),
    ],
    "Collateral & property": [
        ("Collateral", "FBC"), ("RealProperty", "FND"), ("Appraisal", "FND"),
        ("AppraisedValue", "FND"), ("LenderLienPosition", "LOAN"),
        ("OwnershipInterest", "LOAN"), ("PropertyUsage", "LOAN"),
    ],
    "Contract & obligations": [
        ("CreditAgreement", "FBC"), ("Principal", "FBC"), ("LoanOrCreditAccount", "FBC"),
        ("LegalObligation", "FND"), ("DisclosureProvision", "FND"),
        ("UseOfProceedsProvision", "FND"), ("Payment", "FND"),
    ],
    "Purpose": [
        ("LoanPurpose", "LOAN"), ("MortgageLoanPurpose", "LOAN"),
    ],
    "Regulatory & disclosure (US)": [
        ("HMDA-CoveredLoanContract", "LOAN"), ("HMDA-Report", "LOAN"), ("RegB", "LOAN"),
        ("RegZ", "LOAN"), ("ConsumerCreditProtectionLaw", "LOAN"),
        ("LoanRegulatoryRequirement", "LOAN"), ("BorrowerDisclosureRequirement", "LOAN"),
        ("UniversalLoanIdentifier", "LOAN"), ("NMLSR-ID", "LOAN"),
    ],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", default="out/intermediate.json")
    ap.add_argument("--out", default="curation/loan-origination.json")
    args = ap.parse_args()

    recs = json.load(open(args.inp))
    idx = {}
    for r in recs:
        idx.setdefault((r["id"], r["cluster"]), []).append(r)

    resolved, unresolved, dupes = [], [], []
    for facet, entries in FACETS.items():
        for cid, cl in entries:
            hits = idx.get((cid, cl), [])
            if not hits:
                unresolved.append((facet, cid, cl))
            else:
                if len(hits) > 1:
                    dupes.append((cid, cl, len(hits)))
                r = hits[0]
                resolved.append({"facet": facet, "iri": r["iri"], "id": r["id"],
                                 "cluster": r["cluster"], "title": r["title"],
                                 "description": r["description"], "core": True})

    # ---- report ----
    print(f"\n=== CORE NOMINATION — {USE_CASE} ===")
    by_facet = {}
    for r in resolved:
        by_facet.setdefault(r["facet"], []).append(r)
    for facet in FACETS:
        rows = by_facet.get(facet, [])
        print(f"\n## {facet}  ({len(rows)})")
        for r in rows:
            d = (r["description"] or "").split(".")[0][:72]
            print(f'   [{r["cluster"]:4}] {r["title"]:<34} — {d}')
    print(f"\nTOTAL resolved core concepts: {len(resolved)}")
    print("Clusters: " + ", ".join(f"{k}={v}" for k, v in
                                    Counter(r['cluster'] for r in resolved).most_common()))
    if dupes:
        print(f"\n⚠ ambiguous ids (multiple modules): {dupes}")
    if unresolved:
        print("\n❌ UNRESOLVED (not found in extracted data — fix the spec):")
        for facet, cid, cl in unresolved:
            print(f"   {facet}: {cid} [{cl}]")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump({"use_case": USE_CASE, "core": resolved}, open(args.out, "w"), indent=2)
    print(f"\nWrote {args.out} ({len(resolved)} concepts)")
    return 1 if unresolved else 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
