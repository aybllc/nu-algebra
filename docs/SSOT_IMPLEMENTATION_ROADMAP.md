# SSOT v3.0 Implementation Roadmap
## Actionable Checklist for Cross-Document Consistency
**Updated: March 21, 2026**

---

## PHASE 0: IMMEDIATE (This Week) — 3 CRITICAL Issues

### ✅ Task 0.1: Resolve Flip Operator Contradiction (F-002)
**Status:** BLOCKING formal verification credibility
**Time:** 2-4 hours

**Actions:**
- [ ] Replace `FlipInvolutive.lean` with `FlipIdempotent.lean`
- [ ] Update theorem statement: `B³ = B²` (not `B² = id`)
- [ ] Update NUProof README line 33-35 to list as "Complete"
- [ ] Regenerate proof_manifest.json with new hash
- [ ] Update proof status count from 3 complete to 3 complete (no change in count)
- [ ] Add test_flip_not_involutive and test_flip_idempotent to test suite
- [ ] Update o1 Outline Section 2.2, Definition 5 to note B is NOT involutive
- [ ] Verify NASA Paper Section 3.2 note on B³=B² is present

**Cross-checks:**
- NUProof README should show "FlipIdempotent.lean" instead of "FlipInvolutive.lean"
- Lean build should pass with `lake build` (no sorry in complete proofs)
- GitHub Actions CI should green

**Owner:** NUProof maintainer
**Depends On:** None
**Blocks:** F-031 (test coverage), F-008 (operator usage)

---

### ✅ Task 0.2: Create 4 Missing eBIOS Layer Specifications (F-038)
**Status:** BLOCKING all external implementation
**Time:** 1-2 weeks (can parallelize)

**Actions:**

**Part 0.2a: NULedger_SPEC.md**
- [ ] Document Ledger class interface (append, query, verify_merkle_root, verify_signature)
- [ ] Define append(operation: str, inputs: List[NUPair], output: NUPair) → entry_id
- [ ] Define query(operation: str, limit: int, before: Optional[timestamp]) → List[entry]
- [ ] Define verify_merkle_root() → bool
- [ ] Document Merkle tree algorithm (SHA-256, binary tree structure)
- [ ] Document entry serialization format (JSON or protobuf?)
- [ ] Provide code example: creating ledger, appending operation, verifying integrity
- [ ] Note performance: "append O(log n) < 1ms, query O(k) < 5ms"

**Part 0.2b: NUGuard_POLICY.md**
- [ ] Document Monitor class interface (check, validate, enable_event_escalation)
- [ ] Define check(rule_type: str, operands: List[NUPair], result: NUPair) → bool
- [ ] Document rule evaluation for: non_negativity, enclosure_preservation, threshold
- [ ] Define event types: PASS, WARN, VIOLATION
- [ ] Document escalation levels: LOG, ALERT, FAIL_OPERATION
- [ ] Provide code example: creating monitor, checking operations
- [ ] Note performance: "check O(r) < 100μs for r=5 rules"

**Part 0.2c: NUPolicy_SPEC.md**
- [ ] Create JSON schema for policy files (with $schema reference)
- [ ] Define required fields: version, name, rules[], audit_level
- [ ] Document rule types:
  - non_negativity: {type: "non_negativity", enabled: bool}
  - enclosure_preservation: {type: "enclosure", enabled: bool}
  - coverage_allocation: {type: "coverage_allocation", method: "bonferroni"|"independence", alpha: float}
  - threshold: {type: "threshold", max_u: float}
- [ ] Document audit levels: silent, verbose, full
- [ ] Document policy signing (Ed25519 private key signing)
- [ ] Provide code example: loading policy, applying rules
- [ ] Include 3 example policies: conservative.json, strict.json, permissive.json

**Part 0.2d: NUGovern_API.md**
- [ ] Document base URL: `http://localhost:8000` (or configurable?)
- [ ] Document authentication: (None? Bearer token? mTLS?)
- [ ] Document 5+ endpoints:
  - POST /operations/execute: {operation, inputs} → {result, entry_id}
  - POST /coverage/validate: {inputs, per_input_coverage, method} → {valid, message}
  - GET /ledger/query: {operation, limit, before} → {entries}
  - POST /ledger/verify: {} → {valid, merkle_root}
  - GET /health: {} → {status, version}
- [ ] Document error responses: {error, code, message}
- [ ] Document rate limits: (requests/sec? per IP?)
- [ ] Document timeout: (default 30s?)
- [ ] Provide curl examples for each endpoint
- [ ] Include Python/JavaScript client library usage examples

**Cross-checks:**
- All 4 spec files should be in `/docs/` directory
- Each spec should have markdown format with code examples
- Each spec should reference other layers where applicable
- Quick Start should link to these specs

**Owner:** eBIOS maintainer
**Depends On:** None
**Blocks:** F-033, F-035, F-039, F-044

---

### ✅ Task 0.3: Define Layer 0 Interface (F-041)
**Status:** BLOCKING formal Layer 0 specification
**Time:** 4-6 hours

**Actions:**
- [ ] Create Layer0_SPEC.md
- [ ] Define 4 functions with full signatures:
  - Verify(data: bytes, signature: bytes, public_key: bytes) → bool
  - Seal(data: bytes, private_key: bytes) → bytes (signature)
  - Unseal(sealed: bytes) → Tuple[bytes, bytes, Dict[str, Any]]
  - Attest(claim: str, evidence: bytes, witness: str) → Dict[str, Any]
- [ ] Document cryptographic primitives used: Ed25519, SHA-256
- [ ] Document expected error cases and exceptions
- [ ] Provide Python implementation example
- [ ] Link to Layer 1-6 usage of these primitives
- [ ] Explain immutability guarantees enforced by Layer 0

**Cross-checks:**
- Layer0_SPEC.md should exist in `/docs/`
- eBIOS README should reference Layer0_SPEC.md
- NUProof should document how Layer 0 primitives are used for proof attestation

**Owner:** eBIOS architect
**Depends On:** Task 0.2d (API spec for context)
**Blocks:** F-032 (layer clarity)

---

## PHASE 1: HIGH PRIORITY (Weeks 2-3) — 7 HIGH Issues

### ✅ Task 1.1: Complete Enclosure Preservation Proof (F-003)
**Status:** BLOCKING PAC coverage theorem verification
**Time:** 2-3 days

**Actions:**
- [ ] Replace sorry placeholders in Enclosure.lean
- [ ] Implement add_enclosure proof (addition preserves enclosure)
- [ ] Implement scalar_enclosure proof (scalar multiplication preserves enclosure)
- [ ] Implement mul_enclosure proof (multiplication preserves enclosure)
  - [ ] Decompose x·y = n₁n₂ + n₁(y-n₂) + n₂(x-n₁) + (x-n₁)(y-n₂)
  - [ ] Bound each term using abs_le from Mathlib
  - [ ] Combine bounds using linarith
- [ ] Run `lake build` to verify no sorry remains
- [ ] Regenerate proof_manifest.json with new hash
- [ ] Update NUProof README lines 19-20 status to "Complete"
- [ ] Update proof status count (still 3 complete, just Enclosure now instead of placeholder)

**Cross-checks:**
- `lake build` should succeed with no warnings
- Proof should type-check in Lean kernel
- proof_manifest.json should show "status": "complete"

**Owner:** NUProof maintainer
**Depends On:** Task 0.1 (establish proof discipline)
**Blocks:** F-004 (coverage enforcement depends on verified enclosure)

---

### ✅ Task 1.2: Add Coverage Allocation to eBIOS Policy (F-004)
**Status:** BLOCKING runtime enforcement of PAC guarantees
**Time:** 2 days

**Actions:**
- [ ] Add coverage_allocation rule type to NUPolicy_SPEC.md
- [ ] Document rule structure:
  ```json
  {
    "type": "coverage_allocation",
    "method": "bonferroni" | "independence",
    "alpha": 0.05,
    "per_input_coverage": [0.975, 0.975, 0.975, ...]
  }
  ```
- [ ] Add check_coverage_allocation method to NUGuard_POLICY.md
  - Input: number of inputs n, desired system coverage α
  - Output: required per-input coverage (either bonferroni or independence)
  - Validation: verify configured per-input coverage ≥ required coverage
- [ ] Add POST /coverage/validate endpoint to NUGovern_API.md
  - Input: {inputs: int, system_alpha: float, method: string}
  - Output: {required_per_input_coverage: float, valid: bool}
- [ ] Update o1 Outline Section 4.4 with implementation note:
  ```
  Corollary 3 (Independence Calibration):
  If inputs independent, use per-input coverage = (1-α)^(1/n).
  This is implemented in eBIOS NUPolicy with method: "independence"
  and enforced at runtime by NUGuard.check_coverage_allocation().
  ```

**Cross-checks:**
- NUPolicy_SPEC.md should have coverage_allocation rule type
- NUGuard_POLICY.md should have check_coverage_allocation implementation
- NUGovern_API.md should have /coverage/validate endpoint
- o1 Outline should reference eBIOS implementation

**Owner:** eBIOS + o1 maintainers (coordinate)
**Depends On:** Task 0.2c, 0.2d (spec templates)
**Blocks:** None (enhances but not critical)

---

### ✅ Task 1.3: Clarify Multiplication Formula Definition (F-001)
**Status:** BLOCKING formula consistency across all documents
**Time:** 1 day

**Actions:**
- [ ] Update o1 Outline Section 2.2, Definition 3:
  ```
  ADD AFTER multiplication rule:
  "Note: This algebra supports a safety margin parameter λ ≥ 1.
   When λ = 0, this recovers the first-order approximation (no u₁u₂ cross-term)
   used in the NASA paper. When λ = 1, this equals exact interval arithmetic.
   The published validation dataset (Zenodo 10.5281/zenodo.17221863) uses λ = 0."
  ```
- [ ] Update o1 Outline Section 5.1, Theorem 10:
  ```
  REWRITE:
  "Interval Consistency: For λ = 1 and nonnegative nominals, N/U multiplication
   with cross-term (|n₁|u₂ + |n₂|u₁ + u₁u₂) matches exact interval arithmetic.
   For λ = 0 (first-order), this matches the NASA paper's formula."
  ```
- [ ] Update NASA Paper Section 3.1 if revising:
  ```
  ADD NOTE:
  "The multiplication rule (n₁n₂, |n₁|u₂ + |n₂|u₁) is the first-order
   approximation, dropping the u₁u₂ cross-term. This is valid when u << n
   (relative uncertainty < 100%). For higher relative uncertainties,
   see the N/U outline's λ-parameterized version with cross-term."
  ```

**Cross-checks:**
- o1 Definition 3 should mention both λ=0 and λ=1 cases
- o1 Theorem 10 should clarify interval equivalence
- NASA Paper should note first-order approximation explicitly
- Validation dataset (Zenodo) should use consistent formula

**Owner:** Paper authors
**Depends On:** None
**Blocks:** F-020 (validation dataset), F-028 (DOI matching)

---

### ✅ Task 1.4: Resolve Layer 7 Reference Confusion (F-032, F-042)
**Status:** BLOCKING architectural clarity
**Time:** 4 hours

**Actions:**
- [ ] Update NUProof README lines 119-136:
  ```
  REPLACE:
  "Layer 7 (Certification): Proof status included in compliance reports"
  
  WITH:
  "Layer 2 Attestation: NUProof generates cryptographic attestations of proof completion.
   These attestations are:
   - Logged in Layer 3 (NULedger) Merkle chain for immutability
   - Reported by Layer 6 (NUGovern) in API compliance responses
   - Used by Layer 5 (NUPolicy) to enforce proof verification requirements"
  ```
- [ ] Update eBIOS README architecture diagram to confirm 6 layers (0-6) or document Layer 7 if planned
- [ ] Clarify: is "Certification" an output property (not a layer) or a future Layer 7?
  - If output: update documentation to say "Proof attestations feed into compliance reporting"
  - If Layer 7: create Layer7_SPEC.md for certification system

**Cross-checks:**
- eBIOS README architecture should list all layers consistently
- NUProof README should not reference non-existent layers
- All layer references should be bidirectional (Layer X mentions Layer Y, and vice versa)

**Owner:** eBIOS architect
**Depends On:** Task 0.2 (clarify layer responsibilities)
**Blocks:** F-032 (clarity)

---

### ✅ Task 1.5: Update Project URLs for Consistency (F-022)
**Status:** BLOCKING correct citation and linking
**Time:** 2 hours

**Actions:**
- [ ] Decide on canonical GitHub organization and repository names
  - Option A: `github.com/abba-01/nualgebra` (o1 outline, CHANGELOG.md prefer this)
  - Option B: `github.com/aybllc/nu-algebra` (CITATION.cff, .zenodo.json prefer this)
  - Recommendation: Consolidate to Option A (`abba-01` GitHub org)
- [ ] Update 4 files to use canonical URL:
  - [ ] setup.py: url='https://github.com/abba-01/nualgebra'
  - [ ] CITATION.cff: url: 'https://github.com/abba-01/nualgebra'
  - [ ] .zenodo.json: related_identifiers with canonical URL
  - [ ] CHANGELOG.md: all links → canonical URL
  - [ ] README.md: repository reference → canonical URL
- [ ] Verify Zenodo DOI resolves to correct repo
- [ ] Create redirect from alternate URL to canonical URL (if applicable)

**Cross-checks:**
- All 5 files should reference same URL
- Zenodo DOI should resolve to canonical repo
- GitHub repo should be accessible at canonical URL

**Owner:** Repo maintainer
**Depends On:** None
**Blocks:** None (but affects citation accuracy)

---

## PHASE 2: MEDIUM PRIORITY (Weeks 3-4) — 16 MEDIUM Issues

### ✅ Task 2.1: Create Example Policy Files (F-036, F-044)
**Status:** BLOCKING user ability to run Quick Start examples
**Time:** 1 day

**Actions:**
- [ ] Create `policies/conservative.json`:
  ```json
  {
    "version": "1.0",
    "name": "conservative",
    "description": "Strict policy for safety-critical systems. All checks enabled.",
    "rules": [
      {
        "type": "non_negativity",
        "enabled": true,
        "severity": "FAIL"
      },
      {
        "type": "enclosure_preservation",
        "enabled": true,
        "severity": "FAIL"
      },
      {
        "type": "coverage_allocation",
        "method": "bonferroni",
        "alpha": 0.01,
        "severity": "WARN"
      },
      {
        "type": "threshold",
        "max_u": 1.0,
        "severity": "WARN"
      }
    ],
    "audit_level": "full",
    "ledger_writes": "synchronous"
  }
  ```
- [ ] Create `policies/strict.json`:
  ```json
  {
    "version": "1.0",
    "name": "strict",
    "description": "Strict coverage requirements.",
    "rules": [
      {
        "type": "coverage_allocation",
        "method": "independence",
        "alpha": 0.001,
        "severity": "FAIL"
      }
    ],
    "audit_level": "verbose"
  }
  ```
- [ ] Create `policies/permissive.json`:
  ```json
  {
    "version": "1.0",
    "name": "permissive",
    "description": "Performance-focused. Minimal overhead.",
    "rules": [
      {
        "type": "non_negativity",
        "enabled": true,
        "severity": "LOG"
      }
    ],
    "audit_level": "silent",
    "ledger_writes": "asynchronous"
  }
  ```
- [ ] Create JSON schema at `policies/policy_schema.json`
- [ ] Update eBIOS README Quick Start line 96 with path:
  ```python
  # Policies are in ./policies/ directory
  policy = manager.load_policy("conservative")
  ```
- [ ] Add note to README: "Example policies are provided in policies/"

**Cross-checks:**
- All 3 policy files should be valid JSON
- Files should be in `policies/` directory at repo root
- Quick Start should succeed without modification

**Owner:** eBIOS maintainer
**Depends On:** Task 0.2c (NUPolicy_SPEC.md for schema definition)
**Blocks:** None (makes Quick Start work)

---

### ✅ Task 2.2: Expand Quick Start Examples (F-034, F-039)
**Status:** IMPROVING usability
**Time:** 1 day

**Actions:**
- [ ] Add imports to NUPolicy example:
  ```python
  from src.nupolicy import PolicyManager, PolicyNotFoundError
  from src.nuledger import Ledger
  ```
- [ ] Add error handling:
  ```python
  try:
      policy = manager.load_policy("conservative")
  except PolicyNotFoundError:
      print("Error: conservative policy not found in ./policies/")
      policy = manager.create_default_policy()
  ```
- [ ] Add NULedger example after NUPolicy:
  ```python
  #### NULedger (Direct)

  from src.nuledger import Ledger

  # Create ledger
  ledger = Ledger(storage="./ledger.db")

  # Append operation
  entry_id = ledger.append("mul", [(10.0, 0.5), (20.0, 1.0)], (200.0, 10.5))

  # Query ledger
  entries = ledger.query(operation="mul", limit=10)

  # Verify integrity
  assert ledger.verify_merkle_root()
  print(f"Ledger integrity verified. {len(entries)} entries found.")
  ```

**Cross-checks:**
- All examples should run without errors
- Each example should have imports and error handling
- All 4 layers covered: NUCore, NUGovern, NUPolicy, NULedger

**Owner:** eBIOS maintainer
**Depends On:** Task 0.2 (spec completion)
**Blocks:** None (improves UX)

---

### ✅ Task 2.3: Document Development Phases (F-037)
**Status:** IMPROVING project clarity
**Time:** 2 hours

**Actions:**
- [ ] Create `PHASES.md` documenting project lifecycle:
  ```
  # eBIOS Development Phases

  ## Phase 0: Architecture & Specification
  - Design 7-layer architecture
  - Create specification documents
  - Define mathematical invariants
  Status: ✅ Complete (2025-09)

  ## Phase 1: NUCore Implementation
  - Implement N/U algebra operations
  - Achieve O(1) per-operation performance
  - Build Python + R implementations
  Status: ✅ Complete (2025-10)

  ## Phase 2: NUProof (Formal Verification)
  - Create Lean 4 proofs for mathematical properties
  - Set up proof hash attestation
  - Add CI pipeline for proof verification
  Status: ⏳ In Progress (target 2026-04)

  ... (continue through Phase 6)

  ## Phase 7: Production Hardening (Planned)
  - Performance optimization
  - Load testing and benchmarking
  - Security audit and certification

  ## Phase 8: Compliance & Certification (Planned)
  - FDA/NIST certification for safety-critical systems
  - Formal standards alignment
  ```
- [ ] Update eBIOS README footer to reference PHASES.md

**Cross-checks:**
- PHASES.md should align with README "Development (Phases 0-6 complete)"
- Each phase should have clear deliverables and status
- Phase timeline should be realistic

**Owner:** Project manager
**Depends On:** None
**Blocks:** None (documentation only)

---

### ✅ Task 2.4: Fix Example Formula Result (F-005, F-021)
**Status:** CORRECTING documentation errors
**Time:** 30 minutes

**Actions:**
- [ ] Update eBIOS README line 72:
  ```python
  # CHANGE FROM:
  # Result: (30.0, 1.12)
  
  # CHANGE TO:
  # Result: (30.0, 1.5)
  ```
- [ ] Verify NUCore implementation uses u₁+u₂ (not √(u₁²+u₂²)):
  ```python
  def add(self, other):
      return NU(self.n + other.n, self.u + other.u)  # Correct
  ```
- [ ] If implementation uses RSS, fix it and update comment
- [ ] Add note explaining conservatism:
  ```python
  # N/U addition is conservative: adds uncertainties linearly (u₁+u₂)
  # This is stricter than Gaussian RSS (√(u₁²+u₂²)) but still realistic
  ```

**Cross-checks:**
- add(10.0, 0.5, 20.0, 1.0) should return exactly (30.0, 1.5)
- Comment should explain why u₁+u₂ is conservative but not excessive

**Owner:** eBIOS maintainer
**Depends On:** None
**Blocks:** None (fixes existing code)

---

### ✅ Task 2.5: Update Performance Table with Hardware Details (F-040)
**Status:** IMPROVING measurement credibility
**Time:** 2 hours

**Actions:**
- [ ] Measure NUCore operations on reference hardware:
  ```python
  import timeit
  import platform
  
  # Measure add operation
  setup = "from src.nucore import add"
  time_ns = timeit.timeit("add((10.0, 0.5), (20.0, 1.0))", setup=setup, number=1000000)
  time_us = time_ns / 1000 / 1000
  
  print(f"add() average: {time_us:.3f}µs")
  print(f"CPU: {platform.processor()}")
  ```
- [ ] Update eBIOS README performance table:
  ```
  | NUCore operations | O(1) | < 1µs p50 |
  |                   |      | Hardware: Intel i7-13700K, 32GB RAM |
  |                   |      | Compiler: Python 3.11 (no Cython) |
  |                   |      | Method: timeit, 1M iterations |
  
  | Ledger append | O(log n) | < 1ms p50 |
  |              |          | Hardware: NVMe SSD (Samsung 990 Pro) |
  |              |          | Method: perf_counter, measured on n=1000 entries |
  ```
- [ ] Add footnote explaining measurement methodology

**Cross-checks:**
- Performance numbers should be measured and reproducible
- Hardware should be documented
- Compiler and optimization flags should be noted

**Owner:** Performance engineer
**Depends On:** Access to reference hardware
**Blocks:** None (improves documentation)

---

### ✅ Task 2.6: Update Version and Date (F-045)
**Status:** MAINTAINING accuracy
**Time:** 15 minutes

**Actions:**
- [ ] Update eBIOS README footer:
  ```markdown
  ## Version

  - **eBIOS Version**: 0.2.0 (updated from 0.1.0)
  - **Status**: Development (Phases 0-2 complete, Phase 3 in progress)
  - **Last Updated**: 2026-03-21 (from 2025-10-20)
  ```
- [ ] Add CHANGELOG entry for v0.2.0:
  ```markdown
  ## v0.2.0 (2026-03-21)
  - Added: NULedger, NUGuard, NUPolicy, NUGovern specifications
  - Added: Layer 0 (Verify/Seal/Unseal/Attest) interface definition
  - Fixed: Layer 7 reference removed (architecture clarified)
  - Improved: Quick Start examples with error handling
  - Improved: Performance table with hardware details
  ```

**Cross-checks:**
- Version should be consistent across files (README, setup.py, etc.)
- Last-updated date should match current date
- CHANGELOG should document what changed since last version

**Owner:** Repo maintainer
**Depends On:** All other tasks in this phase
**Blocks:** None (final step of phase)

---

## PHASE 3: LOWER PRIORITY (Weeks 4-6) — 15 LOW Issues

[Remaining findings F-005-F-030 plus new LOW findings F-034, F-037, F-043, F-045]

**Recommended actions for these items:**
- Link test files in README (F-035)
- Clarify latency vs throughput measurements (F-043)
- Document division operator if implemented (F-008)
- Add other missing proofs (F-009, F-011, F-012, etc.)

---

## COMPLETION CHECKLIST

### After PHASE 0 (This Week):
- [ ] Flip operator contradiction resolved
- [ ] 4 layer specifications created
- [ ] Layer 0 interface defined
- [ ] 3 CRITICAL issues resolved ✓

### After PHASE 1 (Weeks 2-3):
- [ ] Enclosure proof completed
- [ ] Coverage allocation implemented
- [ ] Multiplication formula clarified
- [ ] Layer architecture consistent
- [ ] GitHub URLs unified
- [ ] 7 HIGH issues resolved ✓
- [ ] Total: 3 CRITICAL + 7 HIGH ✓

### After PHASE 2 (Weeks 3-4):
- [ ] Policy files created
- [ ] Quick Start examples improved
- [ ] Development phases documented
- [ ] Documentation errors fixed
- [ ] Performance table enhanced
- [ ] Version updated
- [ ] 16 MEDIUM issues resolved ✓
- [ ] Total: 3 CRITICAL + 7 HIGH + 16 MEDIUM ✓

### After PHASE 3 (Weeks 4-6):
- [ ] 15 LOW issues addressed
- [ ] 45 total findings resolved
- [ ] All edit locations completed
- [ ] Cross-document consistency verified
- [ ] **SSOT v3.0 COMPLETE** ✓

---

## Timeline Summary

| Phase | Priority | Issues | Timeline | Owner |
|-------|----------|--------|----------|-------|
| 0 | CRITICAL | 3 | This week | NUProof + eBIOS lead |
| 1 | HIGH | 7 | Weeks 2-3 | Paper + eBIOS authors |
| 2 | MEDIUM | 16 | Weeks 3-4 | eBIOS maintainer |
| 3 | LOW | 15 | Weeks 4-6 | Various |
| **Total** | | **45** | **6 weeks** | |

**Estimated effort:** 80-120 hours across team

---

*Generated by SSOT v3.0 Implementation Roadmap*
*For questions, refer to SSOT_NU_Algebra_UPDATED_v3_0.docx*
