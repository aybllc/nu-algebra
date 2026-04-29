# Pre-Compile Patch for the Two Compiled Protocols

**Status:** Working note. Pre-staged before Eric's compiled protocols land. When the protocols arrive, fold these items in or document why each was rejected.

**Date:** 2026-04-28
**Scope:** Items that are load-bearing for protocol execution and are not yet in either v0.1 of the canonical checklists.

**Discipline:** Only items that change protocol outcomes if missing. No "nice to have." No "comprehensive coverage" padding.

---

## Cross-protocol items (apply to both)

### P-1. Standing-rules block at §0 of each compiled protocol

**Why load-bearing:** Without an inline rules block, mid-execution drift back into yes-manning is statistically inevitable. The 1st CHECKLIST.md has §B; the 2nd PDF doesn't.

**What to insert:** Top-of-document block referencing:
- `feedback_others_contradict_not_prove.md`
- `feedback_no_input_uncertainty_rumination.md`
- `feedback_zenodo_publish_gate.md`
- `feedback_submission_print_gate.md`
- `feedback_overreach_narrow_dont_defend.md`
- `feedback_show_failures_publicly.md`
- `feedback_register_discipline_formal_vs_motivational.md`

### P-2. Cross-protocol dependency map

**Why load-bearing:** Phase 4 of 2nd (cosmology error-propagation) overlaps with Phase 0–3 of 1st (residual-3% experiment). Without an explicit deferral, the same analysis runs twice with different framing.

**What to insert:** In the 2nd, before Phase 4 begins:
> Phase 4 of this protocol is canonically executed under the 1st (Research/IP) checklist's L5 residual-3% experiment design (`hubble-tensor/research/HUBBLE_RESIDUAL_3PCT_EXPERIMENT_DESIGN_2026-04-28.md` commit 3871870). This protocol's Phase 4 references the 1st's Phase 0–3 deliverables; it does not re-run the analysis. If 1st Phase 0 fires KS1, this Phase 4 also halts.

### P-3. Halt-propagation wiring across protocols

**Why load-bearing:** When a kill switch fires in one protocol, the other doesn't automatically know. Without explicit cascading, a protocol can continue running on a dead premise.

**What to insert:** Each kill switch in each protocol gets a cascade clause:
- 1st KS1 (identical Ω_m) → halts 2nd Phase 4
- 1st KS2 (back-of-envelope falsifies propagation) → halts 2nd Phase 4
- 2nd G1 (frame-stack source audit fails) → halts 1st Phase 0 documentation requirement (use whatever's verifiable; downgrade claims)
- 2nd G2 (encoding round-trip fails) → halts 1st Phase 1 (UHA Ω_m baseline can't be computed without round-trip integrity)

### P-4. Failure-publication template pre-locked before pre-registration

**Why load-bearing:** "Negative result still valuable" is a vague commitment. Without a pre-locked venue + format, post-hoc rescue is structurally possible (e.g., re-frame the negative result as "exploratory" and never deposit it).

**What to insert:** For each protocol, a "negative-result deposit template" section specifying:
- Venue (e.g., MNRAS for cosmology negative; Zenodo standalone for methodological null)
- Title format (e.g., "Pre-registration outcome: [hypothesis] is not supported by [test]")
- Length (~3000 words target)
- Required content (methodology recap, kill-switch trigger, data, code, sha256)
- Deposit timeline (within 14 days of kill-switch firing; no extensions)

This goes IN the pre-registration deposit so review reviewers can verify the commitment.

---

## 1st-checklist-specific (Research/IP)

### P-5. Phase 0 primary sources cited by DOI per item

**Why load-bearing:** Forensic extraction needs to be auditable. "Riess et al. 2022" without DOI means an auditor re-finds the paper.

**Insertions:**
- Riess 2022 ApJ 934 L7 → `10.3847/2041-8213/ac5c5b`
- Planck 2018 results VI → `10.1051/0004-6361/201833910`
- Freedman 2019 (TRGB) → `10.3847/1538-4357/ab2f73`
- Wong 2020 (H0LiCOW) → `10.1093/mnras/stz3094`
- Khetan 2021 (SBF) → `10.1051/0004-6361/202039196`
- Pesce 2020 (masers) → `10.3847/2041-8213/ab9eb0`

### P-6. Kill-switch threshold |ΔΩ_m| < 0.005 sourced explicitly

**Why load-bearing:** The threshold floats without justification otherwise. 0.005 is approximately 1σ on Planck (Ω_m = 0.3153 ± 0.0073).

**What to insert:** Beside the threshold line:
> Threshold derives from 1σ on Planck 2018 Ω_m posterior central value 0.3153 with stated 1σ ≈ 0.0073 (Planck 2018 results VI, [10.1051/0004-6361/201833910](https://doi.org/10.1051/0004-6361/201833910)). Below this, surveys are statistically indistinguishable on Ω_m and the residual cannot be attributed to Ω_m disagreement.

### P-7. Δχ² = 279 per-occurrence qualifier

**Why load-bearing:** If only the cross-cutting rules section says "submitted not peer-reviewed," the qualifier gets lost when individual phase steps are quoted out of context.

**What to insert:** Every literal mention of the number gets the inline qualifier:
> Δχ² = 279 (from MN-26-1117-P submitted manuscript, not peer-reviewed)

Apply globally across the 1st CHECKLIST.md by sed pass before pre-registration deposit.

---

## 2nd-checklist-specific (Space-Frame/PNT)

### P-8. Drift-to-marketing-language audit step in compilation phase

**Why load-bearing:** The 2nd already has Section 2 "Claim Discipline" but doesn't have a final-pass grep step. Marketing phrases creep into prose during integration.

**What to insert:** Add as final compilation step before deposit:
> Run grep against banned phrases: "revolutionary", "Nobel", "100% explained", "completely solves", "definitively", "groundbreaking", "paradigm shift", "Einstein-level", "textbook-level". Any match is a fail; rewrite or remove.

### P-9. Phase 5 SSA TLE source license compliance

**Why load-bearing:** Real legal/redistribution issue. Space-Track.org TOS prohibits redistribution; CelesTrak permits it under their stated terms.

**What to insert:** In Phase 5 deliverable specification:
> TLE source must be CelesTrak (permits redistribution under stated terms) or equivalent open source. Space-Track.org data is NOT redistributable under their TOS and cannot enter a public Zenodo deposit. Source-of-record locked in pre-registration.

### P-10. Phase 8 minimum viable demo dataset locked

**Why load-bearing:** Without a specific snapshot, the demo isn't reproducible by anyone else.

**What to insert:** In §8 step 1:
> Pull public ephemeris/state data from `celestrak.org/NORAD/elements/active.txt` snapshot at locked timestamp recorded in pre-registration deposit; sha256 the snapshot at download; archive sha256 in deposit.

---

## Provenance / cross-reference layer

### P-11. Originating-protocol tag in commit messages

**Why load-bearing:** When commits across the two protocols accumulate, future sessions won't know which protocol an artifact belongs to without the tag.

**What to insert:** Convention in both protocols:
> Commit message convention: prefix with `[1st-PhaseN]` or `[2nd-PhaseN]` (e.g., `[2nd-Phase0] frame-stack forensic audit complete`). Same for Zenodo deposit titles.

This replaces the originally-suggested redundant sha256+phase+protocol bullet — the tag carries the same information without restating the existing provenance discipline at §0.2 of the 1st checklist.

---

## Application sequence when protocols land

1. Read both compiled protocols end-to-end without interrupting.
2. For each P-1 through P-11, check if already present (Eric or his synthesizer may have included some).
3. For items not present: insert at the indicated location.
4. For items present in different form: reconcile (defer to Eric's wording unless it's a technical correction).
5. Run a final premise-audit pass after integration (one more grep for marketing language, one more check that all DOIs resolve, one more check that kill-switch cascades close).
6. Commit the integrated protocols.
7. Update master roadmap §8b to point at the integrated versions.

---

## Items that were considered and dropped (don't re-suggest)

- **Sole-author re-lock at §0.** Already covered by `feedback_no_coauthor.md` + commit-message convention. Re-stating per protocol is padding.
- **OGC (Open Geospatial Consortium) in 2nd Track A.** Terrestrial WGS84 scope; this protocol's primary axis is celestial/space frames. Out of scope.
- **NASA Artemis architecture anchor in 2nd Phase 6.** Phase 6 is a concept demo with explicit "synthetic" framing; anchoring to Artemis adds suggestion of operational claim that isn't being made.
- **Separate sha256 + phase + protocol provenance bullet.** Redundant with P-11; existing 1st checklist §0.2 covers sha256 + commit hash already.

---

*End of pre-compile patch document. To be applied when protocols land.*
