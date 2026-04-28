# EB Carrier Tier-1 Dataset Hunt — Findings 2026-04-28

**Goal:** Find a public behavioral dataset where the EB carrier exposes structure the original analysis qualitatively missed (Tier 1) — distinguishing from cases where it merely formalizes structure already named (Tier 2, e.g., Swensson 2024).

**Method:** PubMed search across FCT, FA, resurgence, matching law, behavioral economics. Filter for full-text PMC access. Score each candidate against EB Hunt Gate G1–G7.

According to PubMed.

## Sources reviewed

| Reference | DOI | Domain | PMC access |
|---|---|---|---|
| Gilroy et al. (2019) | [10.1080/17518423.2019.1646342](https://doi.org/10.1080/17518423.2019.1646342) | FCT + behavioral economics | abstract only |
| Kurtz et al. (2011) | [10.1016/j.ridd.2011.05.009](https://doi.org/10.1016/j.ridd.2011.05.009) | FCT meta-analytic review | abstract only |
| Walker & Snell (2013) | [10.3109/07434618.2013.785020](https://doi.org/10.3109/07434618.2013.785020) | AAC + challenging behavior meta | abstract only |
| Walker et al. (2018) | [10.1080/07434618.2018.1461240](https://doi.org/10.1080/07434618.2018.1461240) | FCT in schools | abstract only |
| Carr & Durand (1985) | [10.1901/jaba.1985.18-111](https://doi.org/10.1901/jaba.1985.18-111) | FCT founding paper | full text access blocked |
| Wacker et al. (1993) | [10.1901/jaba.1993.26-23](https://doi.org/10.1901/jaba.1993.26-23) | FCT + extinction/punishment | full text access blocked |
| **Shahan et al. (2024)** | [10.1016/j.beproc.2024.105082](https://doi.org/10.1016/j.beproc.2024.105082) | **Resurgence + DRA + extinction** | **full text via PMC11317034** |
| Falligant et al. (2022) | [10.1016/j.beproc.2022.104776](https://doi.org/10.1016/j.beproc.2022.104776) | Resurgence theory (ETBD) | abstract only |
| Klapes et al. (2023) | [10.1016/j.beproc.2023.104860](https://doi.org/10.1016/j.beproc.2023.104860) | Resurgence quantitative model fitting | abstract only |
| Lerman et al. (2024) | [10.1002/jaba.1045](https://doi.org/10.1002/jaba.1045) | FBA comparative effectiveness | full text via PMC10843530 |

## Gate scoring (G1–G7)

| Candidate | G1 rails | G2 collapsed? | G3 carrier | G4 new var | G5 interpretation Δ | G6 data | G7 additive | **Tier** |
|---|---|---|---|---|---|---|---|---|
| Swensson 2024 (control) | ✅ | ⚠ | ✅ | ✅ slack | ⚠ partial | ✅ | ✅ | **Tier 2** |
| Gilroy 2019 (FCT+economics) | ✅ rate × price | ⚠ | ✅ | ✅ essential value bound | ⚠ unknown without data | abstract only | ✅ | unscored |
| Carr & Durand 1985 | ✅ PB + comm | ✅ | ✅ | ✅ | ⚠ field already names function transfer | ⚠ access | ✅ | likely Tier 2 |
| **Shahan et al. 2024** | ✅ target + alt | ✅ | ✅ | ✅ **conservation + bound** | ✅ **plausible** | ✅ figures in PMC | ✅ | **candidate Tier 1** |
| Lerman 2024 FBA | partial | ⚠ | ⚠ | — | — | ✅ | ✅ | Tier 3 |

## Top candidate: Shahan et al. (2024) Resurgence

[10.1016/j.beproc.2024.105082](https://doi.org/10.1016/j.beproc.2024.105082) — PMC11317034

### Paradigm

Three-phase resurgence procedure (rats, $n=36$):
- **Phase 1 (Baseline, 32 sessions):** Target lever press reinforced VI 30s. Stable rate ≈ 29 responses/min.
- **Phase 2 (Treatment):** Target on extinction; alternative lever reinforced. Two conditions:
  - **All On**: alternative reinforced every session (continuous DRA)
  - **CDT** (Contingency Discrimination Training): alternative reinforced in alternating sessions (on/off cycling)
  - Two durations: 4 cycles vs 8 cycles
- **Phase 3 (Resurgence test, 10 sessions):** Both levers on extinction. Resurgence = increase in target responding when alternative also unavailable.

### What Shahan et al. report (standard analysis)

- ANOVAs with main effects, η² effect sizes
- "Target rates were higher for CDT groups than for All On groups during Phase 2"
- "Resurgence occurred and was larger for All On than CDT"
- "4 cycles of CDT as effective as 8" — interpretation: discrimination saturates by 4 cycles
- Multiple competing theories invoked: Bouton's context theory, Resurgence-as-Choice-in-Context (RaC2)

### What the EB carrier would surface (Tier 1 hypothesis)

**The two rails (target rate, alternative rate) have a saturation/conservation structure during Phase 2 that is not formally named in the resurgence literature.**

Carrier object:
$$
L_t = (R^{\text{target}}_t, R^{\text{alt}}_t)
$$
with hypothesised bound (per-session conservation):
$$
R^{\text{target}}_t + R^{\text{alt}}_t \leq R^{\text{baseline}}
$$

where $R^{\text{baseline}} \approx 29$ (the asymptotic VI 30s rate from Phase 1).

**Three Tier 1 readings the carrier admits:**

1. **Conservation during Phase 2.** If $R^{\text{target}}_t + R^{\text{alt}}_t \approx R^{\text{baseline}}$ throughout Phase 2, the rail trade is *strict* (one rail's gain = the other rail's loss). Standard analysis treats target↓ and alt↑ as independent dependents; conservation makes them algebraically linked. Resurgence-as-Choice theory implies relative valuation but doesn't formalise total-rate conservation as a constraint.

2. **Resurgence bounded by Phase 2 residual.** The "extinguished" target rate at end of Phase 2 is near-zero but positive. Phase 3 resurgence magnitude is bounded by this residual (latent persistence). The carrier expresses this as a width $b$ on the target rail at end of Phase 2; resurgence magnitude can't exceed this width without the conservation constraint being violated. This reframes resurgence theories: it's not "memory of original training" but "bound width that hadn't fully contracted under DRA."

3. **CDT saturation as bound contraction.** The 4-cycle ≈ 8-cycle equivalence finding (which Shahan et al. attribute to discrimination saturation) becomes structurally explicit: the bound width contracts asymptotically to its CDT-floor; additional cycles can't tighten it further. The 4 ≈ 8 finding is a *prediction* of the carrier reading, not a surprise.

### Why this is Tier 1 (G5 passes)

The resurgence field has rich quantitative theory (RaC, RaC2, ETBD, behavioural momentum). What it doesn't have is a **conservation law** for total response rate during DRA. The carrier would supply that. If conservation holds:
- The "transfer of behaviour from target to alternative" is not metaphor — it's algebraic.
- Resurgence under All On (where alternative was reinforced every session) reflects a *less contracted* bound than CDT (where the discrimination forces tighter contraction).
- The bound width $b$ is a single quantity that predicts both Phase 2 endpoint and Phase 3 magnitude — replacing two separately reported outcomes with one.

This passes G5 (interpretation change) where Swensson failed: Swensson's caption already named the inverse relation. Shahan et al. report two rails separately and use parametric models to fit them, but no analysis they cite expresses the conservation hypothesis directly.

### Why this is not yet proven Tier 1

The conservation hypothesis is testable but unverified. To verify:
- Digitize Shahan Figure 1 (target + alternative rates per session, both Phase 2 and Phase 3) for all four groups.
- Compute $R^{\text{target}}_t + R^{\text{alt}}_t$ per session.
- Test whether the sum is constant (strict conservation) or follows a predictable trajectory (bound saturation).
- Check whether Phase 2 endpoint width $b^{\text{target}}$ predicts Phase 3 resurgence magnitude across groups.

If conservation holds: Tier 1 confirmed, paper can be written.
If conservation fails: the carrier still surfaces the bound width as new variable but the "law" framing is downgraded to "structural constraint with violations."

## Other candidates worth probing later

**Behavioural economics demand curves** (Gilroy 2019 lineage). Demand $Q = Q_0 \exp(-\alpha P)$ with parameters $Q_0$ and $\alpha$. The carrier could surface that the essential value $1/\alpha$ has a bound width derived from cross-session reinforcer-magnitude variation. Public datasets are limited; would need to access full Gilroy paper or equivalent.

**Stimulus equivalence / derived relations.** Multi-class derived relation tests (transitivity, equivalence) where derived performance is bounded by trained performance. Carrier could surface a bound between trained and derived rails. Publicly accessible datasets exist in JEAB but PMC access is uneven.

**Behavioural momentum / disrupter studies.** Pre-disruption rate × resistance-to-change product. The carrier could express momentum as a centre×width pair where mass=rate, velocity=resistance. Conservation under disruption is the structural prediction.

**Probability discounting** with shared subject. Indifference-point ratios across delays cancel subject-specific impulsivity (the $k$ parameter). Tier 1 if the carrier surfaces shared-latent cancellation that the field's $\log(k)$ analysis treats as separate per condition.

## Recommended next step

**Digitize Shahan et al. 2024 Figure 1.** It's the single most defensible Tier 1 candidate from this hunt:
- Full text + figure available in PMC (PMC11317034).
- Two-rail structure with hypothesised conservation.
- Resurgence literature has interpretive room (multiple competing theories).
- Conservation hypothesis is concrete and testable from the published figure alone.

If conservation holds, the paper writes itself: "Behavioural Conservation Under Differential Reinforcement of Alternative Behaviour: An EB Carrier Reading of Shahan et al. (2024)."

If conservation fails or is partial, the bound-width finding is still novel but framed as a structural constraint rather than a law.

Either way, the hunt has identified a target where the carrier could plausibly *change interpretation*, not just reformulate it.

According to PubMed, primary source: Shahan TA, Sutton GM, Avellaneda M (2024). [DOI](https://doi.org/10.1016/j.beproc.2024.105082).

## Provenance

- Search performed via PubMed MCP, 2026-04-28
- Searches: FCT + single-case (10 hits), resurgence + extinction (203 hits, top 10 reviewed), FCT + free-full-text filter (151 hits, top 10 reviewed)
- Full text retrieved for: Lerman 2024 (PMC10843530), Shahan 2024 (PMC11317034)
- Older PMCs (Carr & Durand 1985 PMC1307999, Wacker 1993 PMC1297717) returned empty full_text — likely metadata-only PMC entries for pre-1995 journals
