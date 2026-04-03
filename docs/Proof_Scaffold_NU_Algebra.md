# Proof Scaffold: N/U Algebra O(1) vs. Affine Arithmetic O(k)

## Proof Obligations

### 1. Complexity Definitions

**Computational Complexity Measure:**
- **n** = number of independent input variables
- **k** = size of uncertainty representation
- **m** = number of operations in computation chain

**N/U Representation:**
- Storage: Fixed 2-tuple (n, u)
- Size: k = 2 (constant)

**Affine Arithmetic Representation:**
- Storage: Central value + k noise symbols
- Size: k = 1 + (number of tracked sources)
- Grows with operation count

---

### 2. N/U Addition Complexity

**Operation:** (n₁, u₁) ⊕ (n₂, u₂) = (n₁+n₂, u₁+u₂)

**Proof:**
```
Time Complexity:
  - n_result = n₁ + n₂         [1 addition]
  - u_result = u₁ + u₂         [1 addition]
  Total: 2 arithmetic operations = O(1)

Space Complexity:
  - Input:  (n₁, u₁), (n₂, u₂)   [4 floats]
  - Output: (n_result, u_result)  [2 floats]
  Total: O(1) storage
```

**Result:** Addition is O(1) in both time and space.

---

### 3. N/U Multiplication Complexity

**Operation:** (n₁, u₁) ⊗ (n₂, u₂) = (n₁n₂, |n₁|u₂ + |n₂|u₁)

**Proof:**
```
Time Complexity:
  - n_result = n₁ × n₂                [1 multiplication]
  - term1 = |n₁| × u₂                 [1 abs, 1 mult]
  - term2 = |n₂| × u₁                 [1 abs, 1 mult]
  - u_result = term1 + term2          [1 addition]
  Total: 6 operations = O(1)

Space Complexity:
  - Same as addition: O(1)
```

**Result:** Multiplication is O(1) in both time and space.

---

### 4. Affine Arithmetic Addition Complexity

**Representation:** x = x₀ + Σᵢ xᵢεᵢ (k noise symbols)

**Operation:** z = x + y

**Proof:**
```
Time Complexity:
  - z₀ = x₀ + y₀                      [1 addition]
  - For each noise symbol εᵢ:
      zᵢ = xᵢ + yᵢ                    [k additions]
  Total: 1 + k operations = O(k)

Space Complexity:
  - Input:  x₀ + k terms, y₀ + k terms
  - Output: z₀ + k terms
  - Must track all k noise symbols
  Total: O(k) storage
```

**Result:** Affine addition is O(k) in both time and space.

---

### 5. Affine Arithmetic Multiplication Complexity

**Operation:** z = x × y

**Proof:**
```
Time Complexity:
  - z₀ = x₀ × y₀                      [1 multiplication]
  - For each noise symbol εᵖ:
      zₚ = x₀yₚ + y₀xₚ                [2k multiplications, k additions]
  - Nonlinear terms: Σᵢⱼ xᵢyⱼεᵢεⱼ
      Create new noise symbol εₙₑw
      Apply Chebyshev approximation    [O(k²) worst case]
  Total: O(k²) operations

Space Complexity:
  - New noise symbols may be created
  - Representation grows: k → k+1
  Total: O(k) storage, grows over time
```

**Result:** Affine multiplication is O(k²) time, O(k) space (with growth).

---

### 6. Chain Composition Comparison

**Problem:** Compute z = f(x₁, x₂, ..., xₙ) with m operations

**N/U Algebra:**
```
For m operations:
  - Each operation: O(1)
  - Total: m × O(1) = O(m)
  - Representation size: Always 2 floats

Space growth: None (constant)
```

**Affine Arithmetic:**
```
For m operations:
  - Best case (additions only): O(m × k)
  - Worst case (multiplications): O(m × k²)
  - Representation size: k grows with m

Space growth: Linear in m
```

---

### 7. Formal Complexity Theorem

**Theorem (N/U O(1) Operations):**
```
Let OP ∈ {⊕, ⊗, ⊙} be an N/U operation.
For any inputs (n₁, u₁), (n₂, u₂):
  
  Time(OP) = O(1)
  Space(OP) = O(1)
  
Proof:
  1. All operations use fixed number of arithmetic operations
  2. No data structure growth
  3. No iterative loops over k
  □
```

**Theorem (Affine O(k) Operations):**
```
Let OP be an affine operation on k noise symbols.
For any inputs x, y with k noise terms:
  
  Time(OP) = O(k) for addition
  Time(OP) = O(k²) for multiplication
  Space(OP) = O(k) with potential growth
  
Proof:
  1. Must process all k noise symbols
  2. Multiplication creates new terms
  3. Representation may grow
  □
```

---

### 8. Trade-Off Analysis

**Why N/U is O(1):**
- Uses absolute values: |n₁|u₂ + |n₂|u₁
- This *discards correlation information*
- Result: Conservative bound, no tracking needed

**Why Affine is O(k):**
- Tracks exact correlation via noise symbols
- Preserves dependency information
- Result: Tighter bounds, higher complexity

**Key Insight:**
```
N/U trades precision for speed:
  - Precision: Affine ≥ N/U (tighter bounds)
  - Speed: N/U >> Affine (O(1) vs O(k))
```

---

### 9. Experimental Validation

**Test Setup:**
- Chain of m multiplications
- Measure: Time per operation, memory usage
- Compare: N/U vs Affine Arithmetic

**Expected Results:**
```
              N/U        Affine
m=10         O(1)       O(k) ≈ O(10)
m=100        O(1)       O(k) ≈ O(100)
m=1000       O(1)       O(k) ≈ O(1000)

Memory:
m=10         2 floats   ~10 floats
m=100        2 floats   ~100 floats
m=1000       2 floats   ~1000 floats
```

---

### 10. Formal Asymptotic Bounds

**N/U Algebra:**
```
For any chain of m operations:
  
  Time:  T_NU(m) = O(m)        [m operations × O(1) each]
  Space: S_NU(m) = O(1)        [constant representation]
```

**Affine Arithmetic:**
```
For a chain of m operations:
  
  Time:  T_AA(m) = O(m × k)    [additions]
         T_AA(m) = O(m × k²)   [multiplications]
  
  Space: S_AA(m) = O(k)        [k grows with m]
         k = O(m) worst case
```

**Asymptotic Comparison:**
```
lim(m→∞) T_NU(m) / T_AA(m) = O(1/k) → 0
  
N/U is asymptotically faster by factor of k.
```

---

## Proof Verification Checklist

- [ ] Definition of complexity measure (time/space)
- [ ] N/U operations shown to be O(1)
- [ ] Affine operations shown to be O(k)
- [ ] Chain composition analyzed
- [ ] Trade-off (precision vs. speed) explained
- [ ] Experimental validation proposed
- [ ] Asymptotic bounds formalized
- [ ] Correlation handling addressed

---

## Implementation Test

**Code to verify O(1) claim:**

```python
import time
import numpy as np
from nu_algebra import NU

def benchmark_nu(m):
    """Chain of m multiplications"""
    start = time.time()
    result = NU(1.5, 0.1)
    for _ in range(m):
        result = result.mul(NU(1.5, 0.1))
    return time.time() - start

# Test
for m in [10, 100, 1000, 10000]:
    t = benchmark_nu(m)
    print(f"m={m}: {t:.6f}s, {t/m:.9f}s per op")
```

**Expected:** Time per operation stays constant as m increases.

---

## Next Steps

1. Run benchmark comparing N/U vs. Affine Arithmetic
2. Plot time/space complexity as function of m
3. Document trade-off quantitatively
4. Add to validation suite (tests/)

**Where to place proof:**
- `docs/theoretical_foundation.md` (Section: Complexity Analysis)
- `tests/test_complexity.py` (Benchmark suite)
