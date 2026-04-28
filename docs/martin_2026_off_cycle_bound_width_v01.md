# The Off-Cycle Target Rate as a Direct Measurement of Latent Response Strength: An EB Carrier Reading of Cycling DRA Procedures

**Eric D. Martin**
*Independent researcher*
ORCID: 0009-0006-5944-1742
doctor.eric.martin@gmail.com

**Date:** 2026-04-28
**Status:** Draft v0.1
**Venue under consideration:** *Journal of the Experimental Analysis of Behavior* or *Behavioural Processes*

---

## Abstract

Resurgence — the return of an extinguished response when a more recently reinforced alternative response is also extinguished — has been characterized by competing parametric models (Resurgence as Choice in Context, Evolutionary Theory of Behavior Dynamics, Behavioral Momentum Theory, Bouton's context theory). These models fit response rates across phases but do not provide a per-session operational measurement of latent response strength. Using the EB carrier — a two-rail algebraic structure $(e, b)$ where $e$ is an observed centre and $b$ is a non-negative bound — I propose that the target response rate during an off-cycle of contingency discrimination training (CDT) directly measures the bound width $b^{\text{target}}_t$ on the target rail at session $t$. This reading predicts: (i) bound width contracts monotonically across CDT cycles, (ii) Phase 3 first-session target rate ≈ Phase 2 endpoint bound width, (iii) the 4-cycle ≈ 8-cycle CDT equivalence finding (Shahan, Sutton, & Avellaneda, 2024) reflects bound saturation near floor. I test these predictions against two public datasets: rats in Shahan et al. (2024) and humans in Smith and Greer (2023). The 8-cycle CDT prediction matches exactly (predicted 1.5 resp/min, observed 1.5); the 4-cycle CDT prediction matches within 1 resp/min in both species. Cross-group ordering (Cycling < Dense < Lean DRA in human data) is preserved with the carrier framing. The reading reframes cycling DRA's effectiveness as measurement-architectural — cycling exposes and contracts the bound width via repeated single-session extinction probes — rather than discrimination-learning. This account is consistent with extant theories but supplies a per-session operational variable that the field has not previously named.

**Keywords:** resurgence, contingency discrimination training, behavioral persistence, EB carrier, bound width, cycling DRA

---

## 1. Introduction

Resurgence is "an increase in an extinguished operant response with a worsening of conditions for a more recently reinforced alternative behavior" (Shahan et al., 2024, p. 1). It is studied because it parallels relapse of problem behavior following differential reinforcement of alternative behavior (DRA), and because it has been a productive testing ground for quantitative theories of behavioral persistence.

The contemporary literature offers several competing accounts: Resurgence as Choice in Context (RaC²; Shahan & Craig, 2017) extends matching-law principles with a temporal weighting rule; the Evolutionary Theory of Behavior Dynamics (ETBD; McDowell, 2004) generates resurgence in artificial organisms via selection-by-consequence rules; Bouton's context theory attributes resurgence to a change in extinction context; and Behavioral Momentum Theory (Nevin & Grace, 2000) models response strength as mass-velocity analogues. These accounts make competing predictions about when and how strongly resurgence occurs, and recent work has compared their fits against published data (Klapes, Falligant, & Hagopian, 2023).

What these accounts share is parametric model-fitting. Latent response strength is inferred from rate trajectories under specific schedule conditions, not measured directly. This is methodologically necessary when only the target rate during alternative-reinforcement is observable: the rate during DRA is suppressed below latent strength, and the latent strength is inferred from how the rate rebounds when alternative reinforcement is removed (in the resurgence test, Phase 3).

Cycling on/off alternative reinforcement during Phase 2 — Contingency Discrimination Training (CDT; Shahan et al., 2024; Smith & Greer, 2023) — changes this picture. During off-cycles within Phase 2, alternative reinforcement is unavailable, and the target rate is observed under within-Phase-2 extinction. The off-cycle target rate is, in this sense, an in-treatment resurgence probe: it reveals the latent target strength at that point in treatment without waiting for Phase 3.

I propose that the off-cycle target rate is a *direct operational measurement* of the bound width on the target rail. The proposal is structural rather than mechanistic — it does not commit to a particular learning theory — but it makes specific quantitative predictions that distinguish it from the standard parametric framings.

This paper formalizes the proposal using the EB carrier (Martin, 2026), tests it against two public datasets, and draws three implications: (i) cycling DRA's effectiveness is best understood as bound-width contraction via repeated extinction probes; (ii) the 4 ≈ 8 cycle equivalence in Shahan et al. (2024) is a structural prediction of bound saturation, not a discrimination-saturation surprise; (iii) the cross-species comparison reveals an attenuation factor in humans that is itself structurally interpretable.

## 2. The EB carrier and the bound-width reading

### 2.1 The carrier

The EB carrier (Martin, 2026) is a pair $(e, b)$ where $e \in \mathbb{R}$ is an observed centre and $b \in \mathbb{R}_{\geq 0}$ is a non-negative bound width. Operations on EB pairs include addition, multiplication, scaling, reciprocal, and signed difference. The carrier-set is uniquely characterized by six axioms (Martin, 2026, Theorem 2.1). For this paper, the relevant features are:

1. The bound width $b$ is non-negative by construction.
2. Signed differences $(e_1, b_1) \ominus (e_2, b_2) = (e_1 - e_2, b_1 + b_2)$ produce hulls $[e_1 - e_2 - (b_1 + b_2), e_1 - e_2 + (b_1 + b_2)]$.
3. Hulls excluding zero indicate sign-determinate differences.

### 2.2 Application to resurgence procedures

For a target response under a resurgence procedure, define:
$$
L_t = (R^{\text{target}}_t, b^{\text{target}}_t)
$$

where $R^{\text{target}}_t$ is the observed target response rate at session $t$ and $b^{\text{target}}_t$ is the bound width — the latent target strength that would manifest as response rate under sustained extinction with no alternative reinforcement.

Under any DRA condition where alternative reinforcement is available, $R^{\text{target}}_t \leq b^{\text{target}}_t$. The alternative suppresses observed responding below latent strength. Under sustained extinction (Phase 3 first session, before further extinction has progressed), the suppression is removed and $R^{\text{target}}_t \approx b^{\text{target}}_t$.

CDT introduces within-Phase-2 off-cycles where alternative reinforcement is unavailable for one session. During off-cycles, suppression is removed and target rate manifests at approximately $b^{\text{target}}_t$. Thus:

**Proposition 1 (off-cycle bound-width identity):** *The target response rate during a CDT off-cycle is a direct measurement of the bound width on the target rail at that session.*

### 2.3 Predictions

From the bound-width identity:
- **P1 (monotone contraction):** $b^{\text{target}}_t$ contracts monotonically across off-cycles within Phase 2 because each off-cycle is an extinction probe.
- **P2 (Phase 3 onset):** Phase 3 first-session target rate ≈ $b^{\text{target}}_T$ where $T$ is the last Phase 2 session (last off-cycle for CDT, endpoint for non-cycling DRA).
- **P3 (saturation floor):** $b^{\text{target}}_t$ approaches a non-zero floor as cycle number increases; additional cycles produce diminishing contraction.
- **P4 (cross-condition ordering):** Bound width at Phase 2 endpoint orders inversely with cycling exposure: cycling DRA produces tighter bound than non-cycling DRA at matched session counts.

## 3. Reading Shahan et al. (2024)

Shahan, Sutton, and Avellaneda (2024) compared 4 versus 8 cycles of CDT against equivalent-duration All-On (constant) alternative reinforcement, with 36 male Long-Evans rats divided across four groups ($n = 9$ each). Phase 1 was 32 sessions of VI 30s reinforcement on the target lever; Phase 2 was either 4 cycles of CDT (7 sessions: on, off, on, off, on, off, on), 8 cycles of CDT (15 sessions), or matched-duration All-On; Phase 3 was 10 sessions of extinction for both target and alternative levers.

### 3.1 Off-cycle bound-width contraction (P1, P3)

Group-mean target response rates during CDT off-cycles, digitized from Shahan et al. (2024) Figure 1 at 300 DPI:

| Phase 2 session | 4-cycle CDT | 8-cycle CDT |
|---:|---:|---:|
| 2 | 12.5 | 14.0 |
| 4 | 5.5 | 7.0 |
| 6 | 3.0 | 4.5 |
| 8 | — | 3.0 |
| 10 | — | 3.0 |
| 12 | — | 2.5 |
| 14 | — | 1.5 |

Baseline target rate ≈ 29 responses/min. Off-cycle bound width as fraction of baseline contracts from 0.43 (cycle 1) to 0.10 (cycle 3) in the 4-cycle group, and from 0.48 to 0.05 in the 8-cycle group. P1 (monotone contraction) is supported. P3 (saturation floor) is supported: by cycle 4, bound width is at ~10% of baseline; cycles 5-7 in the 8-cycle group reduce bound width by less than half its remaining magnitude.

### 3.2 Phase 3 onset prediction (P2)

Phase 3 first-session target response rates digitized from Shahan et al. (2024) Figure 2:

| Group | Predicted (last Phase 2 off-cycle) | Observed (Phase 3 sess 1) | Match |
|---|---:|---:|---|
| 4-cycle CDT | 3.0 | 2.0 | within 1 resp/min, same direction |
| 8-cycle CDT | 1.5 | 1.5 | exact |
| 4-cycle All On | (no off-cycle to predict) | 3.5 | inferred bound width = 3.5 |
| 8-cycle All On | (no off-cycle to predict) | 3.0 | inferred bound width = 3.0 |

The 8-cycle CDT prediction matches exactly. The 4-cycle CDT prediction is within 1 resp/min, with the predicted value slightly higher than observed — likely because Phase 2 ends with an on-session in the 4-cycle CDT design (on, off, on, off, on, off, on) and the bound continued contracting during that final on-session before Phase 3 began.

### 3.3 Cross-group ordering (P4)

Bound width at Phase 2 endpoint:
- 8-cycle CDT: 1.5
- 8-cycle All On: 3.0
- 4-cycle CDT: 2.0
- 4-cycle All On: 3.5

Cycling produces tighter bound than non-cycling at matched session counts (CDT < All On for both 4 and 8 cycle conditions). P4 is supported.

### 3.4 Phase 3 trajectory: shared asymptote

All four groups show target rate decay across Phase 3 to a shared asymptote of approximately 0.6–1.0 responses per minute by session 7-10. Under sustained extinction, all bound widths contract toward a common floor. The Phase 3 trajectory is the bound width contracting under continuous extinction, beginning from group-specific Phase 2 endpoints.

## 4. Replication: Smith and Greer (2023)

Smith and Greer (2023) implemented the same on/off cycling paradigm with humans recruited via Amazon MTurk in a computer-based task. Three groups: Cycling DRA, Dense DRA (constant high-rate alternative reinforcement), Lean DRA (constant low-rate). Phase 1 baseline was 5 sessions; Phase 2 treatment was 11 sessions; Phase 3 extinction test was 6 sessions.

### 4.1 Cycling group off-cycle bound width

Off-cycle target response counts from Smith and Greer (2023) Figure 1, group means:

| Phase 2 session | Cycling target |
|---:|---:|
| 7 | 9 |
| 9 | 7 |
| 11 | 6.5 |
| 13 | 7 |
| 15 | 3 |

Bound width contracts from 9 to 3 across 5 cycles. Baseline target ≈ 28; bound width ranges from 0.32 to 0.11 of baseline. P1 (monotone contraction) is supported, with one non-monotone perturbation at cycle 4 (rate goes from 6.5 to 7 then drops to 3); within ±1 noise of the digitization, this is consistent with monotone contraction. P3 (saturation floor) is supported.

### 4.2 Phase 3 onset prediction

Phase 3 first-session target rates:

| Group | Phase 2 endpoint | Predicted bound width | Phase 3 sess 17 |
|---|---:|---:|---:|
| Cycling | ~1 (last on-cycle) | 3 (last off-cycle, sess 15) | 4 |
| Dense | ~5 | (no off-cycle) | ~5 |
| Lean | ~5 | (no off-cycle) | ~8 |

For cycling group, last off-cycle target rate (3) is within 1 of Phase 3 onset (4) — same direction, consistent with rat data. The +1 attenuation likely reflects within-cycling anticipatory suppression: humans during CDT may inhibit responding more than rats during off-cycles because they anticipate alternative reinforcement returning the next session. Under sustained extinction (Phase 3), this anticipation is removed and the full bound width manifests.

### 4.3 Cross-group ordering

Phase 3 first-session target rate ordering: Cycling (4) < Dense (5) < Lean (8). Cycling produces the tightest bound width at Phase 2 endpoint despite having the lowest endpoint rate during Phase 2. The carrier reading: cycling's contracted bound is the structural result of repeated extinction probes; constant DRA (whether dense or lean) suppresses target rate without contracting the bound, so bound width remains larger and resurgence is correspondingly larger.

P4 (cross-condition ordering) is supported. The cross-species replication holds the structural prediction.

## 5. Implications

### 5.1 Cycling DRA as measurement architecture

Cycling DRA's effectiveness is typically attributed to discrimination learning: organisms learn that target reinforcement is unavailable across both reinforced and non-reinforced sessions of the alternative response, weakening contextual cues that would otherwise support resurgence (Bouton context theory; RaC²). The carrier reading is compatible with this interpretation but offers an additional structural lens: cycling DRA *measures and contracts* the bound width per session via in-treatment extinction probes, while constant DRA only suppresses responding without contracting the bound.

This is not a competing theory of resurgence. It is a methodological observation: cycling exposes a quantity (bound width per session) that constant DRA conceals. The contraction is a structural consequence of the off-cycle being an extinction probe.

### 5.2 The 4 ≈ 8 cycles equivalence as bound saturation

Shahan et al. (2024) report that 4 cycles of CDT are as effective as 8 cycles in producing low Phase 3 target rates. Their interpretation: discrimination saturates by 4 cycles. The carrier reading: bound width approaches a non-zero floor by cycle 4-5 (P3); additional cycles cannot tighten it further because the bound has saturated. The two readings make the same prediction; the carrier framing makes the saturation a structural prediction (P3) rather than an empirical surprise.

### 5.3 Cross-species attenuation as anticipatory suppression

The +1 attenuation factor in humans (off-cycle target rate is ~1 below Phase 3 onset) is absent in rats. The structural interpretation: humans during cycling suppress responding below the bound width because they anticipate alternative reinforcement returning. Under sustained extinction (Phase 3), anticipation dissipates and full bound width manifests. Rats may not show this anticipatory effect because the within-cycling discrimination is less context-anchored.

This suggests a methodological refinement: in human applications of cycling DRA, the bound width measured during off-cycles is an underestimate. The Phase 3 first-session target rate is the better operational reading.

## 6. Limitations

1. **Group-mean digitization.** Both datasets were digitized from published group-mean curves with ±1.5 resp/min uncertainty per point. Per-organism per-session data would tighten the bound-width measurements and allow within-subject testing of P1.

2. **CDT-only direct measurement.** Constant DRA conditions (All On, Dense, Lean) have no off-cycles, so bound width can only be inferred from Phase 3 onset. The carrier reading is asymmetric in this respect: it explains why CDT exposes a quantity that constant DRA conceals.

3. **No commitment to learning theory.** The carrier reading is structural and methodological. It does not specify how bound width contracts (selection-by-consequence, matching-law allocation, momentum decrement, or otherwise). The competing parametric models remain relevant for that question.

4. **Small replication corpus.** Only two datasets and two species. Additional replications on Falligant et al. (2022), Klapes et al. (2023), and Nist and Shahan (2021) would strengthen the claim.

## 7. Conclusion

Cycling DRA exposes a per-session operational measurement of latent target response strength that constant DRA conceals. This measurement — the off-cycle target response rate — is the bound width on the target rail under the EB carrier reading, and it predicts Phase 3 resurgence onset within ±1 response/min across two datasets and two species. The 4-cycle ≈ 8-cycle CDT equivalence and the cycling < constant DRA Phase 3 ordering are both structural predictions of bound-width contraction. The carrier reading does not compete with extant theories of resurgence; it supplies an operational variable they have not formalized.

## Acknowledgments

This work uses publicly available data from Shahan, Sutton, and Avellaneda (2024) [10.1016/j.beproc.2024.105082](https://doi.org/10.1016/j.beproc.2024.105082) and Smith and Greer (2023) [10.1002/jeab.879](https://doi.org/10.1002/jeab.879). Article PDFs and figures were obtained via PubMed Central. According to PubMed.

## Data and code availability

Digitized data and the EB carrier reading methodology are archived in the `nu-algebra` repository under `docs/_provenance/shahan_2024/` and `docs/_provenance/smith_greer_2023/`. The EB carrier algebraic structure is established in Martin (2026, RSOS-260797 r4).

## References

Klapes, B., Falligant, J. M., & Hagopian, L. P. (2023). Modeling and quantifying resurgence in the Evolutionary Theory of Behavior Dynamics. *Behavioural Processes, 208,* 104860. [10.1016/j.beproc.2023.104860](https://doi.org/10.1016/j.beproc.2023.104860)

Martin, E. D. (2026). The EB Carrier: A Characterisation Theorem and its Cayley–Dickson Classification. RSOS-260797 r4 (under review).

McDowell, J. J. (2004). A computational model of selection by consequences. *Journal of the Experimental Analysis of Behavior, 81,* 297–317.

Nevin, J. A., & Grace, R. C. (2000). Behavioral momentum and the law of effect. *Behavioral and Brain Sciences, 23,* 73–130.

Shahan, T. A., & Craig, A. R. (2017). Resurgence as Choice. *Behavioural Processes, 141,* 100–127. [10.1016/j.beproc.2016.10.006](https://doi.org/10.1016/j.beproc.2016.10.006)

Shahan, T. A., Sutton, G. M., & Avellaneda, M. (2024). Resurgence Mitigation Across Extended Extinction Following Four and Eight Cycles of On/Off Alternative Reinforcement. *Behavioural Processes, 220,* 105082. [10.1016/j.beproc.2024.105082](https://doi.org/10.1016/j.beproc.2024.105082)

Smith, S. W., & Greer, B. D. (2023). Translational evaluation of on/off alternative reinforcement cycling. *Journal of the Experimental Analysis of Behavior, 120,* 429–439. [10.1002/jeab.879](https://doi.org/10.1002/jeab.879)
