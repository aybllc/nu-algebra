# Focus Checklist — EB Carrier + UHA Program

**Purpose:** detailed action checklist to drive execution. No dates, no time estimates. Just items in priority order with subtasks.

**Owner:** Eric D. Martin
**Anchor docs:** `docs/ROADMAP_2026_2027.md`, `hubble-tensor/research/HUBBLE_RESIDUAL_3PCT_EXPERIMENT_DESIGN_2026-04-28.md`, `hubble-tensor/patent_filing/UHA_GPS_REPLACEMENT_ANALYSIS.md`

**Standing rules active throughout:**
- Pre-registration deposit (with DOI) must precede any analysis run
- Sha256-lock all intermediate results
- Premise audit at end of each phase against primary sources
- Every Δχ² = 279 mention notes "from MN-26-1117-P submitted (not peer-reviewed)"
- Cross-link every deposit to RSOS-260797, US 63/902,536, 10.5281/zenodo.19676236
- Use other AI instances to attack findings, not endorse them
- "Don't know any better" is learning posture privately, malpractice publicly

---

## PHASE −1: Pre-conditions (clear before Phase 0)

### Status checks on existing submissions

- [ ] **RSOS-260797 r4 status**
  - [ ] Log into RSOS submission portal
  - [ ] Confirm: under review / with editor / decision pending
  - [ ] Note last editor contact date
  - [ ] If silent > 30 days: send polite status query email
  - [ ] If rejected: identify alternative open-access venue (e.g., *Open Mathematics*, *Axioms*, *Mathematics*)
  - [ ] Document outcome in `docs/_status/rsos_260797_r4_status.md`

- [ ] **AMS Memoirs (260427-umo36) status**
  - [ ] Check AMS portal for editor message
  - [ ] Note: still waiting on memo-l.cls reply per `memoirs/eb-carrier-monograph/_provenance/memo_l_request_email.txt`
  - [ ] If memo-l.cls received: hand off to memoir Phase B1 task below
  - [ ] Document in `_status/ams_memoirs_status.md`

- [ ] **MNRAS submissions**
  - [ ] MN-26-1108-L revise & resubmit
    - [ ] Open ScholarOne, pull reviewer comments
    - [ ] List remaining unaddressed items
    - [ ] Note R&R deadline
  - [ ] MN-26-1117-P (multi-probe Δχ² = 279)
    - [ ] Check ScholarOne: in review / with editor / awaiting reviews
  - [ ] MN-26-1198-P (Pantheon+ analysis)
    - [ ] Check status
  - [ ] MN-26-1171-P (SH0ES distance ladder)
    - [ ] Check status
  - [ ] Compile single-page status summary at `docs/_status/mnras_pipeline.md`

- [ ] **Acta Informatica (propagation monopoly)**
  - [ ] Check submission ID `fbc8c519-b2f6-46fb-b3c9-5cd57bee010b`
  - [ ] Note status; document in `_status/acta_propagation.md`

### Patent-attorney consultation (GATE)

- [ ] **Identify retained patent attorney** (firm + primary contact)
- [ ] **Compose attorney email** with three specific questions:
  - [ ] (1) Can the UHA Ω_m derivation procedure be deposited on Zenodo as part of pre-registration BEFORE the CIP non-provisional filing, or must CIP precede?
  - [ ] (2) Is the GPS-replacement architecture analysis (committed at `hubble-tensor/patent_filing/UHA_GPS_REPLACEMENT_ANALYSIS.md`) ready for public release, or does it require CIP protection first?
  - [ ] (3) International filing deadlines (we have ~18 months from US provisional — when is each major jurisdiction's deadline?)
- [ ] Send via secure channel; archive sent message
- [ ] **Wait for written response** — do NOT pre-register until received
- [ ] Save response at `hubble-tensor/patent_filing/attorney_consult_2026.md`
- [ ] If attorney says "CIP must precede pre-registration": adjust the experiment timing
- [ ] If attorney says "Zenodo first OK": proceed to Phase 0

### Infrastructure confirmation

- [ ] **Compute**
  - [ ] Verify ≥ 50 CPU-hours of headroom on local workstation
  - [ ] Confirm storage: ≥ 50 GB free for intermediate results
  - [ ] Test scipy, astropy, healpy installations work
  - [ ] If MCMC needed downstream: install/test cobaya or emcee
- [ ] **Zenodo**
  - [ ] Log into Zenodo with ORCID 0009-0006-5944-1742
  - [ ] Verify upload quota
  - [ ] Confirm CC-BY-4.0 default license set
- [ ] **OSF (Open Science Framework)**
  - [ ] Confirm account active
  - [ ] Pre-create project for L5 experiment (skeleton only; no content yet)
- [ ] **GitHub**
  - [ ] `aybllc/hubble-tensor` repo: confirm private until L5 Phase 0 — opens at pre-registration
  - [ ] Verify Zenodo-GitHub integration enabled per `feedback_zenodo_new_repos.md`

### Foundation-stability gate

- [ ] Confirm at least one of:
  - [ ] RSOS-260797 r4 in advanced review (not early triage)
  - [ ] OR at least one MNRAS companion paper past first round
  - [ ] OR memoir preliminary review concluded with positive signal
- [ ] If none of the above: **hold L5 experiment**; foundation must stabilize first

---

## PHASE 0: Forensics (kill-switch dependent)

### Read primary sources — extract Ω_m

For each: locate paper, read methods section, document specific Ω_m value used and its derivation chain.

- [ ] **Riess et al. (2022) ApJ 934 L7** + supplementary materials
  - [ ] Extract exact Ω_m value used in distance-ladder pipeline
  - [ ] Document derivation: did they use Planck Ω_m as input, or a different cosmology paper?
  - [ ] Note any priors and assumed parameters
  - [ ] Save to `docs/_phase0/forensics_riess.md` with paragraph + page citations
- [ ] **Planck 2018 results VI (cosmological parameters)**
  - [ ] Extract Ω_m posterior central value and 1σ
  - [ ] Identify which parameters are derived vs treated as nuisance
  - [ ] Save to `_phase0/forensics_planck.md`
- [ ] **TRGB (CCHP) — Freedman et al. 2019, 2020**
  - [ ] Extract Ω_m baseline used
  - [ ] Note any Planck or independent input
  - [ ] Save to `_phase0/forensics_trgb.md`
- [ ] **H0LiCOW — Wong et al. 2020**
  - [ ] Extract Ω_m treatment
  - [ ] Save to `_phase0/forensics_h0licow.md`
- [ ] **SBF — Khetan et al. 2021**
  - [ ] Extract Ω_m treatment
  - [ ] Save to `_phase0/forensics_sbf.md`
- [ ] **Maser — Pesce et al. 2020**
  - [ ] Extract Ω_m treatment
  - [ ] Save to `_phase0/forensics_maser.md`

### Read primary sources — positioning chains

For each: document the operational positioning precision and coordinate-frame assumptions.

- [ ] **HST attitude — Bely (1992) + most recent FGS calibration document**
  - [ ] Document FGS precision specs
  - [ ] Document gyroscope / star-tracker chain
  - [ ] Save to `_phase0/positioning_hst.md`
- [ ] **Planck spacecraft — Tauber et al. (2010)**
  - [ ] Document attitude-determination precision
  - [ ] Save to `_phase0/positioning_planck.md`
- [ ] **DESI Mayall telescope position survey**
  - [ ] Locate DESI Collaboration technical paper
  - [ ] Document mm-class geodetic survey methodology
  - [ ] Save to `_phase0/positioning_desi.md`
- [ ] **Gaia DR3 reference frame — Lindegren et al.**
  - [ ] Document µas-class astrometric precision
  - [ ] Note relationship between Gaia frame and ICRS / J2000
  - [ ] Save to `_phase0/positioning_gaia.md`

### Aggregate forensics outputs

- [ ] **Ω_m comparison table** (markdown table)
  - [ ] One row per survey
  - [ ] Columns: survey, Ω_m central, 1σ, derivation chain (1 sentence), citations
  - [ ] Save at `_phase0/omega_m_comparison_table.md`
- [ ] **Positioning-chain precision table**
  - [ ] One row per survey
  - [ ] Columns: survey, position determination method, claimed precision, coordinate frame
  - [ ] Save at `_phase0/positioning_precision_table.md`
- [ ] **Ω_m insertion-point map** per pipeline
  - [ ] Where does Ω_m enter the SH0ES pipeline? (Cepheid distance integral, SN Hubble-flow anchor, etc.)
  - [ ] Where does Ω_m enter the Planck likelihood?
  - [ ] Same for each cross-survey pipeline
  - [ ] Save at `_phase0/omega_m_insertion_map.md`
- [ ] **Coupling check**: are any of the surveys explicitly using a Planck Ω_m prior?
  - [ ] If yes: document the coupling; this changes the substitution-test interpretation
  - [ ] Save at `_phase0/cross_survey_coupling.md`
- [ ] **Compose Phase 0 deliverable**: 5–10 page forensics document
  - [ ] Save at `_phase0/PHASE_0_FORENSICS_REPORT.md`
- [ ] **Internal premise-audit pass**
  - [ ] Re-read deliverable against original sources
  - [ ] Flag any premise smuggling
  - [ ] If found: revise

### KILL SWITCH 1

- [ ] Compute |Ω_m^Riess − Ω_m^Planck|
- [ ] If < 0.005 (within 1σ): **ABORT EXPERIMENT**
  - [ ] Document the negative finding as standalone Zenodo deposit
  - [ ] Title: "Pre-experiment forensic check: SH0ES and Planck Ω_m baselines are statistically identical"
  - [ ] Update master roadmap: L5 branch closed
  - [ ] Pivot to next priority (memoir compliance, CIP filing, etc.)
- [ ] If ≥ 0.005: continue to back-of-envelope

### Quantitative back-of-envelope (KILL SWITCH 2)

- [ ] **Set up the propagation chain**
  - [ ] δr_telescope (coordinate-frame imprecision at telescope position)
  - [ ] → δ_baseline (parallax baseline error)
  - [ ] → δ_parallax (stellar-distance-scale error)
  - [ ] → δ_distance (cosmic distance ladder)
  - [ ] → δH_0
- [ ] **Compute for three δr cases**: 1mm, 1cm, 1m
- [ ] **Compare against ~1.5 km/s/Mpc residual gap**
- [ ] **KILL SWITCH 2 decision**
  - [ ] If no plausible δr produces δH_0 ≥ 1.5 km/s/Mpc: **ABORT**
    - [ ] Document falsification as analytical bound on hypothesis
    - [ ] Standalone Zenodo deposit
  - [ ] If a plausible δr does produce sufficient δH_0: continue
- [ ] Save calculation at `_phase0/back_of_envelope_propagation.md` (single page)

### Pre-registration

- [ ] **Lock methodology v1.0 final**
  - [ ] Phase 0 forensics outputs reviewed and locked
  - [ ] Phase 1–4 methodology specifications locked
  - [ ] Success / failure / abort thresholds locked (quantitative)
  - [ ] Analysis pipeline code skeleton (parameter values filled, no result-dependent branching)
  - [ ] Expected effect-size predictions and confidence intervals
- [ ] **Compose Zenodo deposit metadata**
  - [ ] Title: "Pre-registration: Testing Coordinate-Frame Composition Precision as Source of Residual Hubble Tension After EB Carrier Correction"
  - [ ] Author: Eric D. Martin / ORCID 0009-0006-5944-1742
  - [ ] Affiliation: Independent researcher
  - [ ] License: CC-BY-4.0
  - [ ] Keywords: as listed in master roadmap
  - [ ] Related identifiers: cite priority hash 10.5281/zenodo.19676236, RSOS-260797, MN-26-1117-P, MN-26-1108-L, US 63/902,536
- [ ] **Upload pre-registration deposit**
- [ ] **Verify DOI assigned**
- [ ] **Cross-link to OSF** (post Zenodo DOI to OSF project; post OSF link back into Zenodo deposit description)
- [ ] **NO ANALYSIS RUNS UNTIL DOI EXISTS**

---

## PHASE 1: UHA Ω_m baseline

### Specification and verification

- [ ] **Write methodology spec** at `_phase1/methodology.md`
  - [ ] Which probes (CMB, BAO, SNe — specify exact datasets)
  - [ ] Which weights (uniform / inverse-variance / EB-derived)
  - [ ] Which EB carrier propagation rules (addition for combined likelihoods)
  - [ ] How to handle shared latent factors (sound horizon between CMB and BAO)
- [ ] **Verify nu-algebra implementation**
  - [ ] ξ-normalization function exists and is tested
  - [ ] EB carrier addition implemented per RSOS-260797 r4 axioms
  - [ ] Tests pass on canonical inputs

### Computation

- [ ] **Apply ξ-normalization to each probe likelihood**
  - [ ] CMB (Planck 2018 likelihood)
  - [ ] BAO (DESI DR2 + SDSS BAO consensus)
  - [ ] SNe (Pantheon+ or equivalent public)
  - [ ] Save normalized outputs as sha256-locked CSVs
- [ ] **Apply EB carrier addition rules**
  - [ ] Combine the (e, b) pairs from each probe
  - [ ] Document the combination in `_phase1/eb_combination_log.md`
- [ ] **Extract Ω_m_UHA**
  - [ ] Central value e
  - [ ] EB carrier bound b
  - [ ] Hull [e − b, e + b]
- [ ] **Compare against Phase 0 per-survey values**
  - [ ] Compute differences
  - [ ] Note which surveys' Ω_m falls inside / outside the UHA hull

### Cross-check

- [ ] **Reproduce Δχ² = 279 multi-probe number** from MN-26-1117-P
- [ ] If reproduces: continue
- [ ] If does NOT reproduce: debug
  - [ ] Compare against companion paper draft intermediate results
  - [ ] Identify implementation gap
  - [ ] Resolve before proceeding

### Sensitivity

- [ ] Vary each probe's weight: ±10% in turn
- [ ] Re-extract Ω_m_UHA each time
- [ ] Document stability in `_phase1/sensitivity_analysis.md`

### Deposit

- [ ] **Sha256-lock all intermediate results**
- [ ] **Compose Zenodo Phase 1 deposit**
  - [ ] Title: `UHA-EB-2026-Phase1-OmegaM-Baseline-v1.0`
  - [ ] Include: code, intermediate results, final Ω_m_UHA value, sensitivity table
- [ ] Upload, verify DOI

---

## PHASE 2: Substitution test

### Sanity check

- [ ] **Reproduce Riess et al. (2022) H_0 = 73.04 ± 1.04 km/s/Mpc**
  - [ ] Use their published pipeline and fiducial parameters
  - [ ] Confirm H_0 reproduces within statistical tolerance
  - [ ] If not: debug; do not proceed

### Identify insertion points

- [ ] **Document each Ω_m insertion point in SH0ES pipeline**
  - [ ] Cepheid distance integral
  - [ ] SN Hubble-flow anchor
  - [ ] Any others
  - [ ] Save at `_phase2/sh0es_insertion_points.md`

### Substitution: SH0ES

- [ ] **Substitute Ω_m_UHA at each insertion point**
- [ ] **Compute H_0^SH0ES_UHA**
- [ ] **Apply EB carrier propagation** to derive bound
- [ ] **Document result** at `_phase2/sh0es_uha_corrected.md`

### Substitution: Planck

- [ ] **Substitute Ω_m_UHA into Planck likelihood chain**
- [ ] **Re-derive H_0^Planck_UHA**
- [ ] **Apply EB carrier propagation**
- [ ] **Document at `_phase2/planck_uha_corrected.md`**

### Test statistic

- [ ] **Compute signed difference Δ = H_0^SH0ES_UHA − H_0^Planck_UHA**
- [ ] **Apply EB carrier hull on Δ**
- [ ] **Test success criterion: |Δ| / σ_Δ < 0.5?**
- [ ] **Record outcome**: success / partial / falsification
  - [ ] If success: continue to Phase 3 with confidence
  - [ ] If partial: continue but with revised expectations for Phase 3
  - [ ] If falsification: document, stop or proceed only with weakened claim

### Visualization and deposit

- [ ] **Plot pre-substitution and post-substitution H_0 distributions** with EB carrier hulls
- [ ] **Sha256-lock**
- [ ] **Zenodo Phase 2 deposit**: `UHA-EB-2026-Phase2-Substitution-v1.0`

---

## PHASE 3: Cross-survey validation

### For each independent local H_0 measurement

- [ ] **H0LiCOW (time-delay cosmography)**
  - [ ] Locate public pipeline / code
  - [ ] Apply Ω_m_UHA substitution
  - [ ] Compute H_0^H0LiCOW_UHA
  - [ ] Document at `_phase3/h0licow_uha.md`
- [ ] **TRGB (CCHP)**
  - [ ] Locate public pipeline
  - [ ] Apply substitution
  - [ ] Compute H_0^TRGB_UHA
  - [ ] Document
- [ ] **SBF**
  - [ ] Locate pipeline
  - [ ] Apply substitution
  - [ ] Compute H_0^SBF_UHA
  - [ ] Document
- [ ] **Masers**
  - [ ] Locate pipeline
  - [ ] Apply substitution
  - [ ] Compute H_0^Maser_UHA
  - [ ] Document

### Aggregation

- [ ] **Compute scatter across all UHA-corrected local H_0 values**
- [ ] **Compute scatter across pre-substitution local H_0 values**
- [ ] **Test success criterion: scatter reduction ≥ factor of 2?**
- [ ] **Record outcome**

### Deposit

- [ ] Sha256-lock
- [ ] Zenodo Phase 3 deposit: `UHA-EB-2026-Phase3-CrossSurvey-v1.0`

---

## PHASE 4: Pre-Euclid lock

### Forward propagation

- [ ] **Forward-propagate UHA-corrected parameter posteriors** to predict DR1 BAO Ω_m
- [ ] **Forward-propagate** to predict DR1-derived H_0 under standard reduction

### Lock

- [ ] **Lock prediction with EB carrier hull**: Ω_m^Euclid_predicted = X.XXX ± Y.YYY
- [ ] **Lock prediction**: H_0^DR1_predicted = Z.ZZ ± W.WW (UHA framework) vs Z'.ZZ ± W'.WW (standard ΛCDM)
- [ ] **Document falsification criteria** for each locked prediction
  - [ ] What outcome falsifies UHA framework?
  - [ ] What outcome confirms?
  - [ ] What outcome is inconclusive?
- [ ] Save at `_phase4/locked_predictions.md`

### Deposit (must precede DR1 release)

- [ ] **Compose Zenodo pre-Euclid deposit**: `UHA-EB-2026-Phase4-EuclidLock-v1.0`
- [ ] Include locked predictions, falsification criteria, full methodology
- [ ] Upload before October 2026
- [ ] Verify DOI assigned and timestamp stamped

---

## CROSS-CUTTING (ongoing throughout all phases)

- [ ] After each phase: update `MEMORY.md` with anchor information
- [ ] Append progress notes to `notes/progress_2026.md` per checkpoint
- [ ] Citation hygiene: every Δχ² = 279 reference notes "from MN-26-1117-P submitted manuscript, not peer-reviewed"
- [ ] Premise audit at end of each phase against primary sources
- [ ] Cross-link each Zenodo deposit to RSOS-260797 + US 63/902,536 + 10.5281/zenodo.19676236

---

## FOUNDATION WORK IN PARALLEL (not blocking L5)

### Memoir Phase 2 (B1: memo-l.cls)

- [ ] Wait for AMS reply on `_provenance/memo_l_request_email.txt`
- [ ] When received: download memo-l.cls
- [ ] Rebuild `eb_carrier_memoirs.tex` with memo-l class
- [ ] Re-verify 162-page compile
- [ ] Re-verify 0 undefined references
- [ ] Re-verify natbib clean
- [ ] Update `_provenance/memoir_compliance_phase2_log.md`
- [ ] Recompile anonymized PDF
- [ ] If acceptance reached: prepare source bundle for AMS post-acceptance submission

### Companion papers

- [ ] **MN-26-1108-L revise & resubmit**
  - [ ] Pull reviewer comments from ScholarOne
  - [ ] List items: addressed / unaddressed / disputed
  - [ ] Address each unaddressed item
  - [ ] Compose response-to-reviewers letter
  - [ ] Resubmit; archive resubmission record
- [ ] **MN-26-1117-P (Δχ² = 279)**
  - [ ] Track review progress
  - [ ] If reviews come back: respond per standard
- [ ] **MN-26-1198-P (Pantheon+)**
  - [ ] Track review progress
- [ ] **MN-26-1171-P (SH0ES distance ladder)**
  - [ ] Track review progress

### Resurgence paper (Tier 1)

- [ ] **Polish pass on `martin_2026_off_cycle_bound_width_v01.md`**
  - [ ] Cross-check Phase 3 prediction values against Shahan Fig 2 readings
  - [ ] Tighten abstract
  - [ ] Verify all DOI links resolve
  - [ ] Apply Jeric voice review (short sentences, no compounds)
- [ ] **arXiv preprint preparation**
  - [ ] Convert to LaTeX (template: standard JEAB or BeProc style)
  - [ ] Submit to arXiv (q-bio.NC primary, q-bio.PE cross-list)
  - [ ] Verify endorsement if needed
  - [ ] Note arXiv ID
- [ ] **Journal submission**
  - [ ] Decide: JEAB or *Behavioural Processes*
  - [ ] Compose cover letter
  - [ ] Submit
  - [ ] Track review progress

### CIP non-provisional drafting (deadline-gated)

- [ ] Review existing `hubble-tensor/patent_filing/PATENT_AMENDMENTS_CIP.md`
- [ ] Determine which UHA-related material needs CIP protection
  - [ ] UHA Ω_m derivation procedure (pending attorney advice)
  - [ ] GPS-replacement architecture (per `UHA_GPS_REPLACEMENT_ANALYSIS.md`)
  - [ ] Mode-switch architecture (Section F)
  - [ ] Adaptive bit depth (claims 41–42)
- [ ] Draft new claims as needed
- [ ] Compose CIP filing package
  - [ ] Specifications
  - [ ] Drawings (regenerate from `generate_cip_figures.py` if needed)
  - [ ] Claims
  - [ ] Cover letter
- [ ] Engage patent attorney for filing review
- [ ] File with USPTO
- [ ] Archive filing receipts

### UHA-replaces-GPS brief (post-CIP)

- [ ] After CIP filed: assess whether GPS-replacement brief is ready for public release
- [ ] If ready: prepare public release version
- [ ] Distribute through standards-body conversation channels (IEEE, ITU, IAU)

---

## DISCIPLINE CHECKLIST (run weekly)

- [ ] Re-read `MEMORY.md` for active rules
- [ ] Review last week's progress against this checklist
- [ ] Identify any premise smuggling in recent work
- [ ] Identify any salami-slicing temptation in recent drafts
- [ ] Verify no Δχ² = 279 reference is missing the "submitted not peer-reviewed" qualifier
- [ ] Verify no AI-instance agreement is being treated as validation
- [ ] Verify no methodology change has been made without pre-registration amendment

---

## KILL-SWITCH SUMMARY (review before each phase)

| Switch | Trigger | Branch outcome |
|---|---|---|
| K1 | RSOS-260797 r4 rejected | Foundation continues independently; alternative open-access venue search |
| K2 | Δχ² = 279 fails to reproduce in Phase 1 | MN-26-1117-P withdrawn or revised; L5 paused until reproduction achieved |
| K3 | Phase 0 forensics: |Ω_m^Riess − Ω_m^Planck| < 0.005 | L5 ABORTS cleanly; standalone negative-result deposit |
| K4 | Back-of-envelope: no plausible δr produces sufficient δH_0 | L5 ABORTS; analytical-bound deposit |
| K5 | Phase 2: Ω_m_UHA substitution produces no shift | L5 falsified; standalone negative-result paper |
| K6 | Phase 2: substitution shifts H_0 in wrong direction | L5 falsified; pre-registration protects |
| K7 | Phase 3: scatter doesn't reduce ≥ 2x | L5 partial; weakened claim |
| K8 | Euclid DR1 contradicts locked predictions | Predictions falsified; falsification record canonical |
| K9 | Patent attorney advises against pre-registration | L5 deposit timing adjusted; possible re-scoping |

---

*End of checklist. Update as items complete. Re-export to roadmap when phase boundaries are crossed.*
