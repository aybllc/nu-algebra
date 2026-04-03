# NU Algebra — Verification & Comparison Report

This report recomputes key comparisons from the uploaded dataset to provide proof-style evidence prior to external outreach.

## Addition: NU vs Gaussian RSS

- Rows: **8000**

- Ratio NU/RSS: min **1.000000**, median **1.740593**, max **3.539944**

- Difference NU−RSS: min **0**, max **30.598**

- Any violation (NU < RSS beyond tol)? **False**

## Product: NU vs First-Order Gaussian Propagation

- Rows: **30000**

- Ratio NU/Gaussian: min **1.000000000000**, median **1.001143063513**, max **1.414213486103**

- Difference NU−Gaussian: min **2.04604e-08**, max **2.01505e+06**

- Any violation (NU < Gaussian beyond tol)? **False**

## Interval Relation (n₁,n₂ ≥ 0): NU vs Exact Interval Half-Width

- Rows: **30000**

- Max |NU − Interval|: **0.000143584**

- Max relative error (stable denom): **0.000143584**

- Counts: |diff| > 1e−9 → **29973**, relative error > 1e−12 → **29384**

## Repeated Products (Chain): NU vs Interval Half-Width by Length L

- L=3: count **800**, ratio min **0.999999656921**, median **0.999999999999**, max **1.000000001310**, max |diff| **5.25073e-09**

- L=5: count **800**, ratio min **0.999994059051**, median **0.999999999943**, max **1.000000000447**, max |diff| **5.81812e-07**

- L=10: count **800**, ratio min **0.999995463856**, median **0.999999987661**, max **1.000000000014**, max |diff| **0.000318045**

- L=20: count **800**, ratio min **0.999972455790**, median **0.999999500654**, max **0.999999999955**, max |diff| **1.46573**

- Global max |diff| across all chains: **1.46573**

## Monte Carlo Comparisons (empirical std vs NU.u)

- Rows: **24**

- Margin NU.u − MC.std: min **0.685886**, median **2.61641**, max **4.23806**

- Any MC.std > NU.u beyond tol? **False**

## Invariants Check (M = |n| + u)

- Rows: **54**

- Max absolute error across grid: **0**

## Associativity (Nominal Equality up to FP)

- Extended study (rows 10000): max rel diff **3.432e-16**, p99 **2.183e-16**, median **0.000e+00**

- Nominal absolute diff study: rows **20000**, max |diff| **128** (large values occur only at huge magnitudes; relative errors are epsilon-scale).
