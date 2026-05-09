# N/U Algebra Numerical Validation Dataset

This archive contains the full dataset and scripts used to validate the revised N/U (Nominal/Uncertainty) Algebra framework.

## Contents

- `addition_sweep.csv` — Results of addition experiments (N/U vs Gaussian RSS). Columns: k, sum_u_nu, rss_u, ratio_nu_over_rss, nu_minus_rss.
- `product_sweep.csv` — Results of product experiments (N/U vs first-order Gaussian). Columns: n1, u1, n2, u2, u_nu, u_gauss, ratio_nu_over_gauss, diff_nu_minus_gauss.
- `interval_relation.csv` — Comparison of N/U vs exact interval arithmetic (n1,n2 ≥ 0). Columns: n1, u1, n2, u2, u_nu, interval_halfwidth, nu_minus_interval.
- `interval_relation_with_rel.csv` — Same as above, with relative error column.
- `chain_experiment.csv` — Repeated multiplication chains. Columns: L, nu_u, interval_half, ratio_nu_over_interval, diff_nu_minus_interval.
- `mc_comparisons.csv` — Monte Carlo experiments (24 rows). Columns: pair_id, a_n, a_u, b_n, b_u, dist, mc_std, u_nu, margin_nu_minus_mc.
- `invariants_grid.csv` — Invariant preservation tests. Columns: n, u, M0, M_catch, M_flip, max_abs_error.
- `associativity_nominal_diffs.csv` — Associativity test nominal differences.
- `associativity_nominal_extended.csv` — Extended associativity test, includes abs_diff and rel_diff.
- `summary.json` — Machine-readable digest of all results (min/median/max ratios, differences, tolerances).

## How to Reproduce

1. Ensure Python 3.9+ is installed.
2. Install required packages:

   ```bash
   pip install numpy pandas
   ```

3. Run the script `generate_nu_data.py` (included in supplementary material or manuscript) to regenerate all datasets.  

   ```bash
   python generate_nu_data.py
   ```

4. Outputs will match the included CSVs when using:  
   - RNG seed: **20250926** (with fixed offsets per test block)  
   - Absolute tolerance: **1e-9**  
   - Relative tolerance: **1e-12**

## Validation Results (Key Findings)

- **Addition:** N/U uncertainty ≥ Gaussian RSS in all 8,000 cases. Ratio range: 1.00–3.54, median 1.74.
- **Multiplication:** N/U uncertainty ≥ first-order Gaussian in 30,000 cases. Ratio range: 1.00–1.41 (√2 cap), median ~1.001.
- **Interval Relation:** For n1,n2 ≥ 0, N/U matches interval half-width to within floating-point error (≤0.014% relative).
- **Chain Stability:** No explosion in repeated products; max relative error ~1e-16, differences ~1e-12 (machine epsilon).
- **Monte Carlo:** Across Gaussian, Uniform, Laplace, Student-t (24 runs, 30,000 samples each), empirical std never exceeded N/U bounds.
- **Invariants:** Catch and Flip preserve M = |n| + u exactly (max abs error 0.0).
- **Associativity:** Holds within machine precision (rel error ~3.4e-16).

## License

Released under the **CC-BY 4.0 License**. You are free to use, share, and adapt with attribution.

## Citation

If you use this dataset, please cite:

Martin, E.D. (2025). The NASA Paper & Small Falcon Algebra – Numerical Validation Dataset. Zenodo. https://doi.org/10.5281/zenodo.17221863

Author Identifier
ORCID: 0009-0006-5944-1742
