# nua_psychology

**N/U Algebra for Psychology Research**

This repository applies **N/U Algebra (NUA)** to experimental and clinical psychology datasets.  
NUA is a conservative error-propagation framework originally specified in *The NASA Paper & Small Falcon Algebra*. It represents each effect as a pair `(n, u)`:

- **n** = nominal effect size (e.g., proportion correct, mean difference)  
- **u** = uncertainty (≥ Gaussian error; propagated linearly across operations)  

The system enforces:

- **Conservatism**: uncertainty never shrinks spuriously  
- **Reproducibility**: same inputs → same outputs, regardless of chaining  
- **Invariance**: the total magnitude `M = |n| + u` is preserved under all transformations  

---

## Why NUA in Psychology?

Traditional psychology often reports effects as point estimates (means, percentages, effect sizes) with confidence intervals derived from parametric assumptions. These can understate error in **small-N, single-case, or highly variable designs**.

NUA instead:

- Propagates uncertainty conservatively (e.g., subtraction → `(n₁−n₂, u₁+u₂)`)  
- Stays valid across small samples and chained designs (multiple-baseline, ABAB, cross-participant aggregation)  
- Flags only effects that survive conservative thresholds (`|Δn| > u`)  

---

## Repository Contents

- `The_NASA_Paper_and_Small_Falcon_Algebra.pdf` — Specification and proofs of the algebra  
- `summary.json` + CSV sweeps — Validation artifacts (addition, product, chain, invariants, Monte Carlo checks)  
- `nua_psychology/` — Python code and notebooks for applying NUA to psychology datasets  
- `examples/` — Worked re-analyses of published papers:  
  - Echoic blocking & tact emergence (Miller, Cox, Swensson, Oliveira, & Petursdottir, 2021)  
  - Telehealth manding intervention (Swensson et al., 2024)  
  - Daily living skills coaching (Gerow et al., 2021)  
- `tests/` — Unit tests reproducing invariant checks and numeric guarantees  

---

## Quick Start

```bash
git clone https://github.com/yourusername/nua_psychology
cd nua_psychology
pip install -r requirements.txt
```

Example (Python):

```python
from nua import Effect

# Baseline: 0/5 trials
baseline = Effect(0.0, 0.20)

# Intervention: 4/5 trials
intervention = Effect(0.80, 0.20)

# Contrast
delta = intervention - baseline
print(delta)   # (0.80, 0.40)

# Decision: is |n| > u?
if abs(delta.n) > delta.u:
    print("Flagged effect")
```

---

## Decision Rule

For a contrast `(n, u)`:

- **Flagged effect** if `|n| > u`  
- **Indeterminate** if `|n| ≤ u`  

This creates an honest filter: only effects that tower over their uncertainty survive.

---

## Examples of Application

1. **Echoic Blocking Study** (EJBA 2021)  
   - Ashley: Echoic > Blocking → Flagged `(0.70, 0.30)`  
   - Joana: NRR > Echoic → Flagged (opposite direction) `(0.80, 0.35)`  
   - Group pooled: `(0.25, 0.30)` → Indeterminate  

2. **Telehealth Mands Study** (Behavioral Interventions 2024)  
   - All 3 participants: IDKPTM acquired  
   - Pooled effect: `(0.87, 0.33)` → Robust  

3. **Daily Living Skills Coaching** (JABA 2021)  
   - 7/12 skills mastered  
   - NUA confirms mastery only where `|Δn| > u`  

---

## Validation

- **Associativity**: >99% agreement, tolerances logged  
- **Invariants**: preserved exactly (`M = |n| + u`)  
- **Monte Carlo tests**: simulated data never exceeded NUA uncertainty bounds  
- **Comparison with Gaussian/Taylor**: NUA ≥ conventional error  
  - Median ratio ~1.7 for sums  
  - Median ratio ~1.0 for products  

---

## Roadmap

- Extend NUA operators to psychology effect sizes (Hedges’ g, log odds ratio)  
- Publish replication-ready notebooks for more Swensson/telehealth datasets  
- Package into a lightweight Python module (`pip install nua-psych`)  

---

## Citation

If you use this repo, please cite:

- *The NASA Paper & Small Falcon Algebra* (2025)  
- Miller, A. C., Cox, R. E., Swensson, R. M., Oliveira, J. S. C. D., & Petursdottir, A. I. (2021). *Effects of blocking echoic responses on tact emergence following stimulus pairing.* *European Journal of Behavior Analysis, 22*(2), 213–225.  
- Swensson, R. M., et al. (2024). *Teaching children with ASD to mand for answers via telehealth.* *Behavioral Interventions.*  
- Gerow, S., et al. (2021). *Telehealth parent coaching to improve daily living skills for children with ASD.* *Journal of Applied Behavior Analysis, 54*(2), 566–581.  
