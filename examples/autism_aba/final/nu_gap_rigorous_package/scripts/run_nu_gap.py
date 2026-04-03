#!/usr/bin/env python3
"""
N/U Algebra Gap-Effect Test (Weighted) — Self-Contained

Implements the METHODS.md specification:
- u = (1-ioa) + (1-caregiver_fidelity) + (1-researcher_fidelity), clipped to [0,1]
- w = 1/(u + eps)
- Level effect ΔL: weighted mean(post) − weighted mean(pre)
- Trend effect ΔT: WLS slope(post) − WLS slope(pre)
- Permutation inference: circularly shift (values, weights) together; pre/post mask fixed; two-sided p with add-one
- SESOI thresholds: ±0.10 (level), ±0.005/session (slope)

Usage:
  python scripts/run_nu_gap.py --csv data/sessions_swensson_master_GE_with_correct.csv --perms 10000 --sesoi_level 0.10 --sesoi_slope 0.005

CSV columns (case-insensitive; auto-mapped if needed):
  participant, metric_name, session_index, metric_value, phase, ioa, caregiver_fidelity, researcher_fidelity, gap_flag
"""

import argparse, pandas as pd, numpy as np, os, sys, math, random

def _lc_cols(df):
    m = {c:c for c in df.columns}
    # try common alternatives
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
    # Weighted least squares via normal equations
    X = np.column_stack([np.ones_like(x), x])
    WX = X * w[:, None]
    XtWX = X.T @ WX
    XtWy = X.T @ (w * y)
    try:
        beta = np.linalg.pinv(XtWX) @ XtWy
    except np.linalg.LinAlgError:
        return float("nan")
    return float(beta[1])

def delta_stats(sub):
    # Expect columns: session_index, metric_value, gap_flag, ioa, caregiver_fidelity, researcher_fidelity
    pre = sub[sub["gap_flag"].str.lower() == "pre"].copy()
    post = sub[sub["gap_flag"].str.lower() == "post"].copy()
    if len(pre) < 3 or len(post) < 3:
        return None
    # weights
    u_pre, w_pre = weights_from_uncertainty(pre)
    u_post, w_post = weights_from_uncertainty(post)
    # level
    dL = wmean(pre["metric_value"], w_pre)
    dL = wmean(post["metric_value"], w_post) - dL
    # slope
    b_pre = wls_slope(pre["session_index"], pre["metric_value"], w_pre)
    b_post = wls_slope(post["session_index"], post["metric_value"], w_post)
    dT = b_post - b_pre
    return dict(delta_L=float(dL), delta_T=float(dT),
                n_pre=int(len(pre)), n_post=int(len(post)),
                ubar=float((u_pre.mean() + u_post.mean()) / 2.0))

def perm_pvals(sub, perms=10000, seed=1337):
    sub = sub.sort_values("session_index").reset_index(drop=True).copy()
    mask_post = sub["gap_flag"].str.lower() == "post"
    if mask_post.sum() == 0 or (~mask_post).sum() == 0:
        return None
    # observed
    obs = delta_stats(sub)
    if obs is None:
        return None
    obsL, obsT = obs["delta_L"], obs["delta_T"]
    # values & weights for rotation (recompute weights per row once)
    u_all, w_all = weights_from_uncertainty(sub)
    y = sub["metric_value"].to_numpy(float)
    t = sub["session_index"].to_numpy(float)
    rng = np.random.RandomState(seed)
    Ls = []; Ts = []
    n = len(sub)
    pre_idx = np.where(~mask_post)[0]
    post_idx = np.where(mask_post)[0]
    for _ in range(perms):
        k = rng.randint(0, n)  # circular shift amount
        y_b = np.roll(y, k)
        w_b = np.roll(w_all, k)  # rotate weights WITH values
        # level
        L_pre = wmean(y_b[pre_idx], w_b[pre_idx])
        L_post = wmean(y_b[post_idx], w_b[post_idx])
        dL_b = L_post - L_pre
        # slope
        b_pre = wls_slope(t[pre_idx], y_b[pre_idx], w_b[pre_idx])
        b_post = wls_slope(t[post_idx], y_b[post_idx], w_b[post_idx])
        dT_b = b_post - b_pre
        if not (math.isnan(dL_b) or math.isnan(dT_b)):
            Ls.append(dL_b); Ts.append(dT_b)
    Ls = np.array(Ls); Ts = np.array(Ts)
    pL = (1 + np.sum(np.abs(Ls) >= abs(obsL))) / (1 + len(Ls))
    pT = (1 + np.sum(np.abs(Ts) >= abs(obsT))) / (1 + len(Ts))
    return obs, float(pL), float(pT)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--perms", type=int, default=10000)
    ap.add_argument("--sesoi_level", type=float, default=0.10)
    ap.add_argument("--sesoi_slope", type=float, default=0.005)
    ap.add_argument("--alpha", type=float, default=0.05)
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    df = _lc_cols(df)
    required = ["participant","metric_name","session_index","metric_value","gap_flag","ioa","caregiver_fidelity","researcher_fidelity"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        sys.stderr.write(f"ERROR: missing columns: {missing}\n")
        sys.exit(2)

    rows = []
    for (p, m), sub in df.groupby(["participant","metric_name"]):
        res = perm_pvals(sub, perms=args.perms, seed=1337)
        if res is None:
            rows.append(dict(participant=p, metric=m, status="insufficient_prepost"))
            continue
        obs, pL, pT = res
        # Decision: AND rule (exceeds SESOI and significant)
        eff_L = (abs(obs["delta_L"]) >= args.sesoi_level) and (pL < args.alpha)
        eff_T = (abs(obs["delta_T"]) >= args.sesoi_slope) and (pT < args.alpha)
        status = "effect_present" if (eff_L or eff_T) else "no_effect_or_inconclusive"
        rows.append(dict(participant=p, metric=m, status=status,
                         delta_level=obs["delta_L"], delta_slope=obs["delta_T"],
                         p_level=pL, p_slope=pT,
                         n_pre=obs["n_pre"], n_post=obs["n_post"], u_bar=obs["ubar"]))

    out_dir = os.path.join(os.path.dirname(args.csv), "..", "results")
    os.makedirs(out_dir, exist_ok=True)
    out_csv = os.path.join(out_dir, "gap_effect_summary.csv")
    pd.DataFrame(rows).to_csv(out_csv, index=False)

    # decision.md
    lines = [f"# Gap-Effect Results (Weighted; perms={args.perms}; SESOI L±{args.sesoi_level}, T±{args.sesoi_slope}/session)",""]
    for r in rows:
        if r.get("status") == "insufficient_prepost":
            lines.append(f"- {r['participant']} · {r['metric']}: insufficient pre/post data")
        else:
            lines.append(f"- {r['participant']} · {r['metric']}: {r['status']} "
                         f"(ΔL={r['delta_level']:.3f}, p_L={r['p_level']:.3f}; "
                         f"ΔT={r['delta_slope']:.3f}, p_T={r['p_slope']:.3f}; "
                         f"n_pre={r['n_pre']}, n_post={r['n_post']}, ū={r['u_bar']:.3f})")
    with open(os.path.join(out_dir, "decision.md"), "w") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    main()
