#!/usr/bin/env python3
"""
Detailed computation breakdown for Aden
Shows step-by-step calculations for the gap-effect analysis
"""

import pandas as pd
import numpy as np
import sys

def _lc_cols(df):
    ren = {}
    for c in df.columns:
        lc = c.strip().lower()
        if lc == "participant": ren[c] = "participant"
        elif lc in ("metric_name","metric"): ren[c] = "metric_name"
        elif lc in ("session_index","session","x"): ren[c] = "session_index"
        elif lc in ("metric_value","value","y"): ren[c] = "metric_value"
        elif lc == "phase": ren[c] = "phase"
        elif lc == "ioa": ren[c] = "ioa"
        elif lc in ("caregiver_fidelity","caregiver"): ren[c] = "caregiver_fidelity"
        elif lc in ("researcher_fidelity","researcher"): ren[c] = "researcher_fidelity"
        elif lc in ("gap_flag","flag","gap"): ren[c] = "gap_flag"
    return df.rename(columns=ren)

def compute_u(ioa, cf, rf):
    def c(v):
        try:
            v = float(v)
        except Exception:
            return 1.0
        return min(max(v, 0.0), 1.0)
    ioa = c(ioa); cf = c(cf); rf = c(rf)
    u = (1.0 - ioa) + (1.0 - cf) + (1.0 - rf)
    return min(max(u, 0.0), 1.0)

def weights_from_uncertainty(df, eps=1e-6):
    u = []
    for r in df.itertuples():
        u.append(compute_u(getattr(r, "ioa", 1.0),
                           getattr(r, "caregiver_fidelity", 1.0),
                           getattr(r, "researcher_fidelity", 1.0)))
    u = np.array(u, dtype=float)
    w = 1.0 / (u + eps)
    return u, w

def wmean(y, w):
    y = np.asarray(y, float); w = np.asarray(w, float)
    s = w.sum()
    return float((w * y).sum() / s) if s > 0 else float("nan")

def wls_slope(x, y, w):
    x = np.asarray(x, float); y = np.asarray(y, float); w = np.asarray(w, float)
    if len(x) < 2: return float("nan")
    X = np.column_stack([np.ones_like(x), x])
    WX = X * w[:, None]
    XtWX = X.T @ WX
    XtWy = X.T @ (w * y)
    try:
        beta = np.linalg.pinv(XtWX) @ XtWy
    except np.linalg.LinAlgError:
        return float("nan")
    return float(beta[1])

# Read data
df = pd.read_csv("sessions_swensson_master_GE_with_correct.csv")
df = _lc_cols(df)

# Filter for Aden
aden = df[df["participant"] == "Aden"].copy()

print("="*80)
print("DETAILED COMPUTATION BREAKDOWN FOR ADEN")
print("="*80)

for metric in aden["metric_name"].unique():
    print(f"\n{'='*80}")
    print(f"METRIC: {metric}")
    print(f"{'='*80}\n")

    sub = aden[aden["metric_name"] == metric].copy()
    pre = sub[sub["gap_flag"].str.lower() == "pre"].copy()
    post = sub[sub["gap_flag"].str.lower() == "post"].copy()

    print(f"Total observations: {len(sub)}")
    print(f"  Pre-phase: {len(pre)}")
    print(f"  Post-phase: {len(post)}")

    if len(pre) < 3 or len(post) < 3:
        print(f"\n⚠️  INSUFFICIENT DATA (need ≥3 in each phase)")
        continue

    print(f"\n{'-'*80}")
    print(f"STEP 1: UNCERTAINTY & WEIGHT COMPUTATION")
    print(f"{'-'*80}")

    # Show first few rows of each phase
    print(f"\nPRE-PHASE (first 5 rows):")
    print(f"{'Session':<10} {'Value':<15} {'IOA':<8} {'CaregFid':<8} {'ResFid':<8} {'u':<12} {'w':<12}")
    print(f"{'-'*95}")

    u_pre, w_pre = weights_from_uncertainty(pre)
    for i, (idx, row) in enumerate(pre.head(5).iterrows()):
        ioa = row.get('ioa', 1.0)
        cf = row.get('caregiver_fidelity', 1.0)
        rf = row.get('researcher_fidelity', 1.0)
        print(f"{row['session_index']:<10.2f} {row['metric_value']:<15.4f} {ioa:<8.4f} {cf:<8.4f} {rf:<8.4f} {u_pre[i]:<12.6f} {w_pre[i]:<12.2f}")

    if len(pre) > 5:
        print(f"... ({len(pre)-5} more rows)")

    print(f"\nPOST-PHASE (first 5 rows):")
    print(f"{'Session':<10} {'Value':<15} {'IOA':<8} {'CaregFid':<8} {'ResFid':<8} {'u':<12} {'w':<12}")
    print(f"{'-'*95}")

    u_post, w_post = weights_from_uncertainty(post)
    for i, (idx, row) in enumerate(post.head(5).iterrows()):
        ioa = row.get('ioa', 1.0)
        cf = row.get('caregiver_fidelity', 1.0)
        rf = row.get('researcher_fidelity', 1.0)
        print(f"{row['session_index']:<10.2f} {row['metric_value']:<15.4f} {ioa:<8.4f} {cf:<8.4f} {rf:<8.4f} {u_post[i]:<12.6f} {w_post[i]:<12.2f}")

    if len(post) > 5:
        print(f"... ({len(post)-5} more rows)")

    print(f"\n{'-'*80}")
    print(f"STEP 2: LEVEL EFFECT (ΔL)")
    print(f"{'-'*80}")

    mean_pre = wmean(pre["metric_value"], w_pre)
    mean_post = wmean(post["metric_value"], w_post)
    delta_L = mean_post - mean_pre

    print(f"\nWeighted mean (pre):  {mean_pre:.6f}")
    print(f"Weighted mean (post): {mean_post:.6f}")
    print(f"ΔL = {mean_post:.6f} - {mean_pre:.6f} = {delta_L:.6f}")

    print(f"\n{'-'*80}")
    print(f"STEP 3: TREND EFFECT (ΔT)")
    print(f"{'-'*80}")

    slope_pre = wls_slope(pre["session_index"], pre["metric_value"], w_pre)
    slope_post = wls_slope(post["session_index"], post["metric_value"], w_post)
    delta_T = slope_post - slope_pre

    print(f"\nWLS slope (pre):  {slope_pre:.6f}")
    print(f"WLS slope (post): {slope_post:.6f}")
    print(f"ΔT = {slope_post:.6f} - {slope_pre:.6f} = {delta_T:.6f}")

    print(f"\n{'-'*80}")
    print(f"STEP 4: PERMUTATION TEST")
    print(f"{'-'*80}")

    # Run a few permutations as examples
    sub_sorted = sub.sort_values("session_index").reset_index(drop=True).copy()
    mask_post = sub_sorted["gap_flag"].str.lower() == "post"
    u_all, w_all = weights_from_uncertainty(sub_sorted)
    y = sub_sorted["metric_value"].to_numpy(float)
    t = sub_sorted["session_index"].to_numpy(float)

    pre_idx = np.where(~mask_post)[0]
    post_idx = np.where(mask_post)[0]

    print(f"\nObserved ΔL: {delta_L:.6f}")
    print(f"Observed ΔT: {delta_T:.6f}")
    print(f"\nExample permutations (first 5 of 10000):")
    print(f"{'Perm':<6} {'Shift':<7} {'ΔL_perm':<15} {'ΔT_perm':<15} {'|ΔL_perm|≥|ΔL_obs|':<20} {'|ΔT_perm|≥|ΔT_obs|':<20}")
    print(f"{'-'*95}")

    rng = np.random.RandomState(1337)
    n = len(sub_sorted)

    for perm_idx in range(5):
        k = rng.randint(0, n)
        y_b = np.roll(y, k)
        w_b = np.roll(w_all, k)

        L_pre = wmean(y_b[pre_idx], w_b[pre_idx])
        L_post = wmean(y_b[post_idx], w_b[post_idx])
        dL_b = L_post - L_pre

        b_pre = wls_slope(t[pre_idx], y_b[pre_idx], w_b[pre_idx])
        b_post = wls_slope(t[post_idx], y_b[post_idx], w_b[post_idx])
        dT_b = b_post - b_pre

        L_extreme = "Yes" if abs(dL_b) >= abs(delta_L) else "No"
        T_extreme = "Yes" if abs(dT_b) >= abs(delta_T) else "No"

        print(f"{perm_idx+1:<6} {k:<7} {dL_b:<15.6f} {dT_b:<15.6f} {L_extreme:<20} {T_extreme:<20}")

    print(f"... (9995 more permutations)")

    # Load actual results
    results = pd.read_csv("../results/gap_effect_summary.csv")
    result = results[(results["participant"] == "Aden") & (results["metric"] == metric)]

    if not result.empty:
        pL = result.iloc[0]["p_level"]
        pT = result.iloc[0]["p_slope"]

        print(f"\n{'-'*80}")
        print(f"STEP 5: STATISTICAL DECISION")
        print(f"{'-'*80}")

        print(f"\nTwo-sided p-values:")
        print(f"  p_level: {pL:.4f}")
        print(f"  p_slope: {pT:.4f}")

        sesoi_L = 0.10
        sesoi_T = 0.005
        alpha = 0.05

        print(f"\nSESOI thresholds:")
        print(f"  Level: ±{sesoi_L}")
        print(f"  Slope: ±{sesoi_T}/session")
        print(f"  Alpha: {alpha}")

        eff_L = (abs(delta_L) >= sesoi_L) and (pL < alpha)
        eff_T = (abs(delta_T) >= sesoi_T) and (pT < alpha)

        print(f"\nLevel effect check:")
        print(f"  |ΔL| = {abs(delta_L):.4f} {'≥' if abs(delta_L) >= sesoi_L else '<'} {sesoi_L} AND p = {pL:.4f} {'<' if pL < alpha else '≥'} {alpha}")
        print(f"  → Effect present: {eff_L}")

        print(f"\nTrend effect check:")
        print(f"  |ΔT| = {abs(delta_T):.4f} {'≥' if abs(delta_T) >= sesoi_T else '<'} {sesoi_T} AND p = {pT:.4f} {'<' if pT < alpha else '≥'} {alpha}")
        print(f"  → Effect present: {eff_T}")

        status = "EFFECT PRESENT" if (eff_L or eff_T) else "NO EFFECT OR INCONCLUSIVE"
        print(f"\nFINAL DECISION (OR rule): {status}")
        print(f"  (Effect present if either level OR trend shows significant SESOI-exceeding change)")

print(f"\n{'='*80}")
print(f"END OF REPORT")
print(f"{'='*80}\n")
