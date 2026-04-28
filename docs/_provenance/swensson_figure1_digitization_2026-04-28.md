# Swensson et al. (2024) Figure 1 — Digitization

**Source:** Swensson, R. M., et al. (2024). *Behavioral Interventions, 39*(3), e2015. Figure 1 (page 6 of 9).
**Method:** Visual extraction from 300 DPI rendering of the published figure.
**Date:** 2026-04-28
**Status:** Approximate eyeball digitization. Per-trial data is not publicly available (Swensson Data Availability Statement: "supporting data is not available"). Values below are integers (counts out of 5 trials per session). Sessions with ambiguous markers are flagged with `?`.

**Encoding:**
- $K_t$ = independent correct answers in session $t$
- $I_t^{(1)}$ = independent IDKPTM responses to Unknown Set 1 (training)
- $I_t^{(2)}$ = independent IDKPTM responses to Unknown Set 2 (generalization probes; only present at probe sessions)
- $A_t = K_t + I_t^{(1)}$ = adaptive response coverage on training trials
- $R_t = 5 - A_t$ = residual nonadaptive trials

Phase markers per Swensson Figure 1:
- BL = baseline (no prompts)
- Teaching = instruction sessions
- Intervention = training with IDKPTM prompt
- 5-targets = target reduction from 10 → 5 questions
- Break = Aden's 6-week session gap

---

## Alex (top panel)

| Session | Phase | $K_t$ | $I_t^{(1)}$ | $I_t^{(2)}$ | $A_t$ | $R_t$ | Notes |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | BL | 0 | 0 | — | 0 | 5 | |
| 2 | BL | 0 | 0 | — | 0 | 5 | |
| 3 | BL | 0 | 0 | — | 0 | 5 | |
| 4 | BL | 0 | 0 | — | 0 | 5 | |
| 5 | BL | 0 | 0 | — | 0 | 5 | |
| 6 | BL | 0 | 0 | — | 0 | 5 | |
| 7 | BL | 0 | 0 | — | 0 | 5 | |
| 8 | BL | 0 | 0 | — | 0 | 5 | |
| 9 | BL | 0 | 0 | — | 0 | 5 | |
| 10 | Teaching | 0 | — | — | — | — | instruction; no scored response |
| 11 | Intervention | 0 | 2 | — | 2 | 3 | |
| 12 | Intervention | 0 | 4 | — | 4 | 1 | |
| 13 | Intervention | 0 | 2 | — | 2 | 3 | |
| 14 | Intervention | 0 | 1 | — | 1 | 4 | |
| 15 | Intervention | 0 | 4 | — | 4 | 1 | |
| 16 | Intervention | 0 | 3 | — | 3 | 2 | |
| 17 | Intervention | 0 | 2? | — | 2 | 3 | |
| 18 | Intervention | 0 | 3 | — | 3 | 2 | |
| 19 | Intervention | 0 | 3 | — | 3 | 2 | |
| 20 | Intervention | 0 | 4 | — | 4 | 1 | |
| 21 | Intervention | 1 | 3 | — | 4 | 1 | first $K_t > 0$ |
| 22 | Intervention | 0 | 3 | — | 3 | 2 | |
| 23 | Intervention | 0 | 4 | — | 4 | 1 | |
| 24 | Intervention | 1 | 2 | — | 3 | 2 | |
| 25 | Intervention | 0 | 3 | 3 | 3 | 2 | Set 2 probe |
| 26 | Intervention | 1 | 3 | — | 4 | 1 | |
| 27 | Intervention | 0 | 2 | — | 2 | 3 | |
| 28 | Intervention | 1 | 4 | — | 5 | 0 | |
| 29 | Intervention | 1 | 3 | — | 4 | 1 | |
| 30 | Intervention | 1 | 3 | — | 4 | 1 | |
| 31 | Intervention | 1 | 2 | — | 3 | 2 | |
| 32 | Intervention | 1 | 3 | 4? | 4 | 1 | Set 2 probe |
| 33 | Intervention | 2 | 1 | — | 3 | 2 | |
| 34 | Intervention | 1 | 3 | — | 4 | 1 | |
| 35 | Intervention | 1 | 3 | — | 4 | 1 | |
| 36 | Intervention | 1 | 2 | — | 3 | 2 | |
| 37 | Intervention | 1 | 3 | — | 4 | 1 | |
| 38 | Intervention | 2 | 1 | — | 3 | 2 | |
| 39 | Intervention | 2 | 2 | — | 4 | 1 | |
| 40 | Intervention/5-tgt | 2 | 3 | — | 5 | 0 | 5-target line |
| 41 | 5-targets | 2 | 2 | — | 4 | 1 | |
| 42 | 5-targets | 3 | 2 | — | 5 | 0 | |
| 43 | 5-targets | 3 | 1 | — | 4 | 1 | |
| 44 | 5-targets | 3 | 2 | — | 5 | 0 | |
| 45 | 5-targets | 3 | 1 | — | 4 | 1 | |
| 46 | 5-targets | 4 | 2 | — | 6 | -1? | over-coverage suggests overlap |
| 47 | 5-targets | 3 | 1 | 4? | 4 | 1 | Set 2 probe |
| 48 | 5-targets | 4 | 2 | — | 6 | -1? | over-coverage |
| 49 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 50 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 51 | 5-targets | 4 | 2 | — | 6 | -1? | over-coverage |
| 52 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 53 | 5-targets | 5 | 1 | — | 6 | -1? | over-coverage |
| 54 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 55 | 5-targets | 5 | 1 | — | 6 | -1? | over-coverage |
| 56 | 5-targets | 4 | 1 | 4? | 5 | 0 | Set 2 probe; mastery sessions begin |
| 57 | 5-targets | 5 | 0 | — | 5 | 0 | |
| 58 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 59 | 5-targets | 5 | 0 | — | 5 | 0 | |
| 60 | 5-targets | 5 | 1 | — | 6 | -1? | mastery threshold reached (Swensson narrative) |
| 61 | 5-targets | 5 | 0 | — | 5 | 0 | |
| 62 | 5-targets | 4 | 0 | — | 4 | 1 | |

**Alex anomaly:** Several sessions show $A_t > 5$, which is structurally impossible (only 5 trials per session). This is digitization error — likely the bar height or square placement is being misread; or a single trial may be counted on both rails (if the child mands and then is given the answer and answers correctly within the same trial, both could be coded). The Swensson trial-coding rules say a trial is scored as "agreement if both researchers marked the same symbol" — a trial yields one outcome, not multiple. So $K_t + I_t \leq 5$ should hold strictly. The over-coverage entries flag where the digitization needs to be re-read against the original or against per-trial data.

---

## Aden (middle panel)

| Session | Phase | $K_t$ | $I_t^{(1)}$ | $I_t^{(2)}$ | $A_t$ | $R_t$ | Notes |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | BL | 0 | 0 | — | 0 | 5 | |
| 2 | BL | 0 | 0 | — | 0 | 5 | |
| 3 | BL | 0 | 0 | — | 0 | 5 | |
| 4 | BL | 0 | 0 | — | 0 | 5 | |
| 5 | BL | 0 | 0 | — | 0 | 5 | |
| 6 | BL | 0 | 0 | — | 0 | 5 | |
| 7 | BL | 0 | 0 | — | 0 | 5 | |
| 8 | Teaching | 0 | — | — | — | — | instruction |
| 9 | Teaching | 0 | — | — | — | — | instruction |
| 10 | Intervention | 0 | 5 | — | 5 | 0 | |
| 11 | Intervention | 0 | 5 | — | 5 | 0 | |
| 12 | Intervention | 0 | 5 | — | 5 | 0 | |
| 13 | Intervention | 0 | 5 | — | 5 | 0 | |
| 14 | Intervention | 0 | 5 | — | 5 | 0 | |
| 15 | Intervention | 0 | 5 | — | 5 | 0 | |
| 16 | Intervention | 0 | 5 | — | 5 | 0 | |
| 17 | Intervention | 0 | 4 | — | 4 | 1 | |
| 18 | Intervention | 0 | 5 | — | 5 | 0 | |
| 19 | Intervention | 0 | 4 | — | 4 | 1 | |
| 20 | Intervention | 0 | 4 | — | 4 | 1 | |
| 21 | Intervention | 0 | 4 | 4? | 4 | 1 | Set 2 probe; LAST PRE-BREAK |
| **break** | — | — | — | — | — | — | **6-week gap** |
| 22 | Post-break | 0 | 2 | — | 2 | 3 | sessions resume |
| 23 | Post-break | 0 | 2 | — | 2 | 3 | |
| 24 | Post-break | 0 | 3 | — | 3 | 2 | |
| 25 | Post-break | 0 | 2 | — | 2 | 3 | |
| 26 | Post-break | 0 | 3 | — | 3 | 2 | |
| 27 | Post-break | 0 | 2 | — | 2 | 3 | |
| 28 | Post-break | 0 | 3 | — | 3 | 2 | |
| 29 | Post-break | 0 | 2 | — | 2 | 3 | |
| 30 | Post-break | 0 | 2 | — | 2 | 3 | |
| 31 | Post-break | 0 | 2 | — | 2 | 3 | |
| 32 | Post-break | 0 | 2 | 4? | 2 | 3 | Set 2 probe |
| 33 | Post-break | 0 | 2 | — | 2 | 3 | |
| 34 | 5-targets | 1 | 2 | — | 3 | 2 | 5-target line |
| 35 | 5-targets | 1 | 2 | — | 3 | 2 | |
| 36 | 5-targets | 2 | 2 | — | 4 | 1 | |
| 37 | 5-targets | 3 | 1 | — | 4 | 1 | |
| 38 | 5-targets | 4 | 1 | — | 5 | 0 | |
| 39 | 5-targets | 4 | 1 | — | 5 | 0 | mastery threshold (Swensson narrative) |
| 40 | 5-targets | 4 | 0 | — | 4 | 1 | |

**Aden break note:** Pre-break IDKPTM was 4–5/session (sessions 17–21 average ≈ 4.4). Post-break dropped to 2–3/session (sessions 22–33 average ≈ 2.3). That's the maintenance-probe finding — a pre/post-break difference visible in the digitized data. Signed difference on the EB carrier: $\Delta I = I_{\text{post}} - I_{\text{pre}} = 2.3 - 4.4 = -2.1$ with substantive bound spread; this is where $B^2 \neq \mathrm{id}$ activates per Memoirs Ch 7.

---

## Ida (bottom panel)

| Session | Phase | $K_t$ | $I_t^{(1)}$ | $I_t^{(2)}$ | $A_t$ | $R_t$ | Notes |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | BL | 0 | 0 | — | 0 | 5 | |
| 2 | BL | 0 | 0 | — | 0 | 5 | |
| 3 | BL | 0 | 0 | — | 0 | 5 | |
| 4 | BL | 0 | 0 | — | 0 | 5 | |
| 5 | BL | 1 | 0 | — | 1 | 4 | Swensson reports "two instances of correct" in baseline |
| 6 | BL | 1 | 0 | — | 1 | 4 | |
| 7 | BL | 0 | 0 | — | 0 | 5 | |
| 8 | BL | 0 | 0 | — | 0 | 5 | |
| 9 | BL | 0 | 0 | — | 0 | 5 | |
| 10 | BL | 0 | 0 | — | 0 | 5 | |
| 11 | BL | 0 | 0 | — | 0 | 5 | |
| 12 | BL | 0 | 0 | — | 0 | 5 | |
| 13 | BL | 0 | 0 | — | 0 | 5 | |
| 14 | Teaching | 0 | — | — | — | — | instruction |
| 15 | Intervention | 0 | 0 | — | 0 | 5 | |
| 16 | Intervention | 0 | 1 | — | 1 | 4 | |
| 17 | Intervention | 0 | 1 | — | 1 | 4 | |
| 18 | Intervention | 0 | 2 | 3? | 2 | 3 | Set 2 probe |
| 19 | Intervention | 0 | 1 | — | 1 | 4 | |
| 20 | Intervention | 0 | 1 | — | 1 | 4 | |
| 21 | Intervention | 1 | 2 | — | 3 | 2 | |
| 22 | Intervention | 1 | 2 | — | 3 | 2 | |
| 23 | Intervention | 1 | 1 | — | 2 | 3 | |
| 24 | 5-targets | 2 | 1 | — | 3 | 2 | 5-target line |
| 25 | 5-targets | 3 | 0 | — | 3 | 2 | |
| 26 | 5-targets | 4 | 0 | — | 4 | 1 | mastery threshold reached (Swensson narrative) |

---

## Summary computations

### Mastery-session counts (Swensson narrative; cross-checked against digitization)

| Child | Mastery session | Notes |
|---|---:|---|
| Alex | 60 | first session in run that meets 80–100% correct over 3 consecutive sessions (per Swensson §4) |
| Aden | 39 | post-break; 4/5 correct sustained |
| Ida | 26 | clean acquisition |

### EB pair encoding for time-to-mastery (with $b = 5$ per agents' choice — generous bound covering target-reduction and break variation)

| Child | $(\text{sessions}, b)$ |
|---|---|
| Alex | (60, 5) |
| Aden | (39, 5) |
| Ida | (26, 5) |

### Verified ratio computations (full EB carrier, $\lambda = 1$)

$\xi_{\text{Aden/Alex}} = (39, 5) \oslash (60, 5)$:
- $e = 39/60 = 0.6500$
- $b = (39 \cdot 5)/3600 + 5/60 + (5 \cdot 5)/3600 = 0.0542 + 0.0833 + 0.00694 = 0.1444$
- Hull: $[0.506, 0.794]$

$\xi_{\text{Ida/Alex}} = (26, 5) \oslash (60, 5)$:
- $e = 26/60 = 0.4333$
- $b = (26 \cdot 5)/3600 + 5/60 + (5 \cdot 5)/3600 = 0.0361 + 0.0833 + 0.00694 = 0.1264$
- Hull: $[0.307, 0.560]$

### Aden pre/post-break EB pairs (from digitization)

Pre-break (sessions 17–21): $I_t \in \{4, 5, 4, 4, 4\}$, mean = 4.2, range = [4, 5], $b_{R1} = 0.5$
- Pre-break EB: $(4.2, 0.5)$ under R2 (mean-centred)

Post-break (sessions 22–26): $I_t \in \{2, 2, 3, 2, 3\}$, mean = 2.4, range = [2, 3], $b_{R1} = 0.5$
- Post-break EB: $(2.4, 0.5)$ under R2

Signed difference (full EB carrier; activates $B^2 \neq \mathrm{id}$):
- $(2.4, 0.5) - (4.2, 0.5) = (-1.8, 1.0)$
- Hull: $[-2.8, -0.8]$
- Hull does NOT include zero. The break produced a measurable, sign-determinate decline in IDKPTM that is not absorbed by the bound.

### Set 2 generalization observations (from digitization)

| Child | Probe sessions | $I_t^{(2)}$ values | EB pair (R1) |
|---|---|---|---|
| Alex | 25, 32, 47, 56 | 3, 4, 4, 4 | (3.75, 0.5) |
| Aden | 21, 32 | 4, 4 | (4.0, 0.0) |
| Ida | 18 | 3 | (3.0, 0.0) |

---

## Caveats

1. **Digitization is approximate.** Per-trial data is restricted by Swensson (Data Availability Statement). Numbers above are integer-quantized eyeball estimates from the published figure. Several Alex sessions show $A_t > 5$ which is structurally impossible — those flag re-reads needed.

2. **Mastery-session boundaries** are taken from Swensson's narrative text (sessions 60, 39, 26), not strictly from the digitized data alone.

3. **Set 2 generalization probe** sessions are inferred from triangle markers in the figure; their exact session number is approximate.

4. **The over-coverage anomaly in Alex** ($A_t > 5$ in several late sessions) is the most likely real digitization issue. Either (a) my reading of bar height vs. square value is off, or (b) a trial can be coded as both correct and IDKPTM in the published rubric — the latter is unlikely given Swensson's "scored as agreement if both researchers marked the same symbol" rule which implies exclusive coding. Re-reading the figure with higher resolution or requesting per-trial data from authors would resolve.

5. **Bound discipline $u \leq n$ on substrate-pair carrier** is violated for Aden's early intervention sessions (e.g., session 10–16 where $K_t = 0, I_t = 5$, so $I > K$). This is the encoding subtlety the framework paper needs to address: when the second rail is read as "behavioral count" rather than "measurement bound", substrate-pair discipline is not the right constraint. The framework lives on $\mathbb{R}_{\geq 0} \times \mathbb{R}_{\geq 0}$ as an ordered-pair space, but the $u \leq n$ axiom does not apply because $I_t$ is not a measurement uncertainty around $K_t$.
