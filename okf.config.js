/* ============================================================================
   Bodhi Map for FIBO — Controlled vocabulary + presentation flows (Node + browser).
   Single source of truth for everything that is NOT a concept ("knowledge"). The OKF
   bundle under knowledge/ holds the concepts (nodes) + their typed, provenance-tagged
   relations (edges); this file holds the clusters (FIBO domains), relation styling,
   maturity levels, and the interactive flows. scripts/okf.js inlines it into js/data.js.

   Flows (DECISION_TREE / GUIDED_PATH / COMPARISONS) reference concepts by their real FIBO
   `resource` IRI; the build resolves each to a node id and drops any that don't resolve —
   so nothing here can hallucinate a concept that isn't in the extract.
   Forked from Bodhi's okf.config.js (MIT, © Sanjeev Azad).
   ============================================================================ */
(function (root, factory) {
  const o = factory();
  if (typeof module === 'object' && module.exports) module.exports = o; // Node (scripts/okf.js)
  else { root.CLUSTERS = o.CLUSTERS; root.RELATIONS = o.RELATIONS; root.LEVELS = o.LEVELS;
         root.CLUSTER_TYPE = o.CLUSTER_TYPE; root.DECISION_TREE = o.DECISION_TREE; root.GUIDED_PATH = o.GUIDED_PATH;
         root.RELEASE = o.RELEASE; }
})(typeof self !== 'undefined' ? self : this, function () {
  const F = 'https://spec.edmcouncil.org/fibo/ontology/';

  const RELEASE = { version: '0.1.0', label: 'v0.1.0' };

  // FIBO domains + base hue. The build (scripts/okf.js) SPLITS each domain into its FIBO
  // modules (2nd IRI segment, e.g. FBC/FunctionalEntities) as sub-clusters — coloured with
  // shades of the domain hue — so the canvas shows per-sub-domain hulls and the left legend
  // groups them under the domain. `order` fixes the legend group order.
  const DOMAINS = {
    LOAN: { label: 'Loans',                color: '#10b981', order: 1 },
    FBC:  { label: 'Business & Commerce',  color: '#f59e0b', order: 2 },
    FND:  { label: 'Foundations',          color: '#3b82f6', order: 3 },
    BE:   { label: 'Business Entities',    color: '#8b5cf6', order: 4 },
    SEC:  { label: 'Securities',           color: '#ec4899', order: 5 },
    DER:  { label: 'Derivatives',          color: '#ef4444', order: 6 },
    IND:  { label: 'Indices & Indicators', color: '#14b8a6', order: 7 },
    MD:   { label: 'Market Data',          color: '#84cc16', order: 8 },
    BP:   { label: 'Business Process',     color: '#fb923c', order: 9 },
    CAE:  { label: 'Corporate Actions',    color: '#d946ef', order: 10 },
    CMNS: { label: 'Commons (shared)',     color: '#64748b', order: 11 },  // FIBO upper ontology
  };

  const CLUSTER_TYPE = { LOAN: 'FIBO Class', FBC: 'FIBO Class', FND: 'FIBO Class', BE: 'FIBO Class',
                         SEC: 'FIBO Class', DER: 'FIBO Class', IND: 'FIBO Class', MD: 'FIBO Class',
                         BP: 'FIBO Class', CAE: 'FIBO Class', CMNS: 'Commons Class' };

  // FIBO maturity, propagated per class — reused as Bodhi's "level" filter dimension.
  const LEVELS = { 1: 'Release', 2: 'Provisional', 3: 'Informative' };
  const MATURITY_LEVEL = { Release: 1, Provisional: 2, Informative: 3 };

  // Relation styling. is-a is the taxonomic spine; curated cross-domain bridge edge-names
  // are drawn distinctly (red, dashed) — the project's contribution, made visible. Unknown
  // FIBO object properties fall back to is-a's neutral style in the renderer.
  const RELATIONS = {
    'is-a':             { label: 'is a type of',     color: '#64748b', style: 'solid'  },
    'is-classified-by': { label: 'is classified by', color: '#0ea5e9', style: 'solid'  },
    'comprises':        { label: 'comprises',        color: '#14b8a6', style: 'solid'  },
    'identifies':       { label: 'identifies',       color: '#06b6d4', style: 'solid'  },
    'is-identified-by': { label: 'is identified by', color: '#06b6d4', style: 'solid'  },
    'has-party-role':   { label: 'has party role',   color: '#f97316', style: 'solid'  },
    'is-played-by':     { label: 'is played by',     color: '#f97316', style: 'solid'  },
    'governs':          { label: 'governs',          color: '#8b5cf6', style: 'solid'  },
    'applies-to':       { label: 'applies to',       color: '#a78bfa', style: 'dotted' },
    'path':             { label: 'workflow step',    color: '#fbbf24', style: 'solid'  },
    // curated cross-domain bridges (provenance: curated)
    'reported-in':      { label: 'reported in',      color: '#e11d48', style: 'dashed' },
    'filed-by':         { label: 'filed by',         color: '#e11d48', style: 'dashed' },
    'played-by':        { label: 'played by',        color: '#e11d48', style: 'dashed' },
    'identified-by':    { label: 'identified by',    color: '#e11d48', style: 'dashed' },
    'backed-by':        { label: 'backed by',        color: '#e11d48', style: 'dashed' },
    'submitted-to':     { label: 'submitted to',     color: '#e11d48', style: 'dashed' },
    'required-by':      { label: 'required by',      color: '#e11d48', style: 'dashed' },
  };

  // Decision wizard: "Which FIBO concept models what I'm working with?" (rec = FIBO IRI).
  const DECISION_TREE = {
    start: 'aspect',
    steps: {
      aspect: {
        q: 'What part of a loan origination are you trying to model?',
        a: [
          { label: 'The loan / mortgage instrument', next: 'instrument' },
          { label: 'A party or role (borrower, lender, guarantor…)', next: 'party' },
          { label: 'Underwriting & risk', rec: F + 'LOAN/LoansGeneral/LoanApplications/CreditRiskAssessment',
            why: 'Credit risk assessment determines the likelihood a borrower repays — the core of underwriting.' },
          { label: 'Regulatory reporting (US HMDA)', rec: F + 'LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report',
            why: 'The HMDA report satisfies US Home Mortgage Disclosure Act reporting for covered loans.' },
        ],
      },
      instrument: {
        q: 'Is the loan secured by real property?',
        a: [
          { label: 'Yes — a residential mortgage', rec: F + 'LOAN/RealEstateLoans/Mortgages/Mortgage',
            why: 'A mortgage grants a financial interest in real property to a non-owner, recorded by a registration authority.' },
          { label: 'Yes — a revolving line against home equity', rec: F + 'LOAN/LoansSpecific/ConsumerLoans/HomeEquityLineOfCredit',
            why: 'A HELOC is a line of credit secured by the equity in the borrower’s home.' },
          { label: 'No — a general loan', rec: F + 'LOAN/LoansGeneral/Loans/Loan',
            why: 'Loan is the base debt instrument: money/credit extended to be repaid per contract terms.' },
        ],
      },
      party: {
        q: 'Which side of the agreement?',
        a: [
          { label: 'The party that repays', rec: F + 'FBC/DebtAndEquities/Debt/Borrower',
            why: 'The borrower is obligated to repay principal with interest under the credit agreement.' },
          { label: 'The party that extends credit', rec: F + 'FBC/DebtAndEquities/Debt/Lender',
            why: 'The lender extends credit expecting repayment with interest.' },
          { label: 'A third party guaranteeing the obligation', rec: F + 'FBC/DebtAndEquities/Guaranty/Guarantor',
            why: 'A guarantor provides indemnity for the obligation on behalf of the borrower.' },
        ],
      },
    },
  };

  // Guided tour of the underwriting arc (each step = a real core concept IRI).
  const GUIDED_PATH = {
    title: 'Loan origination — the underwriting arc',
    steps: [
      { id: F + 'LOAN/LoansGeneral/LoanApplications/LoanApplication', note: 'A potential borrower applies to a lender to borrow money — the entry point of origination.' },
      { id: F + 'FBC/DebtAndEquities/Debt/Borrower', note: 'The party obligated to repay principal with interest under the credit agreement.' },
      { id: F + 'FBC/DebtAndEquities/Debt/Lender', note: 'The party extending credit, expecting repayment with interest.' },
      { id: F + 'LOAN/LoansGeneral/LoanApplications/CreditRiskAssessment', note: 'The lender assesses how likely the borrower is to repay.' },
      { id: F + 'FBC/DebtAndEquities/Debt/Collateral', note: 'Something pledged as security for the loan obligation.' },
      { id: F + 'FND/Arrangements/Assessments/Appraisal', note: 'A written estimate of the collateral’s market value.' },
      { id: F + 'LOAN/LoansGeneral/Loans/LoanToValueRatio', note: 'Loan principal ÷ appraised value — a key underwriting ratio.' },
      { id: F + 'LOAN/LoansGeneral/LoanApplications/UnderwritingDecision', note: 'The approval recommendation — what origination drives toward.' },
      { id: F + 'LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report', note: 'For covered loans, the decision is reported to the regulator (a curated bridge).' },
    ],
  };

  // Side-by-side comparison matrices. Each row links to its graph node by FIBO IRI.
  const COMPARISONS = [
    {
      id: 'mortgage-types', title: 'Mortgage types',
      blurb: 'Real-estate-secured loan products in FIBO — how they differ on additional draws and purpose.',
      dimensions: [
        { key: 'secured', label: 'Secured by' },
        { key: 'draw', label: 'Additional draws?' },
        { key: 'note', label: 'Note' },
      ],
      rows: [
        { id: F + 'LOAN/RealEstateLoans/Mortgages/ClosedEndMortgageLoan', secured: 'Real estate', draw: 'No', note: 'No further funds after origination' },
        { id: F + 'LOAN/RealEstateLoans/Mortgages/OpenEndMortgageLoan', secured: 'Real estate', draw: 'Yes (by mutual agreement)', note: 'Outstanding amount may increase' },
        { id: F + 'LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan', secured: 'Real estate', draw: 'Pays borrower', note: 'Draws against existing equity' },
        { id: F + 'LOAN/LoansSpecific/ConsumerLoans/HomeEquityLineOfCredit', secured: 'Home equity', draw: 'Revolving', note: 'Line of credit, not a lump sum' },
      ],
    },
    {
      id: 'party-roles', title: 'Party roles',
      blurb: 'The parties to a credit agreement and what each one does.',
      dimensions: [
        { key: 'domain', label: 'Domain' },
        { key: 'role', label: 'Role' },
      ],
      rows: [
        { id: F + 'FBC/DebtAndEquities/Debt/Borrower', domain: 'FBC', role: 'Repays principal + interest' },
        { id: F + 'FBC/DebtAndEquities/Debt/Lender', domain: 'FBC', role: 'Extends credit' },
        { id: F + 'FBC/DebtAndEquities/Debt/Creditor', domain: 'FBC', role: 'Is owed the obligation' },
        { id: F + 'FBC/DebtAndEquities/Guaranty/Guarantor', domain: 'FBC', role: 'Guarantees / indemnifies' },
        { id: F + 'LOAN/LoansGeneral/Loans/Servicer', domain: 'LOAN', role: 'Collects payments for the lender' },
      ],
    },
  ];

  return { DOMAINS, CLUSTER_TYPE, LEVELS, MATURITY_LEVEL, RELATIONS, RELEASE, DECISION_TREE, GUIDED_PATH, COMPARISONS };
});
