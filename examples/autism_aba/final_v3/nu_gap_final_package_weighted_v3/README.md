# N/U Gap-Effect Verification Package (Final)

Reproducible package to validate the effect of a long session gap on learning in Swensson et al.

## How to reproduce

```bash
python scripts/run_nu_gap.py     --csv data/sessions_swensson_master_GE_with_correct.csv     --perms 10000     --sesoi_level 0.10     --sesoi_slope 0.005
```

Outputs: `results/gap_effect_summary.csv` & `results/decision.md`

## Key results

- **IDKPTM-Set1:** ΔL=-0.95 (p=.73), ΔT=-0.415 (p=.03) → slope significantly slower post-gap.
- **CorrectAnswers:** ΔL=-0.564 (p=.55), ΔT=-0.162 (p=.31) → large but nonsignificant.

Alex & Ida: insufficient pre/post.

See `docs/CHRONOLOGY.md` for full step-by-step workflow.
