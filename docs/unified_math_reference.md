# Unified Mathematical Framework Reference
**Eric D. Martin - All Mathematical Definitions**

---

## 1. N/U (Nominal/Uncertainty) Algebra

### 1.1 Domain Definition
**Carrier Set:**
```
A = ℝ × ℝ≥₀
(n, u) where n ∈ ℝ (nominal), u ≥ 0 (uncertainty)
```

**Interval Representation:**
```
I(n, u) = [n - u, n + u]
```

### 1.2 Core Operations

**Addition (⊕):**
```
(n₁, u₁) ⊕ (n₂, u₂) = (n₁ + n₂, u₁ + u₂)
```

**Subtraction:**
```
(n₁, u₁) - (n₂, u₂) = (n₁ - n₂, u₁ + u₂)
```

**Multiplication (⊗):**
```
(n₁, u₁) ⊗ (n₂, u₂) = (n₁n₂, |n₁|u₂ + |n₂|u₁ + λu₁u₂)
where λ ≥ 1 is tunable safety margin
```

**For λ = 1 (standard):**
```
(n₁, u₁) ⊗ (n₂, u₂) = (n₁n₂, |n₁|u₂ + |n₂|u₁)
```

**Scalar Multiplication (⊙):**
```
a ⊙ (n, u) = (an, |a|u)
```

**Affine Transformation:**
```
a ⊙ (n, u) + b = (an + b, |a|u)
```

### 1.3 Special Operators

**Catch Operator (C):**
```
C(n, u) = (0, |n| + u)
```
*Collapses nominal into uncertainty*

**Flip Operator (B):**
```
B(n, u) = (u, |n|)
```
*Swaps nominal and uncertainty*

### 1.4 Uncertainty Invariant

**Invariant M:**
```
M(n, u) = |n| + u
```

**Preservation Property:**
```
M(C(n, u)) = M(n, u)
M(B(n, u)) = M(n, u)
```

### 1.5 Properties

**Lower Bound:**
```
L(n, u) = n - u
```

**Upper Bound:**
```
U(n, u) = n + u
```

**Relative Uncertainty:**
```
r(n, u) = u / |n|  (if n ≠ 0)
```

**Sign Stability:**
```
stable(n, u) ⟺ |n| > u
```

### 1.6 Cumulative Operations

**Cumulative Sum:**
```
⊕ᵢ₌₁ⁿ (nᵢ, uᵢ) = (∑ᵢ₌₁ⁿ nᵢ, ∑ᵢ₌₁ⁿ uᵢ)
```

**Cumulative Product:**
```
⊗ᵢ₌₁ᵐ (nᵢ, uᵢ) = (∏ᵢ₌₁ᵐ nᵢ, ∑ᵢ₌₁ᵐ |∏ⱼ≠ᵢ nⱼ|uᵢ)
```

**Weighted Mean:**
```
weighted_mean({(nᵢ, uᵢ)}, {wᵢ}) = 
  (1/W) ⊙ ⊕ᵢ (wᵢ ⊙ (nᵢ, uᵢ))
where W = ∑ᵢ wᵢ
```

### 1.7 Complexity

**Per Operation:**
```
Time(⊕) = O(1)
Time(⊗) = O(1)
Time(⊙) = O(1)

Space = O(1) per operation
```

**Chain of m operations:**
```
Total Time = O(m)
Total Space = O(1)
```

---

## 2. Observer Domain Tensors

### 2.1 Tensor Components

**Observer Tensor T:**
```
T = (P_m, 0_t, 0_m, 0_a) ∈ [0,1] × [-1,1]³
```

### 2.2 Material Probability (P_m)

**Definition:**
```
P_m = 1 - (σ_H₀ / H₀_mean)
```

**Range:** [0, 1]

**Physical Interpretation:**
- P_m → 1: High measurement precision
- P_m → 0: Low measurement precision

### 2.3 Temporal Zero-Anchor (0_t)

**Definition:**
```
a = 1/(1 + z)  (scale factor)
0_t = 1 - a = z/(1 + z)
```

**Range:** [0, 1]

**Examples:**
```
CMB (z=1090):     0_t = 0.999083
BAO (z=0.5):      0_t = 0.333333
Distance (z=0.01): 0_t = 0.009901
```

### 2.4 Material Zero-Anchor (0_m)

**Definition:**
```
Ω_m,fid = 0.315  (Planck 2018)
0_m = (Ω_m - Ω_m,fid) / Ω_m,fid
```

**Range:** Typically [-0.1, 0.1]

**Examples:**
```
Planck (Ω_m=0.315): 0_m = 0.000
DES (Ω_m=0.320):    0_m = +0.016
SH0ES (Ω_m=0.300):  0_m = -0.048
```

### 2.5 Awareness Zero-Anchor (0_a)

**Definition (MC Calibrated):**
```
σ_sys = std(systematic_component)
σ_total = std(H₀_samples)
sys_fraction = σ_sys / σ_total

sign = -1  (early/indirect methods)
       +1  (late/direct methods)

base = 0.5
amplification = 1.0 + 0.5 × sys_fraction

0_a = sign × base × amplification
```

**Range:** [-1, 1]

**Examples:**
```
CMB (early):    0_a ≈ -0.651
Cepheids (late): 0_a ≈ +0.660
```

### 2.6 Epistemic Distance

**Definition:**
```
Δ_T = ||T_early - T_late||

Δ_T = √(
  (P_m,early - P_m,late)² +
  (0_t,early - 0_t,late)² +
  (0_m,early - 0_m,late)² +
  (0_a,early - 0_a,late)²
)
```

**Component Contributions:**
```
Δ_T² = ΔP_m² + Δ0_t² + Δ0_m² + Δ0_a²

Percentage contribution:
  contrib_i = 100 × Δi² / Δ_T²
```

### 2.7 Domain-Aware Merge

**Base Merge (N/U):**
```
n_merged = (n_early + n_late) / 2
u_base = (u_early + u_late) / 2
```

**Epistemic Expansion:**
```
disagreement = |n_early - n_late|
u_merged = u_base + (disagreement / 2) × Δ_T
```

**Final Interval:**
```
I_merged = [n_merged - u_merged, n_merged + u_merged]
```

**Concordance Test:**
```
concordant ⟺ I_early ⊆ I_merged AND I_late ⊆ I_merged

gap = max{0, max(I_late) - max(I_merged)}
```

---

## 3. Universal Horizon Address (UHA)

### 3.1 Cosmological Framework

**Hubble Rate (flat ΛCDM):**
```
H(a) = H₀√(Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ)
```

**Cosmic Time:**
```
T(a) = ∫₀ᵃ (a'/H(a')) da'
```

**Comoving Particle Horizon:**
```
R_H(a) = c ∫₀ᵃ (a'/a'²H(a')) da'
```

### 3.2 Normalized Coordinates

**Spatial Coordinates (spherical to normalized):**
```
s₁ = r / R_H(a)
s₂ = (1 - cos θ) / 2
s₃ = φ / (2π)
```

All sᵢ ∈ [0, 1)

### 3.3 Space-Filling Curve (Morton Z-Order)

**3D to 1D Encoding:**
```
Discretize: sᵢ → ⌊sᵢ × 2ᴺ⌋  (N bits each)

Morton index I ∈ {0, ..., 2³ᴺ - 1}

Canonical fraction:
ξ = (I + 0.5) / 2³ᴺ ∈ (0, 1)
```

### 3.4 Time-Like Offset

**Horizon-Normalized:**
```
Δt = (ξ × R_H(a)) / c
```

### 3.5 UHA Address Tuple

**Complete Address:**
```
A = (a, ξ, û, CosmoID; anchors)

where:
  a          : scale factor (dimensionless)
  ξ          : Morton index fraction (dimensionless)
  û ∈ ℝ³     : unit direction vector
  CosmoID    : cosmology fingerprint
  anchors    : {c, f₂₁}
```

### 3.6 Physical Anchors (Unit Calibration)

**Speed of Light:**
```
c = 299792458 [m·s⁻¹]
Unit tag: [0, 1, -1, 0, 0, 0, 0]
```

**Hydrogen 21cm Frequency:**
```
f₂₁ ≈ 1.42040575177 × 10⁹ [s⁻¹]
Unit tag: [0, 0, -1, 0, 0, 0, 0]
```

**Derived Units:**
```
unit_time = 1 / f₂₁
unit_length = c / f₂₁
```

### 3.7 Decode Algorithm

**Position Recovery:**
```
Given (a, ξ, û):

1. Compute R_H(a) for chosen cosmology
2. r = ξ × R_H(a)
3. x⃗ = r × û
```

**Result:** Comoving position in physical units

### 3.8 Multi-Vector Extension (UHA-MV)

**Directional Expansion:**
```
Construct orthonormal basis: {û, ê₁, ê₂}

Define expansion:
D(û; Δθ, Δφ, M) = {û₀ = û} ∪ {
  R_ê₁(±Δθ)û,
  R_ê₂(±Δθ)û,
  R_(ê₁±ê₂)(Δφ)û,
  ...
}
```

**Storage:**
```
DirExpand = (AlgoID, Δθ, Δφ, M)
```

---

## 4. Comparative Complexity Analysis

### 4.1 N/U Algebra vs Other Methods

**Time Complexity:**
```
N/U Algebra:       O(1) per operation
Gaussian RSS:      O(1) per operation
Monte Carlo:       O(n) samples
Affine Arithmetic: O(k²) per multiplication
Polynomial Chaos:  O(pᵈ) for degree d
Interval (general): O(2ᵈ) for d-dimensional
```

**Space Complexity:**
```
N/U Algebra:       O(1) per pair
Gaussian:          O(1) per value
Monte Carlo:       O(n) storage
Affine Arithmetic: O(k) coefficients (grows with operations)
```

### 4.2 Chain Composition (m operations)

**N/U Algebra:**
```
Time:  T_NU(m) = O(m)
Space: S_NU(m) = O(1)
```

**Affine Arithmetic:**
```
Time:  T_AA(m) = O(mk²)
Space: S_AA(m) = O(m)

where k = O(m) in worst case
→ T_AA(m) = O(m³)
```

**Asymptotic Advantage:**
```
lim_(m→∞) T_NU(m) / T_AA(m) = O(m/m³) = O(1/m²) → 0
```

---

## 5. Key Theorems and Properties

### 5.1 N/U Algebra Properties

**Closure:**
```
∀x, y ∈ A: x ⊕ y ∈ A
∀x, y ∈ A: x ⊗ y ∈ A
∀a ∈ ℝ, x ∈ A: a ⊙ x ∈ A
```

**Commutativity:**
```
x ⊕ y = y ⊕ x
x ⊗ y = y ⊗ x
```

**Associativity:**
```
(x ⊕ y) ⊕ z = x ⊕ (y ⊕ z)
(x ⊗ y) ⊗ z = x ⊗ (y ⊗ z)  (for nominals exactly)
```

**Monotonicity:**
```
If u₁ ≤ u₂, then:
  (n, u₁) ⊕ (m, v) ⪯ (n, u₂) ⊕ (m, v)
  (n, u₁) ⊗ (m, v) ⪯ (n, u₂) ⊗ (m, v)
```

### 5.2 Conservatism Bounds

**Addition vs Gaussian RSS:**
```
u_NU / u_RSS ∈ [1, √n]

Median ratio ≈ 1.74 (empirical)
```

**Multiplication vs Gaussian:**
```
u_NU / u_Gauss ≤ √2

Median ratio ≈ 1.001 (empirical)
```

**Interval Consistency (λ=1, n≥0):**
```
u_NU = u_interval

Max relative error < 0.014% (floating-point)
```

### 5.3 Observer Tensor Properties

**Invariant Conservation:**
```
M(n, u) = |n| + u

Preserved by C and B operators
```

**Epistemic Distance Decomposition:**
```
Δ_T² = ΔP_m² + Δ0_t² + Δ0_m² + Δ0_a²

Typical contribution:
  Δ0_a²: 72-87% (dominant)
  Δ0_t²: 27-34%
  ΔP_m², Δ0_m²: < 2%
```

---

## 6. Validation Statistics (70,000+ Test Cases)

**Addition Tests (8,000 cases):**
```
Ratio u_NU/u_RSS: [1.00, 3.54]
Median: 1.74
100% satisfy u_NU ≥ u_RSS
```

**Multiplication Tests (30,000 cases):**
```
Ratio u_NU/u_Gauss: [1.00, 1.41]
Median: 1.001
100% satisfy u_NU ≥ u_Gauss
```

**Interval Consistency (30,000 cases):**
```
Max relative error: 1.4 × 10⁻⁴
All within floating-point tolerance
```

**Chain Stability (3,200 cases):**
```
Lengths: {3, 5, 10, 20}
Max difference: 1.7 × 10⁻¹²
No error explosion
```

**Monte Carlo Comparison (24 cases):**
```
All cases: u_NU > σ_empirical
Minimum margin: 0.69
Maximum margin: 4.24
```

**Invariant Preservation (54 cases):**
```
Max error: 0.0 (exact)
Perfect conservation
```

---

## 7. Practical Formulas

### 7.1 Simple Operations

**Add two measurements:**
```
(10, 1) ⊕ (5, 0.5) = (15, 1.5)
```

**Multiply with uncertainty:**
```
(4.0, 0.1) ⊗ (3.0, 0.2) = (12.0, 1.1)
```

**Scale by constant:**
```
2.5 ⊙ (10, 1) = (25, 2.5)
```

### 7.2 Interval Bounds

**From N/U pair:**
```
(n, u) → [n - u, n + u]
```

**Check containment:**
```
I₁ ⊆ I₂ ⟺ L₂ ≤ L₁ AND U₁ ≤ U₂
```

### 7.3 Hubble Tension Application

**Given early and late measurements:**
```
H₀_early = (n_e, u_e)
H₀_late = (n_l, u_l)

Construct tensors:
T_early = (P_m,e, 0_t,e, 0_m,e, 0_a,e)
T_late = (P_m,l, 0_t,l, 0_m,l, 0_a,l)

Compute epistemic distance:
Δ_T = ||T_early - T_late||

Merge with expansion:
n_merged = (n_e + n_l) / 2
u_merged = (u_e + u_l) / 2 + (|n_e - n_l| / 2) × Δ_T

Test concordance:
[n_e - u_e, n_e + u_e] ⊆ [n_merged - u_merged, n_merged + u_merged]
[n_l - u_l, n_l + u_l] ⊆ [n_merged - u_merged, n_merged + u_merged]
```

---

## 8. Implementation Notes

### 8.1 Python Snippets

**N/U Class:**
```python
class NU:
    def __init__(self, n, u):
        self.n = float(n)
        self.u = max(0.0, float(u))
    
    def add(self, other):
        return NU(self.n + other.n, self.u + other.u)
    
    def mul(self, other):
        return NU(
            self.n * other.n,
            abs(self.n) * other.u + abs(other.n) * self.u
        )
```

**Observer Tensor:**
```python
class ObserverTensor:
    def __init__(self, P_m, zero_t, zero_m, zero_a):
        self.P_m = P_m
        self.zero_t = zero_t
        self.zero_m = zero_m
        self.zero_a = zero_a
    
    def distance(self, other):
        return math.sqrt(
            (self.P_m - other.P_m)**2 +
            (self.zero_t - other.zero_t)**2 +
            (self.zero_m - other.zero_m)**2 +
            (self.zero_a - other.zero_a)**2
        )
```

### 8.2 R Functions

**Basic Operations:**
```r
NU_add <- function(x, y) {
  c(n = x[1] + y[1], u = x[2] + y[2])
}

NU_mul <- function(x, y) {
  c(
    n = x[1] * y[1],
    u = abs(x[1]) * y[2] + abs(y[1]) * x[2]
  )
}
```

---

## 9. References and Sources

**N/U Algebra:**
- Martin, E.D. (2025). The NASA Paper & Small Falcon Algebra. DOI: 10.5281/zenodo.17172694
- Martin, E.D. (2025). Numerical Validation Dataset. DOI: 10.5281/zenodo.17221863

**Observer Domain Tensors:**
- Martin, E.D. (2025). Resolving the Hubble Tension via MC-Calibrated Observer Domain Tensors.

**UHA:**
- Martin, E.D. (2025). UHA Universal Horizon Address (Draft specification)

**Comparative Methods:**
- Moore, R.E. (1966). Interval Analysis.
- JCGM (2008). Guide to Expression of Uncertainty in Measurement.
- Ferson et al. (2003). Probability Boxes and Dempster-Shafer Structures.

---

## 10. Summary Table: All Key Formulas

| **Framework** | **Core Formula** | **Complexity** |
|---------------|------------------|----------------|
| N/U Addition | (n₁+n₂, u₁+u₂) | O(1) |
| N/U Multiplication | (n₁n₂, \|n₁\|u₂+\|n₂\|u₁) | O(1) |
| N/U Invariant | M = \|n\| + u | O(1) |
| Observer Tensor | T = (P_m, 0_t, 0_m, 0_a) | O(1) |
| Epistemic Distance | Δ_T = \\|T₁ - T₂\\| | O(1) |
| Domain Merge | u_merged = u_base + (Δn/2)×Δ_T | O(1) |
| UHA Encoding | ξ = (I+0.5)/2³ᴺ | O(N) |
| UHA Decoding | x⃗ = ξ×R_H(a)×û | O(1) |
| Cumulative Product | ∑ \|∏_{j≠i} nⱼ\|uᵢ | O(m) |
| Chain Complexity | O(m) total | Linear |

---

**Document Version:** 1.0  
**Last Updated:** 2025-10-12  
**Author:** Eric D. Martin  
**License:** CC BY 4.0

---

*All Your Baseline*