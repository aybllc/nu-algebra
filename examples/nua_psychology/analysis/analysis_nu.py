import pandas as pd
import json
import os

def run_nu_meta(csv_path):
    """
    Conservative N/U algebra bounds for a meta-analysis dataset.
    """
    df = pd.read_csv(csv_path)
    df["u_nu"] = df["SE"].abs() * 1.96
    df["lower"] = df["EffectSize"] - df["u_nu"]
    df["upper"] = df["EffectSize"] + df["u_nu"]

    outpath = os.path.join("results", os.path.basename(csv_path).replace(".csv","_nu.json"))
    os.makedirs("results", exist_ok=True)
    df.to_json(outpath, orient="records", indent=2)

    return {
        "nu_bounds": [float(df["lower"].min()), float(df["upper"].max())],
        "rows": int(len(df))
    }
