"""
Tensor-Extended N/U Algebra for Hubble Tension Resolution

This module implements observer domain-aware uncertainty propagation
that resolves the Hubble tension through conservative epistemic bounds.

Author: Eric D. Martin
Date: 2025-10-11
Framework: N/U Algebra + Observer Tensors + UHA
"""

import numpy as np
import pandas as pd
from typing import Tuple, List, Dict, Optional
from dataclasses import dataclass


@dataclass
class TensorNU:
    """
    Tensor-extended Nominal/Uncertainty pair.
    
    Attributes:
        n: Nominal value
        u: Uncertainty (non-negative)
        T_obs: Observer tensor [P_m, 0_t, 0_m, 0_a]
            - P_m: Material probability (measurement confidence)
            - 0_t: Temporal zero-anchor (observation epoch)
            - 0_m: Material zero-anchor (matter density context)
            - 0_a: Awareness zero-anchor (systematic bias signature)
    """
    n: float
    u: float
    T_obs: np.ndarray
    
    def __post_init__(self):
        """Enforce non-negative uncertainty."""
        self.u = max(0.0, self.u)
        if self.T_obs is None:
            self.T_obs = np.array([1.0, 0.0, 0.0, 0.0])
    
    @property
    def interval(self) -> Tuple[float, float]:
        """Return closed interval [n-u, n+u]."""
        return (self.n - self.u, self.n + self.u)
    
    def __repr__(self) -> str:
        return f"TensorNU(n={self.n:.2f}, u={self.u:.2f}, T={self.T_obs})"


class TensorNUAlgebra:
    """
    Tensor-extended N/U algebra operations.
    
    Implements domain-aware uncertainty propagation that accounts
    for epistemic distance between observer contexts.
    """
    
    @staticmethod
    def epistemic_distance(T1: np.ndarray, T2: np.ndarray) -> float:
        """
        Compute epistemic distance between observer domains.
        
        Args:
            T1, T2: Observer tensors [P_m, 0_t, 0_m, 0_a]
        
        Returns:
            Euclidean distance ||T1 - T2||
        """
        return np.linalg.norm(T1 - T2)
    
    @staticmethod
    def merge(tnu1: TensorNU, tnu2: TensorNU) -> TensorNU:
        """
        Merge two tensor-extended N/U pairs.
        
        Uses domain-aware weighting where uncertainty expansion
        is scaled by epistemic distance between observer contexts.
        
        Args:
            tnu1, tnu2: TensorNU pairs to merge
        
        Returns:
            Merged TensorNU with domain-aware uncertainty
        """
        # Extract components
        n1, u1, T1 = tnu1.n, tnu1.u, tnu1.T_obs
        n2, u2, T2 = tnu2.n, tnu2.u, tnu2.T_obs
        
        # Material probability weights
        P_m1, P_m2 = T1[0], T2[0]
        
        # Weighted nominal value
        n_merge = (n1 * P_m1 + n2 * P_m2) / (P_m1 + P_m2)
        
        # Epistemic distance
        delta_T = TensorNUAlgebra.epistemic_distance(T1, T2)
        
        # Domain-aware uncertainty
        # Base: average of individual uncertainties
        # Expansion: disagreement scaled by domain separation
        u_merge = (u1 + u2) / 2 + abs(n1 - n2) / 2 * delta_T
        
        # Merged tensor (weighted average)
        T_merge = (T1 * P_m1 + T2 * P_m2) / (P_m1 + P_m2)
        
        return TensorNU(n=n_merge, u=u_merge, T_obs=T_merge)
    
    @staticmethod
    def add(tnu1: TensorNU, tnu2: TensorNU) -> TensorNU:
        """
        Addition operator: (n1,u1) ⊕ (n2,u2) = (n1+n2, u1+u2).
        
        Tensors are averaged (assumes independent observations).
        """
        n_sum = tnu1.n + tnu2.n
        u_sum = tnu1.u + tnu2.u
        T_avg = (tnu1.T_obs + tnu2.T_obs) / 2
        
        return TensorNU(n=n_sum, u=u_sum, T_obs=T_avg)
    
    @staticmethod
    def multiply(tnu1: TensorNU, tnu2: TensorNU) -> TensorNU:
        """
        Multiplication operator: (n1,u1) ⊗ (n2,u2) = (n1·n2, |n1|·u2 + |n2|·u1).
        
        Tensors are averaged.
        """
        n_prod = tnu1.n * tnu2.n
        u_prod = abs(tnu1.n) * tnu2.u + abs(tnu2.n) * tnu1.u
        T_avg = (tnu1.T_obs + tnu2.T_obs) / 2
        
        return TensorNU(n=n_prod, u=u_prod, T_obs=T_avg)
    
    @staticmethod
    def scalar_multiply(scalar: float, tnu: TensorNU) -> TensorNU:
        """
        Scalar multiplication: a ⊙ (n,u) = (a·n, |a|·u).
        
        Tensor unchanged.
        """
        n_scaled = scalar * tnu.n
        u_scaled = abs(scalar) * tnu.u
        
        return TensorNU(n=n_scaled, u=u_scaled, T_obs=tnu.T_obs.copy())


def construct_observer_tensor(
    redshift: float,
    measurement_type: str,
    omega_m: float = 0.315,
    H0_prior: float = 70.0,
    instrument_lag: float = 0.0
) -> np.ndarray:
    """
    Construct observer tensor from physical parameters.
    
    Args:
        redshift: Observation redshift
        measurement_type: 'CMB', 'BAO', 'SNe', 'Cepheid', 'TRGB', 'Maser', 'Lens'
        omega_m: Matter density parameter
        H0_prior: Prior H₀ assumption (affects temporal anchor)
        instrument_lag: Systematic temporal offset
    
    Returns:
        Observer tensor T_obs = [P_m, 0_t, 0_m, 0_a]
    """
    # Material probability: measurement precision/confidence
    confidence_map = {
        'CMB': 0.95,      # Planck: high precision
        'BAO': 0.90,      # Geometric: good precision
        'SNe': 0.85,      # Well-calibrated standard candles
        'Cepheid': 0.80,  # Distance ladder uncertainties
        'TRGB': 0.75,     # Newer method, fewer calibrators
        'Maser': 0.85,    # Direct geometric
        'Lens': 0.70      # Model-dependent
    }
    P_m = confidence_map.get(measurement_type, 0.50)
    
    # Temporal zero-anchor: normalized lookback time
    # Scale factor a = 1/(1+z)
    # 0_t → 1 for high-z (early), 0 for z→0 (late)
    a = 1.0 / (1.0 + redshift)
    zero_t = 1.0 - a + instrument_lag
    
    # Material zero-anchor: deviation from fiducial Ωm
    # Normalized to [-1, 1] range
    zero_m = (omega_m - 0.315) / 0.315
    
    # Awareness zero-anchor: systematic bias signature
    # Negative for early/indirect, positive for late/direct
    if measurement_type == 'CMB':
        zero_a = -0.5  # Early, model-dependent
    elif measurement_type == 'BAO':
        zero_a = -0.3  # Early, geometric but model-based
    elif measurement_type in ['SNe', 'Cepheid', 'TRGB']:
        zero_a = 0.5   # Late, direct empirical
    elif measurement_type == 'Maser':
        zero_a = 0.4   # Late, direct geometric
    elif measurement_type == 'Lens':
        zero_a = 0.0   # Intermediate, model-dependent
    else:
        zero_a = 0.0   # Neutral
    
    return np.array([P_m, zero_t, zero_m, zero_a])


def create_hubble_dataset() -> pd.DataFrame:
    """
    Create Hubble tension dataset with observer tensors.
    
    Returns:
        DataFrame with columns: name, H0_n, H0_u, redshift, type, era, T_obs, TensorNU
    """
    probes = [
        # Early Universe
        {
            'name': 'Planck18',
            'H0_n': 67.40,
            'H0_u': 0.50,
            'redshift': 1090.0,
            'type': 'CMB',
            'omega_m': 0.315,
            'era': 'early',
            'reference': 'Planck Collaboration 2020'
        },
        {
            'name': 'DES-IDL',
            'H0_n': 67.19,
            'H0_u': 0.65,
            'redshift': 0.5,
            'type': 'BAO',
            'omega_m': 0.320,
            'era': 'early',
            'reference': 'DES Collaboration 2024'
        },
        
        # Late Universe
        {
            'name': 'SH0ES',
            'H0_n': 73.04,
            'H0_u': 1.04,
            'redshift': 0.01,
            'type': 'Cepheid',
            'omega_m': 0.300,
            'era': 'late',
            'reference': 'Riess et al. 2022'
        },
        {
            'name': 'TRGB',
            'H0_n': 69.80,
            'H0_u': 2.50,
            'redshift': 0.01,
            'type': 'TRGB',
            'omega_m': 0.300,
            'era': 'late',
            'reference': 'Freedman et al. 2021'
        },
        {
            'name': 'Megamaser',
            'H0_n': 73.50,
            'H0_u': 3.00,
            'redshift': 0.01,
            'type': 'Maser',
            'omega_m': 0.300,
            'era': 'late',
            'reference': 'Pesce et al. 2020'
        },
        {
            'name': 'TDCOSMO',
            'H0_n': 77.10,
            'H0_u': 7.20,
            'redshift': 0.3,
            'type': 'Lens',
            'omega_m': 0.300,
            'era': 'late',
            'reference': 'Millon et al. 2020'
        }
    ]
    
    df = pd.DataFrame(probes)
    
    # Construct observer tensors
    df['T_obs'] = df.apply(
        lambda r: construct_observer_tensor(
            r['redshift'],
            r['type'],
            r['omega_m']
        ),
        axis=1
    )
    
    # Create TensorNU objects
    df['TensorNU'] = df.apply(
        lambda r: TensorNU(r['H0_n'], r['H0_u'], r['T_obs']),
        axis=1
    )
    
    return df


def analyze_hubble_tension(df: pd.DataFrame) -> Dict:
    """
    Perform complete Hubble tension analysis with tensor-aware merging.
    
    Args:
        df: DataFrame with TensorNU column
    
    Returns:
        Dictionary with analysis results
    """
    results = {
        'probes': df.to_dict('records'),
        'pairwise': [],
        'group_merges': {}
    }
    
    # Pairwise analysis
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            probe1 = df.iloc[i]
            probe2 = df.iloc[j]
            
            tnu1 = probe1['TensorNU']
            tnu2 = probe2['TensorNU']
            
            # Standard N/U merge (no tensor)
            standard_u = (tnu1.u + tnu2.u) / 2 + abs(tnu1.n - tnu2.n) / 2
            
            # Tensor-aware merge
            merged = TensorNUAlgebra.merge(tnu1, tnu2)
            
            # Epistemic distance
            delta_T = TensorNUAlgebra.epistemic_distance(tnu1.T_obs, tnu2.T_obs)
            
            # Check interval overlap
            int1 = tnu1.interval
            int2 = tnu2.interval
            overlap = max(0, min(int1[1], int2[1]) - max(int1[0], int2[0]))
            
            results['pairwise'].append({
                'probe1': probe1['name'],
                'probe2': probe2['name'],
                'n1': tnu1.n,
                'n2': tnu2.n,
                'delta_n': abs(tnu1.n - tnu2.n),
                'standard_u': standard_u,
                'tensor_u': merged.u,
                'delta_T': delta_T,
                'expansion_ratio': merged.u / standard_u if standard_u > 0 else 1.0,
                'original_overlap': overlap,
                'era_match': probe1['era'] == probe2['era']
            })
    
    # Group-level merges
    early_probes = df[df['era'] == 'early']['TensorNU'].tolist()
    late_probes = df[df['era'] == 'late']['TensorNU'].tolist()
    
    # Merge early universe
    early_merged = early_probes[0]
    for tnu in early_probes[1:]:
        early_merged = TensorNUAlgebra.merge(early_merged, tnu)
    
    # Merge late universe
    late_merged = late_probes[0]
    for tnu in late_probes[1:]:
        late_merged = TensorNUAlgebra.merge(late_merged, tnu)
    
    # Cross-era merge
    global_merged = TensorNUAlgebra.merge(early_merged, late_merged)
    
    # Standard merge for comparison
    standard_u_global = (early_merged.u + late_merged.u) / 2 + \
                        abs(early_merged.n - late_merged.n) / 2
    
    # Check concordance
    early_int = early_merged.interval
    late_int = late_merged.interval
    global_int = global_merged.interval
    
    early_late_overlap = max(0, min(early_int[1], late_int[1]) - max(early_int[0], late_int[0]))
    
    early_in_global = (global_int[0] <= early_int[0] <= global_int[1]) and \
                      (global_int[0] <= early_int[1] <= global_int[1])
    late_in_global = (global_int[0] <= late_int[0] <= global_int[1]) and \
                     (global_int[0] <= late_int[1] <= global_int[1])
    
    results['group_merges'] = {
        'early': {
            'n': early_merged.n,
            'u': early_merged.u,
            'interval': early_int,
            'T_obs': early_merged.T_obs
        },
        'late': {
            'n': late_merged.n,
            'u': late_merged.u,
            'interval': late_int,
            'T_obs': late_merged.T_obs
        },
        'global': {
            'n': global_merged.n,
            'u': global_merged.u,
            'interval': global_int,
            'T_obs': global_merged.T_obs,
            'delta_T': TensorNUAlgebra.epistemic_distance(
                early_merged.T_obs, late_merged.T_obs
            ),
            'standard_u': standard_u_global,
            'expansion_ratio': global_merged.u / standard_u_global
        },
        'concordance': {
            'early_late_overlap': early_late_overlap,
            'early_in_global': early_in_global,
            'late_in_global': late_in_global,
            'full_concordance': early_in_global and late_in_global
        }
    }
    
    return results


def print_analysis_report(results: Dict):
    """Print comprehensive analysis report."""
    
    print("=" * 80)
    print("TENSOR-EXTENDED N/U ALGEBRA: HUBBLE TENSION ANALYSIS")
    print("=" * 80)
    print()
    
    # Probes
    print("Input Probes:")
    print("-" * 80)
    for probe in results['probes']:
        print(f"{probe['name']:12s} | H₀ = ({probe['H0_n']:5.2f} ± {probe['H0_u']:4.2f}) km/s/Mpc")
        print(f"             | z = {probe['redshift']:8.2f} | {probe['type']:8s} | {probe['era']:5s}")
    print()
    
    # Group merges
    gm = results['group_merges']
    print("=" * 80)
    print("GROUP-LEVEL MERGES")
    print("=" * 80)
    print()
    
    early = gm['early']
    late = gm['late']
    glob = gm['global']
    
    print(f"Early Universe (CMB + BAO):")
    print(f"  H₀ = ({early['n']:.2f} ± {early['u']:.2f}) km/s/Mpc")
    print(f"  Interval: [{early['interval'][0]:.2f}, {early['interval'][1]:.2f}]")
    print()
    
    print(f"Late Universe (Distance Ladder):")
    print(f"  H₀ = ({late['n']:.2f} ± {late['u']:.2f}) km/s/Mpc")
    print(f"  Interval: [{late['interval'][0]:.2f}, {late['interval'][1]:.2f}]")
    print()
    
    print(f"Tensor-Extended Global Merge:")
    print(f"  H₀ = ({glob['n']:.2f} ± {glob['u']:.2f}) km/s/Mpc")
    print(f"  Interval: [{glob['interval'][0]:.2f}, {glob['interval'][1]:.2f}]")
    print(f"  Epistemic distance: Δ_T = {glob['delta_T']:.4f}")
    print(f"  Standard uncertainty: {glob['standard_u']:.2f} km/s/Mpc")
    print(f"  Expansion ratio: {glob['expansion_ratio']:.3f}x")
    print()
    
    # Concordance
    conc = gm['concordance']
    print("=" * 80)
    print("CONCORDANCE TEST")
    print("=" * 80)
    print()
    
    if conc['early_late_overlap'] > 0:
        print(f"✓ Direct overlap: {conc['early_late_overlap']:.2f} km/s/Mpc")
    else:
        print(f"✗ No direct overlap (gap: {abs(conc['early_late_overlap']):.2f} km/s/Mpc)")
    print()
    
    print(f"Tensor-merged interval coverage:")
    print(f"  Early [{early['interval'][0]:.2f}, {early['interval'][1]:.2f}] in global: {'✓ YES' if conc['early_in_global'] else '✗ NO'}")
    print(f"  Late [{late['interval'][0]:.2f}, {late['interval'][1]:.2f}] in global:  {'✓ YES' if conc['late_in_global'] else '✗ NO'}")
    print()
    
    if conc['full_concordance']:
        print("=" * 80)
        print("✓✓✓ HUBBLE TENSION RESOLVED ✓✓✓")
        print("=" * 80)
        print()
        print("Tensor-extended N/U algebra achieves full concordance through")
        print("domain-aware uncertainty expansion that properly accounts for")
        print("epistemic distance between early and late universe measurements.")
    else:
        print("=" * 80)
        print("✗ PARTIAL RESOLUTION")
        print("=" * 80)
        print("Additional systematic budget may be required.")
    
    print()


if __name__ == "__main__":
    # Create dataset
    df = create_hubble_dataset()
    
    # Run analysis
    results = analyze_hubble_tension(df)
    
    # Print report
    print_analysis_report(results)
    
    # Save results
    # pd.DataFrame(results['pairwise']).to_csv('tensor_nu_pairwise.csv', index=False)
    # import json
    # with open('tensor_nu_results.json', 'w') as f:
    #     json.dump(results['group_merges'], f, indent=2, default=str)