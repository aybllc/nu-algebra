# METHODS

### Data
Single-case session-by-session data digitized from Swensson et al. (2024) Figure 1.
Metrics: IDKPTM-Set1 (black points) and CorrectAnswers (light-gray bars).
Each row: participant, metric_name, session_index, metric_value, phase, ioa, caregiver_fidelity, researcher_fidelity, gap_flag.

### N/U Algebra
Observation = (n,u) where n ∈ [0,1], u≥0 uncertainty from IOA/fidelity:
u = (1−IOA)+(1−Caregiver)+(1−Researcher) clipped [0,1]; weight = 1/(u+ε).
Level ΔL = weighted mean(post) − weighted mean(pre).
Trend ΔT = difference of weighted least-squares slopes (metric on session).

### SESOI
Smallest Effect Size Of Interest: ±0.10 for level, ±0.005/session for slope.

### Permutation
Pre/post labels circularly shifted B=10,000 times to create null.
Two-sided p = (1 + #{|Δb| ≥ |Δobs|})/(1+B).
