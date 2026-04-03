# Chronology of Verification Work

**2025-10-02** — Final package creation

1. **Digitization**  
   - Extracted IDKPTM-Set1 points (black markers) from Figure 1 using WebPlotDigitizer.  
   - Built `sessions_swensson_master_GE_flagged.csv` with IOA/fidelity values and `gap_flag` marking Aden ≤25=pre, >25=post.

2. **First analysis (IDKPTM only)**  
   - Ran N/U Algebra gap-effect test (permutation, SESOI ±0.10 level ±0.005 slope).  
   - Results: Aden slope ΔT=-0.415 (p=.03) significant; level ΔL=-0.95 (p=.73) nonsignificant. Alex & Ida: insufficient pre/post.

3. **Extended analysis (Correct Answers)**  
   - Digitized light-gray bars (Correct Answers) per participant.  
   - Appended to dataset as new metric_name=CorrectAnswers.  
   - Produced `sessions_swensson_master_GE_with_correct.csv`.  
   - Re-ran analysis: Aden ΔL=-0.564, ΔT=-0.162 (both exceed SESOI but p=.55 & .31, not significant). Alex & Ida: insufficient pre/post.

4. **Packaging for peer review**  
   - Methods documented in `METHODS.md` (N/U algebra, WLS slopes, permutation).  
   - Provenance recorded in `PROVENANCE.md`.  
   - Results saved (`gap_effect_summary.csv`, `decision.md`).  
   - Original intermediate outputs preserved for transparency.

Summary: Gap significantly slowed **IDKPTM** acquisition slope but not mean level; **Correct Answers** showed similar directional slowing/decline but not statistically significant.
