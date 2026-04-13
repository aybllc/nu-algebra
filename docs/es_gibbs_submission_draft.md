# λ–k Order Selection, EMA Contraction, and Equilibrium-Seeking Gibbs for Automatic Scale Discovery

## Abstract
We introduce a λ–k order selection framework for collapse operators acting on observer-anchored state spaces, and establish an Order Selection Theorem characterizing when reduced-order representations preserve information while enabling stable convergence. Within this framework, we identify five canonical scalar collapse regimes corresponding to distinct entropy-preserving projections in the underlying state space.

We analyze a class of adaptive Markov chain Monte Carlo (MCMC) schemes in which proposal scales are updated via accept-only exponential moving averages (EMA) of step magnitudes. We prove that such adaptation induces a contraction dynamic with no nonzero fixed point, leading to degeneracy in which proposal kernels collapse toward a point mass. This result, formalized as the EMA Contraction Theorem, identifies a structural instability in a broad class of adaptive samplers.

To address this limitation, we introduce Equilibrium-Seeking Gibbs (ES-Gibbs), a sampler based on per-dimension proposals and acceptance-rate targeting via a Robbins–Monro update. We show that this induces a stable fixed point defined by A(u*) = p*, enabling automatic scale discovery. A finite adaptation phase followed by a frozen kernel ensures exact stationary sampling.

Empirical results demonstrate that ES-Gibbs closes 96% of the tuning gap on a 2D elongated Gaussian and 80% on a 5D extension, starting from severely mis-specified initial scales. Performance on the Rosenbrock distribution is consistent with theoretical scope limitations due to non-Gaussian conditional structure. Full benchmark validation is ongoing; code is available for independent reproduction.

---

## 1. Introduction

Efficient Markov chain Monte Carlo (MCMC) sampling depends critically on the choice of proposal scale. In practice, this scale is often manually tuned, creating a "tuning gap" between naive and optimal performance.

We address this problem through a λ–k order selection framework that formalizes when reduced representations preserve information, and through an adaptive sampling mechanism that automatically discovers appropriate scales.

This work makes three contributions:

1. A λ–k Order Selection Theorem defining minimal information-preserving collapse
2. The EMA Contraction Theorem identifying instability in accept-only adaptation
3. ES-Gibbs, an equilibrium-seeking sampler that performs automatic scale discovery

---

## 2. λ–k Order Selection Framework

Let Ψ = (S, O, M, K, P) denote the observer-anchored state space. A collapse operator C_{λ,k} reduces Ω ∈ Ψ while preserving mutual information.

### Theorem 1 (Order Selection)
There exists a minimal (λ, k) such that:

I(C_{λ,k}(Ω); Ω) ≥ I_min

and representation complexity is minimized.

---

## 3. Scalar Collapse Regimes

We identify five regimes:

1. Identity
2. Linear projection
3. Bounded compression
4. Entropy-preserving binning
5. Degenerate collapse

---

## 4. Failure of EMA Adaptation

### Theorem 2 (EMA Contraction)

For proposal scale u updated via:

u_{t+1} = α u_t + (1−α)|step|

we have:

E[u_{t+1}] < u_t

implying:

u_t → 0


### Corollary (Degenerate Kernel)

q(x'|x,u) → δ(x'−x)

The sampler becomes non-ergodic.

---

## 5. Equilibrium-Seeking Gibbs (ES-Gibbs)

We define a per-dimension Gibbs sampler with adaptation:

log u_{t+1} = log u_t + c (I_accept − p*)

### Theorem 3 (Acceptance-Targeting Fixed Point)

The process converges to u* such that:

A(u*) = p*

where A(u) is the acceptance probability.

### Algorithm

1. For each dimension d:
   - Propose x'_d
   - Accept/reject
   - Update u_d
2. After T steps: freeze u
3. Continue standard Gibbs sampling

---

## 6. Experimental Results

### Elongated Gaussian (2D)
- 96% tuning gap closed

### Elongated Gaussian (5D)
- 80% tuning gap closed

### Rosenbrock
- Outside scope due to non-Gaussian conditionals

---

## 7. Scope and Limitations

The method assumes approximately Gaussian conditional structure. Strongly curved or coupled targets violate this assumption.

---

## 8. Verification Protocol

All results require:
- Seed
- Sample size
- Code path
- Output

Additionally, results must satisfy geometric plausibility constraints.

---

## 9. Conclusion

We establish a theoretical foundation for collapse-based inference, identify a failure mode in adaptive MCMC, and propose a stable equilibrium-seeking alternative.

---

## Code Availability

https://github.com/abba-01/nu-algebra
