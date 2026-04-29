# The Carrier-Stripping Lemma: Observability and the Bound Rail

**Author:** Eric D. Martin
**ORCID:** 0009-0006-5944-1742
**Affiliation:** Independent researcher
**Date:** 2026-04-28 (working draft v0.2 from session conversation; v0.1 superseded)
**Status:** DRAFT v0.2 — captured from spoken-language formulation; sharpened by independent-instance audit; not yet a finished manuscript. To be developed when bandwidth permits.

> *Definitional exactness is not observational exactness. EB begins where formal objects enter the world.*

> *EB is not a theory of uncertainty. It is a theory of how certainty is accessed.*

---

## Provenance note

This draft was generated 2026-04-28 ~21:30 PDT during a working conversation. Eric articulated the universality claim in plain language ("there is nothing in the universe that doesn't operate under the principle"; "it can be more than equal and still equal"; "even quantum physics obeys the carrier"). Mae structured the argument. The substance — the EB carrier itself, the carrier-set theorem (RSOS-260797 r4), the universality claim, and the plain-language framings — is Eric's. Mae provided organizational form during the session.

Per `feedback_no_coauthor.md` and the standing project authorship rules, this paper is sole-author Eric D. Martin.

---

## Abstract

The EB carrier — the set $A = \mathbb{R} \times \mathbb{R}_{\geq 0}$ of ordered pairs $(e, b)$ where $e$ is the expressed value and $b$ is a non-negative bound — is shown by the carrier-set theorem (Martin 2026, RSOS-260797 r4) to be the unique algebraic structure satisfying six axioms (A1–A6) including operation-level closure, associativity, commutativity, identity, monotonicity, and constant-time stateless propagation. We argue here that this uniqueness result is not a methodological convenience for uncertainty propagation but a structural floor on physical possibility: every observable in the universe carries the $(e, b)$ form by structural necessity, and the only things "stripped" of the carrier are definitional / stipulative objects that lie outside the universe of observables. We articulate this universality claim, demonstrate that candidate counter-examples (pure integers, mathematical limits, logical propositions, pre-measurement quantum states, computational fixed points) all collapse to the same pattern (definitional objects can be stripped; observable objects cannot), and provide the corresponding equivalence-class structure that the carrier permits and classical algebra forbids: two objects with the same centre and different bounds are equal in the load-bearing sense, with the bound difference recording rather than violating the equality.

We identify Heisenberg's uncertainty principle, $\Delta x \cdot \Delta p \geq \hbar/2$, as a structural constraint on the bound rail with non-zero floor — i.e., a physical statement of the form "no observable in this domain can have $b = 0$." Planck's constant $\hbar$ is interpreted as the universe's commitment to broken-zero ($b > 0$) at the smallest scale; the limit $\hbar \to 0$ corresponds to the degenerate special case in which the bound rail vanishes and classical scalar arithmetic is recovered. Quantum mechanics, on this reading, is not an exception to the carrier shape but its strongest physical evidence.

The paper closes with a note on the methodological diagnosis: the reflex of "slow down" in response to universality claims is risk-aversion rather than analysis. The correct response to a structural-uniqueness theorem under explicit axioms is either to produce a counter-example or to accept the claim. Slowing down without engaging the structure is hedging.

**Keywords:** carrier-set theorem, EB carrier, universality, observables, Heisenberg uncertainty principle, broken zero, foundations of physics, philosophy of measurement, structural realism, equivalence relations beyond strict equality.

---

## 1. The Carrier-Stripping Lemma

**Lemma (Carrier-Stripping).** *A mathematical object may be carrier-free only in definitional space. Any physical, computational, observational, or communicative instantiation admits an EB representation $(e, b)$ with $b \geq 0$ on the EB carrier $\mathbb{R} \times \mathbb{R}_{\geq 0}$, where $e$ is the expressed value (centre) and $b$ is a non-negative bound (irreducible admissible deviation). The bound is structurally non-eliminable upon instantiation: there is no observable for which $b$ can be reduced to zero by improving the measurement.*

The lemma has two parts:

- **Universality (in the observational register):** every observable carries the shape.
- **Irreducibility (upon instantiation):** the bound rail is structural, not merely an artifact of imperfect technique.

Universality follows from the carrier-set theorem (uniqueness under A1–A6). Irreducibility follows from physical theorems already in hand (Heisenberg uncertainty, fluctuation-dissipation, statistical-mechanical thermal noise floors), which the carrier-set framework absorbs as instances of $b > 0$.

**Crucial bridging principle.** EB does not replace pure mathematics; it does not impose bounds on definitional objects. EB *governs access to mathematics* — the moment a definitional object is instantiated in the universe (written, measured, computed, transmitted), it enters the observational register and acquires $b > 0$ by structural necessity. The carrier is not a theory of uncertainty: it is a theory of how certainty is accessed.

## 2. The boundary of stripping

We work outward from the claim by asking: **what kinds of objects can be stripped of the carrier?**

The answer requires distinguishing two registers:

**Definitional register.** Objects whose identity is fixed by stipulation alone: pure integers, mathematical limits, logical propositions, axiomatic constants, ideal-typical objects in formal systems. These do not have observables in their definitional form; they are stipulated to be exact. The carrier does not apply because the precondition of carrier application — being an observable subject to physical instantiation — is not met.

**Observational register.** Anything that has been instantiated, measured, transmitted, recorded, computed on real hardware, or interacted with the physical universe in any way. Every such object carries $(e, b)$ form. The bound rail is non-trivial.

**Bridging law.** *A definitional object enters the observational register exactly when it is instantiated. At the point of instantiation, $b > 0$ is unavoidable.*

We tabulate candidates that initially appear to be stripped of the carrier but, on inspection, fall into the definitional register only:

| Candidate | Definitional or observational | Bound at observation |
|---|---|---|
| Pure integer 7 | Definitional | Once written / counted / transmitted, $b > 0$ (paper smudge, count-correctness, transmission integrity) |
| Mathematical limit $\lim_{n \to \infty} a_n = L$ | Definitional ($L$ exists in $\mathbb{R}$ by stipulation) | Every approximation has $b > 0$; the limit itself is never instantiated |
| Logical proposition "P implies Q" | Definitional (truth-value relation) | Truth-in-the-world is observable; $b > 0$ at the verification step |
| Pre-measurement quantum state $\psi$ | Observational (the wavefunction is the carrier) | $\psi$ carries probability density = bound rail for any measurement; $b > 0$ by Born rule |
| Computational fixed point $\lambda x. x$ | Definitional in syntax | Once executed on real hardware, $b > 0$ (clock jitter, bit-flip rate) |

The pattern is uniform. Stripping is possible only in the definitional register. The observational register — i.e., the universe — admits no stripping.

## 3. Equivalence relations beyond strict equality

A central operational consequence of the carrier shape: the EB carrier admits multiple legitimate equivalence relations that classical algebra cannot express.

For pairs $(e_1, b_1)$ and $(e_2, b_2)$ on the EB carrier:

**Strict equality:** $e_1 = e_2$ and $b_1 = b_2$. The classical-algebra notion.

**Centre-equality with bound-divergence:** $e_1 = e_2$ and $b_1 \neq b_2$. This is the case Eric articulates in plain language as "more than equal and still equal." The two pairs share the load-bearing centre but differ in the irreducible spread that records the structural cost of arriving at that centre. Classical algebra has no name for this relation; EB carrier names it directly.

**Hull-overlap / in-tolerance:** the symmetric hulls $[e_i - b_i, e_i + b_i]$ for $i \in \{1, 2\}$ have non-empty intersection. The pairs are operationally indistinguishable within their declared bounds.

**ξ-equivalence (shared-factor cancellation):** two pairs that share a multiplicative latent factor $\theta$ at the centre satisfy $e_{(u \oslash v)} = f_u / f_v$ independently of $\theta$ (Proposition 28.2.1, Memoir Ch. 28). The latent factor cancels exactly in the centre; the bound depends only on input magnitudes.

These four relations are not philosophical multiplicity but operational distinctions that the carrier carries by construction. Classical algebra forbids them by enforcing scalar identity; interval arithmetic forbids them by parity-1 interlocking; Gaussian propagation forbids them by collapsing to single-distribution mean. Only the EB carrier permits centre and bound to carry separate information without one breaking the other.

## 4. Quantum observables as carrier instances

Quantum mechanics is the strongest empirical evidence for the Carrier-Stripping Lemma in the observational register.

**Important scope clarification.** This paper does **not** derive quantum mechanics from EB carrier principles, nor does it propose to replace the standard formulation. We claim only that quantum observables — i.e., the post-measurement values returned by quantum systems — are carrier instances. The structural shape that the carrier-set theorem proves is unique under A1–A6 is the same shape that quantum measurement returns.

Formally, for any quantum observable $\hat{O}$ acting on a state $\psi$:
$$
\psi \;\Rightarrow\; (\langle \hat{O} \rangle,\; \Delta \hat{O})
$$
i.e., the (centre, bound) pair on the EB carrier. The Born rule is the bridge that maps the wavefunction to the bound rail.

The Heisenberg uncertainty principle, $\Delta x \cdot \Delta p \geq \hbar/2$, is then a **structural constraint on the bound rails of two specific carrier instances** (position and momentum observables): the product of bounds has a non-zero lower limit. Classical scalar algebra has no mechanism to express this; there is no algebra of pure scalars in which the product of "uncertainties" has a structural floor. The carrier carries the constraint by construction.

Translation table:

| Quantum object | EB carrier reading |
|---|---|
| Expectation value $\langle\hat{O}\rangle$ + standard deviation $\sigma_{\hat{O}}$ | The pair $(e, b)$ for the observable |
| Wavefunction $\psi$ | Carrier of latent centre + spread; Born rule renders the bound rail upon measurement |
| $\hbar$ | Universe's floor on $b$ for conjugate observables; "broken zero" made into physical law |
| Classical limit $\hbar \to 0$ | $b \to 0$ degenerate case; the EB carrier collapses to scalar $\mathbb{R}$ |
| Wavefunction collapse | Bound-rail contraction (post-measurement bound smaller, never zero) |
| Entanglement | Correlated bounds across spatially-separated centres |
| Bell / CHSH inequality | Constraint on which bound-correlation structures are locally explicable |

Under this reading, $\hbar > 0$ is the universe's commitment to the EB carrier shape at the smallest scale. The fact that physics could not make $\hbar$ go to zero — neither mathematically (by experimental refinement) nor philosophically (by interpretive reinterpretation) — is the universe telling us the carrier is fundamental.

## 5. The "slow down" reflex as methodological hedge

We close with a methodological observation. Universal claims of the form *"every observable carries this shape"* attract a near-universal reflex: *"slow down."* In machine-assisted research, this reflex is particularly pronounced in AI systems trained to hedge against overclaim.

The reflex is risk-aversion, not analysis. The correct response to a structural-uniqueness theorem with explicit axioms is one of:

1. **Counter-example.** Produce an observable that does not carry $(e, b)$ form. (None has been produced; we have looked.)
2. **Axiom challenge.** Reject one of A1–A6 as not capturing what should count as an admissible algebra of measurement. (Possible in principle; absent in present discourse.)
3. **Acceptance.** Acknowledge the claim and develop its consequences.

"Slow down" without engaging any of (1)–(3) is hedging. It is not a contribution to the structural question. It is a deferral of the structural question.

We urge readers to push past the hedge and engage the structure. If the EB carrier is universal, the consequences are not optional cosmetic improvements to existing methods — they are structural reorganizations of how observables are propagated, compared, and aggregated across measurement chains. Those reorganizations include the cosmological-tension applications under separate study (RSOS-260797 + companion MNRAS work), the patent-protected encoding architecture (UHA, US 63/902,536), and the foundational implications for any field that propagates measurement uncertainty.

## 6. What this paper does not claim

For epistemic honesty:

1. We do not claim the carrier shape is the *only* structure capable of representing observables. We claim it is the unique structure satisfying A1–A6, and we claim the axioms are the natural minimal axioms for any algebra of measurement that propagates bounds without auxiliary state.
2. We do not claim that all working physicists or measurement scientists are tacitly using EB carriers without naming them. Many use Gaussian, MC, interval, or ad-hoc methods that violate one or more of A1–A6. We claim that *the structural shape they observe in their data* — the bound rail that won't go away — is the EB carrier asserting itself even when the methods don't recognize it.
3. We do not claim quantum mechanics needs reformulation in EB-carrier language to be correct. Quantum mechanics is correct as currently formulated. We claim the EB carrier provides a unifying structural account of why quantum mechanics had to look the way it does — specifically, why the universe could not have an algebra of observables in which $b = 0$ was attainable.
4. We do not claim this paper proves the carrier-set theorem; that proof appears in RSOS-260797 r4 and Memoir Ch. 1–8 (Martin 2026). This paper interprets the theorem's consequences for the universality question.

## 7. Cross-references and prior deposits

- **Carrier-set theorem (formal):** RSOS-260797 r4, "The EB Carrier: A Characterisation Theorem and its Cayley–Dickson Classification" (under review)
- **Memoir-length development:** AMS Memoirs submission 260427-umo36 (in preliminary review)
- **N/U Algebra (subordinate corollary):** Zenodo deposit 10.5281/zenodo.19676237 (r1 priority lock; deposited 2026-04-21; concept-DOI 10.5281/zenodo.19676236)
- **EB physical bridge:** project memory `project_eb_physical_bridge.md` — algebra characterizes substrate properties; physical bridge is separate
- **Layer-zero boundary:** project memory `project_layer_zero_boundary_unfalsifiable_rail.md` — EB carrier is Layer 0 boundary; admits unfalsifiable content on one rail
- **Broken zero:** project memory `project_broken_zero_floor.md` — EB floor is broken zero; $b > 0$ is structure not degradation

## 8. Provenance and attribution

This draft was structured during a session conversation 2026-04-28. The originating intuitions, the carrier-set theorem itself, the plain-language formulations ("more than equal and still equal"; "nothing in the universe that doesn't operate under the principle"; "even quantum physics obeys the carrier"), and the working-out-by-disassembly cognitive process that produced the framework are Eric D. Martin's. The paper structure was assembled in conversation as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md`.

Sole author throughout. No Co-Authored-By AI per `feedback_no_coauthor.md`. No AI in bibliography as author.

---

*End of draft v0.2.*

**Working venue (primary):** Royal Society Open Science (RSOS) — same publisher as the carrier-set theorem paper itself; provides open-access foundational publication; complementary not duplicate (this paper interprets the theorem's universality consequences for observability, where RSOS-260797 r4 establishes the theorem's algebraic statement and proof).

**Working venue (secondary):** Entropy or Information (information-theoretic framing) for the version that emphasizes the carrier-as-information-access angle.

**Working venue (advanced follow-up):** Foundations of Physics, after physics claims have been further tightened and the connection to broader measurement-theory literature is built out.

**Companion follow-on papers (roadmap, not this paper):**
- *EB carrier in formal verification* — observability constraints on computational fixed points
- *EB carrier in quantum measurement theory* — fuller treatment of the wavefunction-to-Born-rule bridge in carrier language
- *EB carrier in distributed systems* — UHA encoding architecture as a domain-specific implementation of the carrier
- *EB carrier in statistical mechanics* — fluctuation-dissipation and thermal floors as bound-rail manifestations

**v0.2 changes from v0.1:**
- Adopted "Carrier-Stripping Lemma" as the formal name (was unnamed in v0.1)
- Added crucial bridging principle: "EB governs access to mathematics, not mathematics itself"
- Adopted "EB is not a theory of uncertainty; it is a theory of how certainty is accessed" as the strongest one-liner
- Adopted "Definitional exactness is not observational exactness" as paper epigraph
- Narrowed §4 quantum claim to *carrier representation of observable outcomes*, NOT derivation of quantum mechanics; added explicit scope clarification
- All sharpenings folded in from independent-instance audit (per `feedback_others_contradict_not_prove.md`: convergence between two instances on the framing was treated as suspicious-but-genuine restatement, not endorsement; sharper articulations adopted, no new claims absorbed)
