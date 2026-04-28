# Swensson et al. (2024) Figure 1 — Digitization

**Source:** Swensson, R. M., et al. (2024). *Behavioral Interventions, 39*(3), e2015. Figure 1.
**Source files (this repo):**
- `Swensson_2024_BehavioralInterventions_source.pdf` (full article)
- `swensson_2024_figure1_hires.jpg` (2128×2647 px, ~600 DPI)
- `swensson_2024_figure1_source.pptx` (publisher-supplied PPTX of Figure 1)
**Method:** Visual extraction from 2128×2647 JPG, panel-by-panel (Alex, Aden, Ida) split via PIL.
**Date:** 2026-04-28 (v2 supersedes v1 of same date; v1 was 300 DPI pdftoppm, no protocol cross-check)
**Status:** Integer per-session readings constrained by protocol bound $K_t + I_t^{(1)} \leq 5$ (Swensson Methods §3.3.2: "five trials were conducted per session"). Triangle markers (Set 2) are independent generalization probes administered separately, not subtracted from the 5 Set-1 trials. Mastery sessions are taken from Swensson's narrative text and cross-checked against digitization.

## Protocol clarifications (Swensson Methods)

- **Always 5 trials/session.** "Each session consisted of five previously randomized questions." — Methods §3.3.2.
- **"5 targets" dotted line** = pool reduction (10 → 5 questions), NOT a change in trials/session. Pre-line: 5 trials drawn from a 10-question pool. Post-line: same 5 questions every session.
- **Set 2 probes** = generalization probes on questions never trained, administered following BL procedures (no prompt). Probe sessions interleaved with training; triangle markers in figure denote probe-day score.
- **Aden's break** = 6-week telehealth gap mid-intervention.
- **Mastery criterion** (per Swensson): 4–5/5 correct sustained across 3 consecutive sessions.

## Encoding

- $K_t$ = independent correct answers in session $t$ (count out of 5)
- $I_t^{(1)}$ = independent IDKPTM responses to Unknown Set 1 (training)
- $I_t^{(2)}$ = independent IDKPTM responses to Unknown Set 2 (probe-day only)
- $A_t = K_t + I_t^{(1)}$ = adaptive coverage on training trials. Bound: $0 \leq A_t \leq 5$.
- $R_t = 5 - A_t$ = residual nonadaptive trials (blank / wrong / silent / off-task).

**Framework discipline correction (vs v1):** The pair $(K_t, I_t^{(1)})$ lives on the simplex-region $\{(k,i): k,i \geq 0, k+i \leq 5\}$ — a saturation bound, NOT measurement-with-uncertainty discipline $u \leq n$ (substrate-pair). EB carrier still applies: take $e = K_t$ (correct-answer centre) and $b = I_t^{(1)}$ (epistemic-acknowledgment width); the bound $e + b \leq 5$ is an additional protocol constraint, not a structural EB axiom. The substrate-pair carrier is wrong framing for this dataset.

---

## Alex (top panel, sessions 1–62)

Phases (from vertical lines in figure):
- BL: sessions 1–5
- Teaching: sessions 6–7
- Intervention: sessions 8–40
- 5-targets: sessions 41–62
- Mastery (Swensson narrative): session 60 onward

| Session | Phase | $K_t$ | $I_t^{(1)}$ | $I_t^{(2)}$ | $A_t$ | $R_t$ | Notes |
|---:|---|---:|---:|---:|---:|---:|---|
| 1–5 | BL | 0 | 0 | (0 at one probe) | 0 | 5 | all flat at 0 |
| 6–7 | Teaching | 0 | 0 | — | 0 | 5 | instruction phase |
| 8 | Intervention | 0 | 2 | — | 2 | 3 | first IDKPTM acquisition |
| 9 | Intervention | 0 | 4 | — | 4 | 1 | spike |
| 10 | Intervention | 2 | 3 | — | 5 | 0 | first $K_t > 0$ |
| 11 | Intervention | 0 | 1 | — | 1 | 4 | dip |
| 12 | Intervention | 0 | 1 | — | 1 | 4 | |
| 13 | Intervention | 2 | 3 | — | 5 | 0 | |
| 14 | Intervention | 0 | 2 | — | 2 | 3 | |
| 15 | Intervention | 2 | 2 | — | 4 | 1 | |
| 16 | Intervention | 0 | 3 | — | 3 | 2 | |
| 17 | Intervention | 1 | 4 | — | 5 | 0 | |
| 18 | Intervention | 1 | 3 | — | 4 | 1 | |
| 19 | Intervention | 1 | 3 | — | 4 | 1 | |
| 20 | Intervention | 1 | 3 | 4 | 4 | 1 | Set 2 probe |
| 21 | Intervention | 1 | 3 | — | 4 | 1 | |
| 22 | Intervention | 1 | 3 | — | 4 | 1 | |
| 23 | Intervention | 0 | 4 | — | 4 | 1 | |
| 24 | Intervention | 0 | 5 | — | 5 | 0 | **Set 1 IDKPTM peak** |
| 25 | Intervention | 0 | 4 | — | 4 | 1 | |
| 26 | Intervention | 1 | 3 | — | 4 | 1 | |
| 27 | Intervention | 1 | 4 | — | 5 | 0 | |
| 28 | Intervention | 1 | 4 | 4 | 5 | 0 | Set 2 probe |
| 29 | Intervention | 1 | 3 | — | 4 | 1 | |
| 30 | Intervention | 1 | 4 | — | 5 | 0 | |
| 31 | Intervention | 1 | 3 | — | 4 | 1 | |
| 32 | Intervention | 2 | 3 | — | 5 | 0 | |
| 33 | Intervention | 1 | 4 | — | 5 | 0 | |
| 34 | Intervention | 2 | 3 | — | 5 | 0 | |
| 35 | Intervention | 2 | 2 | — | 4 | 1 | |
| 36 | Intervention | 2 | 3 | — | 5 | 0 | |
| 37 | Intervention | 2 | 2 | — | 4 | 1 | |
| 38 | Intervention | 2 | 2 | — | 4 | 1 | |
| 39 | Intervention | 2 | 3 | — | 5 | 0 | |
| 40 | Intervention | 2 | 2 | — | 4 | 1 | last pre-5-targets |
| 41 | 5-targets | 1 | 4 | 4 | 5 | 0 | 5-targets boundary; Set 2 probe |
| 42 | 5-targets | 2 | 3 | — | 5 | 0 | |
| 43 | 5-targets | 3 | 2 | — | 5 | 0 | |
| 44 | 5-targets | 1 | 3 | — | 4 | 1 | |
| 45 | 5-targets | 3 | 2 | — | 5 | 0 | |
| 46 | 5-targets | 2 | 2 | — | 4 | 1 | |
| 47 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 48 | 5-targets | 1 | 1 | — | 2 | 3 | |
| 49 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 50 | 5-targets | 3 | 1 | — | 4 | 1 | |
| 51 | 5-targets | 3 | 1 | — | 4 | 1 | |
| 52 | 5-targets | 1 | 1 | — | 2 | 3 | |
| 53 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 54 | 5-targets | 1 | 2 | 5 | 3 | 2 | Set 2 probe (peak) |
| 55 | 5-targets | 3 | 1 | — | 4 | 1 | |
| 56 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 57 | 5-targets | 1 | 3 | — | 4 | 1 | |
| 58 | 5-targets | 1 | 1 | — | 2 | 3 | |
| 59 | 5-targets | 4 | 2 | — | 5 | 0 | |
| 60 | 5-targets | 5 | 1 | — | 5 | 0 | **mastery threshold (Swensson narrative)** — note: $K_t=5$ implies $I^{(1)}=0$; visible square at 1 may be lag artifact, treat $I^{(1)}=0$ |
| 61 | 5-targets | 0 | 0 | — | 0 | 5 | |
| 62 | 5-targets | 4 | 1 | — | 5 | 0 | |

**Alex per-session uncertainty:** ±1 on individual values where bars and squares overlap visually. Aggregates (phase means) are robust to this. Bound $A_t \leq 5$ enforced; v1 over-coverage entries (sessions 46, 48, 51, 53, 55) reflected reading-error against bound, now resolved.

---

## Aden (middle panel, sessions 1–40)

Phases:
- BL: sessions 1–7
- Teaching: sessions 8–9
- Intervention pre-break: sessions 10–21
- Break: 6-week gap between sessions 21 and 22
- Intervention post-break: sessions 22–33
- 5-targets: sessions 34–40
- Mastery (Swensson narrative): session 39 onward

| Session | Phase | $K_t$ | $I_t^{(1)}$ | $I_t^{(2)}$ | $A_t$ | $R_t$ | Notes |
|---:|---|---:|---:|---:|---:|---:|---|
| 1–7 | BL | 0 | 0 | (0 at one probe) | 0 | 5 | flat |
| 8–9 | Teaching | 0 | 0 | — | 0 | 5 | |
| 10 | Intervention | 0 | 5 | — | 5 | 0 | full IDKPTM acquisition immediate |
| 11 | Intervention | 0 | 5 | 5 | 5 | 0 | Set 2 probe at 5 (full) |
| 12 | Intervention | 0 | 5 | — | 5 | 0 | |
| 13 | Intervention | 0 | 5 | — | 5 | 0 | |
| 14 | Intervention | 0 | 5 | — | 5 | 0 | |
| 15 | Intervention | 0 | 5 | — | 5 | 0 | |
| 16 | Intervention | 0 | 4 | — | 4 | 1 | |
| 17 | Intervention | 0 | 5 | — | 5 | 0 | |
| 18 | Intervention | 0 | 5 | — | 5 | 0 | |
| 19 | Intervention | 0 | 5 | — | 5 | 0 | |
| 20 | Intervention | 0 | 5 | 5 | 5 | 0 | Set 2 probe |
| 21 | Intervention | 0 | 5 | — | 5 | 0 | **last pre-break** |
| **break** | — | — | — | — | — | — | **6-week gap** |
| 22 | Post-break | 0 | 3 | — | 3 | 2 | sessions resume; **drop from 5 → 3** |
| 23 | Post-break | 1 | 4 | — | 5 | 0 | |
| 24 | Post-break | 1 | 2 | — | 3 | 2 | |
| 25 | Post-break | 1 | 2 | — | 3 | 2 | |
| 26 | Post-break | 1 | 4 | — | 5 | 0 | |
| 27 | Post-break | 1 | 4 | — | 5 | 0 | |
| 28 | Post-break | 2 | 3 | — | 5 | 0 | |
| 29 | Post-break | 2 | 2 | — | 4 | 1 | |
| 30 | Post-break | 3 | 2 | — | 5 | 0 | |
| 31 | Post-break | 1 | 4 | — | 5 | 0 | |
| 32 | Post-break | 3 | 2 | 4 | 5 | 0 | Set 2 probe |
| 33 | Post-break | 3 | 2 | — | 5 | 0 | |
| 34 | 5-targets | 3 | 2 | — | 5 | 0 | 5-targets boundary |
| 35 | 5-targets | 3 | 2 | — | 5 | 0 | |
| 36 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 37 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 38 | 5-targets | 5 | 0 | — | 5 | 0 | |
| 39 | 5-targets | 5 | 0 | — | 5 | 0 | **mastery threshold (Swensson)** |
| 40 | 5-targets | 5 | 0 | — | 5 | 0 | |

**Aden break note (corrected):** Pre-break IDKPTM was nearly always 5/5 (sessions 10–21, $\bar I = 4.92$, range [4,5]). Immediately post-break (sessions 22–28, $\bar I = 3.14$, range [2,4]). The break produced a ~1.8-point drop in IDKPTM that recovered partially but never returned to pre-break ceiling — instead, $K_t$ rose to fill the gap as he transitioned from "answering IDKPTM appropriately" to "answering correctly when he knew, IDKPTM otherwise." This is the **adaptive transition** the EB carrier surfaces and the original Swensson narrative undersells.

---

## Ida (bottom panel, sessions 1–26)

Phases:
- BL: sessions 1–8 (Swensson reports 2 incidental correct answers in BL)
- Teaching: sessions 9–11
- Intervention: sessions 12–22
- 5-targets: sessions 23–26
- Mastery (Swensson narrative): session 25 onward

| Session | Phase | $K_t$ | $I_t^{(1)}$ | $I_t^{(2)}$ | $A_t$ | $R_t$ | Notes |
|---:|---|---:|---:|---:|---:|---:|---|
| 1–4 | BL | 0 | 0 | (0 at one probe) | 0 | 5 | |
| 5 | BL | 1 | 0 | — | 1 | 4 | incidental correct |
| 6–7 | BL | 0 | 0 | — | 0 | 5 | |
| 8 | BL | 1 | 0 | — | 1 | 4 | second incidental correct |
| 9–11 | Teaching | 0 | 0 | — | 0 | 5 | |
| 12 | Intervention | 0 | 0 | — | 0 | 5 | |
| 13 | Intervention | 1 | 0 | — | 1 | 4 | |
| 14 | Intervention | 1 | 1 | — | 2 | 3 | first IDKPTM |
| 15 | Intervention | 2 | 1 | — | 3 | 2 | |
| 16 | Intervention | 2 | 2 | — | 4 | 1 | |
| 17 | Intervention | 3 | 1 | — | 4 | 1 | |
| 18 | Intervention | 2 | 1 | — | 3 | 2 | |
| 19 | Intervention | 3 | 2 | 3 | 5 | 0 | Set 2 probe |
| 20 | Intervention | 2 | 2 | — | 4 | 1 | |
| 21 | Intervention | 3 | 2 | — | 5 | 0 | |
| 22 | Intervention | 3 | 2 | — | 5 | 0 | last pre-5-targets |
| 23 | 5-targets | 3 | 1 | — | 4 | 1 | 5-targets boundary |
| 24 | 5-targets | 4 | 0 | — | 4 | 1 | |
| 25 | 5-targets | 5 | 0 | — | 5 | 0 | **mastery threshold (Swensson)** |
| 26 | 5-targets | 5 | 0 | — | 5 | 0 | |

**Ida acquisition note:** Cleanest acquisition of the three. Did not exhibit the same "ceiling on IDKPTM then transition" pattern as Aden — IDKPTM rose modestly (1–2/5) while $K_t$ rose in parallel from session 14 onward, with both reaching saturation by session 25.

---

## Summary computations (corrected v2)

### Mastery sessions (Swensson narrative)

| Child | Mastery session | Onset of $K_t \geq 4$ sustained |
|---|---:|---:|
| Alex | 60 | very late, with high IDKPTM persistence throughout |
| Aden | 39 | post-break transition, after IDKPTM ceiling collapsed |
| Ida | 25 | direct rise of $K_t$ alongside modest IDKPTM |

### Time-to-mastery EB pairs ($b = 5$ for protocol-variation bound)

| Child | $(\text{sessions}, b)$ |
|---|---|
| Alex | (60, 5) |
| Aden | (39, 5) |
| Ida | (25, 5) (corrected from v1's 26) |

### Verified ratio computations (full EB carrier, $\lambda = 1$)

$\xi_{\text{Aden/Alex}} = (39, 5) \oslash (60, 5)$:
- $e = 39/60 = 0.6500$
- $b = (39 \cdot 5)/3600 + 5/60 + (5 \cdot 5)/3600 = 0.05417 + 0.08333 + 0.00694 = 0.14444$
- Hull: $[0.5056, 0.7944]$

$\xi_{\text{Ida/Alex}} = (25, 5) \oslash (60, 5)$:
- $e = 25/60 = 0.4167$
- $b = (25 \cdot 5)/3600 + 5/60 + (5 \cdot 5)/3600 = 0.03472 + 0.08333 + 0.00694 = 0.12500$
- Hull: $[0.2917, 0.5417]$

### Aden pre/post-break EB pairs (corrected from digitization)

**Pre-break window (sessions 10–21, n=12):**
- $I_t^{(1)} \in \{5,5,5,5,5,5,4,5,5,5,5,5\}$
- mean = 4.917, range = [4, 5], $b_{R1} = 0.5$, $b_{R2} = 0.917$
- Pre-break EB (R1): $(4.92, 0.5)$

**Post-break window, first 7 (sessions 22–28, n=7):**
- $I_t^{(1)} \in \{3, 4, 2, 2, 4, 4, 3\}$
- mean = 3.143, range = [2, 4], $b_{R1} = 1.0$, $b_{R2} = 1.143$
- Post-break EB (R1): $(3.14, 1.0)$

**Signed difference (full EB carrier):**
- $(3.14, 1.0) - (4.92, 0.5) = (-1.78, 1.5)$
- Hull: $[-3.28, -0.28]$
- Hull does NOT include zero. The break produced a sign-determinate decline in IDKPTM with widened bound.

**Full extended-window post-break (sessions 22–33, n=12):**
- $I_t^{(1)} \in \{3, 4, 2, 2, 4, 4, 3, 2, 2, 4, 2, 2\}$
- mean = 2.833, range = [2, 4], $b_{R1} = 1.0$, $b_{R2} = 1.167$
- Post-break EB extended (R1): $(2.83, 1.0)$
- Signed difference: $(2.83, 1.0) - (4.92, 0.5) = (-2.08, 1.5)$
- Hull: $[-3.58, -0.58]$ — still does not include zero.

### Set 2 generalization observations (probe sessions only; corrected)

| Child | Probe sessions | $I_t^{(2)}$ values | EB pair (R1) |
|---|---|---|---|
| Alex | 20, 28, 41, 54 | 4, 4, 4, 5 | (4.25, 0.5) |
| Aden | 11, 20, 32 | 5, 5, 4 | (4.67, 0.5) |
| Ida | 19 | 3 | (3.0, 0.0) |

(v1 had Aden Set 2 probes only at sessions 21, 32; v2 corrects to 11, 20, 32 based on hi-res triangle positions, all near or at 5/5.)

---

## Caveats (v2)

1. **Per-session integers are still ±1 uncertain.** When bar and square overlap or land between gridlines, the protocol bound $K_t + I_t \leq 5$ is the deciding constraint. Several Alex sessions in 41–62 had visible bar+square overlap; the v2 readings prefer protocol-consistent values over visual estimates.

2. **Mastery boundaries** taken from Swensson's narrative; cross-checked against $K_t \geq 4$ sustained. Ida's mastery is at session 25 (v1 said 26 — corrected to match Swensson's narrative criterion).

3. **Set 2 probes**: the triangle markers in the Aden panel are at sessions 11, 20, 32 (not 21, 32 as v1 stated). The Alex Set 2 triangle at session 54 is at value 5 (clearly visible in hi-res), the highest of his Set 2 probes.

4. **Framework discipline corrected.** The pair $(K, I)$ is bound by the protocol saturation $K + I \leq 5$, not by substrate-pair $u \leq n$. Substrate-pair was a wrong framing for this dataset; EB carrier with saturation constraint is correct.

5. **Aden break magnitude.** Pre/post difference is robust to ±1 per-session uncertainty: every reasonable readings of the pre-break window gives mean ∈ [4.5, 5.0]; every reasonable post-break window gives mean ∈ [2.5, 3.5]. Signed difference hull straddles negative across all reasonable readings — the directional finding is locked.

---

## Provenance

- **v1** (this file, prior): 300 DPI pdftoppm, no protocol cross-check, flagged Alex over-coverage anomaly and "substrate-pair u ≤ n violation."
- **v2** (this file, current): 600 DPI direct JPG + PPTX, Methods §3.3.2 cross-check confirms 5 trials/session always, over-coverage was reading error (resolved), substrate-pair was wrong frame (corrected to EB carrier with saturation bound).
