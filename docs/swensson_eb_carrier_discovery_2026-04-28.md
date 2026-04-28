# EB Carrier Reading of Swensson et al. (2024): The Slack/Residual Discovery

**Date:** 2026-04-28
**Status:** Canonical framing for any future paper using Swensson 2024 as a Tier-2 EB carrier demonstration. Supersedes prior framings ("methodology audit", "pre/post-break", "substrate-pair").

## Primary discovery

**The EB carrier reveals that the inverse relation between IDKPTM responding and correct answers is not merely two response paths moving in opposite directions. It is a constrained three-state system: correct answering, adaptive uncertainty-manding, and residual nonadaptive responding. The residual/slack term is computable from the published figure but is not separately modeled in the original analysis.**

## The third state

For the IDKPTM intervention with 5 trials per session (Swensson Methods §3.3.2), the saturation bound forces:
$$
K_t + I_t^{(1)} + \text{slack}_t = 5
$$

where $\text{slack}_t$ is trials with neither correct answering nor adaptive information-manding (incorrect, no response, off-task). The original Swensson analysis tracked $K_t$ and $I_t^{(1)}$ separately and noted their inverse relation; it did not separately surface the slack channel.

## What the slack profile shows (Claude-v2 digitization, intervention Set 1 sessions only)

| Child | n | Mean slack | Zero-slack sessions | Reading |
|---|---:|---:|---:|---|
| Alex | 41 | 1.27 | 16/41 (39%) | More residual/nonadaptive space; high session variability |
| Aden | 28 | **0.11** | **25/28 (89%)** | Near-clean adaptive transition; almost every trial yielded a procedure-appropriate response |
| Ida | 14 | 1.07 | 6/14 (43%) | Faster mastery than Alex but more residual space than Aden |

**Aden is the load-bearing case.** Across nearly all his intervention sessions, $I_t^{(1)} + K_t \approx 5$. In plain English: Aden was almost always doing one of the two adaptive things — either asking for the unknown answer or giving the correct answer. This is not "manding increased then correct answers increased." It is **residual responding being almost eliminated while behavior transferred between the uncertainty rail and the knowledge rail.**

## Behavioral state model from the carrier

| State | EB form | Plain meaning |
|---|---|---|
| No adaptive response | $(0, 0)$ | residual / error / nonresponse |
| Adaptive uncertainty | $(0, I)$ | "I don't know, please tell me" |
| Mixed transition | $(K, I)$ | some known, some adaptively unknown |
| Expressed mastery | $(K, 0)$ | known / correct |

## Why this is a carrier finding, not a coding finding

Swensson's coding rules could have surfaced slack if the authors had asked. They didn't. The EB carrier *forces* the question because of the saturation bound: an algebra on $(K, I)$ with $K + I \leq 5$ inherits a third quantity by structure. Once you have the carrier, the slack channel is not optional — it is the residual of the algebraic identity.

This is the contribution of "having the right tool": not new measurements, but the third state being formally exposed by the algebraic structure rather than left implicit in the trial-coding rubric.

## Tier rating

This is **Tier 2** under the EB Dataset Hunt Gate:
- ✅ G1: two meaningful rails ($K$, $I$)
- ✅ G2: original analysis treated rails separately, did not formally name slack
- ✅ G3: EB carrier defines $L_t = (K_t, I_t)$ with bound
- ✅ G4: EB generates new variable (slack)
- ⚠ G5 (partial): interpretation extends rather than overturns — the original "inverse relation" caption already named the qualitative pattern
- ✅ G6: data digitizable from public figure
- ✅ G7: claim is non-adversarial (formalization, not correction)

For a Tier-1 ("science missed structure") flagship, the next target should score full G5 — a dataset where the carrier exposes a phenomenon the authors had no qualitative grasp of.

## Secondary findings (kept; not headline)

### Stimulus-control onset

Operationalizable as the first session $s^*$ such that for all $s \geq s^*$, $K(s) + I(s) \geq 4$:
- Aden: session 10 (immediate)
- Ida: session 15
- Alex: never strict criterion (high variability)

This is sharper than mastery (which only sees the K-rail saturation). Stimulus control is "the child reliably engages with the procedure"; mastery is "the child reliably gives the correct answer." The 29-session gap between stimulus-control onset and mastery for Aden is the **acquisition transition**, structurally invisible in conventional mastery-criterion reporting.

### Cross-child mastery-time ratios with procedural cancellation

Under EB division (Memoirs Prop 28.2.1), shared procedural $\theta$ (telehealth coaching, prompt schedule, trial structure) cancels in the centre rail:

- $\xi_{\text{Aden/Alex}} = (0.65, 0.144)$, hull $[0.51, 0.79]$
- $\xi_{\text{Ida/Alex}} = (0.43, 0.126)$, hull $[0.31, 0.56]$
- $\xi_{\text{Ida/Aden}} = (0.667, 0.230)$, hull $[0.44, 0.90]$

Child-specific intraverbal-acquisition rates differ by factor 2–3 with shared procedure algebraically removed. This is mathematical not behavioral and belongs in an appendix.

## Appendix-grade findings

### Aden's six-week break

Pre-break (sessions 30–32) $I^{(1)} \in \{2, 2, 4\}$ mean 2.67. Post-break (sessions 33–35) $I^{(1)} \in \{2, 2, 2\}$ mean 2.0. Signed difference EB pair $(-0.67, 1.0)$ has hull $[-1.67, 0.33]$ — **straddles zero**.

Caveat: Aden's IDKPTM was already declining before the break as he learned answers. The break does not cleanly isolate the break-induced decrement from the ongoing learning trajectory. The 3-session window is too narrow for a robust signed-difference claim.

The wider acquisition-transition comparison (Phase A vs Phase B over the full ceiling vs full transition) is robust and belongs in the main text. The break per se is a contextual note for the appendix.

## Recommended paper structure (if revising v0.1)

| Section | Content | Source data |
|---|---|---|
| §1 Intro | Inverse-relation framing from Swensson; gap = no formal model of third state | Swensson Fig 1 caption |
| §2 Carrier | EB carrier ($L_t = (K_t, I_t)$, bound, slack as residual) | Carrier-set theorem (RSOS-260797 r4) |
| §3 Reading | Three-state behavioral model + slack profile + Aden's 89% near-zero slack | Three-source digitization (this repo) |
| §4 Stimulus-control onset | Operational definition + per-child results | Carrier + digitization |
| **Headline finding** | Slack as third behavioral channel; Aden's clean adaptive transition | §3 |
| App A | Mastery-time ratios with procedural cancellation | Carrier division |
| App B | Aden's break (with caveat about already-declining trajectory) | §3 |
| App C | Three-source digitization reconciliation | `_provenance/` |

## What this is NOT

- NOT an attack on Swensson. The original paper named the inverse relation explicitly and reported mastery times correctly.
- NOT a discovery of hidden behavior. All three response classes were measurable from the trial-coding rubric.
- NOT a Tier-1 flagship. The slack channel formalizes structure visible in the figure; it doesn't expose phenomena the authors had no grasp of.
- NOT validation of the framework's truth. The EB carrier is independently established (RSOS-260797 r4); this is a demonstration application.

## What this IS

- A clean Tier-2 demonstration that having the right algebraic tool surfaces a third behavioral state by structural force.
- A worked example of how the saturation bound on $(K, I)$ forces the slack quantity into formal view.
- A scaffold for hunting Tier-1 cases (FCT, replacement-behavior, ratio-observable datasets) where the carrier might genuinely expose what conventional methods miss.

## File index

- Source paper: `_provenance/Swensson_2024_BehavioralInterventions_source.pdf`
- Source figure: `_provenance/swensson_2024_figure1_hires.jpg`
- CC-v2 manual digitization: `_provenance/swensson_figure1_digitization_2026-04-28.md`
- Ai1 first-pass: `_provenance/ai1_digitization/`
- Claude-v2 (preferred): `_provenance/claude_v2_digitization/`
- Three-source reconciliation: `_provenance/swensson_figure1_reconciliation_v2.2.md`
- Attribution: `_provenance/ATTRIBUTION.md`
