#!/usr/bin/env python3
import argparse, os, math, sys, json, random
from collections import defaultdict
from statistics import mean
import pandas as pd
import numpy as np

def weighted_mean(y, w):
    y, w = np.asarray(y, dtype=float), np.asarray(w, dtype=float)
    return (w * y).sum() / max(w.sum(), 1e-12)

def wls_slope(y, t, w):
    # Weighted least squares slope of y ~ 1 + t
    y = np.asarray(y, dtype=float)
    t = np.asarray(t, dtype=float)
    w = np.asarray(w, dtype=float)
    X = np.column_stack([np.ones_like(t), t])
    WX = X * w[:, None]
    XtWX = X.T @ WX
    XtWy = X.T @ (w * y)
    beta = np.linalg.pinv(XtWX) @ XtWy
    return float(beta[1])

def compute_u(ioa, cf, rf):
    # clip to [0,1] and combine
    def c(v):
        try:
            v=float(v)
        except:
            return 1.0
        return min(max(v, 0.0), 1.0)
    ioa=c(ioa); cf=c(cf); rf=c(rf)
    u = (1.0-ioa) + (1.0-cf) + (1.0-rf)
    return min(max(u,0.0),1.0)

def block_stats(df_block, metric_col="metric_value"):
    # Compute weights and summary stats for a block
    y = df_block[metric_col].astype(float).values
    t = df_block["session_index"].astype(float).values
    u = [compute_u(r.ioa, r.caregiver_fidelity, r.researcher_fidelity) for r in df_block.itertuples()]
    w = 1.0/(np.asarray(u)+1e-6)
    return {
        "n": float(weighted_mean(y, w)),
        "beta": float(wls_slope(y, t, w)),
        "u_mean": float(np.mean(u)),
        "n_points": int(len(y))
    }

def delta_stats(df_pp, metric_col="metric_value", rng=None):
    pre = df_pp[df_pp["gap_flag"].str.lower()=="pre"]
    post= df_pp[df_pp["gap_flag"].str.lower()=="post"]
    if len(pre)==0 or len(post)==0:
        return None
    s_pre = block_stats(pre, metric_col)
    s_post= block_stats(post, metric_col)
    return {
        "delta_L": s_post["n"] - s_pre["n"],
        "delta_T": s_post["beta"] - s_pre["beta"],
        "u_bar": (s_post["u_mean"] + s_pre["u_mean"])/2.0,
        "n_pre": s_pre["n_points"],
        "n_post": s_post["n_points"]
    }

def permute_cutpoint(series, k_pre):
    # Keep order; change the cutpoint to a different index -> new pre/post split lengths preserved
    # Return list of (pre_idx_set) as boolean mask
    n = len(series)
    admissible = [i for i in range(1, n) if i!=k_pre and i>1 and i<n-1]
    if not admissible:
        return []
    return admissible

def run_permutation(df_pp, metric_col, perms=10000, seed=1337):
    # df_pp: single participant rows ordered by session_index within INTERVENTION (user must filter in CSV)
    df_pp = df_pp.sort_values("session_index")
    # observed split
    pre_n = (df_pp["gap_flag"].str.lower()=="pre").sum()
    post_n= (df_pp["gap_flag"].str.lower()=="post").sum()
    if pre_n==0 or post_n==0:
        return None
    obs = delta_stats(df_pp, metric_col)
    # build all admissible cutpoints that keep the same counts (choose positions)
    n = len(df_pp)
    # Fixed counts -> all binary labelings with pre_n ones then post_n zeros in order -> equivalent to choosing cut at index pre_n
    # For permutation, slide the cutpoint along admissible indices that yield same counts (we'll treat as moving window)
    # But counts must be preserved; hence the only labeling with same counts is the original. Instead, we implement a label-shuffle that preserves run lengths by circular shift.
    # We'll use circular shifts of the label vector to generate permutations.
    labels = (["pre"]*pre_n)+(["post"]*post_n)
    stats_L = []
    stats_T = []
    rng = random.Random(seed)
    y = df_pp[metric_col].astype(float).values
    t = df_pp["session_index"].astype(float).values
    ioa = df_pp["ioa"].values
    cf  = df_pp["caregiver_fidelity"].values
    rf  = df_pp["researcher_fidelity"].values

    def compute_for_labels(labs):
        tmp = df_pp.copy()
        tmp["gap_flag"] = labs
        d = delta_stats(tmp, metric_col)
        return d["delta_L"], d["delta_T"]

    obs_L, obs_T = obs["delta_L"], obs["delta_T"]
    # generate permutations by circularly shifting labels
    for b in range(perms):
        shift = rng.randrange(1, n-1)  # avoid identity shift often; still okay if repeats
        labs = labels[-shift:]+labels[:-shift]
        L,T = compute_for_labels(labs)
        stats_L.append(L)
        stats_T.append(T)
    # two-sided p-values
    p_L = (1 + sum(1 for v in stats_L if abs(v) >= abs(obs_L))) / (1 + perms)
    p_T = (1 + sum(1 for v in stats_T if abs(v) >= abs(obs_T))) / (1 + perms)
    return obs, p_L, p_T

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="path to sessions CSV")
    ap.add_argument("--metric", default="IDKPTM", help="primary metric to analyze")
    ap.add_argument("--sesoi_level", type=float, default=0.10)
    ap.add_argument("--sesoi_slope", type=float, default=0.005)
    ap.add_argument("--perms", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=1337)
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    # normalize
    df["metric_name"] = df["metric_name"].astype(str)
    df = df[df["metric_name"].str.lower() == args.metric.lower()].copy()
    if df.empty:
        print(f"No rows for metric={args.metric}. Check 'metric_name' column.", file=sys.stderr)
        sys.exit(2)

    participants = sorted(df["participant"].dropna().unique())
    rows = []
    decisions = []
    for p in participants:
        dfp = df[df["participant"]==p].copy().sort_values("session_index")
        res = run_permutation(dfp, "metric_value", perms=args.perms, seed=args.seed)
        if res is None:
            rows.append({"participant": p, "note": "insufficient pre/post data"})
            continue
        obs, pL, pT = res
        dec = ("no_detectable_effect" if (abs(obs["delta_L"]) <= args.sesoi_level and abs(obs["delta_T"]) <= args.sesoi_slope and pL>0.10 and pT>0.10) else "possible_effect")
        rows.append({
            "participant": p,
            "delta_level": obs["delta_L"],
            "delta_slope": obs["delta_T"],
            "u_bar": obs["u_bar"],
            "n_pre": obs["n_pre"],
            "n_post": obs["n_post"],
            "p_level": pL,
            "p_slope": pT,
            "decision": dec
        })
        decisions.append((p, dec))

    out_csv = "results/gap_effect_summary.csv"
    os.makedirs("results", exist_ok=True)
    pd.DataFrame(rows).to_csv(out_csv, index=False)

    # decision.md
    lines = ["# Gap‑Effect Decision",
             f"- Primary metric: **{args.metric}**",
             f"- SESOI: level ±{args.sesoi_level}, slope ±{args.sesoi_slope}/session",
             f"- Permutations: {args.perms} (circular label shifts)",
             "",
             "## Per‑participant"
    ]
    for r in rows:
        if "participant" in r and "decision" in r:
            lines.append(f"- {r['participant']}: {r.get('decision','')} "
                         f"(Δ_L={r.get('delta_level',''):.3g}, Δ_T={r.get('delta_slope',''):.3g}, "
                         f"p_L={r.get('p_level',''):.3g}, p_T={r.get('p_slope',''):.3g})")
    lines.extend([
        "",
        "### Notes",
        "- Weighted means and slopes use **w_t = 1/(u_t+ε)** with u_t built from IOA and fidelity.",
        "- Decisions require both stats to be within SESOI and permutation p‑values > 0.10.",
        "- Re‑run with `--metric Correct` as a sensitivity check and include the ‘5‑targets’ sessions as a second run."
    ])
    open("results/decision.md","w").write("\n".join(lines))

    print(f"Wrote {out_csv} and results/decision.md")

if __name__ == "__main__":
    main()
