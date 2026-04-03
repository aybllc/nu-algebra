# Epistemic Layering and Conservative Formalization: A Methodological Framework for Building Verifiable Uncertainty Systems

**Eric D. Martin**  
ORCID: 0009-0006-5944-1742

## Abstract

We present a domain-agnostic methodological framework for formalizing reasoning under irreducible uncertainty. The framework enforces epistemic discipline by requiring explicit layer specification for all claims - from pure mathematical structure through domain application to human interpretation. We demonstrate the framework through a case study: the development of Nominal/Uncertainty (N/U) Algebra, a conservative uncertainty propagation system validated across 70,000 test cases. The key methodological contribution is not the specific algebra, but the systematic process by which informal reasoning patterns become formally verifiable structures. The framework addresses a practical problem: how to build formal systems that preserve uncertainty rather than prematurely collapse it, while maintaining auditability across specializations. We discuss the role of unexpected pattern sources, the distinction between inspiration and validation, and the recognition of research boundaries.

**Keywords:** epistemic methodology, uncertainty formalization, conservative systems, scientific reproducibility, formal verification

---

## 1. Introduction

### 1.1 The Core Problem

Scientific claims require different kinds of evidence depending on their epistemic status. A claim about mathematical structure needs proof. A claim about physical measurement needs empirical validation. A claim about human interpretation needs discourse and consensus. Mixing these categories creates confusion, irreproducibility, and controversy.

Yet most research operates across multiple epistemic layers simultaneously. A physicist makes measurements (layer 4), applies mathematical models (layers 1-2), interprets results in theoretical frameworks (layer 5), and stores findings for future reference (layer 6). Without explicit discipline about which layer each claim occupies, the entire chain becomes fragile.

This paper presents a framework for maintaining epistemic discipline: every artifact must declare its layer, reference only artifacts at or below its layer, and preserve its immutability once committed. The framework emerged from a practical need: building formal systems for reasoning under uncertainty that remain auditable when assumptions prove wrong.

### 1.2 Motivation Through Failure

This work began with attempts to formalize "nominal uncertainty" - the intuition that measurements have both a best-guess value and an explicit uncertainty bound. Early attempts failed because they mixed concerns:

- Mathematical operations at layer 1-2
- Physical interpretation at layer 3
- Computational encoding at layer 4  
- Informal justification at layer 5

Without explicit separation, the system contained contradictions. Operations that seemed reasonable at layer 5 (informal reasoning) violated closure at layer 1 (formal structure). The multiplication rule allowed negative uncertainties when nominal values were negative - a physical impossibility that emerged from insufficient mathematical rigor.

The framework emerged as a response to these failures: separate the layers explicitly, prove properties at the appropriate layer, and maintain immutability.

### 1.3 Case Study: N/U Algebra

We use N/U Algebra (Martin, 2025) as a worked example demonstrating the framework in practice. The algebra:

- Represents quantities as pairs (n, u) where n is nominal and u ≥ 0 is uncertainty
- Defines operations with proven closure, associativity, and monotonicity
- Provides conservative bounds validated across 70,000 numerical tests
- Published at DOI: 10.5281/zenodo.17221863

The algebra itself is not the contribution of this paper - the published mathematical work stands independently. What this paper contributes is the **methodology** by which the algebra was constructed, validated, and positioned within existing literature.

---

## 2. The Seven-Layer Framework

### 2.1 Layer Architecture

The framework stratifies knowledge into seven layers, each with distinct obligations:

**L0 - Epistemic Foundation (UN)**
- Explicit representation of "unknown" as typed value
- Not null, not zero, not missing - a formal placeholder
- Foundation: acknowledging ignorance before building knowledge

**L1 - Pure Mathematical Structure**  
- Logic systems, type theory, state spaces
- Domain-agnostic formal objects
- Immutable once chosen - all changes are conservative extensions

**L2 - Finite Precision Mathematics**
- Quantization, measurement limits, uncertainty as typed objects
- Precision profiles Ξ defining "how finely can we distinguish?"
- Refinement: increasing resolution without changing meaning

**L3 - Domain Application**
- Variables, roles (IV/DV/Control), relationships
- Still formal - no prose, no narrative
- Design operators as typed transformations

**L4 - Technical Infrastructure**
- Encoding, storage, transport, provenance
- Fidelity requirement: decode(encode(x)) = x at specified precision
- No silent coercion

**L5 - Human Discourse**
- Interpretation, peer review, governance decisions
- References must pin to exact L0-4 versions
- Append-only: supersede by addition, never edit committed artifacts

**L6 - Research Memory**
- Immutable provenance DAG
- Typed edges: derivesFrom, refines, contradicts, supersedes
- Branch-preserving: all paths remain visible

### 2.2 System Invariants

The framework enforces seven invariants across all layers:

**S1 - Monotone Knowledge Flow:** Claims at layer k derive only from artifacts at or below k.

**S2 - Conservative Extension:** Layers 0-2 evolve only via conservative extensions - previously valid theorems remain valid.

**S3 - Refinement:** Layers 3-4 evolve by increasing precision without altering denotations.

**S4 - Determinate Interfaces:** Every inter-layer interface specifies total functions or set-valued maps with explicit error structure.

**S5 - Version Pinning:** All cross-layer references pin exact semantic versions.

**S6 - Append-Only Evidence:** Layer 4 artifacts are never edited, only superseded.

**S7 - Provenance Preservation:** Identity, authorship, parameters are cryptographically bound and transitively carried forward.

### 2.3 Why Layering Matters

Different intellectual specializations work at different layers:

- Mathematicians/logicians: L0-2 (structure and precision)
- Domain scientists/engineers: L3-4 (application and encoding)  
- Communities/historians: L5-6 (interpretation and memory)

Without explicit layer discipline, cross-specialization collaboration fails. A mathematician proves associativity (L1), an engineer implements it (L4), but finds the implementation doesn't preserve the property due to floating-point precision (L2). Where did the failure occur? Without layer tracking, it's unclear.

The framework provides a shared language: "This property holds at L1 but requires additional constraints at L2 for numerical stability."

---

## 3. Case Study: Developing N/U Algebra

### 3.1 The Pattern Observation

The initial insight came from an unexpected source: reading Genesis and noticing a structural pattern in how states are described.

The text presents:
1. Void (undefined state)
2. Light (first defined state) 
3. Darkness (explicitly named as opposite of light)
4. Binary pairs following (day/night, water/land, etc.)

This maps structurally to:
- UN (undefined)
- 1 (first defined state)
- 0 (negation of 1)
- Binary operations following

**Critical distinction:** This is pattern recognition, not theological claim. Many ancient texts contain patterns that map to formal structures when extracted. The text's cultural significance is irrelevant to whether the pattern is mathematically useful.

### 3.2 Connection to Information Theory

Information theory (Shannon, 1948) establishes that information is created when distinguishing states. You cannot have "off" without first having "on" to distinguish it from. The first bit of information is the distinction itself.

The Genesis pattern - naming "light" before explicitly naming "darkness" - accidentally captures this ordering. Whether the authors intended this is unknowable and irrelevant. The pattern observation provided a template for exploration.

### 3.3 Formalization Process (Following Layer Discipline)

**Step 1: L0 Foundation**
- Define UN as typed unknown (not NULL)
- Establish resolution lattice R with UN as bottom element
- Prove refinement monotonicity

**Step 2: L1 Grounding**  
- Choose state space: A = ℝ × ℝ≥0
- Define carrier set formally
- No physical interpretation yet

**Step 3: L2 Precision**
- Define operations: ⊕, ⊗, ⊙
- Prove closure, associativity, commutativity
- Establish monotonicity properties
- Critical revision: add absolute values to ensure u ≥ 0 always

**Step 4: L3 Application**
- Map to physical quantities (nominal + uncertainty)
- Define uncertainty invariant M(n,u) = |n| + u
- Prove invariant preservation under transformations

**Step 5: L4 Implementation**
- Numerical validation across 70,000 test cases
- Comparison to Gaussian propagation, interval arithmetic, Monte Carlo
- Establish computational complexity: O(1) per operation
- Document reproducibility: fixed RNG seed, tolerance specifications

**Step 6: L5 Positioning**
- Comparative analysis against existing methods
- Acknowledgment of prior work (Kleene logic, interval arithmetic, uncertainty propagation)
- Clear statement of what's novel vs. what's established

**Step 7: L6 Publication**
- Zenodo deposit with DOI
- Complete code, data, validation scripts
- Immutable artifact with provenance

### 3.4 What Failed and Why

Initial versions violated closure because multiplication didn't use absolute values. This allowed:

(n₁, u₁) ⊗ (n₂, u₂) = (n₁n₂, n₁u₂ + n₂u₁)

When n₁ < 0, the uncertainty term could become negative, violating the codomain A = ℝ × ℝ≥0.

**The failure was at L1** (formal structure), but initially attributed to L3 (physical interpretation). Only by separating layers did the error become visible: the operation wasn't closed at the mathematical level, regardless of physical meaning.

**Fix:** Revise to (n₁n₂, |n₁|u₂ + |n₂|u₁), prove closure, regenerate all validation.

### 3.5 Validation Through Layer Compliance

Each layer required distinct validation:

**L1:** Formal proofs of closure, associativity, monotonicity  
**L2:** Numerical tests confirming properties hold within machine precision  
**L3:** Physical interpretation matching interval arithmetic for non-negative nominals  
**L4:** Reproducibility - same inputs, same outputs, documented configuration  
**L5:** Peer review would occur here (pre-print stage currently)  
**L6:** Permanent archive with immutable DOI

---

## 4. Philosophical Foundations

### 4.1 Structure as Epistemic Container

Personal insight that drove the work: formal boundaries prevent cognitive dissipation.

When reasoning is unbounded, mental energy disperses into speculation. Structure provides stable reference frames - not limiting thought, but channeling it productively. This is particularly relevant when working with mental illness that can distort reasoning patterns.

Formal rules enforce epistemic discipline externally when internal discipline is unreliable.

### 4.2 Inspiration vs. Validation

The Genesis observation provided **inspiration** but not **validation**. Many scientific advances follow this pattern:

- Kekulé: benzene structure from dream of snake eating its tail
- Newton: calculus while studying alchemy texts  
- Ramanujan: mathematical insights attributed to goddess Namagiri
- Poincaré: topological insights during unrelated activities

The source of inspiration doesn't determine validity. What matters:

1. Can the pattern be formalized? (L1-2)
2. Does it generate testable predictions? (L3-4)
3. Do those predictions hold under scrutiny? (Validation)

N/U Algebra is valid because of proofs and numerical validation, not because Genesis contains hidden mathematics. The text was useful scaffolding for thinking, then discarded once the formal structure stood independently.

### 4.3 Conservative by Design

UN propagates unless proven otherwise. Refinements require proof, not assumption. Uncertainty always ≥ 0. These aren't just philosophical stances - they're encoded in the type system.

This reflects epistemic humility: better to overestimate uncertainty than underestimate it, especially in safety-critical applications. The algebra makes this humility mathematically enforceable.

### 4.4 Recognizing Boundaries

The scalar formulation (n, u) is complete and validated. Extensions to tensors for multi-dimensional uncertainty are visible as future work but beyond current capability.

This recognition - "I can see where this leads but cannot execute it yet" - is methodologically sound. Mendel had inheritance ratios without chromosomes or DNA. The pattern was real; the full mechanism came later from others.

Claiming capability you don't have is intellectual dishonesty. Recognizing limitations is professional integrity.

---

## 5. Relationship to Existing Work

### 5.1 What Already Exists

Uncertainty propagation is extensively studied:

- **Kleene three-valued logic (1938):** {true, false, unknown}
- **Interval arithmetic (Moore, 1966):** Conservative bounds via intervals
- **Gaussian propagation (JCGM, 2008):** First-order linearization
- **Monte Carlo methods:** Sampling-based propagation
- **Probability boxes (Ferson et al., 2003):** Conservative probabilistic bounds

N/U Algebra is not claiming to have invented uncertainty propagation. It's a **specific formulation** with particular properties.

### 5.2 What's Novel in N/U Algebra

- **Explicit separation** of nominal and uncertainty at the type level
- **Absolute values** in multiplication rule ensuring closure
- **Formal proofs** of all algebraic properties  
- **Extensive validation** (70,000 test cases) against multiple methods
- **O(1) complexity** per operation
- **Complete reproducibility** with archived code/data

The contribution is the **specific combination** of properties, proven rigorously, not any single aspect.

### 5.3 What's Novel in This Paper

The methodology framework itself:

- Explicit layer discipline for epistemic claims
- Process for formalizing intuitions while maintaining rigor
- Recognition that inspiration sources (even unusual ones) are methodologically acceptable if validation is independent
- Framework for building audit-defensible formal systems

---

## 6. Framework Applicability Beyond N/U Algebra

### 6.1 General Pattern

The framework applies to any domain requiring:

1. Formal structure (mathematics, logic, type systems)
2. Measurement or application (physics, engineering, computation)
3. Human interpretation (theory, peer review, governance)

Examples:

- **Software verification:** Code (L4) must satisfy specifications (L3) derived from formal models (L1-2), reviewed by teams (L5), stored in version control (L6)

- **Clinical trials:** Protocols (L3) encode statistical designs (L2), generate data (L4), undergo peer review (L5), archived permanently (L6)

- **Machine learning:** Architectures (L3) implement mathematical optimization (L1-2), process data (L4), require interpretability (L5), need reproducibility (L6)

### 6.2 Where Framework Adds Value

- **Cross-specialization collaboration:** Clear language for "which layer is this claim about?"
- **Reproducibility:** L4-6 requirements enforce documentation
- **Error localization:** Failures can be traced to specific layer violations  
- **Conservative evolution:** S2-S3 prevent breaking existing systems

---

## 7. Limitations and Open Questions

### 7.1 What the Framework Doesn't Provide

- **Automated verification:** Still requires human judgment at L5
- **Domain guidance:** Framework is agnostic - doesn't tell you what to formalize
- **Quantitative metrics:** "Intellectual gravity" remains metaphorical
- **Scalability proof:** Unknown if framework scales to very large collaborative projects

### 7.2 Future Directions

**Tensor Formulation of N/U Algebra**

The scalar (n, u) formulation could extend to tensor representations:
- Uncertainty tensors capturing directional dependencies
- Covariance structure preservation
- Transformation rules under coordinate changes

This extension is visible but requires:
- Differential geometry expertise
- Covariance propagation theory
- New closure/associativity proofs
- High-dimensional validation

**Formalization of FIGMENT**

The "Framework for Intellectual Gravity Mapping" remains metaphorical. Operationalizing it requires:
- Quantitative metrics for epistemic position
- Empirical studies of knowledge transitions
- Validation across multiple domains

**Integration with Existing Frameworks**

- Mapping to OSI network model
- Alignment with FAIR principles
- Connection to proof assistant ecosystems (Coq, Lean)

---

## 8. Conclusion

We presented a domain-agnostic framework for maintaining epistemic discipline when building formal systems under uncertainty. The framework stratifies knowledge into seven layers, each with distinct validation requirements and evolution rules.

N/U Algebra demonstrates the framework in practice: an intuition from an unexpected source, formalized through explicit layer discipline, validated rigorously, and positioned honestly within existing literature. The algebra's validity comes from proofs and empirical validation, not from its inspiration source.

The key methodological insight: **structure enables rather than constrains**. Formal boundaries prevent epistemic dissipation by providing stable reference frames for reasoning. This is especially valuable when internal reasoning is unreliable due to cognitive limitations or mental health factors.

The framework doesn't claim to revolutionize science. It provides scaffolding for existing good practices, making implicit discipline explicit and enforceable. That's enough.

---

## References

[Complete bibliography from the N/U Algebra paper, plus additions for:]

- Shannon, C.E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379-423.

- Kekulé, A. (1865). *Bulletin de la Société Chimique de Paris*, 3, 98-110. [Historical reference for discovery via dream]

- Hardy, G.H. (1940). *Ramanujan: Twelve Lectures on Subjects Suggested by His Life and Work*. Cambridge University Press. [Reference for unconventional inspiration sources]

[Additional references for three-valued logic, epistemology, and formal methods as needed]

---

## Acknowledgments

To those who taught me what counting from zero truly means.

To the reviewers who correctly identified that "nominal uncertainty" wasn't particularly compelling - that honest critique led directly to the rigorous revision.

To the framework that provided structure when internal structure was unreliable.

---

## Data and Code Availability

N/U Algebra implementation, validation suite, and complete numerical results: [https://doi.org/10.5281/zenodo.17221863](https://doi.org/10.5281/zenodo.17221863)

Seven-Layer Framework specification and examples: [To be archived upon publication]
