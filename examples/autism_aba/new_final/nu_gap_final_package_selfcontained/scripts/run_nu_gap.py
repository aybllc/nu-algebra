#!/usr/bin/env python3
"""
Self-contained N/U Algebra gap-effect test.

Usage:
  python run_nu_gap.py --csv data/sessions_swensson_master_GE_with_correct.csv --perms 10000 --sesoi_level 0.10 --sesoi_slope 0.005

Input CSV must have:
  Participant,Metric,Session,Value,gap_flag

gap_flag: "pre" or "post" (others ignored)
"""

import argparse, pandas as pd, numpy as np

def weighted_mean(x, w):
    w = np.where(np.isnan(w), 0, w)
    return np.sum(w*x) / np.sum(w) if np.sum(w)>0 else np.nan

def wls_slope(x, y, w):
    if len(x)==0: return np.nan
    W = np.diag(w)
    X = np.vstack([np.ones(len(x)), x]).T
    try:
        beta = np.linalg.inv(X.T@W@X) @ (X.T@W@y)
        return beta[1]
    except np.linalg.LinAlgError:
        return np.nan

def run_gap(df, perms=10000, sesoi_level=0.10, sesoi_slope=0.005):
    results = []
    for (p,m),sub in df.groupby(["Participant","Metric"]):
        pre = sub[sub.gap_flag=="pre"]
        post = sub[sub.gap_flag=="post"]
        if len(pre)<3 or len(post)<3:
            results.append([p,m,"insufficient_prepost",np.nan,np.nan,np.nan,np.nan,len(pre),len(post)])
            continue

        # Weights: all 1 because we have no u uncertainty
        w_pre = np.ones(len(pre)); w_post = np.ones(len(post))

        lvl_pre = weighted_mean(pre.Value.values,w_pre)
        lvl_post= weighted_mean(post.Value.values,w_post)
        deltaL = lvl_post - lvl_pre

        slope_pre = wls_slope(pre.Session.values, pre.Value.values, w_pre)
        slope_post= wls_slope(post.Session.values, post.Value.values, w_post)
        deltaT = slope_post - slope_pre

        # Permutation test (circular shift)
        combined = sub.copy()
        vals = combined.Value.values
        sess = combined.Session.values
        # Build label mask
        mask = combined.gap_flag=="post"
        obs_L = deltaL
        obs_T = deltaT

        # Permute by circular shift
        shiftsL = []
        shiftsT = []
        n = len(vals)
        for _ in range(perms):
            k = np.random.randint(0,n)
            rolled_vals = np.roll(vals, k)
            pre_idx = np.where(~mask)[0]
            post_idx= np.where(mask)[0]
            if len(pre_idx)<3 or len(post_idx)<3: continue
            prev = rolled_vals[pre_idx]; postv= rolled_vals[post_idx]
            shiftsL.append(np.mean(postv)-np.mean(prev))
            # slope
            sp = np.polyfit(sess[pre_idx], prev, 1)[0] if len(pre_idx)>1 else 0
            sq = np.polyfit(sess[post_idx],postv,1)[0] if len(post_idx)>1 else 0
            shiftsT.append(sq-sp)
        pL = (1+np.sum(np.abs(shiftsL)>=abs(obs_L)))/(1+len(shiftsL))
        pT = (1+np.sum(np.abs(shiftsT)>=abs(obs_T)))/(1+len(shiftsT))

        status = "possible_effect" if (abs(deltaL)>sesoi_level or abs(deltaT)>sesoi_slope) else "no_effect"
        results.append([p,m,status,deltaL,deltaT,pL,pT,len(pre),len(post)])

    return pd.DataFrame(results,columns=["Participant","Metric","Status","Delta_Level","Delta_Slope","p_Level","p_Slope","Pre_n","Post_n"])

if __name__=="__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv",required=True)
    ap.add_argument("--perms",type=int,default=10000)
    ap.add_argument("--sesoi_level",type=float,default=0.10)
    ap.add_argument("--sesoi_slope",type=float,default=0.005)
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    # Expect columns: Participant,Metric,Session,Value,gap_flag
    out = run_gap(df,args.perms,args.sesoi_level,args.sesoi_slope)
    out.to_csv("results/gap_effect_summary.csv",index=False)
    with open("results/decision.md","w") as f:
        for _,r in out.iterrows():
            f.write(f"""### {r.Participant} - {r.Metric}
Status: {r.Status}
Δ Level={r.Delta_Level:.3f} (p={r.p_Level:.3f}), Δ Slope={r.Delta_Slope:.3f} (p={r.p_Slope:.3f})
Pre n={int(r.Pre_n)}, Post n={int(r.Post_n)}

""")
