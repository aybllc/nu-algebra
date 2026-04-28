# Swensson Figure 1 — Three-Source Reconciliation (v2.2)

**Date:** 2026-04-28
**Status:** Reconciliation across three independent digitizations of Swensson et al. (2024) Figure 1.
**Supersedes:** v2.1 (two-source). Adds Claude-v2's automated bar-detection digitization as third source.

## Sources

1. **CC-v2** (`swensson_figure1_digitization_2026-04-28.md`) — manual eyeball at 2128×2647 hi-res JPG, panel split, integer values constrained by protocol bound $K + I \leq 5$.
2. **Ai1** (`ai1_digitization/`) — pixel-level extraction with calibrated affine axes (gray <90 markers, 120<gray<230 bars; manual triangle QA); source 1646×2048 px JPG.
3. **Claude-v2** (`claude_v2_digitization/`) — external Claude instance, automated bar-detection with iterative debugging: anti-aliasing gap tolerance, IDKPTM-line gap-closing, $K+I \leq 5$ post-hoc rounding correction; reports zero-slack profile per child. (Originally labeled "EDM" in this document — that was a mis-attribution; the digitization is from another Claude instance, not Eric.)

All three independently snap to integers in $[0, 5]$ and enforce protocol bound.

## Convergence on the load-bearing findings

| Quantity | CC-v2 | Ai1 | Claude-v2 | Verdict |
|---|---|---|---|---|
| Aden BL→Intervention split | 1–7 / 10+ | 1–9 / 10+ | 1–7 / 10+ | **converge** at session 10 onset |
| Aden full-IDKPTM phase mean $I$ | 4.92 (s10–21) | 4.91 (s10–20) | 4.91 (s10–20) | **identical** within 0.01 |
| Aden $K_t$ onset | s23 | s21 | s21 | Ai1+Claude-v2 agree at 21 |
| Aden mastery (5/5 K) | session 39 | session 39 | session 39 | **identical** |
| Aden 5-targets transition | session 34 | session 34 | session 34 | **identical** |
| Alex 5-targets transition | session 41 | session 41 | session 41 | **identical** |
| Ida mastery | session 25 | session 25 | session 25 | **identical** |
| Aden break (asterisk position) | "around session 30" | not pixel-resolved | **between sessions 32–33** | Claude-v2 authoritative |

## Claude-v2's added findings

### Slack as third rail (NEW — not in v2 or Ai1)

For the Set 1 protocol, $K + I + \text{slack} = 5$ where slack = third-class trials (incorrect, no response, off-task). The original Swensson coding lumped these into "neither correct nor IDKPTM" without separately surfacing them.

| Child | n intervention | mean slack | zero-slack sessions | max slack |
|---|---:|---:|---:|---:|
| Alex | 41 | 1.27 | 16/41 (39%) | 5 |
| Aden | 28 | 0.11 | 25/28 (89%) | 1 |
| Ida | 14 | 1.07 | 6/14 (43%) | 4 |

**Reading:** Aden showed near-zero slack throughout intervention — clean stimulus control, every trial yielded a procedure-appropriate response (either trained mand or correct intraverbal). Alex and Ida had substantially more third-class responding. The EB carrier's saturation bound $K + I \leq 5$ admits a third quantity (the slack) which Claude-v2's automated extraction surfaces as a behavioral signal the original analysis did not.

(Caveat: Claude-v2's Alex sessions 53–62 show high slack readings that reflect bar-detection failure on the dense post-mastery part of the figure, not real third-class trials. The 39% zero-slack number is conservative within Alex's resolvable sessions.)

### Stimulus-control onset (sharper than mastery)

Operational definition: first session $s^*$ such that for all $s \geq s^*$, $K(s) + I(s) \geq 4$ (sustained ≥4/5 procedure-appropriate response).

| Child | Stimulus-control onset (Claude-v2) | Swensson mastery (4/5 sustained correct) |
|---|---:|---:|
| Alex | never strict; soft (≥85% of tail) at session 22 | session 60 |
| Aden | session 10 (immediate) | session 39 |
| Ida | session 15 | session 25 |

**Reading:** Aden achieved stimulus control immediately upon intervention onset — he was reliably engaging with the procedure from session 10, just *via* the IDKPTM rail rather than the K rail. Mastery (transferring weight from I-rail to K-rail) took 29 more sessions. Conventional reporting only sees mastery; the EB carrier sees stimulus-control onset much earlier and the rail-trade in between.

### Break-pre vs break-post (Claude-v2's reframing)

Claude-v2 places the break asterisk between sessions 32 and 33 (automated detection from figure pixel layout). Pre-break (sessions 30–32) IDKPTM = [2, 2, 4] = mean 2.67. Post-break (sessions 33–35) IDKPTM = [2, 2, 2] = mean 2.0.

**Caveat preserved by Claude-v2:** *"Aden's IDKPTM had ALREADY been declining before the break as he learned answers — so the break is not a clean asymptote-vs-asymptote comparison. It is, however, a 6-week interruption of an active learning curve."*

EB encoding (3-session windows on either side):
- Pre-break (R1): $(2.67, 1.0)$ centre = 2.67, hull width 2 (range [2,4])
- Post-break (R1): $(2.0, 0.0)$ centre = 2.0, hull width 0 (range [2,2])
- Signed difference: $(-0.67, 1.0)$, hull $[-1.67, 0.33]$ — **hull straddles zero**.

The narrow break-window EB pair has a hull that includes zero. The wider-window comparison from v2.1 (Phase A vs Phase B over the full ceiling vs full transition) is the load-bearing finding; the immediate-break-window finding is genuinely uncertain in direction.

## Disagreement profile (per-session ±1, expected)

| Issue | Magnitude |
|---|---|
| CC-v2 has Aden $K_t = 0$ through session 21; Ai1+Claude-v2 have $K_t = 2$ at session 21 | CC-v2 missed the K_t-onset session; aggregates absorb this |
| Claude-v2 Alex sessions 53–62 have unreadable bars (high slack) | Honest pixel-level limit; flagged in Claude-v2 debugging notes |
| Mid-transition $K_t$ values differ ±1 across sources | Per-session noise; phase means converge |

## What converges enough to publish

The triple-source convergence supports these claims with no single-source dependency:

1. **Aden's full-IDKPTM phase (sessions 10–20)**: $I^{(1)} \in \{4, 5\}$ throughout, mean $\geq 4.9$.
2. **Aden's acquisition transition (sessions 21–35)**: K-rail rises from 0 to 4–5, I-rail falls from 5 to 0–1, with $K + I \leq 5$ saturation throughout (89% of these sessions hit equality per Claude-v2).
3. **Aden's mastery onset (session 36 onward)**: $K \geq 4$ sustained; mastery at session 39 ($K=5$).
4. **Ida's clean acquisition**: parallel rise of K and I from session 14, mastery at session 25.
5. **Alex's high-variability profile**: slack rate (per Claude-v2) shows Alex differs from Aden/Ida in stimulus-control quality, not just rate.
6. **Ratios of mastery times** (procedural cancellation): $\xi_{\text{Aden/Alex}}$ hull $[0.51, 0.79]$, $\xi_{\text{Ida/Alex}}$ hull $[0.31, 0.56]$.

## What does NOT converge

The narrow break-window comparison ($n=3$ each side). Claude-v2's centre is small ($-0.67$) with hull straddling zero. The three-source disagreement on per-session $K_t$ in the transition phase makes any 3-session-window claim about the calendar break unreliable.

**Recommendation for the paper:** Replace any "break-induced regression" framing with the broader acquisition-transition framing. The break per se is not a robust EB finding; the rail trade across the entire transition phase is.

## Provenance

- Three independent digitizations converge on phase means, mastery sessions, transition-onset, 5-targets boundary.
- They diverge on per-session integers in the transition phase (±1 typical) and on Alex's late-figure sessions (Claude-v2 honest limit).
- Claude-v2's slack-as-third-rail and stimulus-control-onset findings are new EB carrier readings of the dataset that v2 and Ai1 do not surface.
- The break-window narrow comparison is unreliable across all three sources; the wider acquisition-transition comparison is robust.

## File index

- CC-v2: `swensson_figure1_digitization_2026-04-28.md`
- Ai1: `ai1_digitization/{calibration.json, marks.csv, session_carriers.csv, eb_summary.csv, report.md}`
- Claude-v2: `claude_v2_digitization/{digitized.csv, digitized.json, eb_findings.txt}`
- Source figure: `swensson_2024_figure1_hires.jpg`, `swensson_2024_figure1_source.pptx`
- Source paper: `Swensson_2024_BehavioralInterventions_source.pdf`
- Reconciliation v2.1 (two-source, superseded but kept for trail): `swensson_figure1_reconciliation_v2.1.md`
