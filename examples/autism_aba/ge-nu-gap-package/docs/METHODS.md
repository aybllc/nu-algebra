# METHODS: GE‑NU Gap‑Effect Test

## 0) Context (sourced)
The article reports that session **gaps** occurred, but “each of these gaps occurred **after** we initiated the intervention phase for all three participants, **limiting the effect** of these gaps on the design.” (Swensson et al., 2024, Behavioral Interventions, 39(3), e2015; DOI:10.1002/bin.2015).

## 1) N/U algebra — simple definition (sourced)
Represent each session as a pair **(n, u)**:
- **n** = nominal signal (e.g., proportion independent IDKPTM or proportion correct).  
- **u** ≥ 0 = uncertainty (from IOA and fidelity).
Operations (Lean N/U Core v1):
- Addition: (n1,u1) ⊕ (n2,u2) = (n1+n2, u1+u2)
- Multiplication: (n1,u1) ⊗ (n2,u2) = (n1*n2, |n1|u2 + |n2|u1)
- Scalar: a ⊙ (n,u) = (a n, |a| u)
Special operators used for diagnostics/sensitivity:
- **Catch** Cα(n,u) = (0, |n|+u) — preserves invariant M = |n| + u
- **Flip**  B(n,u) = (u, |n|) — preserves invariant M
See Martin (2025), *The NASA Paper & Small Falcon Algebra* (preprint).

## 2) Data to collect (sourced)
Per session, per participant during **intervention**:
- y_t ∈ [0,1] (choose one metric: IDKPTM **or** Correct).  
- Gap flag (pre/post).  
- IOA, caregiver fidelity, researcher fidelity (session‑level preferred; otherwise phase averages).

## 3) Encoding (specification)
- Set n_t = y_t.
- Set u_t = 1 − IOA_t + (1 − caregiver_t) + (1 − researcher_t), clipped to [0,1].
- Weight each session by w_t = 1/(u_t + ε), ε = 1e−6.

## 4) Statistics (standard + N/U weighting)
- **Level shift:** Δ_L = (weighted mean post‑gap) − (weighted mean pre‑gap).
- **Trend shift:** Δ_T = β_post − β_pre, where each β is a **weighted** OLS slope within block.
- **Permutation test (design‑respecting):** Hold the number of pre/post sessions fixed and randomize the cut‑point index within the intervention series; recompute Δ_L, Δ_T for B permutations (default 10,000). p‑values are computed two‑sided.
- **Equivalence (SESOI):** Conclude “no practically meaningful effect” if |Δ_L| ≤ 0.10 and |Δ_T| ≤ 0.005/session *and* permutation p‑values > 0.10.

## 5) Sensitivity (specification)
- Re‑run with the **inverse metric** (IDKPTM ↔ Correct).  
- Include the **‘5‑targets’** phase and verify conclusions.  
- Apply Flip B_λ by scaling post‑gap weights w_t ← λ·w_t, λ ∈ [0.8, 1.2].

## 6) Outputs
- `gap_effect_summary.csv`: per‑participant and pooled Δ_L, Δ_T, p‑values, decisions.
- `decision.md`: one‑page narrative suitable for a Limitations/Methods addendum.

## 7) Limits
- Session values come from Figure 1 or raw logs; if digitized, include the digitizer output file.  
- Use phase‑average IOA/fidelity if session‑level not available; note this in `decision.md`.

## 8) Citations (see full refs in docs/REFERENCES.md)
- Swensson et al. (2024): Behavioral Interventions 39(3), e2015; DOI:10.1002/bin.2015. (Limitation text cited.)  
- Martin (2025): *The NASA Paper & Small Falcon Algebra*, preprint.
