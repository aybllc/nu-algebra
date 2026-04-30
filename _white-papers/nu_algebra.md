# N/U Algebra — Formula White Paper
**Author:** Eric D. Martin | ORCID: 0009-0006-5944-1742
**DOI:** 10.5281/zenodo.17172694
**Source repo:** /scratch/repos/nu-algebra/

---

## 1. Origin

N/U Algebra (Nominal/Uncertainty Algebra) is a closed, O(1) algebraic system for propagating bounded uncertainty through arithmetic chains. It was developed to satisfy three simultaneous constraints that no prior framework achieves: enclosure preservation, O(1) per-operation complexity, and deterministic bounds without probabilistic assumptions. The pair (n, u) encodes any measured quantity: n is the central (nominal) value and u is the nonnegative bound on deviation.

---

## 2. Carrier Set

```
A = ℝ × ℝ≥0
(n, u) where n ∈ ℝ, u ≥ 0
Interval representation: [n − u, n + u]
```

---

## 3. Primary Operations

### Addition (⊕)
```
(n₁, u₁) ⊕ (n₂, u₂) = (n₁ + n₂, u₁ + u₂)
```
- Commutative, associative
- Uncertainty is strictly additive (conservative — no correlation assumed)

### Subtraction
```
(n₁, u₁) − (n₂, u₂) = (n₁ − n₂, u₁ + u₂)
```
- Uncertainty adds regardless of direction

### Multiplication (⊗)
```
(n₁, u₁) ⊗ (n₂, u₂) = (n₁ · n₂, |n₁| · u₂ + |n₂| · u₁)
```
- First-order Taylor form — does NOT include u₁·u₂ quadratic term (by design)
- Commutative, associative
- Absolute values guarantee non-negative uncertainty output

### Scalar Multiplication (⊙)
```
a ⊙ (n, u) = (a · n, |a| · u)
```

### Affine Form
```
a ⊙ (n, u) + b = (a · n + b, |a| · u)
```

### Catch Operator (C)
```
C(n, u) = (0, |n| + u)
```
- Collapses nominal into uncertainty when sign is ambiguous or unknown
- Preserves invariant M

### Flip Operator (B)
```
B(n, u) = (u, |n|)
```
- Swaps rails; preserves M
- Note: B² ≠ id in general (not a true involution)

---

## 4. Key Invariants

### Epistemic Magnitude M
```
M(n, u) = |n| + u
```
- M ≥ 0 always
- M(C(n, u)) = M(n, u)  [Catch preserves M]
- M(B(n, u)) = M(n, u)  [Flip preserves M]
- M(x ⊕ y) ≤ M(x) + M(y)  [sub-additive]

### Enclosure Bounds
```
Lower: n − u
Upper: n + u
```

### Non-Negativity
```
∀ operations OP: u_out ≥ 0
```

### O(1) Complexity
```
All operations execute in a fixed number of floating-point steps,
independent of chain depth.
```

---

## 5. Cumulative Product (m operands, λ=0)
```
P = ⊗ᵢ₌₁ᵐ (nᵢ, uᵢ)

expressed: Nₘ = ∏ᵢ₌₁ᵐ nᵢ
bound:     Uₘ = Σᵢ₌₁ᵐ |∏ⱼ≠ᵢ nⱼ| · uᵢ
```

---

## 6. Validation Results

| Test | Cases | Finding |
|------|-------|---------|
| Addition vs Gaussian RSS | 8,000 | N/U ≥ RSS in 100% (ratio 1.00–3.54, median 1.74) |
| Multiplication vs Gaussian | 30,000 | Ratio 1.00–1.41, median ≈ 1.001 |
| Interval consistency | 30,000 | Within 0.014% floating-point error |
| Chain stability | 3,200 | Max drift ~10⁻¹² (no explosion) |
| Monte Carlo comparison | 24 | Bounds exceed empirical σ in 100% of cases |
| Invariant M preservation | 54 | Perfect (error: 0.0) |

---

## 7. Application

- Uncertainty propagation through any arithmetic chain
- Safe alternative to Gaussian RSS where independence cannot be assumed
- Compatible with U/N Algebra (see UN Algebra white paper)
- Certified by invariants test suite (18 passed, 0 failed): /scratch/repos/invariants/
