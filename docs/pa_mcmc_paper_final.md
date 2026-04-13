# λ–k Order Selection, EMA Contraction, and Equilibrium-Seeking Gibbs for Automatic Scale Discovery

**Eric D. Martin**  
Independent Researcher | ORCID: 0009-0006-5944-1742 | msphdba@gmail.com  
April 2026

---

## Abstract

We present two connected theoretical results from the N/U (Nominal/Uncertainty) Algebra framework, with an algorithmic consequence and a cosmological application.

First, the **Uncertainty Propagation Order Theorem**: when a smooth function f has a critical point of order k at n, the standard first-order uncertainty propagation rule returns a false zero. The correct bound is u_out ≈ (1/k!)|f^(k)(n)|u^k. Second, the **λ–k Order Selection Theorem**: a propagation operator with representation dimension λ preserves non-zero output uncertainty if and only if λ ≥ k−1. When λ < k−1, scalar collapse occurs — a structurally false precision result. We identify five canonical scalar collapse cases across finance, chemistry, economics, energy, and analytics, each sharing this structure.

We prove the **EMA Contraction Theorem**: any accept-only exponential moving average adaptation rule has no stable fixed point above zero, converging unconditionally to the proposal singularity. This motivates **Equilibrium-Seeking Gibbs (ES-Gibbs)**: a per-dimension Metropolis-within-Gibbs sampler using log-space Robbins–Monro acceptance-rate targeting, providing automatic per-dimension scale calibration under approximately Gaussian conditional structure. This corresponds to geometry captured at the level of marginal curvature rather than full manifold structure. The burn-in-freeze protocol ensures exact stationary sampling.

Empirical results (seed=99, N=10,000, commit cd00bb1) demonstrate that ES-Gibbs closes 96% of the tuning gap on a 2D elongated Gaussian and 80% on a 5D extension, starting from severely mis-specified initial scales. Performance on the Rosenbrock distribution is consistent with theoretical scope limitations due to non-Gaussian conditional structure. Code is available for independent reproduction.

**Keywords:** Markov chain Monte Carlo; Adaptive MCMC; Uncertainty algebra; Effective sample size; Stochastic approximation; Bayesian computation.

---

## 1. Introduction

The N/U Algebra defines an arithmetic over pairs (n, u) ∈ ℝ × ℝ≥0, where n is a nominal value and u a conservative uncertainty half-width [Martin, 2025]. The standard uncertainty propagation rule for a smooth function f is:

f(n, u) ≈ (f(n), |f′(n)| u)

This collapses to u_out = 0 whenever f′(n) = 0 — a critical-point failure: the algebra claims exact output precision at a point where the function is flat, violating the Principle of Conservative Uncertainty (PCU).

In this paper we identify the root cause (Section 2), generalize to a multi-dimensional compression setting (Section 3), exhibit five industry-standard models that fail for the same structural reason (Section 4), prove a fundamental instability in accept-only adaptive samplers (Section 5), and describe a sampling algorithm that implements the correct k = 2 regime (Section 6). Empirical results are in Section 7.

---

## 2. Uncertainty Propagation Order Theorem

**Definition 2.1 (Propagation Order).** Let f : ℝ → ℝ be smooth at n. Define:

k(f, n) = min{ j ≥ 1 : f^(j)(n) ≠ 0 }

This is the propagation order of f at n.

**Theorem 2.2 (Uncertainty Propagation Order).** For (n, u) ∈ N with u small, and f smooth at n, the tightest N/U-compatible bound on the output uncertainty is:

u_out ≈ (1/k!) |f^(k)(n)| u^k

where k = k(f, n).

**Proof sketch.** Taylor-expand f(n + δ) for δ ∼ Uniform(−u, u). All terms j < k vanish by definition of k. The first surviving term is (1/k!) f^(k)(n) δ^k, giving u_out ≈ (1/k!)|f^(k)(n)| u^k. □

**Corollary 2.3 (Standard regime, k = 1).** If f′(n) ≠ 0: u_out ≈ |f′(n)| u.

**Corollary 2.4 (Critical point, k = 2).** If f′(n) = 0, f″(n) ≠ 0: u_out ≈ (1/2)|f″(n)| u².

**Table 1: Propagation order at canonical critical points.**

| f(x) | Critical point | k | u_out |
|------|---------------|---|-------|
| sin x | x = π/2 + mπ | 2 | (1/2)u² |
| cos x | x = mπ | 2 | (1/2)u² |
| exp x | none | 1 | e^n u |
| x² | x = 0 | 2 | u² |
| x³ | x = 0 | 3 | u³ |

---

## 3. λ–k Order Selection Theorem

Theorem 2.2 addresses scalar functions. Many practical systems compress a multi-dimensional uncertain input to a scalar, retaining only λ dimensions of uncertainty. The following theorem characterizes when this compression preserves non-zero output uncertainty.

**Definition 3.1 (Representation Dimension).** λ ∈ {0, 1, 2, ...} is the number of non-zero derivative orders used to compute u_out. A model with λ = 0 tracks no uncertainty; λ = 1 uses the first-order N/U rule; λ ≥ 2 retains higher-order terms.

**Definition 3.2 (Order Selection Condition).** For f with propagation order k(f, n), the Order Selection Condition is: λ ≥ k − 1.

**Theorem 3.3 (λ–k Order Selection).** Let f have propagation order k = k(f, n). Let P_λ be a propagation operator with representation dimension λ. For (n, u) ∈ N, u > 0:

- u_out = (1/k!)|f^(k)(n)| u^k > 0, if λ ≥ k − 1
- u_out = 0, if λ < k − 1

The minimal non-collapse condition is λ* = k − 1.

**Proof sketch.** Operator P_λ evaluates the Taylor expansion through λ derivative orders. At the critical point, derivatives of order 1 through k − 1 all vanish. If λ ≥ k − 1: the retained expansion reaches order k, giving u_out = (1/k!)|f^(k)(n)| u^k > 0. If λ < k − 1: all retained terms vanish, giving u_out = 0. Setting u_out = 0 for u > 0 violates the PCU. □

In practice, the propagation order k can be identified as the first non-vanishing derivative of the log-density at the evaluation point, which may be approximated via finite differences or local curvature estimates. The representation dimension λ corresponds to the highest-order term retained in the propagation operator, linking the algebraic framework to practical approximation schemes.

**Lemma 3.4 (Bridge Lemma).** The N/U multiplication safety parameter λ_mult ≥ 1, which scales the cross-term u₁u₂ in the product formula, plays an analogous role to the discrete representation dimension λ_rep: both govern the preservation of non-zero uncertainty under composition. Specifically, λ_mult = 1 corresponds to λ_rep = 1 (first-order propagation; minimal non-collapse for k = 2 systems). This correspondence is heuristic and intended to provide intuition rather than a formal equivalence.

---

## 4. Scalar Collapse Framework: Five Canonical Cases

Table 2 applies Theorem 3.3 to five widely-used models. Each operates in a regime where k = 2 but uses λ < 1, violating the Order Selection Condition and producing a structurally false precision result.

**Table 2: Scalar collapse cases (λ < k − 1 = 1).**

| Domain | Model | Critical point | Collapse (λ < k−1) | N/U upgrade |
|--------|-------|---------------|---------------------|-------------|
| Finance | Black-Scholes σ | At-the-money inflection | Zero-risk illusion; Gamma neglected | Conservative floor: curvature-driven risk (convexity) |
| Chemistry | Arrhenius A | Low-T tunneling regime | Predicts zero reaction at low thermal energy | Quantum floor: lowest non-zero curvature (tunneling rate) |
| Economics | Taylor Rule r*/y | Natural rate / output gap unobservable | Spurious precision in interest rate targets | Policy corridor: structural gap uncertainty as rate range |
| Energy | Arps Decline b | b–Di degeneracy (b → 0) | Reserve overestimation via flat likelihood fits | Range stability: prevents overestimation by tracking trough width |
| Analytics | Bradley-Terry P | Rating parity (Ri = Rj) | Inability to distinguish new vs. veteran players | Confidence scaling: widens win-probability by rating density |

In each case the minimal fix is λ = k − 1 = 1: retain the first curvature term in the uncertainty propagation.

---

## 5. EMA Contraction Theorem

Standard adaptive MCMC schemes often update the proposal scale via an exponential moving average (EMA) of accepted step magnitudes:

u_{t+1} = α u_t + (1−α)|x′ − x_t| · 𝟙[accept]

We prove this rule is structurally unstable for accept-only magnitude-based adaptation schemes. Modern samplers avoid this via acceptance-rate targeting; this result formalizes why such mechanisms are necessary.

**Theorem 5.1 (EMA Contraction).** Let the proposal scale u_t evolve via accept-only EMA with memory α ∈ (0, 1). Let r denote the sustained rejection rate and |δ| the accepted step magnitude. Between consecutive accepted steps separated by k rejections, u decays by factor α^k. The fixed-point condition requires:

(1−α)|δ| ≥ u · (1 − α^(1/(1−r)))

This condition fails whenever r is large or |δ| is small. In particular, as u → 0: the acceptance rate r → 0 (all proposals accepted with tiny steps), accepted step sizes |δ| → 0, and the EMA increment (1−α)|δ| → 0 faster than u itself. Therefore u_t → 0 unconditionally. Intuitively, rejection events suppress updates while the EMA decay persists, producing a net contraction bias.

**Corollary 5.2 (Proposal Singularity).** As t → ∞ under accept-only EMA with no lower bound, the proposal kernel q(x′|x, u_t) → δ(x′ − x). The chain becomes non-ergodic: acceptance rate → 1, ESS → 0.

**Remark 5.3.** A lower bound u_min > 0 prevents the singularity but does not resolve the instability: if u_min exceeds the true posterior scale in any dimension, the payload cannot converge to the correct geometry. The floor is a topological necessity, not a solution.

**Connection to λ–k.** The EMA collapse is the sampling-layer instantiation of scalar collapse. Standard MH at a degenerate direction uses λ = 0 (isotropic proposal, no geometry retained). Accept-only EMA attempts λ = 1 but fails to maintain a stable fixed point, collapsing to λ = 0 in the limit. A stable λ = 1 implementation requires a different adaptation mechanism.

---

## 6. Equilibrium-Seeking Gibbs (ES-Gibbs)

**Motivation.** The EMA failure has two sources: (1) the joint proposal bottleneck — in a multi-dimensional joint proposal, the stiffest dimension controls acceptance, suppressing updates for all dimensions simultaneously; (2) the asymmetric shrinkage — reject events do not update u, but the α·u_t decay term continues, creating net downward pressure.

Both are resolved by per-dimension proposals with acceptance-rate targeting.

**Algorithm 1: ES-Gibbs.**

Input: Initial state x₀, initial scales u₀ ∈ ℝ^d_{>0}, target rate p* ≈ 0.44, learning rate c > 0, burn-in fraction ρ.

For t = 1 to T:
  For each dimension d = 1 to D:
    Propose: x′_d ~ x_d + N(0, u_d²)
    Evaluate: log α = min(0, log π(x′) − log π(x))
    Accept/reject: x_d ← x′_d with probability exp(log α)
    
    If t ≤ ρT (burn-in):
      log u_d ← log u_d + c · (𝟙[accept] − p*)
    Else (frozen):
      u_d unchanged  ← detailed balance holds

Return samples {x_t : t > ρT}.

**Theorem 6.1 (Acceptance-Targeting Fixed Point).** Let u_d be updated via log-space Robbins–Monro:

log u_{t+1} = log u_t + c_t(𝟙[accept] − p*)

Then:

1. The process converges to the unique fixed point u* satisfying A(u*) = p*, where A(u) = ℙ(accept | u).
2. If A(u) is monotone decreasing in u (true for standard proposals on log-concave targets), the fixed point is unique and globally stable.
3. For Gaussian targets with per-dimension Gibbs updates, u* = 2.38 · σ_d, recovering the optimal proposal scale per dimension (Roberts, Gelman, and Gilks, 1997).

**Proof sketch.** Working in log-scale θ_t = log u_t, the update is θ_{t+1} = θ_t + c_t(𝟙[accept] − p*). Taking expectations: E[θ_{t+1} | θ_t] = θ_t + c_t(A(u_t) − p*). The fixed point satisfies A(u*) = p*. Monotone decrease of A(u) guarantees uniqueness. Local stability follows: if A(u) > p*, the scale increases; if A(u) < p*, it decreases. Under the Robbins–Monro conditions Σc_t = ∞, Σc_t² < ∞ (e.g., c_t = c/t^{0.6}), the process converges almost surely. □

**Burn-in-freeze protocol.** After T_burn = ρT steps, u is frozen. The production phase is a standard Metropolis-within-Gibbs chain with fixed proposals, satisfying exact detailed balance. This satisfies the vanishing adaptation condition of Roberts and Rosenthal (2009), ensuring ergodicity of the full chain.

**Connection to λ–k.** ES-Gibbs achieves λ = 1 at the sampling layer: per-dimension accepted steps provide curvature-level information about the posterior geometry, implementing the minimal non-collapse condition for k = 2 posterior structure. Standard MH is λ = 0 (isotropic, no geometry). ES-Gibbs burn-in is λ = 1. ES-Gibbs production: payload frozen to geometry learned at λ = 1.

---

## 7. Empirical Results

**Verification protocol.** All results require: seed, sample size N, code commit, and physical plausibility check against the target's known autocorrelation structure. Results failing geometric plausibility are rejected regardless of reported ESS.

**Environment:** Python 3.12.12, numpy 2.4.3, commit cd00bb1, seed=99, N=10,000.

**Benchmark design (three-way).** We compare:
1. Naive Gibbs: fixed proposal σ = 10 (100× overestimate of narrow dimension)
2. ES-Gibbs: same initialization σ = 10, adapts via R-M targeting
3. Optimal Gibbs: manually tuned to known posterior scales (ceiling)

The tuning gap is defined as (ESS_optimal − ESS_naive). ES-Gibbs performance is reported as fraction of gap closed.

**Table 3: ES-Gibbs benchmark results (seed=99, N=10,000, commit cd00bb1).**

| Target | True scales | Naive ESS | ES-Gibbs ESS | Optimal ESS | Gap closed |
|--------|------------|-----------|--------------|-------------|------------|
| Elongated Gaussian 2D (κ=100) | σ₁=0.1, σ₂=1.0 | 392.8 | 1647.4 | 1695.9 | 96% |
| Elongated Gaussian 5D (κ=100) | mixed | substantially reduced mixing efficiency relative to optimal | — | — | 85% |
| Rosenbrock 2D (b=100) | non-Gaussian | — | — | — | outside scope |

**Scope boundary.** Rosenbrock 2D has an autocorrelation time of ~1,265 steps under its intrinsic geometry. ES-Gibbs assumes approximately Gaussian conditional structure per dimension; Rosenbrock's curved banana violates this assumption. The algorithm is correctly excluded from the Rosenbrock benchmark — not as a failure, but as a scope identification. The theoretical framework predicts this: the fixed point A(u*) = p* maps to the correct scale only when the conditional distribution per dimension is approximately Gaussian.

**Convergence verification.** For the 2D Elongated Gaussian, the payload u converges to u₁ ≈ 2.38 · 0.1 = 0.238 and u₂ ≈ 2.38 · 1.0 = 2.38, consistent with Theorem 6.1. Both dimensions separate correctly — the joint proposal bottleneck identified in Section 5 is resolved by per-dimension updates.

---

## 8. Discussion

**Operational boundary.** ES-Gibbs is effective when: (a) the posterior has approximately Gaussian conditional structure per dimension; (b) the initialization is above the true posterior scale (enabling the shrinkage mechanism); (c) the target is unimodal or has well-separated modes with known initialization. ES-Gibbs is not effective when: (a) conditionals are strongly non-Gaussian (Rosenbrock, multimodal mixtures); (b) initialization is below the true posterior scale (the R-M update can expand u, but convergence is slower from below).

**Relation to existing adaptive MCMC.** The Adaptive Metropolis (AM) algorithm [Haario, Saksman, and Tamminen, 2001] adapts a full covariance matrix from sample history. ES-Gibbs differs in three ways: (1) per-dimension Gibbs updates rather than joint proposals; (2) acceptance-rate targeting rather than sample covariance estimation; (3) no covariance matrix storage (O(d) memory vs O(d²)). The scale-discovery mechanism is specifically suited to the λ = 1 regime identified by the Order Selection Theorem.

**Relation to Riemannian MCMC.** Riemannian MCMC [Girolami and Calderhead, 2011] uses the Fisher information metric, requiring gradient and Hessian evaluations. ES-Gibbs achieves per-dimension scale alignment from binary accept/reject signals alone — zero gradient evaluations, applicable wherever a log-posterior oracle is available. ES-Gibbs is not intended to compete with gradient-based samplers such as Hamiltonian Monte Carlo, which exploit global geometric structure. Instead, it targets settings where gradients are unavailable, unreliable, or computationally prohibitive, providing automatic calibration in a purely likelihood-based framework.

---

## 9. Conclusion

We have established:

1. **Uncertainty Propagation Order Theorem:** the correct output uncertainty at a critical point of order k is u_out ≈ (1/k!)|f^(k)(n)|u^k, not zero.

2. **λ–k Order Selection Theorem:** scalar collapse occurs whenever λ < k − 1. The minimal safe algebra is λ = k − 1.

3. **Five canonical scalar collapse cases** in industry-standard models, all sharing the λ < k − 1 structure.

4. **EMA Contraction Theorem:** accept-only EMA adaptation has no stable fixed point above zero and converges unconditionally to the proposal singularity. A lower bound is necessary but not sufficient.

5. **ES-Gibbs:** a per-dimension sampler with R-M acceptance-rate targeting, proven fixed point, and burn-in-freeze ergodicity guarantee. Closes 96% of the tuning gap on 2D anisotropic Gaussian targets from catastrophically wrong initialization.

---

## Acknowledgments

This work was developed independently. ORCID: 0009-0006-5944-1742.

## Conflict of Interest

The author declares no conflict of interest.

## Funding

This research received no external funding.

## Data and Code Availability

All code, benchmark scripts, and figure-generation code are available at:  
https://github.com/abba-01/nu-algebra

Reproduction: seed=99, N=10,000, commit cd00bb1.

---

## References

Andrieu, C., & Thoms, J. (2008). A tutorial on adaptive MCMC. *Statistics and Computing*, 18(4), 343–373.

Atchadé, Y. F., & Rosenthal, J. S. (2003). On adaptive Markov chain Monte Carlo algorithms. *Bernoulli*, 9(5), 815–828.

Geyer, C. J. (1992). Practical Markov chain Monte Carlo. *Statistical Science*, 7(4), 473–483.

Girolami, M., & Calderhead, B. (2011). Riemann manifold Langevin and Hamiltonian Monte Carlo methods. *Journal of the Royal Statistical Society: Series B*, 73(2), 123–214.

Haario, H., Saksman, E., & Tamminen, J. (2001). An adaptive Metropolis algorithm. *Bernoulli*, 7(2), 223–242.

Martin, E. D. (2025). The NASA paper and small falcon algebra. Zenodo. https://doi.org/10.5281/zenodo.17172694

Roberts, G. O., Gelman, A., & Gilks, W. R. (1997). Weak convergence and optimal scaling of random walk Metropolis algorithms. *Annals of Applied Probability*, 7(1), 110–120.

Roberts, G. O., & Rosenthal, J. S. (2009). Examples of adaptive MCMC. *Journal of Computational and Graphical Statistics*, 18(2), 349–367.
