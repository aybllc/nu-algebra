# PROVENANCE

- Package generated: 2025-10-02
- Input data:
  - `data/sessions_swensson_master_GE_flagged.csv` (digitized series, with `gap_flag` marking Aden's break at Session 25).
  - Original per‑participant CSVs included if provided.
- Script: `scripts/run_nu_gap.py` recreates the analysis from the CSV.

## Reproducibility
```bash
python scripts/run_nu_gap.py --csv data/sessions_swensson_master_GE_flagged.csv --perms 10000 --sesoi_level 0.10 --sesoi_slope 0.005
```
Expected outputs: `results/gap_effect_summary.csv`, `results/decision.md`.

## Decisions & Parameters
- Metric analyzed: IDKPTM‑Set1
- SESOI: level ±0.10, slope ±0.005/session
- Permutations: 10,000 recommended (5,000 used in this included run for speed)
- Weighting from IOA/fidelity per Table 1 means.
