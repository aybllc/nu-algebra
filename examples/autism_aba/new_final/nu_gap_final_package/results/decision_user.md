# Gap‑Effect Decision
- Primary metric: **IDKPTM-Set1**
- SESOI: level ±0.1, slope ±0.005/session
- Permutations: 10000 (circular label shifts)

## Per‑participant
- Aden: possible_effect (Δ_L=-0.948, Δ_T=-0.415, p_L=0.727, p_T=0.0324)

### Notes
- Weighted means and slopes use **w_t = 1/(u_t+ε)** with u_t built from IOA and fidelity.
- Decisions require both stats to be within SESOI and permutation p‑values > 0.10.
- Re‑run with `--metric Correct` as a sensitivity check and include the ‘5‑targets’ sessions as a second run.