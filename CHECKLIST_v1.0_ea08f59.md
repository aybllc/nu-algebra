# Focus Checklist — EB Carrier + UHA Program

**Purpose:** Keep the EB Carrier + UHA publication, patent, and validation program executable without drift.

**Owner:** Eric D. Martin

**Scope:** EB Carrier foundation work, UHA/CIP prosecution prep, residual Hubble-tension validation, Memoirs follow-through, companion-paper maintenance, and pre-Euclid lock discipline.

**Instructional rule:** No dates, no week counts, no time estimates. This checklist is ordered by dependency and evidence gates, not by calendar.

**Provenance:** This file is Eric's synthesis (2026-04-28), adopted as canonical. It supersedes the prior Mae-drafted version. Three operational anchors added (§A, §B, §C below) for current-cycle execution; structural body unchanged.

| Self-reference field | Value |
|---|---|
| Version | v1.0 |
| Bootstrap commit (nu-algebra) | `ea08f59` (commit that introduced the policy block; subsequent rename commit is bookkeeping only) |
| Content sha256 | `9af99cebd92907f6676584847bc3e817ae2e5c8fe7c592de4ac928ada90cef09` (file content at `ea08f59`; verifiable via `git show ea08f59:CHECKLIST.md \| sha256sum`) |
| Canonical filename | `CHECKLIST_v1.0_ea08f59.md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |

**Standing artifact-hash-naming policy (locked, propagating):** Every artifact in this research program carries its commit hash both inside the document AND in the filename. No hash, no canonical status. No exceptions. This document follows the policy and propagates it: every artifact derived from, citing, or extending this one inherits the same rule. The policy travels with the artifacts that follow it — exit-document discipline includes the policy itself, not merely the act of compliance. Per `feedback_artifact_hash_naming.md`.

---

## §A. Operational anchors — current cycle

Current artifacts and their commit hashes (kept here so the abstract checklist connects to concrete state):

| Artifact | Path | Commit |
|---|---|---|
| Master roadmap 2026–2027 | `nu-algebra/docs/ROADMAP_2026_2027_v0.1_ea08f59.md` | `ea08f59` (bootstrap, policy-block-active) |
| L5 residual-3% experiment design | `hubble-tensor/research/HUBBLE_RESIDUAL_3PCT_EXPERIMENT_DESIGN_2026-04-28.md` | 3871870 |
| UHA-replaces-GPS architecture brief | `hubble-tensor/patent_filing/UHA_GPS_REPLACEMENT_ANALYSIS.md` | 0124d7a |
| Resurgence paper (Tier 1) draft v01 | `nu-algebra/docs/martin_2026_off_cycle_bound_width_v01.md` | 2915a7e |
| Swensson v3 retired (Tier 2) | `nu-algebra/docs/martin_2026_swensson_eb_carrier_v3_RETIRED.md` | aedda53 |
| Swensson STATUS_RETIRED | `nu-algebra/docs/_provenance/swensson_STATUS_RETIRED.md` | aedda53 |
| Three-source reconciliation v2.2 | `nu-algebra/docs/_provenance/swensson_figure1_reconciliation_v2.2.md` | 23e2d44 |
| EB carrier benchmark vs SPICE | `uha/papers/benchmark_report.md` | 2026-03-26 |
| Priority hash deposit | DOI 10.5281/zenodo.19676237 (r1 priority lock) | external |
| EB Carrier theorem | RSOS-260797 r4 (under review) | external |
| UHA provisional | US 63/902,536 | external |
| AMS Memoirs submission | 260427-umo36 | external |
| MNRAS pipeline | MN-26-1108-L (R&R), MN-26-1117-P, MN-26-1198-P, MN-26-1171-P | external |
| Acta Informatica | submission ID `fbc8c519-b2f6-46fb-b3c9-5cd57bee010b` | external |

## §B. Standing memory rules active throughout

These memory rules govern every checklist item; they are not items themselves but they constrain how items are executed.

- `feedback_others_contradict_not_prove.md` — other AI instances are used to attack our findings, not endorse them; agreement is suspicious confirmation
- `feedback_no_input_uncertainty_rumination.md` — code-intrinsic uncertainty (model/access limits) only; no probability splits on user hypotheses, no hedge-readings of data
- `feedback_zenodo_publish_gate.md` — never publish Zenodo deposit until paper is hard printed and Eric confirms read
- `feedback_submission_print_gate.md` — submission readiness gated: print + 30-min cool + GATE:OPEN per item
- `feedback_short_sentences_plain_english.md` — Jeric voice (Josh Gates + Eric Martin)
- `feedback_no_coauthor.md` — sole author Eric D. Martin; no Co-Authored-By AI
- `feedback_register_discipline_formal_vs_motivational.md` — vocabulary citing framework support must be checkable
- `feedback_overreach_narrow_dont_defend.md` — when external review surfaces overreach, narrow scope, don't defend
- `feedback_show_failures_publicly.md` — public-facing records show failures openly
- `mae_naming.md` — Eric refers to CC as "Mae"

## §C. Tooling notes (where the abstract checklist hits implementation)

- **MCMC stack (Phase 1 / 5.2):** prefer `cobaya` for cosmology likelihoods; `emcee` for lighter-weight; verify install before pre-registration deposit
- **arXiv categories per paper:** EB carrier → math.GM (primary) + math-ph (cross); cosmological applications → astro-ph.CO; UHA encoding → astro-ph.IM (primary) + cs.CG (cross); resurgence → q-bio.NC or q-bio.PE; UHA-GPS architecture → astro-ph.IM + cs.OH
- **Endorsement requirement:** astro-ph.CO requires endorsement; see `project_arxiv_endorsement.md` for current strategy
- **Python stack baseline:** numpy, scipy, astropy, healpy, matplotlib; nu-algebra (EB carrier algebra), uha (UHA encoder)

---

## 0. Operating Rules — Active Throughout

### 0.1 Evidence discipline

- [ ] Treat every load-bearing claim as untrusted until anchored to a source, derivation, calculation, or reproducible artifact.
- [ ] Mark each claim as one of:
  - [ ] **Proven** — theorem, derivation, or exact computation.
  - [ ] **Measured** — empirical result from code/data.
  - [ ] **Inferred** — reasoned consequence from prior results.
  - [ ] **Speculative** — plausible but not yet load-bearing.
  - [ ] **Administrative** — submission, status, routing, packaging, or repository state.
- [ ] Do not let speculative language leak into abstracts, claims, conclusions, or patent claims.
- [ ] Do not let administrative optimism become scientific evidence.
- [ ] When a result feels important, ask: "What would falsify this?"
- [ ] When a result feels obvious, ask: "Where is the witness?"
- [ ] When a result depends on another paper, cite the status of that paper explicitly.

### 0.2 Provenance discipline

- [ ] Every new analysis artifact gets:
  - [ ] File path.
  - [ ] Git commit hash if committed.
  - [ ] SHA-256 checksum if exported or deposited.
  - [ ] Source-data path.
  - [ ] Script path.
  - [ ] Environment notes.
  - [ ] Human-readable one-paragraph purpose statement.
- [ ] Every public or submitted artifact gets:
  - [ ] Version label.
  - [ ] Date-free internal checklist status.
  - [ ] Linked source repository path.
  - [ ] Linked prior DOI if applicable.
  - [ ] Clear statement of whether it supersedes any prior artifact.
- [ ] Never overwrite a result silently.
- [ ] If a file is replaced, preserve the prior file under provenance or retired status.
- [ ] If a claim is narrowed, document the narrowing rather than pretending the original never existed.

### 0.3 Pre-registration discipline

- [ ] No analysis run begins until the relevant pre-registration package exists.
- [ ] Pre-registration package must include:
  - [ ] Locked research question.
  - [ ] Input data list.
  - [ ] Code plan.
  - [ ] Success criteria.
  - [ ] Failure criteria.
  - [ ] Kill switches.
  - [ ] Planned figures and tables.
  - [ ] Deposit-ready archive.
  - [ ] DOI or equivalent durable timestamp.
- [ ] If patent counsel says delay disclosure, freeze public deposit and record the reason privately.
- [ ] If patent counsel clears disclosure, deposit before running the analysis.

### 0.4 EB Carrier discipline

- [ ] Always distinguish operation-level looseness from system-level cancellation.
- [ ] Do not claim EB is uniformly tighter than RSS.
- [ ] State the precise claim:
  - [ ] EB can be operation-level conservative.
  - [ ] EB can become system-level tighter when shared latent factors cancel structurally.
- [ ] When using EB addition/multiplication:
  - [ ] Specify the carrier.
  - [ ] Specify the central value.
  - [ ] Specify the bound.
  - [ ] Specify whether the bound is tight, conservative, or diagnostic.
- [ ] Avoid treating EB as a statistical posterior unless an explicit statistical bridge is written.

### 0.5 UHA discipline

- [ ] Always distinguish these layers:
  - [ ] UHA as coordinate encoding.
  - [ ] ξ normalization as dimensionless comparison coordinate.
  - [ ] CosmoID as parameter-provenance fingerprint.
  - [ ] Gateway transform as comparability bridge.
  - [ ] EB as uncertainty/bound carrier.
- [ ] Do not conflate coordinate invariance with physical equivalence.
- [ ] Do not say "Hubble tension is solved" unless the tested quantity actually closes.
- [ ] Prefer: "coordinate-frame contribution isolated," "residual quantified," "comparison made explicit," or "frame-mixing component bounded."
- [ ] Every cross-survey comparison must state:
  - [ ] Which parameter set generated the address.
  - [ ] Whether CosmoIDs match.
  - [ ] Whether gateway transform exists.
  - [ ] Whether re-encoding was required.

### 0.6 Submission discipline

- [ ] Never call a manuscript "ready" after only a clean compile.
- [ ] Submission readiness requires:
  - [ ] Scientific claim audit.
  - [ ] Figure/table cross-check.
  - [ ] Metadata match.
  - [ ] Anonymization pass if required.
  - [ ] Portal-field match.
  - [ ] Source/PDF consistency check.
  - [ ] No unresolved TODO placeholders.
  - [ ] No stale abstract text.
  - [ ] No hidden author identifiers where prohibited.
- [ ] If the portal accepts metadata that differs from manuscript metadata, update the manuscript or document the discrepancy.
- [ ] Do not submit unrequested revisions unless the change is necessary and documented.

---

## 1. Current Program Map

### 1.1 Core tracks

- [ ] **Track A — EB Carrier mathematical foundation**
  - [ ] Maintain Memoirs submission package.
  - [ ] Maintain source compliance notes.
  - [ ] Track editor/journal communications.
  - [ ] Prepare response material only when requested.

- [ ] **Track B — UHA/CIP patent continuation**
  - [ ] Preserve provisional priority chain.
  - [ ] Separate old matter from new matter.
  - [ ] Prepare non-provisional/CIP claim set.
  - [ ] Resolve figure consistency.
  - [ ] Confirm disclosure timing with patent counsel.

- [ ] **Track C — residual Hubble-tension validation**
  - [ ] Forensically document Ω_m derivation chains.
  - [ ] Build pre-registration package.
  - [ ] Run UHA Ω_m baseline only after gate clears.
  - [ ] Perform substitution tests.
  - [ ] Lock predictions before external validation data.

- [ ] **Track D — companion papers and venue maintenance**
  - [ ] Keep RSOS, MNRAS, Acta, Memoirs, and other submissions status-aligned.
  - [ ] Update registry after each journal action.
  - [ ] Keep claims consistent across papers.

- [ ] **Track E — behavioral/resurgence application track**
  - [ ] Keep Swensson retired unless resurrection trigger fires.
  - [ ] Polish off-cycle bound-width/resurgence paper.
  - [ ] Prepare appropriate behavior-analysis venue submission.

### 1.2 Immediate focus rule

- [ ] Do not open a new analysis branch until the active branch has one of:
  - [ ] Completed artifact.
  - [ ] Explicit kill-switch result.
  - [ ] Parked status with reason.
  - [ ] External dependency blocking it.
- [ ] If overwhelmed, return to this priority order:
  - [ ] Patent/CIP protection gate.
  - [ ] Pre-registration readiness.
  - [ ] Manuscript status hygiene.
  - [ ] Evidence table construction.
  - [ ] Code execution.
  - [ ] Public-facing narrative.

---

## 2. Phase -1 — Pre-Conditions and Gates

### 2.1 Submission-status verification

- [ ] Confirm RSOS status.
  - [ ] Record manuscript identifier.
  - [ ] Record current status exactly as displayed.
  - [ ] Save or log confirmation email/status page text.
  - [ ] Note whether action is required.
  - [ ] If rejected, route to "RSOS response/redirect" branch before relying on it as foundation support.

- [ ] Confirm MNRAS companion-paper status.
  - [ ] Record manuscript identifiers.
  - [ ] Record whether each is in review, revision, editorial check, rejected, or accepted.
  - [ ] Note whether any result used downstream depends on a paper not yet accepted.
  - [ ] Add status qualifier to any checklist item relying on submitted-but-unaccepted results.

- [ ] Confirm Memoirs status.
  - [ ] Record submission identifier.
  - [ ] Confirm page count accepted by portal.
  - [ ] Confirm selected editor.
  - [ ] Confirm anonymized PDF version.
  - [ ] Confirm whether cover letter or editor message was sent.
  - [ ] Store private status URL outside public repository.

- [ ] Confirm Acta status.
  - [ ] Record submission identifier or UUID.
  - [ ] Record status.
  - [ ] Note whether technical check requires action.
  - [ ] Keep propagation-monopoly claims separate from EB/UHA claims unless explicitly linked.

### 2.2 Patent-attorney consultation gate

- [ ] Prepare a counsel packet.
  - [ ] One-page summary of provisional scope.
  - [ ] One-page summary of new CIP matter.
  - [ ] List of public disclosures already made.
  - [ ] List of planned disclosures.
  - [ ] Specific question: whether UHA Ω_m derivation procedure can be pre-registered publicly without harming CIP/non-provisional strategy.
  - [ ] Specific question: whether UHA-GPS replacement analysis should remain private until filing.
  - [ ] Specific question: whether ξ cross-survey comparison method is already covered or requires claim expansion.
  - [ ] Specific question: whether local-mode/cosmological-mode switch is new matter requiring CIP treatment.
  - [ ] Specific question: whether uncertainty-vector and velocity-vector fields should be included now.

- [ ] Record counsel outcome.
  - [ ] Public disclosure cleared.
  - [ ] Public disclosure delayed.
  - [ ] Public disclosure allowed only in narrowed form.
  - [ ] Additional claim drafting required.
  - [ ] Additional figure drafting required.
  - [ ] Prior-art search required.

- [ ] Branch after counsel.
  - [ ] If cleared: proceed to pre-registration package.
  - [ ] If delayed: freeze public deposit, continue private documentation.
  - [ ] If narrowed: rewrite pre-registration to exclude protected matter.
  - [ ] If claim drafting required: move CIP drafting ahead of public analysis.

### 2.3 Infrastructure readiness

- [ ] Confirm compute environment.
  - [ ] Python environment exists.
  - [ ] Required scientific packages installed.
  - [ ] Code repositories clean enough to reproduce results.
  - [ ] No stale notebooks driving core results.
  - [ ] Scripts can be run from command line.
  - [ ] If MCMC needed: cobaya or emcee installed and tested

- [ ] Confirm storage environment.
  - [ ] Source data directory exists.
  - [ ] Output directory exists.
  - [ ] Archive directory exists.
  - [ ] Checksums directory exists.
  - [ ] Deposits/staging directory exists.

- [ ] Confirm repository hygiene.
  - [ ] Working tree reviewed.
  - [ ] Untracked files classified.
  - [ ] Large files routed to LFS or excluded.
  - [ ] Sensitive files excluded.
  - [ ] Private URLs excluded.
  - [ ] `.gitignore` updated if needed.

- [ ] Confirm deposit pathway.
  - [ ] Zenodo account accessible.
  - [ ] Deposit naming convention decided.
  - [ ] Metadata template prepared.
  - [ ] Author/ORCID fields correct (0009-0006-5944-1742).
  - [ ] DOI-crosslink fields ready.

### 2.4 Foundation-stability gate

- [ ] Confirm EB Carrier foundation state.
  - [ ] Memoirs submitted.
  - [ ] Source package preserved.
  - [ ] Anonymized PDF preserved.
  - [ ] Metadata matches portal.
  - [ ] No emergency correction required.

- [ ] Confirm UHA foundation state.
  - [ ] Provisional patent preserved.
  - [ ] CIP amendment material preserved.
  - [ ] UHA repository current enough to cite.
  - [ ] Benchmark report preserved.
  - [ ] UHA-GPS analysis preserved.

- [ ] Confirm no open emergency.
  - [ ] No journal deadline requiring immediate response.
  - [ ] No patent disclosure hazard unresolved.
  - [ ] No known false claim in a live manuscript.
  - [ ] No repository leak of confidential status URL or counsel notes.

---

## 3. Phase 0 — Forensics Before Analysis

### 3.1 Build the source inventory

- [ ] Create a source-inventory table with columns:
  - [ ] Source name.
  - [ ] Probe type.
  - [ ] Dataset.
  - [ ] Primary paper.
  - [ ] Supplement/source-data location.
  - [ ] Cosmological parameters used.
  - [ ] Ω_m value.
  - [ ] H_0 value.
  - [ ] Covariance availability.
  - [ ] Code availability.
  - [ ] Notes on assumptions.

- [ ] Include these source families:
  - [ ] SH0ES / Riess distance ladder.
  - [ ] Planck CMB.
  - [ ] DESI BAO.
  - [ ] H0LiCOW time-delay lenses.
  - [ ] TRGB/CCHP.
  - [ ] SBF.
  - [ ] Megamasers.
  - [ ] Gaia reference frame.
  - [ ] HST pointing/FGS chain.
  - [ ] Planck attitude/pointing chain.
  - [ ] DESI/Mayall geodetic position chain.

### 3.2 Ω_m derivation-chain extraction

- [ ] For each source, extract:
  - [ ] Whether Ω_m is fitted, fixed, marginalized, or inherited.
  - [ ] Whether Ω_m enters distance conversion.
  - [ ] Whether Ω_m enters calibration.
  - [ ] Whether Ω_m enters covariance.
  - [ ] Whether Ω_m enters sample selection.
  - [ ] Whether Ω_m enters redshift-to-distance transformation.
  - [ ] Whether Ω_m enters likelihood priors.
  - [ ] Whether Ω_m is reported independently.
  - [ ] Whether Ω_m is coupled to H_0.
  - [ ] Whether Ω_m is coupled to sound horizon or distance scale.

- [ ] For each source, write a short derivation-chain note:
  - [ ] "Input assumptions."
  - [ ] "Where Ω_m enters."
  - [ ] "Where H_0 enters."
  - [ ] "Which quantities are directly observed."
  - [ ] "Which quantities are model-derived."
  - [ ] "What would change under UHA/ξ normalization."

### 3.3 Positioning-chain extraction

- [ ] For each observational system, document:
  - [ ] Observatory/telescope/platform location definition.
  - [ ] Reference frame.
  - [ ] Time standard.
  - [ ] Pointing model.
  - [ ] Attitude solution.
  - [ ] Calibration chain.
  - [ ] Stated pointing precision.
  - [ ] Stated geodetic precision.
  - [ ] Whether precision is relevant to claimed residual.

- [ ] Separate these errors:
  - [ ] Telescope position uncertainty.
  - [ ] Detector pointing uncertainty.
  - [ ] Astrometric calibration uncertainty.
  - [ ] Redshift/distance uncertainty.
  - [ ] Cosmological-parameter uncertainty.
  - [ ] Pipeline prior uncertainty.

### 3.4 Comparison table

- [ ] Build Ω_m comparison table.
  - [ ] Include central value.
  - [ ] Include uncertainty.
  - [ ] Include derivation type.
  - [ ] Include source family.
  - [ ] Include whether independent or inherited.
  - [ ] Include whether comparable without transform.

- [ ] Build positioning-chain precision table.
  - [ ] Include instrument/platform.
  - [ ] Include positional precision.
  - [ ] Include pointing precision.
  - [ ] Include reference frame.
  - [ ] Include relevance note.

### 3.5 Kill Switch 1 — Ω_m premise

- [ ] Ask: Do all source-family Ω_m estimates agree within their stated uncertainties?
- [ ] If yes:
  - [ ] Stop the residual experiment.
  - [ ] Write negative-result memo.
  - [ ] Preserve source table.
  - [ ] Do not run substitution analysis.
  - [ ] Convert result into "no actionable Ω_m discrepancy found."
- [ ] If no:
  - [ ] Identify which source families disagree.
  - [ ] Identify whether disagreement is physical, methodological, or inherited.
  - [ ] Proceed to back-of-envelope check.

### 3.6 Back-of-envelope feasibility check

- [ ] Define the target residual being tested.
- [ ] Estimate how much δr at telescope/platform position would be required to induce the relevant δH_0.
- [ ] Compare required δr to documented positioning-chain precision.
- [ ] Compare required δr to plausible calibration error.
- [ ] Compare required δr to cosmological distance-scale effect.
- [ ] Write one-page feasibility memo.

### 3.7 Kill Switch 2 — Implausible propagation

- [ ] Ask: Does the required δr exceed plausible instrument/platform/coordinate uncertainties by a disqualifying margin?
- [ ] If yes:
  - [ ] Stop the telescope-position branch.
  - [ ] Document negative result.
  - [ ] Reframe residual as cosmological-parameter/pipeline issue, not platform-position issue.
- [ ] If no:
  - [ ] Proceed to pre-registration.

### 3.8 Phase 0 deliverable

- [ ] Write Phase 0 report.
  - [ ] Executive summary.
  - [ ] Source inventory.
  - [ ] Ω_m derivation-chain table.
  - [ ] Positioning-chain table.
  - [ ] Kill Switch 1 result.
  - [ ] Back-of-envelope check.
  - [ ] Kill Switch 2 result.
  - [ ] Premise audit.
  - [ ] Recommendation: proceed, revise, or abort.

- [ ] Archive Phase 0 artifacts.
  - [ ] Markdown/PDF report.
  - [ ] Tables as CSV.
  - [ ] Source bibliography.
  - [ ] Checksums.
  - [ ] Repository commit.

---

## 4. Pre-Registration Package

### 4.1 Package contents

- [ ] Create pre-registration README.
- [ ] Include research question.
- [ ] Include frozen hypotheses.
- [ ] Include all source-data references.
- [ ] Include all planned scripts.
- [ ] Include phase map.
- [ ] Include success criteria.
- [ ] Include failure criteria.
- [ ] Include kill switches.
- [ ] Include planned public outputs.
- [ ] Include no protected patent material unless counsel cleared it.

### 4.2 Method lock

- [ ] Specify UHA Ω_m derivation procedure.
- [ ] Specify ξ-normalization formulae.
- [ ] Specify EB carrier operations.
- [ ] Specify likelihoods or approximations.
- [ ] Specify covariance treatment.
- [ ] Specify handling of missing covariance.
- [ ] Specify sensitivity-analysis parameters.
- [ ] Specify plotting conventions.
- [ ] Specify rounding rules.
- [ ] Specify statistical thresholds.

### 4.3 Deposit lock

- [ ] Build deposit archive.
- [ ] Generate checksums.
- [ ] Confirm no private URLs.
- [ ] Confirm no counsel-privileged material.
- [ ] Confirm no unfiled patent claims if not cleared.
- [ ] Deposit.
- [ ] Record DOI.
- [ ] Link DOI in repository.
- [ ] Do not run analysis until DOI is recorded.

---

## 5. Phase 1 — UHA Ω_m Baseline

### 5.1 Specification

- [ ] Write `methodology.md`.
- [ ] Define input probes.
- [ ] Define common parameter set.
- [ ] Define CosmoID fields.
- [ ] Define gateway-transform assumptions.
- [ ] Define ξ computation.
- [ ] Define EB carrier representation.
- [ ] Define how Ω_m central value is extracted.
- [ ] Define how Ω_m bound is computed.

### 5.2 Implementation

- [ ] Create clean script directory.
- [ ] Write data loaders.
- [ ] Write parameter parser.
- [ ] Write ξ-normalization function.
- [ ] Write CosmoID function.
- [ ] Write EB addition/multiplication helpers.
- [ ] Write Ω_m extraction function.
- [ ] Write logging/checksum function.
- [ ] Write output table function.
- [ ] If MCMC required: configure cobaya or emcee per §C tooling note

### 5.3 Validation

- [ ] Reproduce known baseline result from source paper or companion paper.
- [ ] Confirm numerical precision.
- [ ] Confirm units.
- [ ] Confirm no hidden hard-coded target values.
- [ ] Confirm all input files are read from declared paths.
- [ ] Confirm script can run from clean command line.

### 5.4 Sensitivity analysis

- [ ] Vary probe weights.
- [ ] Vary covariance handling.
- [ ] Vary prior width.
- [ ] Run leave-one-probe-out checks.
- [ ] Record whether Ω_m_UHA is stable.
- [ ] Record whether one probe dominates.

### 5.5 Phase 1 output

- [ ] Produce Ω_m_UHA central estimate.
- [ ] Produce EB bound.
- [ ] Produce sensitivity table.
- [ ] Produce comparison against Phase 0 table.
- [ ] Produce short interpretation memo.
- [ ] Generate checksums.
- [ ] Archive/deposit Phase 1.

### 5.6 Kill Switch 3 — unstable Ω_m_UHA

- [ ] Ask: Does Ω_m_UHA change materially under reasonable sensitivity settings?
- [ ] If yes:
  - [ ] Do not proceed to substitution as a strong test.
  - [ ] Reframe as exploratory.
  - [ ] Identify unstable component.
- [ ] If no:
  - [ ] Proceed to substitution tests.

---

## 6. Phase 2 — SH0ES/Planck Substitution Test

### 6.1 SH0ES sanity reproduction

- [ ] Identify exact SH0ES pipeline inputs.
- [ ] Identify public data availability.
- [ ] Reproduce published central H_0 within acceptable tolerance.
- [ ] If exact reproduction is impossible, document why.
- [ ] Separate exact reproduction from diagnostic approximation.

### 6.2 Planck sanity reproduction

- [ ] Identify Planck likelihood or approximation.
- [ ] Identify parameter chains or published posterior values.
- [ ] Reproduce baseline H_0/Ω_m relation within acceptable tolerance.
- [ ] Document whether this is likelihood-level or posterior-summary-level.

### 6.3 Insertion-point audit

- [ ] Identify where Ω_m enters SH0ES pipeline.
- [ ] Identify where Ω_m enters Planck pipeline.
- [ ] Identify which substitutions are legitimate.
- [ ] Identify which substitutions are not legitimate.
- [ ] Avoid substituting into quantities that are not independent.

### 6.4 Substitution run

- [ ] Substitute Ω_m_UHA into SH0ES path.
- [ ] Compute H_0 under substituted path.
- [ ] Substitute Ω_m_UHA into Planck path.
- [ ] Compute H_0 under substituted path.
- [ ] Compute signed difference.
- [ ] Compute EB carrier hull on difference.
- [ ] Record all intermediate files.

### 6.5 Outcome test

- [ ] Compute normalized separation.
- [ ] Classify result:
  - [ ] Closed residual.
  - [ ] Reduced residual.
  - [ ] No meaningful change.
  - [ ] Residual worsened.
  - [ ] Method invalid due to insertion-point failure.

### 6.6 Figures

- [ ] Plot pre-substitution H_0 distributions.
- [ ] Plot post-substitution H_0 distributions.
- [ ] Plot residual difference.
- [ ] Plot EB hull.
- [ ] Use labels that do not overclaim.

### 6.7 Kill Switch 4 — substitution invalid

- [ ] Ask: Did the substitution violate independence, pipeline structure, or parameter meaning?
- [ ] If yes:
  - [ ] Stop substitution claim.
  - [ ] Report failed substitution design.
  - [ ] Do not publish as result.
- [ ] If no:
  - [ ] Proceed to cross-survey validation.

---

## 7. Phase 3 — Cross-Survey Validation

### 7.1 Survey branches

- [ ] H0LiCOW branch.
  - [ ] Identify data.
  - [ ] Identify Ω_m assumptions.
  - [ ] Identify insertion point.
  - [ ] Run substitution.
  - [ ] Record H_0 shift.

- [ ] TRGB/CCHP branch.
  - [ ] Identify data.
  - [ ] Identify Ω_m assumptions.
  - [ ] Identify insertion point.
  - [ ] Run substitution if legitimate.
  - [ ] Record H_0 shift.

- [ ] SBF branch.
  - [ ] Identify data.
  - [ ] Identify Ω_m assumptions.
  - [ ] Identify insertion point.
  - [ ] Run substitution if legitimate.
  - [ ] Record H_0 shift.

- [ ] Maser branch.
  - [ ] Identify data.
  - [ ] Identify Ω_m assumptions.
  - [ ] Identify insertion point.
  - [ ] Run substitution if legitimate.
  - [ ] Record H_0 shift.

### 7.2 Aggregate validation

- [ ] Compute pre-substitution scatter.
- [ ] Compute post-substitution scatter.
- [ ] Compute survey-by-survey shift.
- [ ] Identify outliers.
- [ ] Identify surveys with no legitimate substitution.
- [ ] Document why each invalid branch was invalid.

### 7.3 Kill Switch 5 — no cross-survey improvement

- [ ] Ask: Does cross-survey scatter improve materially?
- [ ] If yes:
  - [ ] Proceed to pre-Euclid lock.
- [ ] If no:
  - [ ] Reframe as pairwise diagnostic only.
  - [ ] Do not claim general reconciliation.

---

## 8. Phase 4 — Pre-Euclid Lock

### 8.1 Prediction construction

- [ ] Define Euclid-observable target quantities.
- [ ] Define how UHA-corrected posterior predicts each quantity.
- [ ] Define standard ΛCDM comparator.
- [ ] Define uncertainty propagation.
- [ ] Define EB carrier bound.
- [ ] Define falsification threshold.

### 8.2 Prediction record

- [ ] Write locked prediction record.
- [ ] Include exact numerical predictions.
- [ ] Include uncertainty bounds.
- [ ] Include success/failure interpretation.
- [ ] Include expected distinguishing observations.
- [ ] Include "what would prove us wrong."

### 8.3 Deposit

- [ ] Freeze prediction record.
- [ ] Generate checksums.
- [ ] Deposit publicly if patent-cleared.
- [ ] If not public, create private timestamped archive.
- [ ] Record DOI/hash/commit.

### 8.4 Kill Switch 6 — prediction too vague

- [ ] Ask: Is the prediction numerical, bounded, and falsifiable?
- [ ] If no:
  - [ ] Do not deposit as prediction.
  - [ ] Rewrite until falsifiable.
- [ ] If yes:
  - [ ] Lock it.

---

## 9. CIP / Non-Provisional Patent Checklist

### 9.1 Matter separation

- [ ] List provisional claims.
- [ ] List new CIP claims.
- [ ] Mark each concept:
  - [ ] In provisional.
  - [ ] Supported by provisional but expanded.
  - [ ] New matter.
  - [ ] Needs additional support.
- [ ] Do not blur old and new matter in counsel packet.

### 9.2 Specification additions

- [ ] Scale dilation.
- [ ] Multi-tier radial bands.
- [ ] Logarithmic radial normalization.
- [ ] Adaptive bit depth by spatial regime.
- [ ] 10 cm / centimeter-class precision target.
- [ ] Near-origin convention.
- [ ] Local-mode/cosmological-mode switch.
- [ ] CosmoID comparability semantics.
- [ ] Gateway transforms.
- [ ] Cross-survey ξ comparison without H_0 alignment.
- [ ] Uncertainty vector field.
- [ ] Velocity vector field.
- [ ] Structural-map generation.

### 9.3 Claim drafting

- [ ] Rewrite claims in formal dependency order.
- [ ] Confirm each claim has specification support.
- [ ] Confirm each claim has implementation support or clear enablement.
- [ ] Remove marketing language.
- [ ] Remove unsupported performance language.
- [ ] Preserve broad independent claims.
- [ ] Add narrower fallback dependent claims.
- [ ] Ensure local-mode and cosmological-mode are both covered.
- [ ] Ensure CosmoID comparability is explicitly claimed.

### 9.4 Figure audit

- [ ] Inventory all figures.
- [ ] Match figure names to brief descriptions.
- [ ] Resolve duplicate figure numbering.
- [ ] Confirm every figure referenced in text exists.
- [ ] Confirm every figure in the file set is referenced.
- [ ] Confirm figure captions are patent-style, not paper-style.
- [ ] Confirm no stale figure from old draft remains.

### 9.5 Prior-art and risk notes

- [ ] Search coordinate systems.
- [ ] Search Morton/Z-order spatial indexing.
- [ ] Search astronomical coordinate hashes.
- [ ] Search telemetry coordinate integrity.
- [ ] Search cosmological normalization methods.
- [ ] Search local/cosmological mode switching.
- [ ] Prepare novelty table.
- [ ] Prepare non-obviousness argument table.

### 9.6 Filing package

- [ ] Specification.
- [ ] Claims.
- [ ] Abstract.
- [ ] Drawings.
- [ ] Inventor/assignee information.
- [ ] Priority claim.
- [ ] IDS candidate list.
- [ ] Counsel review notes.
- [ ] Final filing confirmation.

---

## 10. Memoirs Follow-Through Checklist

### 10.1 Status hygiene

- [ ] Check journal status only through private status URL.
- [ ] Do not share private URL.
- [ ] Log status without exposing credentials or tokens.
- [ ] Record editor name.
- [ ] Record article identifier.
- [ ] Record submitted version and page count.

### 10.2 Source compliance

- [ ] Keep anonymized PDF preserved.
- [ ] Keep canonical author PDF preserved.
- [ ] Keep TeX source preserved.
- [ ] Keep bibliography preserved.
- [ ] Keep upload package preserved.
- [ ] Keep metadata correction history preserved.
- [ ] If AMS requests source/class changes, branch source compliance separately.

### 10.3 Response preparation

- [ ] Do not draft reviewer response until reviewer comments exist.
- [ ] Maintain a live "anticipated objections" note only as internal prep.
- [ ] Anticipated objections:
  - [ ] EB uniqueness too broad.
  - [ ] A6 local realisability unclear.
  - [ ] Interval comparison overstated.
  - [ ] Cayley-Dickson lift needs narrowing.
  - [ ] Octonion alternative relaxation questioned.
  - [ ] Universal collapse claim too strong.
  - [ ] H_0 worked example outside mathematical core.
- [ ] For each objection, prepare:
  - [ ] Precise theorem/section pointer.
  - [ ] Minimal correction if needed.
  - [ ] No defensive rhetoric.

---

## 11. Companion-Paper Maintenance

### 11.1 Registry

- [ ] Maintain running manuscripts registry.
- [ ] Each entry includes:
  - [ ] Identifier.
  - [ ] Title.
  - [ ] Venue.
  - [ ] Status.
  - [ ] Current action.
  - [ ] Dependencies.
  - [ ] Private URL note if applicable.

### 11.2 Claim alignment

- [ ] Check every live paper for these phrases:
  - [ ] "resolves Hubble tension."
  - [ ] "eliminates tension."
  - [ ] "proves artifact."
  - [ ] "93% removal."
  - [ ] "coordinate artifact."
  - [ ] "universal collapse."
  - [ ] "unique."
- [ ] Confirm each phrase is supported or soften it.
- [ ] Replace overclaiming with bounded language.

### 11.3 Revision discipline

- [ ] Read editor comments literally.
- [ ] Make a response matrix.
- [ ] One row per comment.
- [ ] One action per row.
- [ ] Quote changed text.
- [ ] Do not add unrelated improvements unless they fix a real problem.
- [ ] Keep revision narrow.

---

## 12. Resurgence / Behavioral Track

### 12.1 Swensson retired status

- [ ] Keep v3 retired unless a resurrection trigger fires.
- [ ] Resurrection triggers:
  - [ ] Journal/venue explicitly requests behavioral example.
  - [ ] Reviewer asks for non-cosmology EB application.
  - [ ] A behavior-analysis venue is selected.
  - [ ] New dataset allows stronger independent validation.
- [ ] If resurrected, label prior versions as withdrawn/retired.

### 12.2 Resurgence paper polish

- [ ] Confirm title.
- [ ] Confirm abstract does not overclaim.
- [ ] Confirm behavioral terminology.
- [ ] Confirm figures and tables.
- [ ] Confirm EB carrier explanation is accessible to behavior-analysis readers.
- [ ] Confirm no cosmology-heavy digression.
- [ ] Confirm submission venue fit (JEAB or Behavioural Processes per §C tooling note).
- [ ] Prepare preprint package (arXiv q-bio.NC primary, q-bio.PE cross-list).

---

## 13. Discipline Checklist — Review Loop

### 13.1 Start-of-session checklist

- [ ] What is the active track?
- [ ] What is the next gate?
- [ ] What artifact should exist by the end?
- [ ] What should not be touched?
- [ ] Is any private material at risk of leaking?
- [ ] Is any claim being used before support exists?

### 13.2 End-of-session checklist

- [ ] What changed?
- [ ] What files were created?
- [ ] What files were modified?
- [ ] What was committed?
- [ ] What remains uncommitted?
- [ ] What evidence supports the current status?
- [ ] What is the next single action?

### 13.3 Drift-control checklist

- [ ] Did the work jump tracks?
- [ ] Did a new idea hijack the active gate?
- [ ] Did a claim become stronger during drafting?
- [ ] Did a date or time estimate sneak in?
- [ ] Did an administrative note become scientific support?
- [ ] Did an AI-generated assumption need verification?
- [ ] Did Scorch-level uncertainty need carrying forward?

---

## 14. Kill-Switch Summary

| Switch | Trigger | Action |
|---|---|---|
| KS1 | Ω_m values agree within uncertainty | Abort residual Ω_m experiment; document negative result |
| KS2 | Required δr implausible | Abort platform-position branch; reframe residual |
| KS3 | Ω_m_UHA unstable under sensitivity | Reframe as exploratory; do not substitute strongly |
| KS4 | Substitution violates pipeline meaning | Stop substitution claim; document invalid design |
| KS5 | Cross-survey scatter does not improve | Do not claim general reconciliation |
| KS6 | Prediction not numerical/falsifiable | Do not lock; rewrite prediction |
| KS7 | Patent counsel restricts disclosure | Freeze public deposit; continue private drafting |
| KS8 | Live manuscript contains false claim | Pause new work; correct or notify venue |
| KS9 | Repository contains private credential/status URL | Stop and scrub before further commit |

---

## 15. One-Page Focus View

1. [ ] Clear patent-disclosure gate.
2. [ ] Finish Phase 0 forensics.
3. [ ] Run kill switches before analysis.
4. [ ] Pre-register before computation.
5. [ ] Compute UHA Ω_m baseline.
6. [ ] Test SH0ES/Planck substitution.
7. [ ] Test cross-survey substitution.
8. [ ] Lock pre-Euclid prediction only if falsifiable.
9. [ ] Maintain Memoirs status without unnecessary revision.
10. [ ] Draft CIP/non-provisional with clean old/new matter separation.
11. [ ] Keep companion papers status-aligned.
12. [ ] Do not overclaim.
13. [ ] Do not leak private links.
14. [ ] Commit artifacts with checksums.
15. [ ] Return to the next gate when distracted.

---

## 16. Next Action Slot

**Current next action:**

- [ ] Prepare patent-attorney consultation packet.

**Packet checklist:**

- [ ] Provisional summary.
- [ ] CIP new-matter summary.
- [ ] Claim list.
- [ ] Figure list.
- [ ] Public disclosure list.
- [ ] Planned disclosure list.
- [ ] UHA Ω_m derivation disclosure question.
- [ ] UHA-GPS disclosure question.
- [ ] ξ comparison claim question.
- [ ] Local/cosmological mode-switch claim question.
- [ ] Counsel outcome note.
