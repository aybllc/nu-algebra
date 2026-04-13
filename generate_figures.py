"""
generate_figures.py — PA-MCMC paper figures
============================================
Author: Eric D. Martin, 2026-04-12

Produces four PDF figures for pa_mcmc_paper.tex:
  fig1_rosenbrock_trajectories.pdf  — geometric alignment on Rosenbrock
  fig2_ess_scaling.pdf              — ESS gain vs dimensionality
  fig3_efficiency_per_eval.pdf      — ESS per log-likelihood evaluation
  fig4_multimodal_boundary.pdf      — bimodal posterior histograms

Output: docs/ directory (alongside the paper)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy.linalg import norm

from cu_mcmc import (
    standard_mh, cu_mcmc_burnin_freeze,
    make_rosenbrock, make_elongated_gaussian, make_gaussian_mixture,
    effective_sample_size, ess_multivariate,
)

# ── Style ──────────────────────────────────────────────────────────────────────

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 150,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

COL_STD  = "#4477aa"   # blue  — standard MH
COL_PA   = "#ee6677"   # red   — PA-MCMC
COL_FILL = "#ccddff"   # light blue for contour

OUT_DIR = "docs"
N_STEPS  = 5000
SEED     = 99


# ── Helpers ────────────────────────────────────────────────────────────────────

def count_evals(n_steps):
    """Both samplers evaluate log_p once per step."""
    return n_steps


def save(fig, name, dpi=150):
    path = f"{OUT_DIR}/{name}"
    fig.savefig(path, bbox_inches="tight", dpi=dpi)
    # Also save 300 DPI PNG for journal submission
    png_path = path.replace(".pdf", ".png")
    fig.savefig(png_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"  saved: {path}")
    print(f"  saved: {png_path} (300 dpi)")


# ══════════════════════════════════════════════════════════════════════════════
# Figure 1 — Rosenbrock Trajectories
# ══════════════════════════════════════════════════════════════════════════════

def fig1_rosenbrock():
    print("Figure 1: Rosenbrock trajectories...")
    log_p = make_rosenbrock(dim=2)
    x0 = np.array([0.0, 0.5])

    rng_s = np.random.default_rng(SEED)
    rng_p = np.random.default_rng(SEED)
    chain_s, acc_s = standard_mh(log_p, x0, N_STEPS, proposal_scale=0.05, rng=rng_s)
    chain_p, acc_p = cu_mcmc_burnin_freeze(log_p, x0, N_STEPS,
                                            base_u=0.05, alpha=0.90, rng=rng_p)

    ess_s = ess_multivariate(chain_s)
    ess_p = ess_multivariate(chain_p)

    # Contour grid
    xg = np.linspace(-2.0, 2.5, 300)
    yg = np.linspace(-0.5, 5.5, 300)
    X, Y = np.meshgrid(xg, yg)
    Z = np.exp(np.vectorize(lambda a, b: log_p(np.array([a, b])))(X, Y))

    fig, axes = plt.subplots(1, 2, figsize=(9, 4), sharey=True)

    for ax, chain, acc, ess, label, color, title in [
        (axes[0], chain_s, acc_s, ess_s, "Standard MH", COL_STD, "Standard MH"),
        (axes[1], chain_p, acc_p, ess_p, "PA-MCMC",    COL_PA,  "PA-MCMC"),
    ]:
        ax.contourf(X, Y, Z, levels=12, cmap="Blues", alpha=0.35)
        ax.contour(X, Y, Z, levels=12, colors="steelblue", linewidths=0.4, alpha=0.6)
        # Plot trajectory (thin) then scatter last 1000 points
        ax.plot(chain[:, 0], chain[:, 1], color=color, alpha=0.15, lw=0.5, zorder=1)
        ax.scatter(chain[::5, 0], chain[::5, 1],
                   c=color, s=1.5, alpha=0.4, zorder=2)
        ax.set_title(f"{title}\nESS={ess:.0f}  accept={acc:.2f}", pad=6)
        ax.set_xlabel("$x_1$")
        ax.set_xlim(-2.0, 2.5)
        ax.set_ylim(-0.5, 5.5)

    axes[0].set_ylabel("$x_2$")
    fig.suptitle("Figure 1 — Geometric Alignment on Rosenbrock Density ($b=100$)",
                 y=1.02, fontsize=11)
    fig.tight_layout()
    save(fig, "fig1_rosenbrock_trajectories.pdf")


# ══════════════════════════════════════════════════════════════════════════════
# Figure 2 — ESS gain vs dimensionality
# ══════════════════════════════════════════════════════════════════════════════

def fig2_ess_scaling():
    print("Figure 2: ESS scaling...")
    dims = [2, 3, 5, 7, 10, 15, 20]
    ess_std_list, ess_pa_list, ratio_list = [], [], []

    for d in dims:
        log_p, _, _, _ = make_elongated_gaussian(dim=d, condition_number=100)
        x0 = np.zeros(d)
        ps = 0.08 / np.sqrt(d)

        rng_s = np.random.default_rng(SEED)
        rng_p = np.random.default_rng(SEED)
        chain_s, _ = standard_mh(log_p, x0, N_STEPS, proposal_scale=ps, rng=rng_s)
        chain_p, _ = cu_mcmc_burnin_freeze(log_p, x0, N_STEPS,
                                            base_u=ps, alpha=0.88, rng=rng_p)

        es = ess_multivariate(chain_s)
        ep = ess_multivariate(chain_p)
        ess_std_list.append(es)
        ess_pa_list.append(ep)
        ratio_list.append(ep / max(es, 1.0))
        print(f"  d={d:2d}  ESS_std={es:6.1f}  ESS_PA={ep:6.1f}  ratio={ep/max(es,1):.1f}x")

    dims = np.array(dims)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))

    # Left: absolute ESS
    ax1.plot(dims, ess_std_list, "o-", color=COL_STD, label="Standard MH", lw=1.8, ms=5)
    ax1.plot(dims, ess_pa_list,  "s-", color=COL_PA,  label="PA-MCMC",     lw=1.8, ms=5)
    ax1.set_xlabel("Dimension $d$")
    ax1.set_ylabel("Mean ESS")
    ax1.set_title("Effective Sample Size vs Dimension")
    ax1.legend()

    # Right: gain ratio
    ax2.plot(dims, ratio_list, "D-", color="#aa3377", lw=2, ms=5)
    ax2.axhline(1.0, ls="--", color="gray", lw=0.8, alpha=0.6)
    ax2.set_xlabel("Dimension $d$")
    ax2.set_ylabel("ESS gain (PA / std MH)")
    ax2.set_title("ESS Gain vs Dimension\n(anisotropic Gaussian, $\\kappa=100$)")
    ax2.fill_between(dims, 1.0, ratio_list, alpha=0.15, color="#aa3377")

    # Annotate peak
    peak_i = int(np.argmax(ratio_list))
    ax2.annotate(f"{ratio_list[peak_i]:.0f}×",
                 xy=(dims[peak_i], ratio_list[peak_i]),
                 xytext=(dims[peak_i]+0.5, ratio_list[peak_i]*1.05),
                 fontsize=9, color="#aa3377")

    fig.suptitle("Figure 2 — ESS Scaling with Dimensionality", y=1.02, fontsize=11)
    fig.tight_layout()
    save(fig, "fig2_ess_scaling.pdf")


# ══════════════════════════════════════════════════════════════════════════════
# Figure 3 — ESS per log-likelihood evaluation
# ══════════════════════════════════════════════════════════════════════════════

def fig3_efficiency_per_eval():
    print("Figure 3: ESS per evaluation...")
    targets = [
        ("Elongated Gaussian 2D",  lambda: make_elongated_gaussian(dim=2, condition_number=100)[:1][0],
         np.zeros(2),  0.08, 0.08, 0.88),
        ("Rosenbrock 2D",          lambda: make_rosenbrock(dim=2),
         np.array([0., 0.5]), 0.05, 0.05, 0.90),
        ("Elongated Gaussian 5D",  lambda: make_elongated_gaussian(dim=5, condition_number=100)[:1][0],
         np.zeros(5),  0.08/np.sqrt(5), 0.08/np.sqrt(5), 0.88),
        ("Elongated Gaussian 10D", lambda: make_elongated_gaussian(dim=10, condition_number=100)[:1][0],
         np.zeros(10), 0.08/np.sqrt(10), 0.08/np.sqrt(10), 0.88),
    ]

    labels, eff_std, eff_pa = [], [], []

    for name, lp_fn, x0, ps, bu, alpha in targets:
        log_p = lp_fn()
        rng_s = np.random.default_rng(SEED)
        rng_p = np.random.default_rng(SEED)
        chain_s, _ = standard_mh(log_p, x0, N_STEPS, proposal_scale=ps, rng=rng_s)
        chain_p, _ = cu_mcmc_burnin_freeze(log_p, x0, N_STEPS,
                                            base_u=bu, alpha=alpha, rng=rng_p)

        n_eval = count_evals(N_STEPS)
        es = ess_multivariate(chain_s) / n_eval
        ep = ess_multivariate(chain_p) / n_eval
        labels.append(name)
        eff_std.append(es)
        eff_pa.append(ep)
        print(f"  {name}: std={es*1000:.2f}‰  PA={ep*1000:.2f}‰  ratio={ep/max(es,1e-9):.1f}x")

    x = np.arange(len(labels))
    w = 0.35

    fig, ax = plt.subplots(figsize=(8, 4))
    bars_s = ax.bar(x - w/2, [e*1000 for e in eff_std], w,
                    label="Standard MH", color=COL_STD, alpha=0.85)
    bars_p = ax.bar(x + w/2, [e*1000 for e in eff_pa],  w,
                    label="PA-MCMC",    color=COL_PA,  alpha=0.85)

    # Ratio annotations
    for i, (es, ep) in enumerate(zip(eff_std, eff_pa)):
        r = ep / max(es, 1e-9)
        ypos = max(es, ep) * 1000 + 0.002
        ax.text(i, ypos, f"{r:.0f}×", ha="center", va="bottom", fontsize=8, color="#333")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=15, ha="right", fontsize=8)
    ax.set_ylabel("ESS per 1000 log-likelihood evaluations")
    ax.set_title("Figure 3 — Efficiency: ESS per Evaluation")
    ax.legend()
    fig.tight_layout()
    save(fig, "fig3_efficiency_per_eval.pdf")


# ══════════════════════════════════════════════════════════════════════════════
# Figure 4 — Multimodal boundary
# ══════════════════════════════════════════════════════════════════════════════

def fig4_multimodal():
    print("Figure 4: Multimodal boundary...")
    log_p, true_means = make_gaussian_mixture(dim=2, n_components=2, sep=4.0)
    x0 = np.array([-2.0, 0.0])

    rng_s = np.random.default_rng(SEED)
    rng_p = np.random.default_rng(SEED)
    chain_s, acc_s = standard_mh(log_p, x0, N_STEPS*2, proposal_scale=1.2, rng=rng_s)
    chain_p, acc_p = cu_mcmc_burnin_freeze(log_p, x0, N_STEPS*2,
                                            base_u=1.2, alpha=0.97, rng=rng_p)

    ess_s = ess_multivariate(chain_s)
    ess_p = ess_multivariate(chain_p)
    burn = N_STEPS // 5

    fig, axes = plt.subplots(2, 2, figsize=(9, 7))

    # Top row: 2D scatter
    xg = np.linspace(-7, 7, 200)
    yg = np.linspace(-4, 4, 200)
    X, Y = np.meshgrid(xg, yg)
    Z = np.exp(np.vectorize(lambda a, b: log_p(np.array([a, b])))(X, Y))

    for col, (chain, acc, ess, color, title) in enumerate([
        (chain_s, acc_s, ess_s, COL_STD, "Standard MH"),
        (chain_p, acc_p, ess_p, COL_PA,  "PA-MCMC"),
    ]):
        ax = axes[0, col]
        ax.contourf(X, Y, Z, levels=10, cmap="Greys", alpha=0.3)
        ax.scatter(chain[burn::3, 0], chain[burn::3, 1],
                   c=color, s=1.5, alpha=0.3)
        for m in true_means:
            ax.axvline(m[0], ls=":", color="gray", lw=0.8, alpha=0.7)
        ax.set_title(f"{title}\nESS={ess:.0f}  accept={acc:.2f}")
        ax.set_xlabel("$x_1$")
        ax.set_ylabel("$x_2$")
        ax.set_xlim(-7, 7)
        ax.set_ylim(-4, 4)

    # Bottom row: marginal histograms for x1
    bins = np.linspace(-7, 7, 40)
    for col, (chain, color, label) in enumerate([
        (chain_s, COL_STD, "Standard MH"),
        (chain_p, COL_PA,  "PA-MCMC"),
    ]):
        ax = axes[1, col]
        ax.hist(chain[burn:, 0], bins=bins, density=True,
                color=color, alpha=0.7, edgecolor="white", lw=0.3)
        # True marginal (equal-weight mixture of two Gaussians)
        xs = np.linspace(-7, 7, 300)
        true_marginal = sum(
            np.exp(-0.5*(xs - m[0])**2) / np.sqrt(2*np.pi)
            for m in true_means
        ) / len(true_means)
        ax.plot(xs, true_marginal, "k--", lw=1.2, label="True marginal")
        ax.set_xlabel("$x_1$")
        ax.set_ylabel("Density")
        ax.set_title(f"{label} — $x_1$ marginal")
        ax.legend(fontsize=8)

    fig.suptitle("Figure 4 — Multimodal Boundary: Bimodal Mixture",
                 y=1.01, fontsize=11)
    fig.tight_layout()
    save(fig, "fig4_multimodal_boundary.pdf")


# ── Run all ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import os
    os.makedirs(OUT_DIR, exist_ok=True)

    print("=" * 60)
    print("PA-MCMC Figure Generator")
    print("=" * 60)
    print()

    fig1_rosenbrock()
    fig2_ess_scaling()
    fig3_efficiency_per_eval()
    fig4_multimodal()

    print()
    print("All figures written to docs/")
    print("Wire into pa_mcmc_paper.tex with \\includegraphics{fig1_...}")
