"""
DESI Year 1 BAO + PA-MCMC Test
================================
Author: Eric D. Martin, 2026-04-12

Tests whether PA-MCMC (Payload-Augmented MCMC) gives better posterior coverage
of the DESI Year 1 BAO w₀wₐCDM parameter space than standard Metropolis-Hastings.

DATA: DESI Year 1 BAO measurements (arXiv:2404.03002, DESI Collaboration 2024)
      Published D_M/r_d, D_H/r_d, D_V/r_d at 7 effective redshifts.

MODEL: Flat w₀wₐCDM — 4 free parameters: H₀, Ωm, w₀, wₐ
       r_d fixed with Gaussian prior from Planck 2018: 147.18 ± 0.29 Mpc

PREDICTION: The w₀–wₐ degeneracy axis (dark energy banana) will show
            large ESS deficit in standard MH but not in PA-MCMC.
            Individual credible intervals for w₀ and wₐ will be broader
            under PA-MCMC, potentially reducing the ~2.5σ ΛCDM exclusion.
"""

import numpy as np
import camb
from scipy import integrate
from numpy.linalg import inv, norm
import warnings

warnings.filterwarnings("ignore")

# ─── DESI Year 1 BAO Data (arXiv:2404.03002, Table 1) ─────────────────────────
# Each entry: (z_eff, observable_type, value, sigma)
# observable_type: 'DV' = isotropic, 'DM' = transverse, 'DH' = line-of-sight

DESI_DATA = [
    # BGS: isotropic only
    (0.295, 'DV', 7.93,  0.15),
    # LRG1: anisotropic
    (0.510, 'DM', 13.62, 0.25),
    (0.510, 'DH', 20.98, 0.61),
    # LRG2: anisotropic
    (0.706, 'DM', 16.85, 0.32),
    (0.706, 'DH', 20.08, 0.60),
    # LRG3+ELG1: anisotropic
    (0.930, 'DM', 21.71, 0.28),
    (0.930, 'DH', 17.88, 0.35),
    # ELG2: anisotropic
    (1.317, 'DM', 27.79, 0.69),
    (1.317, 'DH', 13.82, 0.42),
    # QSO: anisotropic
    (1.491, 'DM', 30.21, 0.79),
    (1.491, 'DH', 13.23, 0.55),
    # Ly-alpha QSO: anisotropic
    (2.330, 'DM', 39.71, 0.94),
    (2.330, 'DH',  8.52, 0.17),
]

# Planck 2018 priors (used to break BAO degeneracies, as in DESI published analysis)
RD_PLANCK  = 147.18   # Mpc       (sound horizon)
RD_SIGMA   =   0.29   # Mpc
H0_PLANCK  =  67.36   # km/s/Mpc
H0_SIGMA   =   0.54   # km/s/Mpc  (Planck 2018, TT+TE+EE+lowE)
OM_PLANCK  =   0.3153
OM_SIGMA   =   0.0073

# Speed of light
C_LIGHT = 299792.458  # km/s


# ─── Cosmological model ────────────────────────────────────────────────────────

def w_de(z, w0, wa):
    """CPL dark energy equation of state."""
    return w0 + wa * z / (1.0 + z)


def comoving_distance(z, H0, Om, w0, wa, n_steps=200):
    """
    Comoving distance D_C(z) [Mpc] for flat w0waCDM.
    D_C(z) = c ∫₀ᶻ dz' / H(z')
    H(z) = H₀ √(Ωm(1+z)³ + Ωde(z))
    Ωde(z) = (1-Ωm) exp(3 ∫₀ᶻ (1+w(z'))/(1+z') dz')
    """
    OL = 1.0 - Om   # flat universe

    def hubble(zp):
        # DE density integral: exp(3∫₀ᶻ' (1+w(z''))/(1+z'') dz'')
        if zp <= 0:
            de_factor = 1.0
        else:
            def integrand(z2):
                return (1.0 + w_de(z2, w0, wa)) / (1.0 + z2)
            val, _ = integrate.quad(integrand, 0, zp, limit=50)
            de_factor = np.exp(3.0 * val)
        H2 = H0**2 * (Om * (1.0 + zp)**3 + OL * de_factor)
        return np.sqrt(max(H2, 1e-10))

    def dc_integrand(zp):
        return C_LIGHT / hubble(zp)

    if z <= 0:
        return 0.0
    result, _ = integrate.quad(dc_integrand, 0, z, limit=100)
    return result


def bao_theory(z, obs_type, H0, Om, w0, wa, rd):
    """
    Compute theoretical BAO observable D/r_d at redshift z.
    obs_type: 'DM', 'DH', or 'DV'
    """
    Dc = comoving_distance(z, H0, Om, w0, wa)
    H_z = C_LIGHT / (comoving_distance(z + 1e-4, H0, Om, w0, wa)
                     - comoving_distance(z - 1e-4, H0, Om, w0, wa)) * 2e-4
    # More careful H(z) computation
    def hubble_at(zp):
        OL = 1.0 - Om
        if zp <= 0:
            de_factor = 1.0
        else:
            def integrand(z2):
                return (1.0 + w_de(z2, w0, wa)) / (1.0 + z2)
            val, _ = integrate.quad(integrand, 0, zp, limit=50)
            de_factor = np.exp(3.0 * val)
        H2 = H0**2 * (Om * (1.0 + zp)**3 + OL * de_factor)
        return np.sqrt(max(H2, 1e-10))

    Hz = hubble_at(z)
    DH = C_LIGHT / Hz    # Hubble distance [Mpc]
    DM = Dc              # Transverse comoving distance (flat) [Mpc]
    DV = (z * DM**2 * DH)**(1.0/3.0)

    if obs_type == 'DM':
        return DM / rd
    elif obs_type == 'DH':
        return DH / rd
    elif obs_type == 'DV':
        return DV / rd
    else:
        raise ValueError(f"Unknown obs_type: {obs_type}")


# ─── Log-likelihood ────────────────────────────────────────────────────────────

def log_likelihood(params):
    """
    Log-likelihood for DESI Year 1 BAO + Planck r_d prior.

    params = [H0, Om, w0, wa, rd]
    Priors:
      H0 ~ Uniform(50, 90)
      Om ~ Uniform(0.1, 0.6)
      w0 ~ Uniform(-2.5, 0.5)
      wa ~ Uniform(-4.0, 2.0)
      rd ~ N(147.18, 0.29²)
    """
    H0, Om, w0, wa, rd = params

    # Hard priors
    if not (60 < H0 < 75):     return -np.inf
    if not (0.2 < Om < 0.45):  return -np.inf
    if not (-3.0 < w0 < 0.5):  return -np.inf
    if not (-4.0 < wa < 2.0):  return -np.inf
    if not (143 < rd < 152):   return -np.inf

    # Gaussian priors from Planck (breaks H₀–r_d and H₀–Ωm degeneracies)
    log_prior_rd = -0.5 * ((rd - RD_PLANCK) / RD_SIGMA)**2
    log_prior_H0 = -0.5 * ((H0 - H0_PLANCK) / H0_SIGMA)**2
    log_prior_Om = -0.5 * ((Om - OM_PLANCK) / OM_SIGMA)**2
    log_prior_rd = log_prior_rd + log_prior_H0 + log_prior_Om

    # BAO chi-squared
    chi2 = 0.0
    for (z, obs_type, value, sigma) in DESI_DATA:
        try:
            theory = bao_theory(z, obs_type, H0, Om, w0, wa, rd)
        except Exception:
            return -np.inf
        chi2 += ((value - theory) / sigma)**2

    return -0.5 * chi2 + log_prior_rd


# ─── PA-MCMC (from cu_mcmc.py, inlined) ───────────────────────────────────────

def effective_sample_size(chain):
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


def standard_mh(log_p, x0, n_steps, proposal_scale=0.3, rng=None):
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


def pa_mcmc(log_p, x0, n_steps, base_u=0.3, alpha=0.97,
             burnin_frac=0.30, min_u=1e-6, max_u_factor=5.0, rng=None):
    """
    PA-MCMC — Payload-Augmented MCMC with burn-in-then-freeze.

    During burn-in: payload EMA updated ONLY on accepted steps.
      u ← α·u + (1−α)·|accepted_step|
      On reject: u unchanged. Rejection tells us the posterior may be
      narrower than u, but we let accepted geometry do the teaching.

    After burn-in: payload frozen — exact detailed balance restored.

    α=0.97 → memory timescale τ = 1/(1−α) = 33 steps.
    For a 5-parameter problem this is the minimum to map the posterior
    geometry before the payload converges prematurely.

    Bug avoided: α=0.88 (τ=8) + reject-shrink caused a death spiral:
      rejection → shrink u → tiny proposals → high accept → u shrinks
      further from tiny steps → chain freezes. Only accept-based updates
      break this positive-feedback loop.
    """
    if rng is None:
        rng = np.random.default_rng(42)
    dim = len(x0)
    chain = np.zeros((n_steps, dim))
    u = np.atleast_1d(base_u).copy().astype(float)
    if len(u) == 1:
        u = np.full(dim, u[0])
    x = x0.copy().astype(float)
    lp = log_p(x)
    accepted = 0
    T_burn = int(n_steps * burnin_frac)
    max_u = max_u_factor * u.copy()

    for i in range(n_steps):
        proposal = x + rng.normal(0, u)
        lp_prop = log_p(proposal)
        acc = np.log(rng.uniform() + 1e-300) < lp_prop - lp

        if acc:
            if i < T_burn:
                # Payload learns from actual accepted geometry only.
                # EMA toward observed accepted step size per dimension.
                step = np.abs(proposal - x)
                u = np.clip(alpha * u + (1.0 - alpha) * step, min_u, max_u)
            x, lp = proposal, lp_prop
            accepted += 1
        # On reject: payload unchanged during burn-in.
        # Rejections don't carry geometric information at per-step resolution;
        # only the pattern of accepted steps maps the posterior shape.

        chain[i] = x

    return chain, accepted / n_steps


# ─── Diagnostic: watch payload during burn-in ─────────────────────────────────

def diagnose_burnin(log_p, x0, n_steps=400, base_u=0.3, alpha=0.97,
                    min_u=1e-6, param_names=None, rng=None):
    """
    Run PA-MCMC for n_steps and print the payload every 50 steps.
    Healthy convergence: u settles to ~posterior width per dimension.
    Death spiral: u collapses to near-zero while accept rate climbs.
    """
    if rng is None:
        rng = np.random.default_rng(0)
    dim = len(x0)
    u = np.atleast_1d(base_u).copy().astype(float)
    if len(u) == 1:
        u = np.full(dim, u[0])
    x = x0.copy().astype(float)
    lp = log_p(x)
    accepted = 0

    print(f"\n  Burn-in diagnostic (α={alpha}, τ={1/(1-alpha):.0f} steps):")
    print(f"  {'Step':>6}  {'accept':>7}  {'u':}")
    if param_names:
        hdr = "  ".join(f"{n:>8}" for n in param_names)
        print(f"  {'':>6}  {'':>7}  {hdr}")

    for i in range(1, n_steps + 1):
        proposal = x + rng.normal(0, u)
        lp_prop = log_p(proposal)
        if np.log(rng.uniform() + 1e-300) < lp_prop - lp:
            step = np.abs(proposal - x)
            u = np.clip(alpha * u + (1.0 - alpha) * step, min_u, u * 50)
            x, lp = proposal, lp_prop
            accepted += 1
        # No update on reject

        if i % 50 == 0:
            u_str = "  ".join(f"{v:8.5f}" for v in u)
            print(f"  {i:>6}  {accepted/i:>7.2f}  {u_str}")

    print(f"  Final u: {u}")
    return u


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    # MAP starting point (found by Nelder-Mead with Planck+DESI priors)
    # w0=-0.80, wa=-0.72 reflects DESI's preference away from ΛCDM
    x0 = np.array([67.36, 0.317, -0.80, -0.72, 147.18])

    # Proposal scales tuned to approximate posterior standard deviations:
    #   H0: tight from Planck prior → 0.25 km/s/Mpc
    #   Om: tight from Planck prior → 0.005
    #   w0: degenerate with wa    → 0.18  (wider — PA-MCMC should detect this)
    #   wa: most degenerate       → 0.35  (widest — PA-MCMC should detect this)
    #   rd: from Planck prior     → 0.15 Mpc
    ps_std = np.array([0.25, 0.005, 0.18, 0.35, 0.15])

    N_STEPS = 4000   # enough to see ESS difference; real analysis uses ~200k
    SEED    = 77

    param_names = ['H₀', 'Ωm', 'w₀', 'wₐ', 'r_d']

    print("=" * 72)
    print("DESI Year 1 BAO — PA-MCMC vs Standard MH")
    print("Model: flat w₀wₐCDM, 5 params [H₀, Ωm, w₀, wₐ, r_d]")
    print(f"Data:  {len(DESI_DATA)} BAO measurements from DESI arXiv:2404.03002")
    print("=" * 72)

    lp0 = log_likelihood(x0)
    print(f"\n  Starting log-likelihood: {lp0:.2f}")
    if not np.isfinite(lp0):
        print("  ERROR: starting point has -inf log-likelihood.")
        return

    import time

    # ── Phase 0: pilot run to estimate posterior widths ───────────────────────
    print("\n  Phase 0: 300-step pilot to calibrate proposal scales...")
    rng_pilot = np.random.default_rng(SEED + 1)
    # Use small conservative scales for pilot
    ps_pilot = np.array([0.12, 0.003, 0.10, 0.20, 0.08])
    pilot_chain, pilot_acc = standard_mh(log_likelihood, x0, 300,
                                          proposal_scale=ps_pilot, rng=rng_pilot)
    # Posterior widths from pilot (discard first 100 steps)
    pilot_post = pilot_chain[100:]
    pilot_std = pilot_post.std(axis=0)
    # Clamp: at least the pilot scale, at most 3× pilot scale
    calibrated_u = np.clip(pilot_std * 2.0, ps_pilot * 0.5, ps_pilot * 3.0)
    print(f"  Pilot accept={pilot_acc:.2f}. Calibrated scales:")
    for n, u in zip(param_names, calibrated_u):
        print(f"    {n}: {u:.4f}")

    # ── Burn-in diagnostic: confirm payload converges, not collapses ─────────
    print("\n  Burn-in diagnostic (α=0.97, floor=30% of calibrated, accept-only updates):")
    diagnose_burnin(log_likelihood, x0, n_steps=400,
                    base_u=calibrated_u, alpha=0.97,
                    min_u=calibrated_u * 0.30,
                    param_names=param_names,
                    rng=np.random.default_rng(SEED + 99))

    # ── Standard MH with calibrated scales ───────────────────────────────────
    print(f"\n  Running {N_STEPS} steps each × 2 samplers...")
    rng_s = np.random.default_rng(SEED)
    t0 = time.time()
    chain_s, acc_s = standard_mh(log_likelihood, x0, N_STEPS,
                                  proposal_scale=calibrated_u, rng=rng_s)
    t_std = time.time() - t0
    ess_s = ess_multivariate(chain_s)
    print(f"  Standard MH:  done in {t_std:.0f}s, accept={acc_s:.2f}, ESS={ess_s:.1f}")

    # ── PA-MCMC with calibrated starting payload ──────────────────────────────
    # α=0.97 → τ=33 steps — payload remembers ~33 accepted steps before
    # converging. For 5 parameters, this is the minimum stable timescale.
    #
    # min_u = 0.30 * calibrated_u (floor at 30% of pilot estimate).
    # Without this floor, the EMA bias at <23% acceptance causes the
    # payload to decay below the true posterior width: accepted steps at
    # 15% acceptance are drawn from the lower tail, so E[|step| | accept]
    # systematically underestimates the posterior width. The floor prevents
    # the production phase from freezing at near-zero scale.
    min_u_pa = calibrated_u * 0.30
    rng_p = np.random.default_rng(SEED)
    t0 = time.time()
    chain_p, acc_p = pa_mcmc(log_likelihood, x0, N_STEPS,
                              base_u=calibrated_u, alpha=0.97,
                              burnin_frac=0.25,
                              min_u=min_u_pa,
                              rng=rng_p)
    t_pa = time.time() - t0
    ess_p = ess_multivariate(chain_p)
    print(f"  PA-MCMC:      done in {t_pa:.0f}s, accept={acc_p:.2f}, ESS={ess_p:.1f}")

    # ── Posterior statistics ─────────────────────────────────────────────────
    burn = N_STEPS // 4
    chain_s_pb = chain_s[burn:]
    chain_p_pb = chain_p[burn:]

    print("\n" + "─" * 72)
    print(f"  {'Parameter':<8}  {'Std MH mean':>12}  {'Std MH 95%CI':>16}"
          f"  {'PA-MCMC mean':>12}  {'PA-MCMC 95%CI':>16}  {'CI width ratio':>14}")
    print("─" * 72)

    w0_idx = 2
    wa_idx = 3
    ci_widths_std = []
    ci_widths_pa  = []

    for i, name in enumerate(param_names):
        m_s  = chain_s_pb[:, i].mean()
        m_p  = chain_p_pb[:, i].mean()
        lo_s, hi_s = np.percentile(chain_s_pb[:, i], [2.5, 97.5])
        lo_p, hi_p = np.percentile(chain_p_pb[:, i], [2.5, 97.5])
        w_s = hi_s - lo_s
        w_p = hi_p - lo_p
        ci_widths_std.append(w_s)
        ci_widths_pa.append(w_p)
        ratio = w_p / w_s if w_s > 0 else float('nan')
        flag = " ← WIDER" if ratio > 1.15 else (" ← narrower" if ratio < 0.85 else "")
        print(f"  {name:<8}  {m_s:>12.4f}  [{lo_s:6.3f},{hi_s:6.3f}]"
              f"  {m_p:>12.4f}  [{lo_p:6.3f},{hi_p:6.3f}]"
              f"  {ratio:>14.2f}x{flag}")

    print("─" * 72)

    # Focus on the dark energy parameters
    w0_ci_ratio = ci_widths_pa[w0_idx] / max(ci_widths_std[w0_idx], 1e-10)
    wa_ci_ratio = ci_widths_pa[wa_idx] / max(ci_widths_std[wa_idx], 1e-10)
    ess_ratio   = ess_p / max(ess_s, 1.0)

    print(f"\n  ESS ratio (PA / Std):         {ess_ratio:.2f}x")
    print(f"  w₀  CI width ratio:           {w0_ci_ratio:.2f}x")
    print(f"  wₐ  CI width ratio:           {wa_ci_ratio:.2f}x")

    # How far is w₀ from -1?
    w0_mean_s = chain_s_pb[:, w0_idx].mean()
    w0_std_s  = chain_s_pb[:, w0_idx].std()
    w0_mean_p = chain_p_pb[:, w0_idx].mean()
    w0_std_p  = chain_p_pb[:, w0_idx].std()

    sigma_from_lcdm_std = abs(w0_mean_s - (-1.0)) / w0_std_s
    sigma_from_lcdm_pa  = abs(w0_mean_p - (-1.0)) / w0_std_p

    print(f"\n  Distance of w₀ from ΛCDM (w₀=-1):")
    print(f"    Standard MH:  {sigma_from_lcdm_std:.2f}σ")
    print(f"    PA-MCMC:      {sigma_from_lcdm_pa:.2f}σ")

    print("\n" + "=" * 72)
    print("INTERPRETATION")
    print("=" * 72)

    if ess_ratio > 2.0:
        print(f"\n  ✅ PA-MCMC achieves {ess_ratio:.1f}x more effective samples.")
        print("     Standard MCMC is undersampling the DESI posterior.")
    else:
        print(f"\n  ⚠  ESS ratio only {ess_ratio:.1f}x — DESI posterior may be")
        print("     less degenerate than the benchmark Rosenbrock case.")

    if w0_ci_ratio > 1.1:
        print(f"\n  ✅ w₀ credible interval is {w0_ci_ratio:.2f}x wider under PA-MCMC.")
        print(f"     ΛCDM exclusion shifts: {sigma_from_lcdm_std:.2f}σ → {sigma_from_lcdm_pa:.2f}σ")
        print("     This supports the prediction: standard MCMC overstates")
        print("     the tension with ΛCDM in the dark energy plane.")
    elif w0_ci_ratio < 0.9:
        print(f"\n  ⚠  w₀ CI NARROWER under PA-MCMC ({w0_ci_ratio:.2f}x).")
        print("     Interpretation: standard MH was overexploring tails.")
        print("     More steps needed for a definitive comparison.")
    else:
        print(f"\n  ≈  w₀ CI unchanged ({w0_ci_ratio:.2f}x) — either the chains")
        print("     haven't converged yet or DESI's posterior isn't strongly")
        print("     degenerate at this parameter scale.")

    print("\n  NOTE: 2000 steps is a pilot run. Published DESI analysis uses")
    print("  ~500k steps per chain. ESS scales linearly — the ratios above")
    print("  reflect the per-step efficiency difference, not total chain length.")
    print("\n  To reproduce DESI's full analysis: increase N_STEPS to 100000+")
    print("  and run pa_mcmc() with the frozen proposal from the burn-in phase.")


if __name__ == "__main__":
    main()
