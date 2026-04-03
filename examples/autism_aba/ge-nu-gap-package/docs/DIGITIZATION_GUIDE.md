# Figure Digitization Guide (5–10 minutes)

Goal: Convert Figure 1’s per-session series into `data/sessions_swensson.csv`.

Tools: WebPlotDigitizer (web), or any digitizer you prefer.

Steps:
1) Export Figure 1 as a clean image (we included a placeholder path if you already have it).
2) In WPD: Load image → Define axes (0..1 for y, sessions for x). Use separate datasets for each participant and metric (IDKPTM or Correct).
3) Click each session point in **intervention only** (baseline not needed for this test). Mark cut where the gap occurs as `gap_flag` (pre/post).
4) Export as CSV and map columns to the template:
   - participant, session_index, metric_name (IDKPTM or Correct), metric_value (0–1), gap_flag (pre/post),
     ioa, caregiver_fidelity, researcher_fidelity, targets, notes.

Pro tip: If IOA/fidelity are phase-level only, paste the same values down the column for that block.

Command to run after saving CSV (example with IDKPTM):
```bash
python scripts/ge_nu_gap_effect.py --csv data/sessions_swensson.csv --metric IDKPTM --sesoi_level 0.10 --sesoi_slope 0.005 --perms 10000
```

Outputs appear in `results/` as `gap_effect_summary.csv` and `decision.md`.
