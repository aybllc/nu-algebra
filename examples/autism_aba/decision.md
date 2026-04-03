# Gap‑Effect Decision
- Primary metric: **IDKPTM**
- SESOI: level ±0.1, slope ±0.005/session
- Permutations: 5000 (circular label shifts)

## Per‑participant
- Aden: possible_effect (Δ_L=0.5, Δ_T=0.0197, p_L=0.0686, p_T=0.0002)
- Alex: possible_effect (Δ_L=0.455, Δ_T=0.0169, p_L=0.0862, p_T=0.0002)
- Ida: possible_effect (Δ_L=0.352, Δ_T=0.00838, p_L=0.0002, p_T=0.0002)

### Notes
- Weighted means and slopes use **w_t = 1/(u_t+ε)** with u_t built from IOA and fidelity.
- Decisions require both stats to be within SESOI and permutation p‑values > 0.10.
- Re‑run with `--metric Correct` as a sensitivity check and include the ‘5‑targets’ sessions as a second run.