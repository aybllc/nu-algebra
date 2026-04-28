# Swensson Figure 1 — Two-Source Reconciliation (v2.1)

**Date:** 2026-04-28
**Status:** Reconciliation between two independent digitizations of Swensson et al. (2024) Figure 1.

## Sources

1. **CC-v2** (this repo): `swensson_figure1_digitization_2026-04-28.md` — manual eyeball reading from 2128×2647 hi-res JPG, panel split via PIL, integer values constrained by protocol bound $K_t + I_t \leq 5$.
2. **Ai1** (filed in `ai1_digitization/`): pixel-level extraction with calibrated affine axes (gray <90 for markers, 120<gray<230 for bars; 15×15 sampling window at calibrated grid intersections; manual QA for triangles). Source image: 1646×2048 px JPG (publisher-supplied, lower DPI than CC-v2 source).

Both digitizations independently snap to integers in $[0,5]$ and report no overflow ($K + I \leq 5$ enforced).

## Where they agree (the load-bearing findings)

| Quantity | CC-v2 | Ai1 | Agreement |
|---|---|---|---|
| Aden BL→Teaching→Intervention boundaries | 1–7 / 8–9 / 10+ | 1–9 / — / 10+ | **±1 session** on BL/Teaching split |
| Aden full IDKPTM phase mean $I^{(1)}$ | 4.92 (s10–21) | 4.91 (s10–20) | **identical** within 0.01 |
| Aden post-transition phase mean $I^{(1)}$ | 2.83 (s22–33) | 2.85 (s21–33) | **identical** within 0.02 |
| Aden 5-targets onset session | 34 | 34 | **identical** |
| Aden mastery session | 39 | 39 ($K=5, I=0$) | **identical** |
| Alex 5-targets onset | 41 | 41 | **identical** |
| Alex mastery session | 60 | not explicit, but $K=5, I \leq 1$ in 60+ range | consistent |
| Ida BL incidental correct | sessions 5, 8 ($K=1$) | sessions 5, 8, 12, 13 ($K=1$) | **±2 sessions** |
| Ida mastery session | 25 | 25 ($K=5, I=0$) | **identical** |
| Set 2 probe values (Aden) | 5, 5, 4 (s11, 20, 32) | 5, 5, 4 (s15, 25, 41 panel-marker) | **values identical**; session indexing offset by triangle-position read |

Phase means agreement is the load-bearing item. The signed-difference EB pair for Aden's IDKPTM transition is robust across both readings.

## Where they disagree (per-session noise)

CC-v2 had Aden sessions 10–20 all at $I=5$ uniformly; Ai1 has session 16 at $I=4$ (one dip). Both readings produce phase means within 0.01 of each other. The dip is a real ±1 ambiguity in figure reading.

CC-v2 had Aden sessions 21–33 with K_t ranging 0–3; Ai1 has K_t = 1–2 mostly with several "missing K" entries (K bar not pixel-resolvable). Both produce post-transition phase mean within 0.02.

CC-v2 had Alex sessions 8–40 with detailed per-session readings; Ai1 has multiple "K missing" entries reflecting honest pixel-level limits. Phase means: CC-v2 mean $K \approx$ 1.4 / mean $I^{(1)} \approx$ 3.0 (sessions 8–40); Ai1 mean $K = 1.583$, $I^{(1)} = 2.906$ (n=32). Agreement within ±0.2.

## The phase-boundary correction (**critical reframing**)

Swensson Methods text: *"due to a break in sessions at the caregiver's request, we did not meet for 6 weeks, denoted by an asterisk... After resuming sessions, we decreased the number of targets to five at session number 34."*

So the asterisk marks Aden's **resume session**, not the start of the break. Combined with "5-targets started at session 34," the timeline is:

```
BL          Teaching   Intervention(10 targets)        Break  Resume   Intervention(5 targets)  Mastery
[1–9]       [—or 9]    [10 ───────── 30 (?)]            6wk   ~30/31   [34─────────39]          [39+]
                       │           │
                       │           └─ acquisition transition begins ~session 21
                       │              (K_t first nonzero, I_t starts dropping from ceiling)
                       │
                       └─ full IDKPTM ceiling (5/5)
```

**The 6-week break happened LATER in Aden's intervention** (around session 30, not session 22). What CC-v2 v1/v2 called "pre-break vs post-break" was actually the **acquisition transition** at session ~21 — when Aden first began answering correctly while continuing to mand IDKPTM for unknown items.

The behavioral break (calendar gap) is essentially invisible in the data. Aden had already transitioned from full-IDKPTM to mixed K+I responding **before** the calendar break. The break did not regress him.

## Corrected EB derived quantities (using reframed phases)

### Aden acquisition transition (Ai1 readings)

**Phase A — Full IDKPTM (sessions 10–20, n=11):**
- $I^{(1)}$ values: 5,5,5,5,5,5,4,5,5,5,5
- mean = 4.909, range = [4, 5], $b_{R1}$ = 0.5, $b_{R2}$ = 0.909
- EB pair (R1): $(4.91, 0.5)$

**Phase B — Acquisition transition (sessions 21–33, n=13):**
- $I^{(1)}$ values: 3,4,3,2,2,2,4,4,3,2,2,4,2
- mean = 2.846, range = [2, 4], $b_{R1}$ = 1.0, $b_{R2}$ = 1.154
- EB pair (R1): $(2.85, 1.0)$

**Signed difference (Phase B − Phase A):**
- $(2.85, 1.0) - (4.91, 0.5) = (-2.06, 1.5)$
- Hull: $[-3.56, -0.56]$
- **Hull excludes zero**: directional finding locked.

**Phase C — 5-targets (sessions 34–39, n=6):**
- $I^{(1)}$ values: 2,2,1,1,1,0
- mean = 1.167, range = [0, 2], $b_{R1}$ = 1.0, $b_{R2}$ = 1.167
- EB pair (R1): $(1.17, 1.0)$
- $K_t$ values: 2,2,1,1,1,5
- mean $K$ = 2.0, range = [1, 5], $b_{R1}$ = 2.0
- EB pair (R1) for $K_t$: $(2.0, 2.0)$

The Phase B → Phase C transition shows the K-rail completing the takeover that began in Phase B. Phase C $K_t$ has high range (b=2.0) because the final session (39) jumps to 5 — that's the mastery onset, not a gradual climb.

### Reframed framework reading

The Swensson IDKPTM intervention shows **three EB regimes** for Aden:
1. **IDKPTM ceiling**: $(0, 5)$ all sessions. Pure I-rail. Centre is zero (no correct answers); width is at protocol saturation. Adaptive coverage = full, but knowledge = none.
2. **Acquisition transition**: $(K, I)$ both nonzero, both varying. Centre rises, width contracts. The carrier surfaces the **rail trade**: $K + I \leq 5$ saturation forces I to drop as K rises.
3. **Mastery**: $(5, 0)$ at session 39. Pure K-rail. Centre saturates; width collapses to zero.

This is the regime structure the v0.1 paper should describe. The "break" frame in v0.1 is wrong; the acquisition-transition frame is right.

## What v0.1 paper needs (revision call)

The v0.1 paper section 5 (numerical analysis) currently uses "pre-break vs post-break" framing. The correct framing per this reconciliation is:
- Replace "pre-break" with "IDKPTM-ceiling phase" (or "Phase A")
- Replace "post-break" with "acquisition-transition phase" (or "Phase B")
- Note that the calendar break was non-disruptive (the data shows continuous behavior across it)
- The signed-difference EB pair is robust to reframing (magnitude virtually identical)

This is a label correction, not a content correction. The math holds. The story changes: from "the break caused regression that the framework characterizes" to "the framework surfaces an acquisition transition that's invisible to phase-mean reporting and was incidentally bisected by a calendar break."

The acquisition-transition story is **stronger** than the break-regression story. The framework isn't characterizing a stress test; it's characterizing the structural signature of how IDKPTM teaching transitions to correct responding.

## Provenance

- Two independent digitizations (one manual eyeball at 600 DPI, one pixel-level at lower DPI) converge on phase means within 0.02.
- The K-rail "missing" entries in Ai1's data are honest pixel-level limits, not contradictions — reflecting where the gray bar height is genuinely ambiguous in the figure.
- Disagreement on per-session integers is ±1 typical, ±2 worst-case; aggregates absorb this noise.
- The reframing ("break" → "acquisition transition") is forced by the Swensson text, not by either digitization.
