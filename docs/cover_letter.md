# Cover Letter — Statistics and Computing

**To:** The Editors, Statistics and Computing

**Manuscript title:** Payload-Augmented MCMC and the λ–k Order Selection Theorem: Geometry-Adaptive Sampling from the N/U Uncertainty Algebra

**Author:** Eric D. Martin, Independent Researcher
**ORCID:** 0009-0006-5944-1742
**Email:** msphdba@gmail.com

---

Dear Editors,

I submit for your consideration a manuscript introducing two connected results:
the **λ–k Order Selection Theorem** from the N/U (Nominal/Uncertainty) Algebra
framework, and **Payload-Augmented MCMC (PA-MCMC)**, a geometry-adaptive
sampling algorithm that implements the theorem's minimal non-collapse condition
at the sampling layer.

**Why Statistics and Computing.** The paper is methodological statistics:
a new MCMC algorithm with theoretical grounding, benchmark validation, and a
cosmological application. Statistics and Computing is the natural venue — the
burn-in-freeze protocol used in PA-MCMC directly invokes the vanishing
adaptation condition established in Roberts & Rosenthal (2009, JCGS), a core
paper in this journal's tradition.

**Summary of contributions.**

1. **Uncertainty Propagation Order Theorem.** The standard N/U first-order rule
   returns a false zero at any critical point of the propagation function. The
   correct bound uses the lowest non-zero derivative of order k:
   u_out ≈ (1/k!) |f^(k)(n)| u^k.

2. **λ–k Order Selection Theorem.** A propagation operator with representation
   dimension λ preserves non-zero output uncertainty if and only if λ ≥ k−1.
   When λ < k−1, scalar collapse occurs — a structurally false precision result.
   The minimal non-collapse condition is λ* = k−1.

3. **Five canonical scalar collapse cases.** Black-Scholes σ, Arrhenius rate,
   Taylor Rule, Arps decline, and Bradley-Terry each operate at k=2 with λ < 1,
   unifying a previously scattered set of known model-fragility results under
   a single algebraic condition.

4. **PA-MCMC.** A gradient-free adaptive sampler carrying a per-dimension
   uncertainty payload updated via an exponential moving average of accepted
   step sizes (λ=1 during burn-in; frozen for production). The burn-in-freeze
   protocol satisfies the vanishing adaptation condition, ensuring ergodicity.
   Benchmarks: 17×–58× ESS gains over standard MH on degenerate targets
   (Rosenbrock, anisotropic Gaussians).

5. **DESI application.** PA-MCMC applied to the DESI Year 1 BAO w0-wa posterior
   confirms that the ~2.5σ dark energy preference is not a sampling artifact.
   The DESI+Planck posterior with condition number ~5 is not severely degenerate;
   this is a deliberate negative result demonstrating PA-MCMC's operational
   boundary.

**Scope and length.** The manuscript is 9 pages including four figures and
reference list, consistent with a methodological letter-length paper.

**No conflicts.** This work was developed independently with no external funding.
All code is available at: https://github.com/abba-01/nu-algebra

I believe this paper will be of strong interest to readers working on adaptive
MCMC, computational Bayesian methods, and uncertainty quantification.

Respectfully submitted,

Eric D. Martin
ORCID: 0009-0006-5944-1742
