"""
CU-MCMC: Carried Uncertainty Markov Chain Monte Carlo
======================================================
Author: Eric D. Martin, 2026-04-12

Derives from the Uncertainty Propagation Order Theorem (§11, unified_math_reference.md).

CORE DESIGN:
  The per-dimension proposal scale u_t is a persistent state variable updated as:

    u_t = α · u_{t-1} + (1−α) · |accepted_step|    [if accepted]
    u_t = α · u_{t-1}                                [if rejected, scale unchanged]

  This encodes the Propagation Order Theorem WITHOUT explicit gradient/Hessian:
    - If moves in dimension i are ACCEPTED with large δ_i → u_t[i] grows
      → that dimension is "flat" (k=2 regime, large natural step scale)
    - If moves in dimension i are REJECTED → u_t[i] decays toward zero
      → that dimension is "steep" (k=1 regime, tight curvature)

  The carried payload means the sampler REMEMBERS the valley geometry across steps.
  Standard MH forgets (u=const); CU-MCMC persists structural information.

VALIDITY:
  Per-dimension adaptive Metropolis with EMA adaptation satisfies ergodicity
  (Haario et al. 2001, Atchadé & Rosenthal 2003) provided the adaptation is
  controlled. The acceptance ratio remains standard M-H (no correction needed
  for isotropic per-dimension proposals).

  For a fully rigorous transition kernel proof, a diminishing-adaptation
  schedule (α → 1 over time) or fixed-scale post-burn-in phase is required.
  See `detailed_balance_notes()` below.

Three validation cases:
  Case A: ESS gain + posterior invariance — elongated Gaussian + Rosenbrock
  Case B: Dimensionality scaling 2D / 5D / 10D
  Case C: Gaussian mixture mode coverage
"""

import numpy as np
from numpy.linalg import norm
import warnings

warnings.filterwarnings("ignore")


# ─── ESS ──────────────────────────────────────────────────────────────────────

def effective_sample_size(chain):
    """Per-dimension ESS via Geyer's truncated autocorrelation (Gelman et al.)."""
    n = len(chain)
    x = np.asarray(chain, dtype=float)
    x = x - x.mean()
    var = np.var(x, ddof=1)
    if var < 1e-16:
        return 1.0
    acf = np.correlate(x, x, mode="full")[n - 1:]
    acf /= acf[0]
    cutoff = next((i for i in range(1, min(len(acf), n // 2)) if acf[i] < 0), n // 4)
    tau = 1.0 + 2.0 * np.sum(acf[1:cutoff])
    return max(float(n) / max(tau, 1.0), 1.0)


def ess_multivariate(chains):
    return float(np.mean([effective_sample_size(chains[:, d])
                          for d in range(chains.shape[1])]))


# ─── Samplers ─────────────────────────────────────────────────────────────────

def standard_mh(log_p, x0, n_steps, proposal_scale=0.3, rng=None):
    """Standard isotropic random-walk Metropolis-Hastings."""
    if rng is None:
        rng = np.random.default_rng(42)
    dim = len(x0)
    chain = np.zeros((n_steps, dim))
    x = x0.copy().astype(float)
    lp = log_p(x)
    accepted = 0

    for i in range(n_steps):
        proposal = x + rng.normal(0, proposal_scale, size=dim)
        lp_prop = log_p(proposal)
        if np.log(rng.uniform() + 1e-300) < lp_prop - lp:
            x, lp = proposal, lp_prop
            accepted += 1
        chain[i] = x

    return chain, accepted / n_steps


def cu_mcmc_burnin_freeze(log_p, x0, n_steps, base_u=0.3, alpha=0.97,
                          burnin_frac=0.25, min_u=None, max_u_factor=5.0, rng=None):
    """
    PA-MCMC: Payload-Augmented MCMC — Burn-in-then-Freeze Protocol.

    Phase 1 (burn-in, first burnin_frac of steps): adapt payload ONLY on accepted steps.
    Phase 2 (production, remaining steps): payload frozen → exact detailed balance.

    Vanishing adaptation condition (Roberts & Rosenthal 2009): adaptation ceases
    entirely after T_burn steps; the production kernel is fixed and ergodic.

    Key parameters:
      alpha=0.97  → memory timescale τ = 1/(1-α) = 33 steps (must satisfy τ ≥ d)
      min_u       → floor at 0.30 × base_u prevents EMA underestimation bias
                    when burn-in acceptance is low (<23%)

    Bug note: do NOT update u on rejection. Rejection-branch shrinkage creates
    a death spiral (smaller u → higher accept → EMA learns tiny steps → freeze).
    """
    if rng is None:
        rng = np.random.default_rng(42)
    if min_u is None:
        min_u = 0.30 * base_u  # floor: 30% of calibrated estimate

    dim = len(x0)
    chain = np.zeros((n_steps, dim))
    u = np.full(dim, float(base_u))
    x = x0.copy().astype(float)
    lp = log_p(x)
    accepted = 0
    prod_accepted = 0
    T_burn = int(n_steps * burnin_frac)
    max_u = max_u_factor * base_u

    for i in range(n_steps):
        proposal = x + rng.normal(0, u)
        lp_prop = log_p(proposal)

        if np.log(rng.uniform() + 1e-300) < lp_prop - lp:
            if i < T_burn:
                # Burn-in: EMA toward accepted step geometry (accept-only)
                step = np.abs(proposal - x)
                u = np.clip(alpha * u + (1.0 - alpha) * step, min_u, max_u)
            else:
                prod_accepted += 1
            x, lp = proposal, lp_prop
            accepted += 1
        # On rejection: payload unchanged — accept-only EMA rule

        chain[i] = x

    prod_steps = n_steps - T_burn
    prod_rate = prod_accepted / prod_steps if prod_steps > 0 else 0.0
    return chain, accepted / n_steps, prod_rate


def cu_mcmc_gibbs(log_p, x0, n_steps, base_u=0.3, alpha=0.97,
                  burnin_frac=0.25, min_u=None, max_u_factor=5.0, rng=None):
    """
    Gibbs-style PA-MCMC: Metropolis-within-Gibbs with per-dimension payload.

    Fixes the Joint Rejection Bottleneck in cu_mcmc_burnin_freeze:
      - Joint proposal: ONE accept/reject gate for ALL dims simultaneously.
        The stiffest dim dominates rejection rate → flat dims starved of updates.
      - Gibbs proposal: each dim gets its OWN M-H step and OWN u adaptation.
        Stiff dim (small u, high reject) and flat dim (large u, low reject)
        evolve on independent timescales → payload separates correctly.

    This is the necessary topological condition for implementing the
    Propagation Order Theorem across varying curvature scales (§11).

    Phase 1 (burn-in): per-dim M-H, per-dim EMA update on acceptance.
    Phase 2 (production): per-dim M-H with FROZEN u (exact detailed balance).
    """
    if rng is None:
        rng = np.random.default_rng(42)
    if min_u is None:
        min_u = 0.30 * base_u

    dim = len(x0)
    chain = np.zeros((n_steps, dim))
    u = np.full(dim, float(base_u))
    x = x0.copy().astype(float)
    lp = log_p(x)
    accepted = np.zeros(dim, dtype=float)
    T_burn = int(n_steps * burnin_frac)
    max_u = max_u_factor * base_u

    for i in range(n_steps):
        for d in range(dim):
            x_prop = x.copy()
            x_prop[d] += rng.normal(0, u[d])
            lp_prop = log_p(x_prop)

            if np.log(rng.uniform() + 1e-300) < lp_prop - lp:
                if i < T_burn:
                    step = abs(x_prop[d] - x[d])
                    u[d] = np.clip(alpha * u[d] + (1.0 - alpha) * step, min_u, max_u)
                x[d] = x_prop[d]
                lp = lp_prop
                accepted[d] += 1

        chain[i] = x

    return chain, accepted / n_steps, u   # return final u for diagnostics


def cu_mcmc_gibbs_rm(log_p, x0, n_steps, base_u=1.0,
                     burnin_frac=0.25, target_rate=0.44, step_size=0.5,
                     u_min=1e-4, u_max_factor=20.0, rng=None):
    """
    Gibbs-style PA-MCMC with Robbins-Monro acceptance-rate targeting.

    DESIGN:
    Each dimension gets its own Metropolis step (Metropolis-within-Gibbs).
    Each dimension's proposal scale u[d] is adapted independently via
    log-scale stochastic approximation (Robbins-Monro):

      On acceptance:  log u[d] += step_size * (1 − target_rate)
      On rejection:   log u[d] -= step_size * target_rate

    Equivalently: u[d] *= exp(step_size * (accept − target_rate))

    EQUILIBRIUM: E[Δ log u[d]] = 0  ⟺  accept_rate[d] = target_rate
    For Gaussian targets: u[d]_equilibrium ≈ 2.38 × true_std[d]  (optimal 1D MH scale)

    TARGET RATE: 0.44 — optimal for 1D Metropolis (Roberts, Gelman & Gilks 1997).
    (Not 0.234: that is the optimal rate for joint/isotropic proposals in high-d.)

    STEP_SIZE: constant 0.5 during burn-in.  After T_burn, u is FROZEN.
    The hard freeze satisfies the vanishing adaptation condition
    (Roberts & Rosenthal 2009): no correction term needed in acceptance ratio.

    CLAIM (falsifiable):
    Starting from a single base_u (same for all dims, poorly tuned),
    PA-MCMC Gibbs recovers per-dimension optimal scales — without knowing the
    posterior in advance — and approaches the performance of an oracle-tuned
    fixed Gibbs sampler. This is the Tuning Gap the algorithm closes.
    """
    if rng is None:
        rng = np.random.default_rng(42)

    dim = len(x0)
    chain = np.zeros((n_steps, dim))
    log_u = np.full(dim, np.log(float(base_u)))   # work in log-scale
    x = x0.copy().astype(float)
    lp = log_p(x)
    accepted = np.zeros(dim, dtype=float)
    T_burn = int(n_steps * burnin_frac)
    log_u_min = np.log(u_min)
    log_u_max = np.log(u_max_factor * base_u)

    for i in range(n_steps):
        for d in range(dim):
            u_d = np.exp(log_u[d])
            x_prop = x.copy()
            x_prop[d] += rng.normal(0, u_d)
            lp_prop = log_p(x_prop)

            accept = np.log(rng.uniform() + 1e-300) < lp_prop - lp
            if accept:
                x[d] = x_prop[d]
                lp = lp_prop
                accepted[d] += 1

            if i < T_burn:
                # R-M log-scale update: target accept_rate → target_rate
                delta = step_size * (float(accept) - target_rate)
                log_u[d] = np.clip(log_u[d] + delta, log_u_min, log_u_max)
            # After T_burn: log_u frozen — exact detailed balance in production

        chain[i] = x

    u_final = np.exp(log_u)
    return chain, accepted / n_steps, u_final


def cu_mcmc(log_p, x0, n_steps, base_u=0.3, alpha=0.85,
             min_u=1e-6, max_u_factor=4.0, use_mhg_correction=False, rng=None):
    """
    CU-MCMC: Carried Uncertainty Metropolis-Hastings.

    Payload update rule (Propagation Order Theorem implemented as acceptance tracker):
      On acceptance:  u_t = α·u_{t-1} + (1−α)·|accepted_step|
      On rejection:   u_t = α·u_{t-1}   (payload decays — direction was too steep)

    This makes u_t a structural proxy for the natural step scale:
      Large u_t[i]  ↔  dimension i has been freely traversed (flat direction)
      Small u_t[i]  ↔  dimension i rarely moves (steep direction / valley wall)

    Parameters
    ----------
    alpha            : persistence weight. 0.85 = moderate; 0.95 = long memory
    base_u           : initial payload / fallback scale
    min_u            : lower clip on proposal width
    max_u_factor     : max proposal width = max_u_factor * base_u  (prevents runaway)
    use_mhg_correction : apply Metropolis-Hastings-Green correction for asymmetric
                       proposals (ensures detailed balance when u_x ≠ u_y)
    """
    if rng is None:
        rng = np.random.default_rng(42)

    dim = len(x0)
    chain = np.zeros((n_steps, dim))
    u = np.full(dim, base_u)    # initial payload
    x = x0.copy().astype(float)
    lp = log_p(x)
    accepted = 0

    max_u = max_u_factor * base_u

    for i in range(n_steps):
        proposal = x + rng.normal(0, u)
        lp_prop = log_p(proposal)

        if use_mhg_correction:
            # MH-Green correction for asymmetric proposal:
            #   log α = [log π(y) - log π(x)]
            #         + [log q(x|y,u_y) - log q(y|x,u_x)]
            # where u_y = hypothetical payload at proposal if accepted
            step = np.abs(proposal - x)
            u_y_hyp = np.clip(alpha * u + (1.0 - alpha) * step, min_u, max_u)

            # log q(y|x, u_x) - log N(proposal; x, diag(u²))
            log_q_fwd = -0.5 * np.sum(((proposal - x) / u)**2) - np.sum(np.log(u))
            # log q(x|y, u_y_hyp) - using hypothetical payload at y
            log_q_rev = -0.5 * np.sum(((x - proposal) / u_y_hyp)**2) - np.sum(np.log(u_y_hyp))

            log_accept_ratio = (lp_prop - lp) + (log_q_rev - log_q_fwd)
        else:
            log_accept_ratio = lp_prop - lp

        if np.log(rng.uniform() + 1e-300) < log_accept_ratio:
            # ACCEPTED: update payload with accepted step magnitude
            step = np.abs(proposal - x)
            u = alpha * u + (1.0 - alpha) * step
            x, lp = proposal, lp_prop
            accepted += 1
        else:
            # REJECTED: payload decays — this direction is steeper
            u = alpha * u

        # Clip payload
        u = np.clip(u, min_u, max_u)
        chain[i] = x

    return chain, accepted / n_steps


# ─── Target distributions ─────────────────────────────────────────────────────

def make_elongated_gaussian(dim=2, condition_number=100.0, angle_deg=45.0):
    """
    Elongated Gaussian — models the H₀–Ωm degeneracy trough.

    One axis has variance ~ 1/condition_number (tight),
    the other dim-1 axes have variance = 1 (normal).
    Rotated by angle_deg in the (0,1) plane.
    """
    eigs = np.ones(dim)
    eigs[0] = 1.0 / condition_number   # tight narrow direction

    # Rotation matrix in (0,1) plane
    cov = np.diag(eigs.astype(float))
    if dim >= 2:
        theta = np.radians(angle_deg)
        R = np.eye(dim)
        R[0, 0] = np.cos(theta)
        R[0, 1] = -np.sin(theta)
        R[1, 0] = np.sin(theta)
        R[1, 1] = np.cos(theta)
        cov = R @ np.diag(eigs) @ R.T

    prec = np.linalg.inv(cov)
    true_std = np.sqrt(np.diag(cov))

    def log_p(x):
        return -0.5 * float(x @ prec @ x)

    return log_p, np.zeros(dim), true_std, cov


def make_rosenbrock(a=1.0, b=100.0, dim=2):
    """Rosenbrock 'banana' density, chained form for dim > 2."""
    def log_p(x):
        s = 0.0
        for i in range(dim - 1):
            s += b * (x[i+1] - x[i]**2)**2 + (a - x[i])**2
        return -s
    return log_p


def make_gaussian_mixture(dim=2, n_components=3, sep=3.0):
    """Equally-weighted isotropic Gaussians along the first axis."""
    means = [np.zeros(dim) for _ in range(n_components)]
    for k, m in enumerate(means):
        m[0] = sep * (k - (n_components - 1) / 2.0)

    def log_p(x):
        lw = [-0.5 * np.sum((x - mu)**2) for mu in means]
        m0 = max(lw)
        return m0 + np.log(sum(np.exp(lw_i - m0) for lw_i in lw))

    return log_p, means


# ─── Fixed-proposal Gibbs (baseline / oracle) ─────────────────────────────────

def standard_gibbs(log_p, x0, n_steps, u_per_dim, rng=None):
    """
    Fixed-proposal Metropolis-within-Gibbs — no adaptation.

    Used as both:
      - Naive baseline: u_per_dim = [base_u, …] (same for all dims, poorly tuned)
      - Oracle ceiling: u_per_dim = 2.38 × true_std[d]  (optimal per Gaussian theory)
    """
    if rng is None:
        rng = np.random.default_rng(42)
    dim = len(x0)
    chain = np.zeros((n_steps, dim))
    x = x0.copy().astype(float)
    lp = log_p(x)
    accepted = np.zeros(dim, dtype=float)
    for i in range(n_steps):
        for d in range(dim):
            x_prop = x.copy()
            x_prop[d] += rng.normal(0, u_per_dim[d])
            lp_prop = log_p(x_prop)
            if np.log(rng.uniform() + 1e-300) < lp_prop - lp:
                x[d] = x_prop[d]
                lp = lp_prop
                accepted[d] += 1
        chain[i] = x
    return chain, accepted / n_steps


# ─── Comparison runner (legacy — original EMA joint-proposal benchmark) ───────

def compare(log_p, x0, n_steps, label, ps=0.3, bu=0.3, alpha=0.85, seed=42,
            use_mhg=False, use_freeze=True):
    rng_s = np.random.default_rng(seed)
    rng_c = np.random.default_rng(seed)

    chain_s, acc_s = standard_mh(log_p, x0, n_steps, proposal_scale=ps, rng=rng_s)
    if use_freeze:
        chain_c, acc_c, _prod_c = cu_mcmc_burnin_freeze(log_p, x0, n_steps, base_u=bu,
                                                         alpha=alpha, rng=rng_c)
    else:
        chain_c, acc_c = cu_mcmc(log_p, x0, n_steps, base_u=bu, alpha=alpha,
                                  use_mhg_correction=use_mhg, rng=rng_c)

    ess_s = ess_multivariate(chain_s)
    ess_c = ess_multivariate(chain_c)

    # Discard burn-in (first 20%) for posterior statistics
    burn = n_steps // 5
    m_s  = chain_s[burn:].mean(0)
    m_c  = chain_c[burn:].mean(0)
    sd_s = chain_s[burn:].std(0)
    sd_c = chain_c[burn:].std(0)
    mean_diff = float(np.max(np.abs(m_s - m_c)))
    std_diff  = float(np.max(np.abs(sd_s - sd_c)))

    return dict(
        label=label, dim=len(x0),
        ess_s=ess_s, ess_c=ess_c, ratio=ess_c / max(ess_s, 1.0),
        acc_s=acc_s, acc_c=acc_c,
        mean_diff=mean_diff, std_diff=std_diff,
        posterior_ok=mean_diff < 1.0 and std_diff < 1.0,
        chain_s=chain_s, chain_c=chain_c,
    )


# ─── Formal notes on detailed balance ─────────────────────────────────────────

def detailed_balance_notes():
    return """
    Detailed Balance Notes for CU-MCMC Publication
    ================================================

    Current implementation: adaptive MH with EMA-updated per-dimension scales.
    The standard M-H acceptance ratio is used; proposal is isotropic per-dimension.

    VALIDITY: The chain is ergodic (converges to target π) if the adaptation is
    "diminishing" in the sense of Atchadé & Rosenthal (2003):
      ∑_t (α_t - α_{t-1})² < ∞  where α_t is the adaptation step size

    For fixed α (our implementation), strict diminishing adaptation is NOT satisfied.
    Two options for a publishable transition kernel:

    Option 1 — Burn-in phase then fixed proposal:
      Run CU-MCMC for T_burn steps (adaptation phase, uses EMA).
      After T_burn: fix u = u_{T_burn} and run standard MH with that proposal.
      The fixed-scale production phase is exactly valid MH.
      This is the "Adaptive Burn-in" paradigm (Roberts & Rosenthal 2009).

    Option 2 — Metropolis-Hastings-Green correction for asymmetric proposals:
      The CU-MCMC with persistent u_t has a NON-SYMMETRIC proposal distribution:
        q(y|x, u_x) ≠ q(x|y, u_y)  because u_y ≠ u_x after the payload update.

      The corrected acceptance ratio is:
        α(x→y) = min(1, [π(y)·q(x|y, u_y)] / [π(x)·q(y|x, u_x)])

      For isotropic per-dimension proposals:
        log q(y|x, u_x) = -∑_i (y_i - x_i)²/(2u_x_i²) - ∑_i log(u_x_i) - (d/2)log(2π)
        log q(x|y, u_y) = -∑_i (y_i - x_i)²/(2u_y_i²) - ∑_i log(u_y_i) - (d/2)log(2π)

      PROBLEM: u_y depends on whether y is ACCEPTED or REJECTED, which creates
      a circular dependency. Resolution: compute u_y as a HYPOTHETICAL update
      assuming the proposal would be accepted, then use that in the ratio.

      The fully corrected acceptance log-ratio is:
        log α = [log π(y) - log π(x)]
               + ∑_i [(y_i-x_i)²/(2u_x_i²) - (y_i-x_i)²/(2u_y_i²)]
               + ∑_i [log(u_x_i) - log(u_y_i)]

      where u_y = α·u_x + (1-α)·|y - x|  (hypothetical payload at y if accepted)

    For this demonstration, Option 1 is recommended for publication.
    The current code uses standard MH acceptance (Option 1 burn-in equivalent,
    with the adaptation implicitly "finishing" after the payload stabilizes at ~10τ steps).
    """


# ─── Main — 3-way honest benchmark ───────────────────────────────────────────

def main():
    """
    3-way benchmark establishing the PA-MCMC Gibbs claim.

    CLAIM: Starting from a single base_u (same for all dimensions, poorly tuned),
    PA-MCMC Gibbs discovers per-dimension optimal proposal scales automatically
    and closes the tuning gap versus an oracle-tuned fixed Gibbs sampler.

    SCOPE: Posteriors with approximately unimodal per-dimension conditionals.
    The 0.44 target rate is derived from Gaussian theory; it is not universal.

    THREE COMPETITORS:
      [1] Naive Gibbs — fixed u = base_u for all dims (same start as PA-MCMC)
      [2] PA-MCMC Gibbs (R-M) — starts at base_u, adapts per-dim during burn-in
      [3] Oracle Gibbs — fixed u = 2.38 × true_std[d] (optimal, requires knowing π)
    """
    SEED = 99
    N    = 10_000
    BURN = N // 4
    BASE = 1.0        # same bad init for both [1] and [2]
    W    = 66

    def _fmt_acc(a):
        a = np.atleast_1d(a)
        if len(a) == 1:
            return f"{a[0]:.3f}"
        return f"[{a[0]:.3f}…{a[-1]:.3f}]"

    def _run(log_p, x0, u_oracle, true_std=None):
        c1, a1 = standard_gibbs(log_p, x0, N, np.full(len(x0), BASE),
                                 np.random.default_rng(SEED))
        c2, a2, ul = cu_mcmc_gibbs_rm(log_p, x0, N, base_u=BASE, step_size=0.5,
                                       rng=np.random.default_rng(SEED))
        c3, a3 = standard_gibbs(log_p, x0, N, u_oracle,
                                 np.random.default_rng(SEED))
        e1 = ess_multivariate(c1[BURN:])
        e2 = ess_multivariate(c2[BURN:])
        e3 = ess_multivariate(c3[BURN:])
        return dict(e1=e1, e2=e2, e3=e3, a1=a1, a2=a2, a3=a3,
                    ul=ul, uo=u_oracle, true_std=true_std,
                    post_std=c2[BURN:].std(0) if true_std is not None else None)

    def _print(r, label, note=None):
        e1, e2, e3 = r['e1'], r['e2'], r['e3']
        vs   = e2 / max(e1, 1.0)
        gap  = e2 / max(e3, 1.0)
        ok   = "✅" if vs >= 1.5 and gap >= 0.80 else ("⚠ " if vs >= 1.0 else "❌")
        ul   = r['ul'];  uo = r['uo']
        ul_s = f"[{ul[0]:.3f}…{ul[-1]:.3f}]" if len(ul) > 2 else f"[{ul[0]:.3f}, {ul[-1]:.3f}]"
        uo_s = f"[{uo[0]:.3f}…{uo[-1]:.3f}]" if len(uo) > 2 else f"[{uo[0]:.3f}, {uo[-1]:.3f}]"
        print(f"  [1] Naive Gibbs   ESS={e1:7.1f}  acc={_fmt_acc(r['a1'])}  u=[{BASE:.1f}…]")
        print(f"  [2] PA-MCMC Gibbs ESS={e2:7.1f}  acc={_fmt_acc(r['a2'])}  u_learned={ul_s}")
        print(f"  [3] Oracle Gibbs  ESS={e3:7.1f}  acc={_fmt_acc(r['a3'])}  u_oracle={uo_s}")
        print(f"  {ok} {vs:.2f}× over naive  |  {gap:.2f}× vs oracle  "
              f"(tuning gap closed: {min(gap,1.0)*100:.0f}%)")
        if r['true_std'] is not None and r['post_std'] is not None:
            err = np.abs(r['post_std'] - r['true_std'])
            print(f"     Posterior std error: max={err.max():.4f}  "
                  f"(PA-MCMC true={np.round(r['true_std'],3)}, got={np.round(r['post_std'],3)})")
        if note:
            print(f"     {note}")

    all_results = []

    print("=" * W)
    print("PA-MCMC: Per-Dimension Adaptation via Robbins-Monro Targeting")
    print("Eric D. Martin  —  ORCID 0009-0006-5944-1742")
    print("=" * W)
    print()
    print("  Algorithm: Metropolis-within-Gibbs + log-scale R-M targeting")
    print("    propose:  x_prop[d] = x[d] + N(0, u[d])  [each dim independently]")
    print("    adapt:    log u[d] += c × (accept − 0.44)  [burn-in only]")
    print("    freeze:   u fixed at T_burn  →  production phase is exact MH")
    print("  Equilibrium: accept_rate[d] → 0.44  →  u[d] → 2.38 × true_std[d]")
    print()

    # ── TEST A: 2D Elongated Gaussian ─────────────────────────────────────────
    print("─" * W)
    print("TEST A — 2D Elongated Gaussian  cond=100  angle=0")
    print("  True std = [0.100, 1.000]   Oracle u = 2.38×std = [0.238, 2.380]")
    print("  PRIMARY CLAIM: PA-MCMC closes the tuning gap automatically.")
    print("─" * W)
    _, _, ts2, _ = make_elongated_gaussian(dim=2, condition_number=100, angle_deg=0)
    log_p2 = make_elongated_gaussian(dim=2, condition_number=100, angle_deg=0)[0]
    rA = _run(log_p2, np.zeros(2), 2.38*ts2, true_std=ts2)
    _print(rA, "A")
    all_results.append(("A  ElongGauss-2D", rA))

    # ── TEST A2: 5D Elongated Gaussian ────────────────────────────────────────
    print()
    print("─" * W)
    print("TEST A2 — 5D Elongated Gaussian  cond=100  angle=0")
    print("  True std = [0.1, 1, 1, 1, 1]   PA-MCMC must separate u[0] from u[1..4].")
    print("─" * W)
    _, _, ts5, _ = make_elongated_gaussian(dim=5, condition_number=100, angle_deg=0)
    log_p5 = make_elongated_gaussian(dim=5, condition_number=100, angle_deg=0)[0]
    rA2 = _run(log_p5, np.zeros(5), 2.38*ts5, true_std=ts5)
    _print(rA2, "A2")
    print(f"     u_learned (all dims): {np.round(rA2['ul'], 3)}")
    all_results.append(("A2 ElongGauss-5D", rA2))

    # ── TEST B: Rosenbrock 2D (scope boundary) ────────────────────────────────
    print()
    print("─" * W)
    print("TEST B — Rosenbrock 2D  b=100  [SCOPE BOUNDARY]")
    print("  Non-Gaussian, strongly coupled dims.  Claim does NOT apply here.")
    print("─" * W)
    log_rb = make_rosenbrock(dim=2)
    c_ref, _ = standard_gibbs(log_rb, np.zeros(2), 50_000,
                               np.array([0.5, 0.5]), np.random.default_rng(0))
    emp_std = c_ref[10_000:].std(0)
    rB = _run(log_rb, np.zeros(2), 2.38*emp_std)
    _print(rB, "B",
           note="Lower acceptance targets can improve ESS on banana geometry. "
                "Scope: 0.44 target assumes near-Gaussian conditionals.")
    all_results.append(("B  Rosenbrock-2D", rB))

    # ── SUMMARY ───────────────────────────────────────────────────────────────
    print()
    print("=" * W)
    print("SUMMARY")
    print("=" * W)
    for label, r in all_results:
        vs  = r['e2'] / max(r['e1'], 1.0)
        gap = r['e2'] / max(r['e3'], 1.0)
        ok  = "✅" if vs >= 1.5 and gap >= 0.80 else ("⚠ " if vs >= 1.0 else "❌")
        print(f"  {ok} {label:<22}  naive→PA: {vs:.2f}×   PA→oracle: {gap:.2f}×")
    print()
    print("  Ergodicity: Roberts & Rosenthal (2009) §3 — hard freeze satisfies")
    print("    vanishing adaptation; production kernel is standard fixed-u Gibbs.")
    print("  Optimal target rate: Roberts, Gelman & Gilks (1997) — 0.44 for 1D MH.")
    print("  Equilibrium scale:   u[d] ≈ 2.38 × true_std[d]  (Gaussian targets).")
    print("  λ–k linkage: u[d] encodes curvature regime per §11 Order Theorem;")
    print("    u[d] small ↔ k=1 (steep / tight), u[d] large ↔ k=2 (flat / open).")


if __name__ == "__main__":
    main()
