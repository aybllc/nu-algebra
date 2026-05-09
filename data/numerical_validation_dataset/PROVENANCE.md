# N/U Algebra Numerical Validation Dataset — provenance

**File:** `The_NASA_Paper_and_Small_Falcon_Algebra_Numerical_Validation_Dataset.zip` (sha256 `73a681a6c9aa6029f7f376ef999a0586ff4486ddb460de01da046afada1c43ae`, 6.7 MB, dated 2025-10-03)

**Routed:** 2026-05-08 from `/home/eric/Desktop/research/VOID/`. Source deleted after hash-verified copy at this destination + verification that contents match the already-intaken extraction at `frame-artifact-proof/historical_context/data_scripts_oct_2025/nu_numeric_results_with_readme/`.

**Contents:** 70,000+ N/U algebra validation test cases (addition sweep, product sweep, interval relation comparisons, Monte Carlo comparisons, invariants grid, associativity tests, summary digest, README). Generated 2025-09-28/29 via `generate_nu_data.py` with RNG seed 20250926, abs tol 1e-9, rel tol 1e-12.

**Key validation results** (per inner README):
- Addition: N/U uncertainty ≥ Gaussian RSS in all 8,000 cases (median ratio 1.74, range 1.00–3.54)
- Product: N/U vs first-order Gaussian comparisons
- Interval: comparison vs exact interval arithmetic
- Chain: repeated multiplication chains
- Invariants: M0, M_catch, M_flip preservation tests
- Associativity: nominal differences across the algebra

**Title note:** "NASA Paper" + "Small Falcon Algebra" reference earlier project naming for N/U; canonical name is now N/U algebra (Zenodo 17283314 for v3.1.0 of the core library).
