# A Methodological Note on Applying the EB Carrier Algebra to IOA-Reported Behavioral Data

**Worked example using Swensson et al. (2024)**

Eric D. Martin
Independent Researcher
ORCID: 0009-0006-5944-1742
Date: 2026-04-28

---

## Abstract

This note demonstrates the application of the Expressed--Bound (EB) carrier algebra — the unique pair algebra over $\mathbb{R} \times \mathbb{R}_{\geq 0}$ satisfying axioms A1--A6 (Martin, 2026, RSOS-260797 r4) — to interobserver-agreement (IOA) data reported in Swensson et al. (2024). I convert reported IOA percentages to explicit uncertainty bounds via a worst-case interval-arithmetic conversion, then propagate those bounds through aggregation across participants. The contribution is methodological: a deterministic, audit-defensible way to make IOA-implied measurement precision arithmetic-ready. The worked example does not alter Swensson et al.'s substantive findings, which were already well supported by their methods.

---

## 1. Introduction

Interobserver agreement (IOA) is a standard reliability metric in applied behavior analysis. It is reported as a percentage, which indicates measurement reliability but does not propagate through arithmetic operations used to aggregate observations across sessions, participants, or studies. When researchers compute composite scores, weighted means, or meta-analytic estimates, the implied uncertainty from IOA is typically left implicit.

This note shows that the EB carrier algebra (Martin, 2026) — a pair-valued arithmetic in which each value carries an explicit non-negative uncertainty bound — provides a deterministic conversion from IOA to propagatable bounds. The conversion is conservative and reproducible. It is restricted to the measurement layer; it does not perform statistical inference, model temporal dependencies, or replace standard behavioral analysis methods.

The worked example uses IOA values from Swensson et al. (2024), a multiple-baseline study of caregiver-implemented telehealth coaching for three children with autism spectrum disorder.

---

## 2. The EB Carrier Algebra: Formal Foundation

The EB carrier is the ordered pair $(e, b) \in \mathbb{R} \times \mathbb{R}_{\geq 0}$, where $e$ is an asserted expressed value and $b$ is a non-negative admissible deviation. The pair algebra is fixed by six axioms (A1--A6) imposing exact enclosure preservation, exact tightness, commutativity, associativity, non-negativity of bounds, and local realisability with bounded memory and latency. The unique algebra under these axioms (Martin, 2026, RSOS-260797 r4, currently under review) has the following operations:

- **Addition:** $(e_1, b_1) \oplus (e_2, b_2) = (e_1 + e_2,\ b_1 + b_2)$
- **Multiplication:** $(e_1, b_1) \otimes (e_2, b_2) = (e_1 e_2,\ |e_1| b_2 + |e_2| b_1)$
- **Scalar:** $a \odot (e, b) = (a e,\ |a| b)$

These operations preserve non-negativity, satisfy associativity, and produce conservative bounds (verified across 70,054 deterministic test cases; Martin, 2025).

The framework was previously named "N/U Algebra" in earlier work (Martin, 2025); the present axiomatic characterisation (Martin, 2026) establishes that the same algebra is the unique solution within its axiom class.

---

## 3. Method

### 3.1 Data source

I extract IOA values from Table 1 of Swensson et al. (2024):

| Participant | IOA (%) | Coverage              |
|-------------|---------|-----------------------|
| Alex        | 98.25   | 75% of sessions       |
| Aden        | 99.33   | 58.35% of sessions    |
| Ida         | 98.50   | 78.5% of sessions     |

### 3.2 IOA → uncertainty conversion

For a session of $N$ trials with reported agreement fraction $f$, the worst-case count of disagreements is $N(1 - f)$. Treating that as the conservative bound on measurement-derived counts gives:

$$u_{\text{IOA}} = N \times (1 - f)$$

This is the interval-arithmetic worst-case bound for a count-based agreement procedure. It is conservative by construction: the actual disagreement count cannot exceed this worst-case bound.

In Swensson et al. (2024), each session contained five trials and three sessions were conducted per day. I take $N = 15$ (the daily trial count, reflecting the coarsest natural aggregation unit before across-day combination). The choice is stated explicitly; analysts preferring session-level uncertainty would substitute $N = 5$ and propagate accordingly.

I add a small device-precision term $u_{\text{device}} = 0.1$ (accounting for telehealth video-coding ambiguity), giving total uncertainty:

$$u_{\text{total}} = u_{\text{IOA}} + u_{\text{device}}$$

### 3.3 Pair construction and propagation

Each participant's measurement is encoded as $(e, b)$ where $e$ is the reported mean performance (extracted from Figure 1, mastery range) and $b$ is $u_{\text{total}}$. Aggregation across participants uses EB addition; the mean uses EB scalar multiplication.

---

## 4. Results

### 4.1 IOA-derived bounds

| Participant | $u_{\text{IOA}}$ | $u_{\text{device}}$ | $u_{\text{total}}$ | $(e, b)$       |
|-------------|------------------|---------------------|--------------------|----------------|
| Alex        | 0.26             | 0.1                 | 0.36               | (4.2, 0.36)    |
| Aden        | 0.10             | 0.1                 | 0.20               | (4.8, 0.20)    |
| Ida         | 0.23             | 0.1                 | 0.33               | (4.5, 0.33)    |

Nominal values $e$ represent approximate mastery-level performance from Figure 1; exact session-level data would require digitisation.

### 4.2 Aggregation

Aggregating via EB addition:

$$\sum_i (e_i, b_i) = (4.2 + 4.8 + 4.5,\ 0.36 + 0.20 + 0.33) = (13.5,\ 0.89)$$

Mean via scalar:

$$\tfrac{1}{3} \odot (13.5, 0.89) = (4.5,\ 0.30)$$

The group mean is 4.5 correct responses with conservative uncertainty bound $\pm 0.30$.

### 4.3 Comparison to root-sum-square (RSS)

For reference, the Gaussian RSS aggregate of the three uncertainty values is:

$$\sqrt{0.36^2 + 0.20^2 + 0.33^2} \approx 0.52$$

The EB bound (0.89) is approximately $1.71\times$ the RSS bound. This factor matches the median ratio of 1.74 for addition operations across the 70,054-test validation suite (Martin, 2025), consistent with the EB algebra's conservative-by-construction property.

### 4.4 Monotonicity preservation

Ordering participants by individual uncertainty (Aden 0.20 < Ida 0.33 < Alex 0.36) is preserved through aggregation, consistent with the monotonicity property of EB addition.

---

## 5. What this worked example does and does not show

**What it shows.**

- IOA percentages can be converted to propagatable uncertainty bounds via a deterministic, conservative formula.
- The EB carrier algebra preserves bound order through aggregation and produces bounds approximately $1.5\text{--}2\times$ the RSS reference, consistent with conservative-by-construction propagation.
- Under conservative worst-case propagation, all three participants in Swensson et al. (2024) demonstrated mastery-level responding (group mean 4.5, conservative lower bound 4.2 of 5 trials).

**What it does not show.**

- The example does not test whether telehealth coaching is more or less effective than other delivery methods.
- It does not address learning trajectories, gap effects, or rate of acquisition. These require interrupted time-series methods, which are outside the EB algebra's scope.
- It does not produce p-values or detect change points.
- It does not alter any substantive finding of Swensson et al. (2024). Their data quality was excellent (IOA $> 98\%$) before this analysis, and their conclusion that participants learned the target response remains as supported as it was.

The contribution is methodological transparency, not new empirical findings.

---

## 6. Scope note

An earlier version of this analysis (Martin, October 2025; subsequently withdrawn) attempted to apply EB operations to a time-series gap-effect question on Aden's data following a 6-week session break. The question itself — whether the break affected Aden's trajectory — is data-driven: Figure 1 of Swensson et al. (2024) shows a visibly different pattern pre- and post-break, and asking the question formally is appropriate. The error was in tool choice. EB operations propagate measurement uncertainty through arithmetic; they do not perform interrupted time-series analysis, regression, or hypothesis testing. The earlier version produced p-values that the algebra cannot generate.

The earlier version was withdrawn after temporal-separation review and external consultation in October 2025. The present paper restricts to measurement-layer propagation only. The time-series question about Aden's trajectory remains a valid scientific question; the appropriate tool is interrupted time-series analysis, not the EB algebra.

This note is included for transparency rather than for emphasis. The retraction was correct; the underlying question was not the error.

---

## 7. Discussion

### 7.1 Where measurement-layer propagation adds value

Behavioral research routinely reports IOA as a percentage without propagating that precision estimate through subsequent calculations. Three application contexts where deterministic propagation may be useful:

- **Meta-analysis.** Aggregating across studies with varying IOA (e.g., $75\%\text{--}99\%$), conservative bound propagation could supplement sample-size weighting with measurement-uncertainty weighting.
- **Multi-observer aggregation.** When combining data from observers with different agreement levels, EB propagation quantifies the accumulated bound transparently.
- **Audit-defensible workflows.** Deterministic $O(1)$ propagation may be preferred in regulatory contexts (insurance coverage, audit trails, FDA submissions) where sampling-based methods introduce reproducibility burdens.

### 7.2 Where it does not

Standard behavior-analytic conclusions about treatment effectiveness, learning, generalisation, and maintenance rest on visual analysis, effect-size calculation, and inferential statistics. Those layers are not displaced by measurement-uncertainty propagation; they sit above it. The two-layer separation (Layer 1 = measurement-uncertainty propagation; Layer 2 = inferential statistics) is the discipline that keeps each tool inside its scope.

### 7.3 Calibration

The IOA-to-$u$ conversion $u = N(1 - f)$ is conservative by construction but has not been empirically calibrated against repeated-measures variance in telehealth coding. Future work would compare propagated bounds to observed variance in independent recordings of the same sessions to establish calibration accuracy. The conservative direction of the bound is mathematically guaranteed; the magnitude of conservatism is an empirical question.

---

## 8. Conclusion

The EB carrier algebra provides a deterministic conversion from IOA percentages to propagatable measurement-uncertainty bounds. Applied to Swensson et al. (2024), conservative aggregation preserves all substantive findings: data quality is high, conclusions survive worst-case propagation. The contribution is transparency, not reanalysis.

The framework's axiomatic characterisation (Martin, 2026; RSOS-260797 r4) provides the formal foundation for applications of this kind beyond the worked example.

---

## References

Martin, E. D. (2025). *The NASA Paper & Small Falcon Algebra --- Numerical Validation Dataset* [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.17221863

Martin, E. D. (2026). *The Expressed--Bound (EB) Carrier: A Characterisation Theorem for the Unique Pair Algebra over $\mathbb{R} \times \mathbb{R}_{\geq 0}$ Admitting Native $O(1)$ Summary-State Propagation*. Preprint, Zenodo. https://doi.org/10.5281/zenodo.19676236 [Royal Society Open Science, RSOS-260797 r4, under review]

Swensson, R. M., Akers, J. S., Austin, M., Liu, R., Swafford, L. B., & Gerow, S. (2024). Teaching children with autism spectrum disorder to mand for answers to questions via telehealth: A caregiver implementation. *Behavioral Interventions, 39*(3), e2015. https://doi.org/10.1002/bin.2015

---

## Acknowledgments

I cite the published findings of Swensson et al. (2024) as the data source for this worked example. I thank Dr. Lee William Daffin for referral guidance.

---

## Data availability

The 70,054-test validation suite for the EB carrier algebra is publicly available at https://doi.org/10.5281/zenodo.17221863. IOA values used in this worked example are extracted from Table 1 of Swensson et al. (2024). No additional primary data were collected for this analysis.
