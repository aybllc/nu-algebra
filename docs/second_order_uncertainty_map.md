# Second-Order Uncertainty: Cross-Domain Application Map
**Eric D. Martin — 2026-04-12**

Cross-domain matching of the Uncertainty Propagation Order Theorem (see `unified_math_reference.md §11`) 
against "lightly appreciated" formulas and Eric's first-hand algebraic machinery.

---

## Framework: Three Tiers of Readiness

| Tier | Description | Status |
|------|-------------|--------|
| **Tier 1** | Built: N/U first-order ops, UHA/ΔT, Morton encoding | ✅ Implemented |
| **Tier 2** | Conceptual, not yet formalized: Propagation Order Theorem, second-order extension | ⚠️ Theorem stated (§11), no code |
| **Tier 3** | Gap diagnosed, no algebra yet: transcendentals, Compression Instability as N/U operator | ❌ Future work |

---

## Domain Mapping

### 1. H₀ Inference — Planck CMB (Tier 1 → 2 Bridge)

**Formula:** The CMB likelihood maps parameter vector θ = (Ωm, Ωb, h, ns, τ, As) → H₀.

**Where the critical point occurs:**
```
∂H₀/∂θ_degenerate ≈ 0   along the Ωm–H₀ degeneracy trough
```
The likelihood surface has a narrow curved valley (the "h–Ωm trough"). 
Standard MCMC and first-order N/U both fail here: they report near-zero sensitivity
along the degeneracy direction, when the true propagation is second-order (curvature-driven).

**Eric's existing machinery:** UHA/ΔT framework (Section 2, `unified_math_reference.md`);
multiresolution cosmology paper. The Observer Tensor T captures the epistemic distance 
between early and late H₀, but does NOT yet apply the Propagation Order Theorem to the
likelihood geometry.

**Gap:** The correct uncertainty in H₀ propagated FROM the Planck likelihood surface
near its degeneracy direction is u_H₀ ≈ ½|∂²H₀/∂θ²|·u_θ² — not u_H₀ = 0.
This is why H₀ error bars from CMB alone are arguably too tight: the MCMC doesn't 
correctly explore the curvature-dominated regime.

**Action:** Apply Theorem 11.2, Corollary 5b to the Planck Hessian eigenvalues.
Testable: CU-MCMC (see below) should recover wider, physically correct H₀ posteriors.

---

### 2. S8 Tension Near Convergence (Tier 1 → 2 Bridge)

**Formula:** S8 = σ8 × (Ωm/0.3)^0.5

**Where the critical point occurs:**
```
∂(tension_metric)/∂(parameter) ≈ 0  at the near-convergence saddle point
between weak lensing and galaxy clustering contours
```

**Eric's existing machinery:** `COMPREHENSIVE_MULTIPROBE_RESULTS_SUMMARY.md` (multiresolution
cosmology). The S8 result at 82.1% convergence is from the UHA multi-resolution framework.
The framework correctly identifies this as "systematic-dominated" (ΔT < 0.15).

**Gap:** The S8 convergence point is itself a critical point of the tension metric as a 
function of (σ8, Ωm). The Propagation Order Theorem says the uncertainty at that convergence
is u_out ~ u²/2, not u_out = 0. This means the reported 82.1% convergence confidence has an 
underestimated uncertainty band.

---

### 3. Cepheid Period-Luminosity Relation (Tier 2)

**Formula:** μ = m_W - M_W - Z_W·Δ[Fe/H] + γ(log P - 1)

**Where the critical point occurs:**
At the metallicity calibration pivot ([Fe/H] = 0, P = 10 days):
```
∂μ/∂[Fe/H]|_{pivot} = 0   if the pivot is chosen to minimize metallicity sensitivity
```
This is deliberate in Cepheid calibration (it's why a pivot is chosen!), but it means
the uncertainty in γ (the period-slope) propagates as a SECOND-ORDER term at the pivot.

**Eric's existing machinery:** None direct. The S8/H₀ framework is applicable by analogy.

**Gap:** The distance ladder uncertainty is typically quoted as first-order in γ·u_γ.
Near the pivot, this is the k=2 regime: u_μ ≈ ½|∂²μ/∂P²|·u_P² ≈ ½|γ/ln10²|·u_P².

---

### 4. Black-Scholes Volatility (Tier 3 — Compression Instability)

**Formula (Black-Scholes):** C = S·Φ(d₁) - K·e^{-rT}·Φ(d₂)

**The compression:** 6-dimensional uncertain system (drift, vol, correlation, jumps, 
skew, kurtosis) compressed to σ (implied volatility).

**Where second-order matters:**
```
∂(IV)/∂(option price) → ∞  as option approaches expiry near-the-money (vega → 0)
```
The inverse problem (extract IV from observed price) has a critical point where
first-order propagation fails catastrophically: near expiry, ATM vega → 0, so
the IV uncertainty from price uncertainty is formally infinite in first-order, but
finite (and large) in second-order through the vomma term.

**Eric's existing machinery:** Compression Instability Principle (identified in 
conversation 2026-04-12, not yet formalized). No N/U algebra extension yet.

**Theoretical connection:** The Compression Instability Principle IS the Propagation Order
Theorem applied to the inverse map: when the forward map (sigma → price) has 
∂price/∂sigma = 0, the inverse uncertainty explodes UNLESS the second-order term is used.

---

### 5. Arps Decline Curve (Tier 3 — Compression Instability)

**Formula:** q(t) = q_i / (1 + b·D_i·t)^{1/b}

**Where the critical point occurs:**
```
∂q/∂b → 0  as b → 0 (approaches exponential decline)
lim_{b→0} q(t) = q_i · exp(-D_i · t)
```
At b = 0, the decline curve formula has a removable discontinuity in b. Standard uncertainty
propagation gives ∂q/∂b = 0 at b=0, falsely claiming q is insensitive to b near exponential.

The correct second-order term:
```
u_q ≈ ½|∂²q/∂b²|_{b=0} · u_b²
```
This is non-trivial and explains why reserve estimates are highly sensitive to b uncertainty
even when b is close to zero.

**Compression Instability:** 3D reservoir physics (permeability tensor, pressure gradient, 
completion geometry) compressed to single exponent b. Uncertainty in b at b≈0 maps onto 
uncertainty in long-term EUR (Estimated Ultimate Recovery) via second-order terms.

---

### 6. NU Morton Encoding (Tier 1 + 2 — Eric's Own Machinery)

**Where the critical point occurs:**
Morton encoding z = interleave_bits(x, y) has discontinuities at bit boundaries.
As x or y crosses a power-of-2 boundary, ΔZ jumps discontinuously.

**Near-critical behavior:**
At x = 2^k - ε for small ε > 0:
```
∂Z/∂x ≈ 0  (in the integer sense — the bit pattern is about to flip)
```
The spatial uncertainty u_x propagates as u_Z ~ O(u_x²) near these boundaries
because the first-order sensitivity of Z to x vanishes in the boundary zone.

**Eric's existing machinery:** Morton encoding is built into the UHA framework (Section 3).
The bit-boundary artifact is already documented but not treated with second-order theory.

**Action:** Apply Corollary 5b to the Morton encoding function at bit boundaries.
Result: u_Z at bit boundaries should be u_x², not u_x — meaning the spatial uncertainty
COMPRESSES at bit boundaries rather than propagating linearly.

---

### 7. Psych-Morton (Tier 2 — Cross-Domain Application)

**Where the critical point occurs:**
GAD-7 → Morton encoding → ΔMorton diagnostic signal.
GAD-7 items are 0-3 integer scales. The Morton encoding of two GAD-7 items creates
a 2D diagnostic space. At the score boundary (item_i = 1 → 2 transition):
```
∂(diagnostic signal)/∂(item score) → 0 near the clinical threshold (score = 10)
```

The critical point is exactly where the diagnostic is most important (near the clinical
boundary between "moderate" and "severe" anxiety).

**Eric's existing machinery:** Psych-Morton concept established 2026-04. N/U algebra
applied to GAD-7 in `examples/nua_psychology/`.

**Gap:** The N/U propagation through the clinical threshold is currently first-order.
At the threshold boundary, the correct treatment uses Corollary 5b:
u_diagnostic ≈ ½|∂²signal/∂score²| · u_score²

This has direct clinical relevance: uncertainty in GAD-7 scores near threshold 10 
is QUADRATICALLY smaller in the Morton diagnostic signal — the signal is actually 
more precise at the clinical boundary than elsewhere, by second-order compression.

---

## Priority Matrix

| Domain | Eric's Machinery | Theorem Applies | Impact | Priority |
|--------|-----------------|-----------------|--------|----------|
| H₀ / Planck Hessian | ✅ UHA/ΔT | ✅ k=2 | Resolve H₀ tension framing | **★★★** |
| CU-MCMC Rosenbrock | ✅ N/U algebra | ✅ k=2 | New MCMC class | **★★★** |
| S8 convergence | ✅ multiresolution | ✅ k=2 | Uncertainty underestimate | **★★** |
| Morton bit-boundary | ✅ UHA Morton | ✅ k=2 | UHA precision calibration | **★★** |
| Psych-Morton threshold | ✅ GAD-7 examples | ✅ k=2 | Clinical diagnostic precision | **★★** |
| Cepheid pivot | ❌ no machinery | ✅ k=2 | Distance ladder contribution | ★ |
| Black-Scholes vomma | ❌ no machinery | ✅ k=2 | Finance application | ★ |
| Arps b→0 | ❌ no machinery | ✅ k=2 | Petroleum application | ★ |

---

## CU-MCMC: The Immediate Priority

The CU-MCMC insight (from this session, 2026-04-12) is that the Propagation Order Theorem
can be applied AS A PROPOSAL MECHANISM in MCMC:

```
Standard MCMC:  proposal_width = fixed σ or gradient-scaled σ
CU-MCMC:        proposal_width = max(|f'|·u, ½|f''|·u²)
                — uses whichever propagation order is locally active
```

This transforms the Uncertainty Propagation Order Theorem from a post-hoc uncertainty
correction into an active sampling primitive.

**Testable claim:** On the Rosenbrock function (the canonical "degenerate valley" benchmark):
- Standard MCMC: ESS ~ 20-50 per 1000 steps (trapped in the trough)
- CU-MCMC: ESS ~ 150-300 per 1000 steps (payload carries through the trough)
- Posterior means: unchanged within 1σ

See implementation plan in the CU-MCMC development document.

---

*References:*
- Theorem statement: `unified_math_reference.md §11`
- H₀ multiprobe: `multiresolution-cosmology/COMPREHENSIVE_MULTIPROBE_RESULTS_SUMMARY.md`
- Morton encoding: `unified_math_reference.md §3`
- N/U Psychology: `nu-algebra/examples/nua_psychology/`
- SSOT future work: `nu-algebra/o1.txt §8.3`
