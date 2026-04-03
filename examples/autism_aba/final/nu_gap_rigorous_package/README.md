# N/U Gap‑Effect Verification Package (v2025-10-02)

**Purpose:** Provide a complete, reviewer‑ready record of how we verified whether the session gap affected outcomes in the Swensson et al. study, using digitized Figure 1 data and the Lean N/U Core v1 analysis.

## Contents
- `docs/METHODS.md` — Formal methods (N/U algebra, statistics, permutation, SESOI).
- `docs/PROVENANCE.md` — Data provenance, reproducibility commands, and decisions.
- `docs/REFERENCES.md` — Citations for the study and N/U algebra.
- `data/` — Digitized series (`sessions_swensson_master_GE_flagged.csv`) and, if provided, original participant CSVs.
- `scripts/run_nu_gap.py` — Self‑contained analysis (rebuilds the results from the data).
- `results/` — Computed outputs: `gap_effect_summary.csv` and `decision.md`.

## Quickstart
```bash
python scripts/run_nu_gap.py --csv data/sessions_swensson_master_GE_flagged.csv --perms 10000 --sesoi_level 0.10 --sesoi_slope 0.005
```
Outputs will be written to `results/`.

## Summary (this run)
See `results/decision.md` and `results/gap_effect_summary.csv` for the exact values from the included data.

Martin, E. D. (2025). The NASA Paper & Small Falcon Algebra. Zenodo. 
https://doi.org/10.5281/zenodo.17172694

Martin, E. D. (2025). The NASA Paper and Small Falcon Algebra Numerical Validation Dataset [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17221863
