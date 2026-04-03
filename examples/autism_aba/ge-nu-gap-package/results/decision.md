# Gap‑Effect Decision
- Primary metric: **TODO**
- SESOI: level ±0.1, slope ±0.005/session
- Permutations: 10000 (circular label shifts)

## Per‑participant

### Notes
- Weighted means and slopes use **w_t = 1/(u_t+ε)** with u_t built from IOA and fidelity.
- Decisions require both stats to be within SESOI and permutation p‑values > 0.10.
- Re‑run with `--metric Correct` as a sensitivity check and include the ‘5‑targets’ sessions as a second run.