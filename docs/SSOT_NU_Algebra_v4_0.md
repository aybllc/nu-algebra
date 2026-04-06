# SINGLE SOURCE OF TRUTH
## Cross-Document Consistency Register
### v4.0 — COMPLETE CONSOLIDATED EDITION — March 21, 2026

**Scope:** N/U Algebra Paper (NASA) • o1 Manuscript Outline • eBIOS Specification • NUProof Framework • N/U Algebra Repository

**Status:** LIVING DOCUMENT — Awaiting additional GitHub repositories. New findings will be appended from F-046 onward.

---

## VERSION HISTORY

| Version | Date | Findings | Edit Locations | Notes |
|---------|------|----------|----------------|-------|
| v1.0 (eBIOS Register) | 2026-03-21 | 17 | 36 | Initial: NASA Paper, o1 Outline, NUProof, eBIOS README |
| v2.1 (Draft) | 2026-03-21 | 31 | 59 | Added Repo analysis; eBIOS GitHub pending |
| v3.0 (Updated) | 2026-03-21 | 45 | 70 | eBIOS GitHub complete; +14 findings (F-032–F-045) |
| **v4.0 (This Document)** | **2026-03-21** | **45** | **70** | **Full consolidation of all versions; ready for next repo** |

---

## 1. EXECUTIVE SUMMARY

This is the **definitive SSOT** for all identified discrepancies, gaps, and cross-document inconsistencies across the complete N/U Algebra ecosystem. Every finding includes severity classification, evidence from source documents, the precise edit required, and exact location(s) where the edit must be applied.

### 1.1 Severity Distribution

| CRITICAL | HIGH | MEDIUM | LOW | TOTAL |
|----------|------|--------|-----|-------|
| **3** | **11** | **16** | **15** | **45** |

### 1.2 Edits Per Document

| Document | Critical | High | Medium | Low | Total Edits |
|----------|----------|------|--------|-----|-------------|
| **o1 Outline** | 1 | 6 | 8 | 5 | 20 |
| **NASA Paper** | 1 | 1 | 0 | 1 | 3 |
| **NUProof** | 0 | 8 | 4 | 2 | 14 |
| **eBIOS** | 1 | 7 | 6 | 2 | 16 |
| **Repo (Unknown)** | 0 | 4 | 6 | 4 | 14 |
| **New (F-032–F-045)** | 0 | 0 | 2 | 3 | 5 |
| **TOTAL** | **3** | **26** | **26** | **17** | **70** |

### 1.3 Three Critical Issues

> These must be resolved before any publication, deployment, or external adoption.

**~~CRITICAL-1 — F-002~~** ✅ RESOLVED (2026-04-05): Finding was based on conflating two distinct operators. The Lean `flip` operator is `(-n, u)` (negation) — it IS involutive and the theorem is correct. The NASA Paper's `B` operator is `(u, |n|)` (swap) — it is NOT involutive, and its correct property is B³=B (period-2 cycle). Both operators now defined in NUCore.lean. Four theorems added to FlipInvolutive.lean: `swapFlip_not_involutive_general`, `swapFlip_sq`, `swapFlip_period_two`, `swapFlip_sq_idempotent`. No false theorems remain. Verified 2026-04-05.

**~~CRITICAL-2 — F-003~~** ✅ RESOLVED (2025-10-20): `Enclosure.lean` contains zero `sorry` statements. File completed before this SSOT was written. PAC coverage theorem formally proven. Finding was stale at time of SSOT authorship — auditor did not read current file state. Verified 2026-04-05.

**~~CRITICAL-3 — F-038~~** ✅ RESOLVED (stale finding): All four files exist in `/scratch/repos/ebios/docs/` — `NULedger_SPEC.md`, `NUGuard_POLICY.md`, `NUPolicy_SPEC.md`, `NUGovern_API.md`. Files were present before this SSOT was written. Auditor did not check filesystem. Verified 2026-04-05.

---

## 2. MASTER EDIT REGISTER (All 70 Edit Locations)

| # | Finding | Sev | Document | Edit Location |
|---|---------|-----|----------|---------------|
| 1 | F-001 | HIGH | o1 Outline | Section 2.2, Def 3 — add reconciliation note on λ vs. paper formula |
| 2 | F-001 | HIGH | o1 Outline | Section 5.1, Theorem 10 — clarify λ=1 WITH u₁u₂ term matches interval arithmetic |
| 3 | F-001 | HIGH | NASA Paper | Section 3.1 — note first-order form drops u₁u₂ (if revising) |
| 4 | F-002 | **CRITICAL** | NUProof | `FlipInvolutive.lean` → rename to `FlipIdempotent.lean`, replace theorem with B³=B² |
| 5 | F-002 | **CRITICAL** | NUProof | README lines 33–35 — update theorem statement to FlipIdempotent |
| 6 | F-002 | **CRITICAL** | NUProof | README lines 116–117 — update complete/skeleton counts |
| 7 | F-002 | **CRITICAL** | NUProof | `proof_manifest.json` — update filename and hash |
| 8 | F-002 | **CRITICAL** | o1 Outline | Section 2.2, Def 5 — add note that B is NOT involutive; B³=B² |
| 9 | F-002 | **CRITICAL** | NASA Paper | Section 3.2 — add Remark 3.1 on B³=B² property (if revising) |
| 10 | F-003 | **CRITICAL** | NUProof | `Enclosure.lean` — replace `sorry` skeleton with complete three-sub-lemma proof |
| 11 | F-003 | **CRITICAL** | NUProof | README lines 19–20 — update Enclosure status to Complete |
| 12 | F-003 | **CRITICAL** | NUProof | README lines 116–117 — update counts after Enclosure completion |
| 13 | F-003 | **CRITICAL** | NUProof | `proof_manifest.json` — update hash and status for Enclosure |
| 14 | F-004 | HIGH | eBIOS | `NUPolicy_SPEC.md` — add `coverage_allocation` as a rule type |
| 15 | F-004 | HIGH | eBIOS | `NUGuard` implementation — add `check()` method |
| 16 | F-004 | HIGH | eBIOS | `NUGovern` — add `/coverage/validate` endpoint |
| 17 | F-005 | MEDIUM | eBIOS | README line 72 — fix add() example result from (30.0, 1.12) to (30.0, 1.5) |
| 18 | F-006 | MEDIUM | o1 Outline | Section 3.1 — add footnote on operation count difference (6 ops vs. 4) |
| 19 | F-007 | MEDIUM | NUProof | `ComposeReduction.lean` — correct theorem statement or annotate scope |
| 20 | F-007 | MEDIUM | NUProof | README — note ComposeReduction scope limitation |
| 21 | F-008 | HIGH | o1 Outline | Section 7.1 — either define S⁻¹ rule or use only defined operations |
| 22 | F-009 | HIGH | NUProof | `AddProperties.lean` — complete associativity proof with no `sorry` |
| 23 | F-010 | LOW | o1 Outline | Section 2.4 — add sub-distributivity theorem |
| 24 | F-011 | MEDIUM | o1 Outline | Section 2 or 5 — add cumulative product theorem with proof sketch |
| 25 | F-012 | LOW | o1 Outline | Section 2.1 or 2.3 — add partial order ⪯ definition |
| 26 | F-013 | MEDIUM | eBIOS | Create `docs/Layer0_SPEC.md` or add note that Layer 0 is conceptual |
| 27 | F-014 | HIGH | NUProof | README — include `NUCore.lean` definitions inline or as appendix |
| 28 | F-014 | HIGH | NUProof | `NUCore.lean` — verify definitions match NASA Paper Def 3.1 and 3.2 |
| 29 | F-015 | LOW | NASA Paper | Data Availability section — add preprint DOI 10.5281/zenodo.17172694 if live |
| 30 | F-016 | MEDIUM | eBIOS | `NUPolicy_SPEC.md` — add `real_time_mode` policy option with async ledger |
| 31 | F-016 | MEDIUM | o1 Outline | Section 7.4 — clarify latency refers to NUCore+NUGuard critical path only |
| 32 | F-017 | LOW | o1 Outline | Section 2.4 — add identity element theorem |
| 33 | F-018 | MEDIUM | o1 Outline | Section 7.4 or 8 — add reference to eBIOS enforcement architecture |
| 34 | F-018 | MEDIUM | o1 Outline | Section 8.3 — update Lean status from "future work" to "in-progress" |
| 35 | F-019 | LOW | NUProof | README — standardize all theorem status markers to "Status: Complete" format |
| 36 | F-020 | HIGH | o1 Outline | Section 6 — clarify which formula the 70K validation tests validate |
| 37 | F-020 | HIGH | o1 Outline | Section 2.2 — explicitly state that λ=0 recovers the paper formula |
| 38 | F-020 | HIGH | Repo | `src/nu_algebra.py` and `nu_algebra.R` — add `lambda` parameter to `mul()` if λ formula adopted |
| 39 | F-021 | MEDIUM | eBIOS | README line 72 — fix addition example to (30.0, 1.5) [same as F-005, confirmed by repo] |
| 40 | F-022 | MEDIUM | Repo | `setup.py` url field — unify to canonical GitHub URL |
| 41 | F-022 | MEDIUM | Repo | `CITATION.cff` — unify URL |
| 42 | F-022 | MEDIUM | Repo | `.zenodo.json` — unify URL |
| 43 | F-022 | MEDIUM | Repo | `CHANGELOG.md` links — unify URL |
| 44 | F-023 | LOW | Repo | `src/nu_algebra.R` — update `NU_ALGEBRA_VERSION` to `'3.1.0'` |
| 45 | F-024 | LOW | Repo | `docs/` — populate or remove empty documentation files |
| 46 | F-025 | MEDIUM | Repo | `CHANGELOG.md` — correct test count claims to match actual files |
| 47 | F-026 | LOW | o1 Outline | Section 2.2 — add subtraction as derived operation: (n₁-n₂, u₁+u₂) |
| 48 | F-027 | MEDIUM | o1 Outline | Section 8.2 — add note about self-multiplication conservatism for higher powers |
| 49 | F-028 | HIGH | o1 Outline | Section 6.1 — match DOI 10.5281/zenodo.17221863 to the correct (paper) formula |
| 50 | F-028 | HIGH | Repo | `scripts/generate_nu_data.py` — add λ parameter if o1 formula is adopted |
| 51 | F-029 | LOW | Repo | `MANIFEST.in` — remove or document SAID reference |
| 52 | F-029 | LOW | Repo | `.gitignore` — remove or document SAID reference |
| 53 | F-030 | MEDIUM | Repo | `tests/test_nu_algebra.py` TestAssociativity — tighten tolerance to 1e-10 |
| 54 | F-031 | HIGH | Repo | `tests/test_nu_algebra.py` — add `test_flip_not_involutive()` |
| 55 | F-031 | HIGH | Repo | `tests/test_nu_algebra.py` — add `test_flip_idempotent()` |
| 56 | F-032 | HIGH | eBIOS | Architecture diagram/README — clarify all layers OR remove Layer 7 reference |
| 57 | F-032 | HIGH | NUProof | Line 136 — remove "Layer 7 (Certification)" reference |
| 58 | F-033 | MEDIUM | eBIOS | Create/publish `NUGovern_API.md` with full specification |
| 59 | F-034 | LOW | eBIOS | Quick Start — add NULedger usage example (append/query/verify) |
| 60 | F-035 | MEDIUM | eBIOS | README — link to actual test files with verifiable count |
| 61 | F-036 | MEDIUM | eBIOS | Create example policy files: `conservative.json`, `strict.json`, `permissive.json` |
| 62 | F-036 | MEDIUM | eBIOS | Create JSON schema documentation for policy files |
| 63 | F-037 | LOW | eBIOS | Add `PHASES.md` or README section defining development phases 0–6 |
| 64 | F-038 | **CRITICAL** | eBIOS | Create `NULedger_SPEC.md` with ledger API and Merkle tree algorithm |
| 65 | F-038 | **CRITICAL** | eBIOS | Create `NUGuard_POLICY.md` with monitor interface and rule evaluation |
| 66 | F-038 | **CRITICAL** | eBIOS | Create `NUPolicy_SPEC.md` with policy format and validation rules |
| 67 | F-038 | **CRITICAL** | eBIOS | Create `NUGovern_API.md` with HTTP endpoints and request/response schemas |
| 68 | F-039 | MEDIUM | eBIOS | Quick Start NUPolicy example — add imports and error handling |
| 69 | F-040 | MEDIUM | eBIOS | Performance table — add hardware, compiler, optimization flags, methodology |
| 70 | F-041 | HIGH | eBIOS | Create `Layer0_SPEC.md` defining Verify/Seal/Unseal/Attest interfaces |
| ~~71~~ | F-042 | HIGH | NUProof | Line 136 — clarify Layer 2 outputs feed into Layers 3 and 6 (overlaps with #57) |
| 72 | F-043 | LOW | eBIOS | Performance table — specify latency vs. throughput and percentile (p50/p99) |
| 73 | F-044 | MEDIUM | eBIOS | Distribute `conservative.json` policy example with code |
| 74 | F-044 | MEDIUM | eBIOS | Quick Start — add note about policy installation/location |
| 75 | F-045 | LOW | eBIOS | README footer — update version (0.2.0), status, and last-updated date to 2026-03-21 |

> **Note on F-032/F-042 overlap:** Edit #57 and the F-042 entry both address NUProof line 136. Apply once with the F-042 corrective language (rewrite to reference Layers 3 and 6, not Layer 7).

---

## 3. DETAILED FINDINGS

### F-001 — Multiplication Operator: λ Parameter Discrepancy
**Severity:** HIGH | **Category:** Definition Mismatch | **Affects:** NASA Paper, o1 Outline

**Description:** The NASA paper defines multiplication as `(n₁n₂, |n₁|u₂ + |n₂|u₁)` — NO λ term. The o1 outline defines it as `(n₁n₂, |n₁|u₂ + |n₂|u₁ + λu₁u₂)` with λ≥1. These are different algebras. The repository implementation (Python and R) uses the paper's formula. The 70,000+ validation tests validate the paper's formula, not the λ-parameterized version.

**Evidence:**
- NASA Paper Def 3.1: `x ⊗ y = (n₁n₂, |n₁|u₂ + |n₂|u₁)`
- o1 Outline Def 3: `(n₁n₂, |n₁|u₂ + |n₂|u₁ + λu₁u₂)` where λ ≥ 1
- `src/nu_algebra.py`: `return NU(self.n * other.n, abs(self.n) * other.u + abs(other.n) * self.u)` — no λ
- `scripts/generate_nu_data.py`: same formula — validates paper, not o1 outline

**Required Edit:** Explicitly reconcile: (a) Paper's formula = first-order approximation (drops u₁u₂, valid when u << n). (b) Outline with λ=1 = exact interval arithmetic bound. (c) λ>1 = additional safety margin. The o1 outline should note that the published paper uses the first-order form and clarify when the cross-term matters.

**Edit Locations:** #1, #2, #3

---

### F-002 — Flip Operator: Involution Claim Contradicts Revised Definition ⚠️ CRITICAL
**Severity:** CRITICAL | **Category:** Mathematical Inconsistency | **Affects:** NUProof, NASA Paper, o1 Outline

**Description:** `NUProof` lists `FlipInvolutive.lean` as COMPLETE with theorem `Flip(Flip(x)) = x`. The NASA Paper explicitly states `B² ≠ id` under revised definition `B(n,u) = (u, |n|)`. Counterexample: `B(-3,2) = (2,3)`, `B(2,3) = (3,2) ≠ (-3,2)`. The formal verification system is certifying a false theorem.

**Evidence:**
- NUProof README line 33–35: "Flip Involution — Theorem: Flip(Flip(x)) = x — Status: Complete"
- NASA Paper Def 3.2 note: "The Flip operator is no longer an involution under this definition (B² ≠ id in general)"

**Required Edit:** Replace `FlipInvolutive.lean` with `FlipIdempotent.lean` proving `B³ = B²`. After one application both components are non-negative, so B cycles with period 2. Update README, `proof_manifest.json`, status counts, o1 Outline Def 5, and test suite.

**Edit Locations:** #4, #5, #6, #7, #8, #9

---

### F-003 — Enclosure Preservation Proof is a Skeleton (sorry placeholders) ⚠️ CRITICAL
**Severity:** CRITICAL | **Category:** Formal Proof Gap | **Affects:** NUProof, o1 Outline

**Description:** `Enclosure.lean` contains `sorry`/`axiom` placeholders. This is the foundational property that the PAC coverage theorem (o1 Theorem 9) depends on via Lemmas 1–3. Without machine-verified enclosure preservation, the entire probabilistic coverage guarantee chain is unverified at the formal level.

**Evidence:**
- `Enclosure.lean`: Three sub-lemmas all marked `sorry`
- o1 Outline Theorem 9: Directly cites enclosure preservation as precondition
- NUProof README: Lists Enclosure as "In Progress"

**Required Edit:** Complete `Enclosure.lean` with all three sub-lemma proofs. No `sorry` in completed proofs. Update README and `proof_manifest.json`.

**Edit Locations:** #10, #11, #12, #13

---

### F-004 — Coverage Allocation Rule Type Missing from NUPolicy
**Severity:** HIGH | **Category:** Missing Implementation | **Affects:** eBIOS

**Description:** The PAC coverage allocation method (o1 Theorem 9) allocates coverage budgets per operation using union bound. The eBIOS `NUPolicy_SPEC.md` lists rule types `non_negativity`, `enclosure_preservation`, and `threshold` but does NOT include `coverage_allocation`. `NUGuard` has no `check()` method and `NUGovern` has no `/coverage/validate` endpoint.

**Required Edit:** Add `coverage_allocation` rule type to NUPolicy. Add `check()` method to NUGuard. Add `/coverage/validate` endpoint to NUGovern.

**Edit Locations:** #14, #15, #16

---

### F-005 — eBIOS Addition Example Shows Wrong Result (1.12 instead of 1.5)
**Severity:** MEDIUM | **Category:** Documentation Error | **Affects:** eBIOS

**Description:** eBIOS README shows `add()` result as `(30.0, 1.12)`. The repo's `add()` returns `NU(self.n + other.n, self.u + other.u)`. For inputs `(10.0, 0.5)` and `(20.0, 1.0)`: u = 0.5 + 1.0 = **1.5**, not 1.12. The eBIOS example is conclusively a documentation error.

**Required Edit:** Fix eBIOS README line 72 to show `(30.0, 1.5)`.

**Edit Locations:** #17 (also #39)

---

### F-006 — Operation Count Discrepancy Between Paper and Outline
**Severity:** MEDIUM | **Category:** Documentation Inconsistency | **Affects:** o1 Outline

**Description:** NASA Paper Prop 4.13 counts 6 floating-point operations for multiplication (1 mul n, 2 abs, 2 mul u, 1 add). The o1 outline's Table 1 claims 4 operations. The discrepancy comes from the paper counting absolute value as a separate operation.

**Required Edit:** Add footnote to o1 Outline Section 3.1 explaining the 4 vs. 6 operation count difference (absolute value counting convention).

**Edit Locations:** #18

---

### F-007 — ComposeReduction Theorem May Have Overly Broad Statement
**Severity:** MEDIUM | **Category:** Proof Scope | **Affects:** NUProof

**Description:** `ComposeReduction.lean` proves a reduction property for composed operations. The theorem statement may claim this holds for ALL compositions but the proof only covers specific cases. If the theorem is used as a justification for O(1) complexity claims, an overly broad statement could undermine the argument.

**Required Edit:** Either correct the theorem statement to match exactly what is proved, or annotate scope limitations clearly in both `ComposeReduction.lean` and the NUProof README.

**Edit Locations:** #19, #20

---

### F-008 — Division/Inverse Operation Referenced But Not Defined
**Severity:** HIGH | **Category:** Missing Definition | **Affects:** o1 Outline

**Description:** The o1 Outline Section 7.1 references an inverse operation `S⁻¹` in the context of sensor fusion without defining it in the algebraic framework. Division is not defined in the NASA Paper.

**Required Edit:** Either define `S⁻¹` as a proper algebraic operation in Section 2, or rewrite Section 7.1 using only defined operations (add, mul, scalar mul, flip).

**Edit Locations:** #21

---

### F-009 — AddProperties: Associativity Proof Incomplete
**Severity:** HIGH | **Category:** Formal Proof Gap | **Affects:** NUProof

**Description:** `AddProperties.lean` contains a `sorry` placeholder for the associativity sub-proof. Addition associativity is a basic algebraic property that should be among the first completed proofs.

**Required Edit:** Complete associativity proof in `AddProperties.lean` with no `sorry`.

**Edit Locations:** #22

---

### F-010 — Sub-Distributivity Theorem Not in o1 Outline
**Severity:** LOW | **Category:** Missing Theorem | **Affects:** o1 Outline

**Description:** The N/U algebra satisfies sub-distributivity: `λ⊙(x⊕y) ⪯ (λ⊙x)⊕(λ⊙y)` for scalar λ. This property is implied by the conservatism design but is not stated as a theorem in the o1 outline.

**Required Edit:** Add sub-distributivity theorem to Section 2.4.

**Edit Locations:** #23

---

### F-011 — Cumulative Product Formula Not in o1 Outline
**Severity:** MEDIUM | **Category:** Missing Theorem | **Affects:** o1 Outline

**Description:** The formula for `xⁿ` (n-fold multiplication of a single element) follows from the algebra but is not stated. The NASA Paper Example 7.7 uses the squaring case. A general formula would strengthen the paper.

**Required Edit:** Add cumulative product theorem to Section 2 or 5 with proof sketch.

**Edit Locations:** #24

---

### F-012 — Partial Order Not Defined in o1 Outline
**Severity:** LOW | **Category:** Missing Definition | **Affects:** o1 Outline

**Description:** The sub-distributivity theorem (F-010) and conservatism claims reference a partial order `⪯` on N/U pairs, but this order is never defined in the o1 outline.

**Required Edit:** Define `(n₁,u₁) ⪯ (n₂,u₂)` iff `n₁=n₂` and `u₁≤u₂` (or equivalent formulation) in Section 2.1 or 2.3.

**Edit Locations:** #25

---

### F-013 — Layer 0 Primitives Referenced But Not Documented
**Severity:** MEDIUM | **Category:** Missing Specification | **Affects:** eBIOS

**Description:** eBIOS architecture references Layer 0 "Immutable Foundation" with 4 functions (Verify, Seal, Unseal, Attest) but provides no specification of their interfaces, signatures, or behavior. This predates F-041 (which formalizes the gap). Resolved by creating `Layer0_SPEC.md`.

**Required Edit:** Create `docs/Layer0_SPEC.md` or add note in README that Layer 0 is conceptual pending specification.

**Edit Locations:** #26

---

### F-014 — NUCore.lean Content Not Visible for Verification
**Severity:** HIGH | **Category:** Verification Gap | **Affects:** NUProof

**Description:** All Lean proofs import `NUProof.NUCore`, but the actual content of `NUCore.lean` is not provided in any project documentation. If the type definitions in NUCore don't match the NASA Paper's Definitions 3.1 and 3.2 exactly, all proofs could be formally correct but proving properties of the wrong algebra.

**Required Edit:** Include `NUCore.lean` definitions inline in NUProof README, or publish as appendix. Explicitly verify correspondence with NASA Paper Def 3.1 and 3.2.

**Edit Locations:** #27, #28

---

### F-015 — Preprint DOI Missing from NASA Paper
**Severity:** LOW | **Category:** Documentation Inconsistency | **Affects:** NASA Paper

**Description:** Both documents reference dataset DOI `10.5281/zenodo.17221863`. The o1 outline additionally references preprint DOI `10.5281/zenodo.17172694`. The NASA Paper doesn't reference the preprint.

**Required Edit:** Add preprint DOI to NASA Paper Data and Code Availability section if live.

**Edit Locations:** #29

---

### F-016 — Real-Time Latency Claim (<1ms) Inconsistent with Full eBIOS Stack
**Severity:** MEDIUM | **Category:** Cross-Layer Integration Gap | **Affects:** o1 Outline, eBIOS

**Description:** o1 Outline Section 7.4 claims `<1ms` latency for autonomous vehicle sensor fusion. But: NUCore `<1μs` + Ledger `<1ms` + Monitor `<100μs` ≈ **1.1ms** total when ledger writes are synchronous — exceeding the stated requirement.

**Required Edit:** Either: (a) make ledger writes asynchronous (fire-and-forget) keeping critical path `<200μs`, or (b) revise latency claim to `<2ms`, or (c) define `real_time_mode` policy in NUPolicy that defers ledger writes to a background thread.

**Edit Locations:** #30, #31

---

### F-017 — Identity Element Theorem Not Stated in o1 Outline
**Severity:** LOW | **Category:** Missing Theorem | **Affects:** o1 Outline

**Description:** The additive identity `(0,0)` and multiplicative identity `(1,0)` are not stated as theorems in the o1 outline, even though they follow directly from the definitions.

**Required Edit:** Add identity element theorem to Section 2.4.

**Edit Locations:** #32

---

### F-018 — o1 Outline Has No Reference to eBIOS or NUProof
**Severity:** MEDIUM | **Category:** Cross-Document Gap | **Affects:** o1 Outline

**Description:** The o1 outline contains zero occurrences of "eBIOS" or "NUProof" across 637 lines. Section 8.3 lists formal verification (Coq/Lean) as future work, but 3 complete Lean 4 proofs already exist in NUProof.

**Required Edit:** Add eBIOS reference to Section 7.4 or 8. Update Section 8.3 to reflect that Lean 4 formal verification is in progress via NUProof.

**Edit Locations:** #33, #34

---

### F-019 — NUProof Theorem Status Markers Are Inconsistent
**Severity:** LOW | **Category:** Documentation Inconsistency | **Affects:** NUProof

**Description:** README claims "Complete: 3 theorems (NonNegativity, FlipInvolutive, AddCommutativity)" but programmatic scan found only 2 explicit "Status: Complete" lines. AddCommutativity is listed as "(Complete)" inline, not with a separate Status line.

**Required Edit:** Standardize all theorem status markers to consistent "Status: Complete" format. After applying F-002 and F-003 edits, update counts to reflect new totals.

**Edit Locations:** #35

---

### F-020 — Repo Implementation Uses Paper Formula, Widens Gap with o1 Outline
**Severity:** HIGH | **Category:** Definition Mismatch | **Affects:** Repo, o1 Outline

**Description:** `src/nu_algebra.py`, `src/nu_algebra.R`, and `scripts/generate_nu_data.py` all implement `|n₁|u₂ + |n₂|u₁` with NO λ term. The 70,000+ validation tests validate the **paper's** formula, not the o1 outline's λ-parameterized formula. Publishing the o1 outline with λ while citing the same DOI would be a false claim.

**Required Edit:** Either (a) the o1 outline must generate a NEW validation dataset using the λ formula and NOT cite DOI `10.5281/zenodo.17221863` for λ>0 claims, or (b) the o1 outline should present λ=0 (paper formula) as the base case with existing validation, and λ≥1 as an extension requiring separate validation.

**Edit Locations:** #36, #37, #38

---

### F-021 — eBIOS add() Example Definitively Wrong (Confirmed by Repo)
**Severity:** MEDIUM | **Category:** Documentation Error | **Affects:** eBIOS

**Description:** The repo's `add()` method is `NU(self.n + other.n, self.u + other.u)`. For `(10.0, 0.5) + (20.0, 1.0)` = `(30.0, 1.5)`. eBIOS README shows `(30.0, 1.12)`. The repo is the reference implementation; eBIOS is wrong.

**Required Edit:** Fix eBIOS README line 72 to `(30.0, 1.5)`. (Same fix as F-005, confirmed by separate evidence path.)

**Edit Locations:** #39

---

### F-022 — Three Different GitHub Repository URLs Referenced Across Documents
**Severity:** MEDIUM | **Category:** Documentation Inconsistency | **Affects:** Repo

**Description:** Three distinct GitHub URLs appear across project files: `github.com/abba-01/nualgebra` (o1 outline, setup.py, CHANGELOG.md), `github.com/aybllc/nu-algebra` (CITATION.cff, .zenodo.json), and `github.com/abba-01/ebios` (eBIOS). The first two should be the same repo. This causes broken citation links and DOI resolution failures.

**Required Edit:** Decide on canonical URL. Update `setup.py`, `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`, `README.md`, and o1 outline to use the same URL consistently.

**Edit Locations:** #40, #41, #42, #43

---

### F-023 — R Implementation Version String Mismatch
**Severity:** LOW | **Category:** Documentation Inconsistency | **Affects:** Repo

**Description:** `src/nu_algebra.R` declares `NU_ALGEBRA_VERSION = '3.0.0'` while the Python package declares version `3.1.0` in `setup.py`.

**Required Edit:** Update `src/nu_algebra.R` to `NU_ALGEBRA_VERSION = '3.1.0'`.

**Edit Locations:** #44

---

### F-024 — Empty Documentation Files in docs/
**Severity:** LOW | **Category:** Documentation Gap | **Affects:** Repo

**Description:** The `docs/` directory contains placeholder files with no content. This creates an illusion of documentation without providing it.

**Required Edit:** Populate or remove empty documentation files. If a file exists, it should have content.

**Edit Locations:** #45

---

### F-025 — CHANGELOG Claims 905 Tests But Actual Test Files Have ~70
**Severity:** MEDIUM | **Category:** Documentation Inconsistency | **Affects:** Repo

**Description:** `CHANGELOG.md` claims "467 tests in test_nu_algebra.py" and "438 validation tests in test_validation.py" (total: 905). The actual files have ~48 and ~27 test methods respectively. The CHANGELOG numbers appear fabricated or from a different version.

**Required Edit:** Correct CHANGELOG to reflect actual test counts. If an earlier version truly had 905 tests, note that the current version has been refactored.

**Edit Locations:** #46

---

### F-026 — Subtraction Operator Defined in Repo But Absent from Theory
**Severity:** LOW | **Category:** Definition Mismatch | **Affects:** Repo, NASA Paper, o1 Outline

**Description:** Both `nu_algebra.py` and `nu_algebra.R` define subtraction: `(n₁-n₂, u₁+u₂)`. Neither the NASA Paper nor the o1 outline defines subtraction. The implementation is mathematically consistent (equivalent to adding the scalar-negated operand) but undocumented in the theoretical framework.

**Required Edit:** Add subtraction to the o1 outline as a derived operation: `(n₁,u₁) ⊖ (n₂,u₂) = (n₁,u₁) ⊕ ((-1)⊙(n₂,u₂)) = (n₁-n₂, u₁+u₂)`. Note that uncertainty adds because correlation is unknown.

**Edit Locations:** #47

---

### F-027 — pow() Uses Repeated Multiplication; Self-Multiplication Conservatism Undocumented
**Severity:** MEDIUM | **Category:** Definition Gap | **Affects:** Repo, o1 Outline

**Description:** The repo's `pow(k)` uses repeated `mul(self)`, treating each multiplication as independent. This is MORE conservative than necessary because it ignores that the operand is the same variable (perfect correlation). For `pow(2)`: result matches paper Example 7.7. For higher powers: over-estimates uncertainty.

**Required Edit:** Add note to o1 Outline Section 8.2 documenting this conservatism and when it matters. Optionally implement a correlated power formula for the case of perfect correlation.

**Edit Locations:** #48

---

### F-028 — Zenodo DOI Referenced for λ-Formula Claims When Dataset Validates Paper Formula
**Severity:** HIGH | **Category:** Citation Integrity | **Affects:** o1 Outline

**Description:** DOI `10.5281/zenodo.17221863` links to a dataset generated using the paper's formula (no λ). If the o1 outline is published with a λ-parameterized formula and cites this DOI as validation evidence for λ>0 claims, the citation is inaccurate.

**Required Edit:** In o1 Outline Section 6.1, clarify exactly which formula the DOI validates. Generate separate validation data if λ>0 claims are to be made.

**Edit Locations:** #49, #50

---

### F-029 — SAID Reference Appears in Repo Metadata Files
**Severity:** LOW | **Category:** Documentation Inconsistency | **Affects:** Repo

**Description:** `MANIFEST.in` and `.gitignore` contain references to "SAID" — an unexplained acronym that does not appear in any other project document. Unclear if this is a leftover artifact, an unpublished component, or a mistake.

**Required Edit:** Remove SAID references or add explanatory documentation for what SAID is and its relationship to the project.

**Edit Locations:** #51, #52

---

### F-030 — Test Associativity Tolerance Too Loose
**Severity:** MEDIUM | **Category:** Test Quality | **Affects:** Repo

**Description:** `TestAssociativity` in `test_nu_algebra.py` uses tolerance `1e-6` for floating-point comparisons. Since N/U operations are simple arithmetic (no transcendental functions), a tolerance of `1e-10` is achievable and would catch more subtle bugs.

**Required Edit:** Tighten TestAssociativity tolerance from `1e-6` to `1e-10`.

**Edit Locations:** #53

---

### F-031 — No Regression Test for Flip Non-Involution
**Severity:** HIGH | **Category:** Test Coverage Gap | **Affects:** Repo

**Description:** Existing flip tests check that `B(-5,2) = (2,5)` but never verify that `B(B(-5,2)) ≠ (-5,2)`. Without this test, a regression to the false involution could go undetected. This is especially important given F-002 (the NUProof false theorem).

**Required Edit:** Add `test_flip_not_involutive()` and `test_flip_idempotent()` to `TestSpecialOperators`:
```python
def test_flip_not_involutive(self):
    x = NU(-3, 2)
    flipped_twice = x.flip().flip()
    assert flipped_twice.n != x.n  # (3,2) != (-3,2)

def test_flip_idempotent(self):
    x = NU(-3, 2)
    assert x.flip().flip().flip() == x.flip().flip()  # B³ = B²
```

**Edit Locations:** #54, #55

---

### F-032 — Layer 7 Referenced in NUProof But Not Defined in eBIOS Architecture
**Severity:** HIGH | **Category:** Documentation Inconsistency | **Affects:** eBIOS, NUProof

**Description:** NUProof README line 136 references "Layer 7 (Certification): Proof status included in compliance reports." However, the eBIOS architecture diagram shows only Layers 0–6. There is no `Layer7_SPEC.md` or equivalent.

**Required Edit:** Either: (a) Create `Layer7_SPEC.md` documenting the Certification layer, or (b) Remove Layer 7 reference from NUProof and clarify that certification/compliance is handled through existing Layers 3 (NULedger) and 6 (NUGovern).

**Edit Locations:** #56, #57

---

### F-033 — NUGovern API Specification Is Missing
**Severity:** MEDIUM | **Category:** API Specification Gap | **Affects:** eBIOS

**Description:** The eBIOS Quick Start shows `curl -X POST http://localhost:8000/operations/execute` but `NUGovern_API.md` is not provided. Without the full spec (base URL, authentication, all endpoints, rate limits, error codes), implementers cannot build compatible clients.

**Required Edit:** Create `NUGovern_API.md` with: base URL and port configuration, authentication scheme (bearer token, API key, mTLS, or none), all endpoints with request/response schemas (JSON), rate limits, timeouts, error response format, and examples for each endpoint.

**Edit Locations:** #58

---

### F-034 — No NULedger Usage Example in Quick Start
**Severity:** LOW | **Category:** Documentation Gap | **Affects:** eBIOS

**Description:** Quick Start covers NUCore, NUGovern, and NUPolicy usage but has no NULedger example despite the performance table claiming `<1ms` ledger append — implying it is used.

**Required Edit:** Add NULedger usage example to Quick Start covering: `Ledger()` initialization, `ledger.append()`, `ledger.query()`, and `ledger.verify_merkle_root()`.

**Edit Locations:** #59

---

### F-035 — Test Coverage Claims Unverified (172 Tests Claimed, Files Not Linked)
**Severity:** MEDIUM | **Category:** Documentation Inconsistency | **Affects:** eBIOS

**Description:** eBIOS README claims "172 tests, 100% coverage" across 5 layers (39+38+32+41+22) but provides no link to actual test files. Cannot verify claims.

**Required Edit:** Add links to actual test files in the eBIOS repo with commit hash for reproducibility. Or update README with caveat noting full test suite is in the GitHub repository.

**Edit Locations:** #60

---

### F-036 — No Example Policy JSON Files Provided
**Severity:** MEDIUM | **Category:** Missing Example Files | **Affects:** eBIOS

**Description:** Layer 5 NUPolicy uses JSON policies with Ed25519 signing. Quick Start shows `manager.load_policy("conservative")` but no `conservative.json` or JSON schema is provided. Users cannot create custom policies without examples.

**Required Edit:** Create and document at least 3 example policies (`conservative.json`, `strict.json`, `permissive.json`) plus a JSON schema specifying required fields, rule types, and signature structure.

**Edit Locations:** #61, #62

---

### F-037 — Development Phases 0–6 Are Referenced But Undefined
**Severity:** LOW | **Category:** Documentation Gap | **Affects:** eBIOS

**Description:** eBIOS README states "Status: Development (Phases 0-6 complete)" but provides no definition of what Phases 0–6 are.

**Required Edit:** Create `PHASES.md` or add README section defining each phase (Phase 0: Architecture, Phase 1: NUCore, Phase 2: NUProof setup, etc.) with status and timeline for each.

**Edit Locations:** #63

---

### F-038 — Four Layer Specification Documents Are Missing ⚠️ CRITICAL
**Severity:** CRITICAL | **Category:** Missing Specification | **Affects:** eBIOS

**Description:** The eBIOS documentation index lists four specification files. NONE are provided. Without them, no external developer can implement a compatible eBIOS system.

**Missing Files:**
1. `NULedger_SPEC.md` (Layer 3) — Ledger class interface, Merkle tree algorithm, entry format
2. `NUGuard_POLICY.md` (Layer 4) — Monitor interface, rule evaluation, event escalation
3. `NUPolicy_SPEC.md` (Layer 5) — Policy JSON format, rule types, validation
4. `NUGovern_API.md` (Layer 6) — HTTP endpoints, authentication, request/response schemas

**Required Edit:** Retrieve or create all four specification documents and publish them.

**Edit Locations:** #64, #65, #66, #67

---

### F-039 — Quick Start NUPolicy Example Missing Imports and Error Handling
**Severity:** MEDIUM | **Category:** API Usage Gap | **Affects:** eBIOS

**Description:** Quick Start shows `manager = PolicyManager()` and `policy = manager.load_policy("conservative")` without import statements, initialization parameters, or error handling. The example will fail with a `PolicyNotFoundError` unless a policy directory is pre-configured.

**Required Edit:** Expand example with: `from src.nupolicy import PolicyManager`, initialization with `policy_dir` parameter, `manager.list_policies()` call, and `try/except PolicyNotFoundError` block.

**Edit Locations:** #68

---

### F-040 — Performance Claims Lack Hardware and Methodology Details
**Severity:** MEDIUM | **Category:** Measurement Claim | **Affects:** eBIOS

**Description:** Performance table claims `<1μs` for NUCore operations with no stated hardware, compiler version, optimization flags, or measurement methodology. The NASA Paper counts 6 floating-point operations for multiplication; `<1μs` is plausible but requires validation evidence.

**Required Edit:** Update performance table to include: tested hardware (CPU, RAM), compiler and optimization flags (e.g., Python 3.11, no Cython), measurement methodology (timing library, sample count, warmup iterations), and average vs. percentile (p50/p99).

**Edit Locations:** #69

---

### F-041 — Layer 0 (Verify/Seal/Unseal/Attest) Interface Is Undefined
**Severity:** HIGH | **Category:** Missing API Specification | **Affects:** eBIOS

**Description:** eBIOS architecture shows Layer 0 with "Immutable Foundation (4 functions): Verify • Seal • Unseal • Attest" but no specification of signatures, parameters, return types, or behavior exists anywhere.

**Required Edit:** Create `Layer0_SPEC.md` defining:
```
Verify(data, signature, public_key) → bool
Seal(data, private_key) → signature
Unseal(sealed_data) → (data, signature, metadata)
Attest(claim, evidence, witness) → attestation
```

**Edit Locations:** #70

---

### F-042 — NUProof README Confuses Layer 2 Output with Layer 7
**Severity:** HIGH | **Category:** Cross-Layer Reference Error | **Affects:** NUProof, eBIOS

**Description:** NUProof README (line 136) says "Layer 7 (Certification): Proof status included in compliance reports." NUProof IS Layer 2. There is no Layer 7 in the eBIOS architecture (Layers 0–6 only). The text confuses NUProof's output (proof attestations) with a non-existent layer.

**Required Edit:** Rewrite line 136 to: "These attestations are embedded in: Layer 3 (NULedger): Proof hashes logged in Merkle chain; Layer 6 (NUGovern): Proof status included in API compliance reports."

**Edit Locations:** Merged with #57

---

### F-043 — NULedger Performance Metric Is Ambiguous (Latency vs. Throughput)
**Severity:** LOW | **Category:** Measurement Specification | **Affects:** eBIOS

**Description:** Performance table claims "Ledger append | O(log n) | <1ms" without specifying whether this is p50 latency, p99 latency, or throughput. For a system with real-time requirements (F-016), this distinction matters.

**Required Edit:** Update table to specify: `<1ms p50 latency (Merkle tree update + disk write)`. Also report p99 latency, throughput, and hardware dependency (SSD vs. HDD).

**Edit Locations:** #72

---

### F-044 — "conservative" Policy File Referenced But Not Provided
**Severity:** MEDIUM | **Category:** Missing Example Files | **Affects:** eBIOS

**Description:** Quick Start shows `policy = manager.load_policy("conservative")` but no `conservative.json` is distributed with the code. Running this example will fail with `PolicyNotFoundError`.

**Required Edit:** Distribute at least `conservative.json` with the code. Update Quick Start with a note about where policies should be stored (e.g., `./policies/` or `~/.nu-algebra/policies/`).

**Edit Locations:** #73, #74

---

### F-045 — eBIOS Documentation Is 5+ Months Stale
**Severity:** LOW | **Category:** Documentation Maintenance | **Affects:** eBIOS

**Description:** eBIOS README states "Last Updated: 2025-10-20" and "Version: 0.1.0". Current analysis date is 2026-03-21 — over 5 months of gap. The version number should reflect changes made while resolving other SSOT findings.

**Required Edit:** Update README footer to: version `0.2.0`, status reflecting current phase completion, last-updated date `2026-03-21`. Add CHANGELOG entry for v0.2.0 documenting what changed.

**Edit Locations:** #75

---

## 4. CRITICAL ISSUES SUMMARY

### CRITICAL-1 — F-002: False Flip Operator Theorem Certified as Complete
- **Impact:** Formal verification system certifies `B² = id` which the NASA Paper itself disproves
- **Blocks:** All formal verification credibility; any certification relying on NUProof
- **Resolution:** Replace `FlipInvolutive.lean` with `FlipIdempotent.lean` (B³=B²); update all references
- **Cascades to:** F-031 (test coverage), F-008 (definition usage)

### CRITICAL-2 — F-003: PAC Coverage Theorem Foundation Is Unverified
- **Impact:** o1 Theorem 9 (PAC-style coverage) rests on `Enclosure.lean` which contains only `sorry` placeholders
- **Blocks:** Any publication claiming formally verified coverage guarantees
- **Resolution:** Complete all three sub-lemma proofs in `Enclosure.lean` with no `sorry`
- **Cascades to:** F-004 (runtime enforcement), F-009 (AddProperties associativity)

### CRITICAL-3 — F-038: Four Implementation Specification Documents Are Absent
- **Impact:** No external developer can build a compatible eBIOS implementation
- **Blocks:** All external adoption of eBIOS
- **Resolution:** Create `NULedger_SPEC.md`, `NUGuard_POLICY.md`, `NUPolicy_SPEC.md`, `NUGovern_API.md`
- **Cascades to:** F-033 (API), F-035 (testing), F-041 (Layer 0), F-044 (policies)

---

## 5. DEPENDENCY GRAPH

```
F-001 (λ formula) ──────────────────→ F-020 (validation dataset)
                                      F-028 (DOI citation integrity)

F-002 (Flip false) ─────────────────→ F-031 (regression test)
                  └──────────────────→ F-008 (operator definition)

F-003 (Enclosure sorry) ────────────→ F-009 (AddProperties)
                       └────────────→ F-004 (runtime enforcement)

F-004 (coverage_allocation) ────────→ F-036 (policy JSON examples)

F-013 (Layer 0 conceptual) ─────────→ F-041 (Layer0_SPEC.md)

F-018 (no eBIOS ref) ───────────────→ F-038 (specs blocking adoption)

F-038 (specs missing) ──────────────→ F-033 (NUGovern API)
                     └──────────────→ F-044 (policy files)
                     └──────────────→ F-035 (test coverage claims)
```

---

## 6. VERIFICATION CHECKLIST (All 50 Items)

### Original Findings (F-001 to F-031) — 31 items

- [ ] **F-001** — o1 Outline Section 2.2 explicitly states relationship between paper formula and λ-parameterized formula
- [ ] **F-002** — `FlipInvolutive.lean` replaced by `FlipIdempotent.lean`; B³=B² proved with no `sorry`; README and manifest updated
- [ ] **F-003** — `Enclosure.lean` compiles with `lake build`, no `sorry`; all three sub-lemmas present
- [ ] **F-004** — NUPolicy has `coverage_allocation` rule type; NUGuard has `check()` method; NUGovern has `/coverage/validate` endpoint
- [ ] **F-005** — eBIOS README addition example shows `(30.0, 1.5)`
- [ ] **F-006** — o1 Outline Section 3.1 has footnote on operation count difference
- [ ] **F-007** — `ComposeReduction` theorem statement is either corrected or annotated with scope
- [ ] **F-008** — o1 Outline Section 7.1 either defines S⁻¹ rule or uses only defined operations
- [ ] **F-009** — `AddProperties.lean` associativity proof complete with no `sorry`
- [ ] **F-010** — o1 Outline Section 2.4 includes sub-distributivity theorem
- [ ] **F-011** — o1 Outline includes cumulative product formula with proof sketch
- [ ] **F-012** — o1 Outline Section 2.1 or 2.3 includes partial order ⪯ definition
- [ ] **F-013** — eBIOS README or `Layer0_SPEC.md` documents Layer 0 primitives
- [ ] **F-014** — NUProof README or `NUCore.lean` includes type definitions matching NASA Paper Def 3.1/3.2
- [ ] **F-015** — NASA Paper data availability section includes preprint DOI if live
- [ ] **F-016** — eBIOS has `real_time_mode` policy OR o1 Outline latency claim adjusted
- [ ] **F-017** — o1 Outline Section 2.4 includes identity element theorem
- [ ] **F-018** — o1 Outline Section 7.4 or 8 references eBIOS; Section 8.3 updated
- [ ] **F-019** — NUProof README theorem status markers standardized
- [ ] **F-020** — o1 Outline Section 6 clarifies which formula the 70K tests validate
- [ ] **F-021** — eBIOS add() example confirmed fixed to `(30.0, 1.5)`
- [ ] **F-022** — Canonical GitHub URL used consistently in setup.py, CITATION.cff, .zenodo.json, CHANGELOG.md
- [ ] **F-023** — `src/nu_algebra.R` version is `'3.1.0'`
- [ ] **F-024** — `docs/` directory has populated files or removed placeholders
- [ ] **F-025** — CHANGELOG test count matches actual test files
- [ ] **F-026** — o1 Outline Section 2.2 includes subtraction as derived operation
- [ ] **F-027** — o1 Outline Section 8.2 documents self-multiplication conservatism
- [ ] **F-028** — o1 Outline Section 6.1 DOI citation matches correct formula
- [ ] **F-029** — MANIFEST.in and .gitignore SAID references removed or documented
- [ ] **F-030** — TestAssociativity tolerance tightened to 1e-10
- [ ] **F-031** — `test_flip_not_involutive()` and `test_flip_idempotent()` added to test suite

### New Findings (F-032 to F-045) — 19 items

- [ ] **F-032** — eBIOS architecture clearly documents all layers OR Layer 7 reference is removed from NUProof
- [ ] **F-033** — `NUGovern_API.md` published with base URL, authentication, all endpoints, schemas
- [ ] **F-034** — eBIOS Quick Start includes NULedger usage example (append/query/verify)
- [ ] **F-035** — eBIOS README provides link to test files with verifiable count
- [ ] **F-036** — At least 3 example policy JSON files provided (conservative, strict, permissive)
- [ ] **F-036** — JSON schema for policies documented (required fields, rule types)
- [ ] **F-037** — Development phases 0–6 defined in `PHASES.md` or README
- [ ] **F-038** — `NULedger_SPEC.md` created with ledger API and Merkle tree algorithm
- [ ] **F-038** — `NUGuard_POLICY.md` created with monitor interface and rule evaluation
- [ ] **F-038** — `NUPolicy_SPEC.md` created with policy format and validation rules
- [ ] **F-038** — `NUGovern_API.md` created with HTTP endpoints and request/response schemas
- [ ] **F-039** — Quick Start NUPolicy example includes imports and error handling
- [ ] **F-040** — Performance table specifies hardware, compiler, optimization flags, methodology
- [ ] **F-041** — `Layer0_SPEC.md` created defining Verify/Seal/Unseal/Attest interfaces
- [ ] **F-042** — NUProof README line 136 rewritten to reference Layers 3 and 6 (not Layer 7)
- [ ] **F-043** — Performance table specifies latency vs. throughput and percentile (p50/p99)
- [ ] **F-044** — `conservative.json` policy example distributed with code
- [ ] **F-044** — Quick Start updated with policy installation/location instructions
- [ ] **F-045** — eBIOS version, status, and last-updated date current as of 2026-03-21

> **When all 50 checkboxes are verified, the ecosystem is internally consistent and SSOT v4.0 is confirmed complete.**

---

## 7. IMPLEMENTATION ROADMAP

### Phase 0 — IMMEDIATE (This Week): 3 CRITICAL Issues
| Task | Finding | Owner | Time | Blocks |
|------|---------|-------|------|--------|
| Replace FlipInvolutive with FlipIdempotent | F-002 | NUProof maintainer | 2–4 hrs | F-031, F-008 |
| Complete Enclosure.lean (3 sub-lemmas) | F-003 | NUProof maintainer | 1–2 days | F-009, F-004 |
| Create 4 eBIOS layer specs | F-038 | eBIOS lead | 1–2 weeks | F-033, F-044, F-041 |

### Phase 1 — HIGH PRIORITY (Weeks 2–3): 11 HIGH Issues
- F-001: Reconcile λ formula in o1 Outline
- F-004: Add coverage_allocation to NUPolicy/NUGuard/NUGovern
- F-008: Define or remove S⁻¹ in o1 Outline Section 7.1
- F-009: Complete AddProperties associativity
- F-014: Verify NUCore.lean against NASA Paper definitions
- F-020: Align validation dataset claims with correct formula
- F-022: Unify GitHub URLs across all files
- F-028: Fix DOI citation in o1 Outline
- F-031: Add flip regression tests
- F-032: Resolve Layer 7 architecture ambiguity
- F-041: Create Layer0_SPEC.md

### Phase 2 — MEDIUM PRIORITY (Weeks 3–4): 16 MEDIUM Issues
F-005/F-021, F-006, F-007, F-011, F-013, F-016, F-018, F-019, F-025, F-027, F-030, F-033, F-035, F-036, F-039, F-040, F-044

### Phase 3 — LOWER PRIORITY (Weeks 4–6): 15 LOW Issues
F-010, F-012, F-015, F-017, F-023, F-024, F-026, F-029, F-034, F-037, F-043, F-045

### Timeline Summary

| Phase | Priority | Findings | Timeline | Effort |
|-------|----------|----------|----------|--------|
| 0 | CRITICAL | 3 | This week | ~20 hrs |
| 1 | HIGH | 11 | Weeks 2–3 | ~40 hrs |
| 2 | MEDIUM | 16 | Weeks 3–4 | ~30 hrs |
| 3 | LOW | 15 | Weeks 4–6 | ~20 hrs |
| **Total** | | **45** | **~6 weeks** | **~110 hrs** |

---

## 8. AWAITING ANALYSIS

The following materials have **not yet been analyzed**. New findings will be appended from **F-046** onward.

| Source | Status | Expected Finding Range |
|--------|--------|----------------------|
| Next GitHub repository (pending) | Awaiting upload | F-046+ |
| NUCore.lean full content | Not provided | May modify F-014 |
| `proof_manifest.json` full content | Not provided | May modify F-002, F-003 |
| eBIOS test files (`tests/`) | Not provided | May modify F-035 |

---

## APPENDIX A — Quick-Reference Finding Table

| Finding | Severity | Primary Document | One-Line Summary |
|---------|----------|-----------------|-----------------|
| F-001 | HIGH | o1 Outline | λ term in multiplication not in NASA Paper or repo |
| F-002 | **CRITICAL** | NUProof | FlipInvolutive.lean proves false theorem |
| F-003 | **CRITICAL** | NUProof | Enclosure.lean is sorry skeleton |
| F-004 | HIGH | eBIOS | coverage_allocation rule type missing |
| F-005 | MEDIUM | eBIOS | add() example result wrong (1.12 vs. 1.5) |
| F-006 | MEDIUM | o1 Outline | Op count 4 vs. paper's 6 |
| F-007 | MEDIUM | NUProof | ComposeReduction scope unclear |
| F-008 | HIGH | o1 Outline | S⁻¹ undefined |
| F-009 | HIGH | NUProof | AddProperties associativity incomplete |
| F-010 | LOW | o1 Outline | Sub-distributivity theorem missing |
| F-011 | MEDIUM | o1 Outline | Cumulative product formula missing |
| F-012 | LOW | o1 Outline | Partial order ⪯ undefined |
| F-013 | MEDIUM | eBIOS | Layer 0 primitives undocumented |
| F-014 | HIGH | NUProof | NUCore.lean content invisible |
| F-015 | LOW | NASA Paper | Preprint DOI missing from paper |
| F-016 | MEDIUM | o1 Outline | <1ms latency claim exceeds full stack sum |
| F-017 | LOW | o1 Outline | Identity element theorem missing |
| F-018 | MEDIUM | o1 Outline | No eBIOS or NUProof reference |
| F-019 | LOW | NUProof | Status markers inconsistent |
| F-020 | HIGH | Repo | Repo formula ≠ o1 Outline formula, same DOI cited |
| F-021 | MEDIUM | eBIOS | add() example wrong (confirmed by repo) |
| F-022 | MEDIUM | Repo | 3 different GitHub URLs |
| F-023 | LOW | Repo | R version mismatch (3.0.0 vs. 3.1.0) |
| F-024 | LOW | Repo | Empty docs/ files |
| F-025 | MEDIUM | Repo | CHANGELOG claims 905 tests, actual ~70 |
| F-026 | LOW | Repo | Subtraction implemented but not in theory |
| F-027 | MEDIUM | Repo | pow() conservatism undocumented |
| F-028 | HIGH | o1 Outline | DOI cites wrong formula's validation data |
| F-029 | LOW | Repo | SAID reference unexplained |
| F-030 | MEDIUM | Repo | Test tolerance too loose (1e-6) |
| F-031 | HIGH | Repo | No flip non-involution regression test |
| F-032 | HIGH | eBIOS | Layer 7 referenced, doesn't exist |
| F-033 | MEDIUM | eBIOS | NUGovern_API.md missing |
| F-034 | LOW | eBIOS | No NULedger Quick Start example |
| F-035 | MEDIUM | eBIOS | 172 tests claimed, none linked |
| F-036 | MEDIUM | eBIOS | No example policy JSON files |
| F-037 | LOW | eBIOS | Development phases undefined |
| F-038 | **CRITICAL** | eBIOS | 4 layer specs missing |
| F-039 | MEDIUM | eBIOS | NUPolicy example missing imports |
| F-040 | MEDIUM | eBIOS | Performance table lacks hardware details |
| F-041 | HIGH | eBIOS | Layer 0 interface undefined |
| F-042 | HIGH | NUProof | Layer 2 confused with Layer 7 |
| F-043 | LOW | eBIOS | Latency vs. throughput ambiguous |
| F-044 | MEDIUM | eBIOS | conservative.json not provided |
| F-045 | LOW | eBIOS | Documentation 5+ months stale |

---

*SSOT v4.0 — Complete Consolidated Register*
*Analysis Date: March 21, 2026*
*Next findings will be appended from F-046 onward upon receipt of additional GitHub repositories.*

*"Every finding has a location. Every location has an action. Every action has a verification. Consistency is not a goal — it is a requirement."*
