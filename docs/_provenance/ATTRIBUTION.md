# Swensson Figure 1 — Source attribution

Three independent digitizations of Swensson et al. (2024) Figure 1.

| Label | Origin | Method | Notes |
|---|---|---|---|
| **CC-v2** (`swensson_figure1_digitization_2026-04-28.md`) | Claude Code (this session) | Manual eyeball at 2128×2647 hi-res JPG, panel split via PIL | Per-session ±1 noise, phase aggregates robust |
| **Ai1** (`ai1_digitization/`) | External Claude instance (web), first-pass | Pixel-level affine calibration; 1646×2048 px source | 126 rows; missed Alex session 11 |
| **Claude-v2** (`claude_v2_digitization/`) | External Claude instance (web), second-pass | Automated bar-detection with iterative debugging (AA gap tolerance, line-passing-through-bar handling); reports slack profile per child | 127 rows; preferred source per Eric's manual overlay check |

(Earlier git commits referred to claude_v2_digitization as "edm_digitization"; that was a labeling error on my part — the files were not produced by Eric. The directory rename in commit-rename preserves attribution accuracy.)

## Convergence

All three sources agree within 0.02 on phase means; mastery sessions identical (Alex 60, Aden 39, Ida 25); 5-targets boundary identical (s34 Aden, s41 Alex). Per-session integers diverge ±1 typical, ±2 worst-case.

## Load-bearing claim

**The EB carrier surfaces residual/slack responding as a third behavioral class** that the original Swensson analysis did not separately model:
$$
\text{slack}_t = 5 - (K_t + I_t^{(1)})
$$

Per Claude-v2 digitization across intervention Set 1 sessions:
- Aden: 89% zero-slack (25/28 sessions)
- Alex: 39% zero-slack (16/41 sessions)
- Ida: 43% zero-slack (6/14 sessions)

This is the additive contribution of the framework: the saturation bound $K + I \leq 5$ forces a third quantity into algebraic view, and that quantity tracks stimulus-control quality across children even when mastery time is similar.

## Source files

- `Swensson_2024_BehavioralInterventions_source.pdf` — original article
- `swensson_2024_figure1_hires.jpg` — publisher hi-res JPG (2128×2647)
- `swensson_2024_figure1_source.pptx` — publisher PPTX (embeds JPG only; no chart data)
- `2025-10_swensson_validation_v1_withdrawn.pdf` — Eric's earlier withdrawn validation paper
