# Nominal/Uncertainty Algebra as a Peer Review Instrument in Psychological Science: A Conservative Framework for Claim Robustness

**Author note.** This is a Zenodo preprint. All analysis files and numerical validation artifacts are openly available. See "Data & Code Availability."

## Abstract
Psychological science faces persistent challenges in replicability and effect-size stability. 
We present Nominal/Uncertainty (N/U) algebra—a conservative, distribution-agnostic representation in which every result is a pair (n, u) of nominal value and explicit uncertainty bound—and evaluate it as a peer-review instrument for stress-testing claims.
The revised algebra restores closure, associativity, and monotonicity via absolute-value terms in products and preserves the invariant M(n,u)=|n|+u. 
Using only published point estimates and 95% confidence intervals, we recode several contested effects (ego depletion, power posing behaviors/hormones, facial feedback) and classify claims as fragile whenever |n| ≤ u. 
Results align with preregistered multi-lab replications: the conservative intervals include zero for ego depletion, facial feedback, mortality salience, while a positive-control anchoring meta-estimate remains robust.
A 70k-case validation corpus shows N/U ≥ Gaussian first-order/RSS and matches interval arithmetic for nonnegative nominals to within floating-point error, with stable chaining across long products.
We argue for a one-line N/U check in review guidelines as a low-cost, auditable safety net complementing Registered Reports, equivalence tests, and Bayesian estimation.


## Introduction
Psychological science has wrestled with heterogeneous replicability and effect-size stability across large coordinated replication efforts and meta-analyses. We adopt a conservative, fully auditable calculus—Nominal/Uncertainty (N/U) algebra—in which each quantity is an ordered pair (n, u) of nominal value and nonnegative bound. We evaluate N/U as a peer-review instrument that transforms published estimates and CIs into conservative statements about claim robustness.

## N/U Algebra (revised)
All quantities live in A = R × R≥0. Primary operations:
- Addition: (n1,u1) ⊕ (n2,u2) = (n1+n2, u1+u2)
- Multiplication: (n1,u1) ⊗ (n2,u2) = (n1 n2, |n1| u2 + |n2| u1)
- Scalar: a ⊙ (n,u) = (a n, |a| u)
Special operators Catch C(n,u)=(0, |n|+u) and Flip B(n,u)=(u, |n|) conserve M(n,u)=|n|+u.
Formal properties (closure, associativity, monotonicity) and worked examples are given in the companion paper and dataset notes.

## Methods
**Decision rule.** Encode a published point estimate and 95% CI as (n,u) with u = (CI_high − CI_low)/2. Classify a claim as *fragile* if |n| ≤ u (conservative interval includes 0); otherwise *robust*.
**Case selection.** Ego depletion (RRR, 23 labs), Power posing (behavioral & hormonal outcomes), Facial feedback (RRR), Mortality salience (Many Labs), and a positive-control anchoring meta-estimate.
**Validation.** A 70k-case corpus demonstrates strict conservatism (N/U ≥ Gaussian first-order/RSS), interval consistency for n≥0, and chain stability (no explosion).

## Results (selected audits)
- Ego depletion (RRR): d = 0.04 [−0.07, 0.15] ⇒ (n,u) = (0.04, 0.11) ⇒ fragile.
- Power posing → risk-taking: −0.033 [−0.085, 0.019] ⇒ (−0.033, 0.052) ⇒ fragile.
- Power posing → testosterone: −4.077 [−9.801, 1.647] ⇒ (−4.077, 5.724) ⇒ fragile.
- Facial feedback (RRR): 0.03 [−0.11, 0.16] ⇒ (0.03, 0.135) ⇒ fragile.
- Mortality salience (ML4): g = 0.07 [−0.03, 0.17] ⇒ (0.07, 0.10) ⇒ fragile.
- Anchoring (meta): d = 0.876 [0.808, 0.943] ⇒ (0.876, 0.0675) ⇒ robust.

## Discussion
N/U provides an immediate, distribution-free *floor* on uncertainty for peer reviewers. The approach is auditable, algebraically consistent, and computationally trivial (O(1) per operation). It complements equivalence testing, Bayesian estimation, and Registered Reports.
**Limitations.** N/U does not track covariance; it provides worst-case (conservative) envelopes. For strong dependencies, extend with interval/affine arithmetic or fully probabilistic models.

## Policy & Practice Recommendations
1. Require (n, u) reporting for all primary claims.
2. Pre-specify desired precision (target u) in Stage-1 protocols.
3. Combine N/U with equivalence tests or Bayesian estimation for richer inference.

## Data & Code Availability
Validation corpus (70k+ cases), proofs, tolerances, and scripts: Zenodo dataset DOI 10.5281/zenodo.17221863.
This preprint includes a compact audit CSV and figure as supplementary files.

## Acknowledgments
We thank colleagues in metascience and replication initiatives. Any errors are our own.

## License
CC-BY-4.0.
