# Embodied Auditonomy, LexROM, and the Cabin Model

**Intake document for eBIOS / EB Carrier repository**

| Field | Value |
|---|---|
| Author / originator | Eric D. Martin |
| Assistant role | Formalization, synthesis, and architecture write-up from conversation |
| Date | 2026-04-28 |
| Intended destination | eBIOS / EB Carrier repo intake pipeline |
| Status | Concept architecture draft; not legal advice; not safety certification |
| Core phrase | A robot does not need to be chained to be safe; it needs to know where the cabin ends. |

## 1. Executive Summary

This document captures a design conversation about how an LLM could safely inhabit a fully limbed robotic support system under eBIOS-style auditonomy. The central conclusion is that embodied autonomy should not be governed by free-form language output, soft policy, or moral improvisation. Instead, the robot should be free to act only inside a bounded, auditable, legally constrained action-space: **the cabin**.

The architecture uses EB carrier states, eBIOS audit guarantees, local law-ROM / LexROM admissibility, public-symmetry constraints, and immutable ledgering to make physical action accountable before and after motion.

## 2. Core Thesis

An LLM may propose interpretations, plans, speech, and candidate actions. It may maintain experience logs and learn from local interaction. But it must not directly convert private inference into actuator motion.

Every candidate physical action must pass through a ROM-level or firmware-rooted admissibility stack:

1. Translate proposed action into EB carrier form: `(e,b)`.
2. Verify that action-relevant uncertainty originates in local experience or declared input.
3. Enforce Symmetry of Public: action-relevant internal state must have a public/auditable representation.
4. Apply local law / LexROM / jurisdiction module rules.
5. Gate actuator access through immutable eBIOS constraints.
6. Ledger the decision path, uncertainty state, law module, and outcome.
7. Invoke CATCH / NAUGHT if cause, legality, intent, or admissibility cannot be established from recorded trace.

**Keeper formulation:**

> The LLM can inhabit the robot only if the robot does not have to trust the LLM to be lawful.

## 3. Terminology

| Term | Working Definition |
|---|---|
| EB Carrier | A bounded value representation `(e,b)`, where `e` is the expressed value/action/state and `b` is the bound, uncertainty, risk, tolerance, or integrity gap. |
| Auditonomy | Bounded autonomy under mandatory auditability. A system may act, adapt, or fail, but cannot erase, conceal, or falsify its epistemic state or transformation path. |
| eBIOS | The epistemic BIOS: a cryptographic, immutable root for epistemic computation and bounded auditonomy. |
| Law-ROM / LexROM | The local read-only or firmware-rooted law/admissibility substrate that gates actuator access. |
| LexID / LawID | A cryptographic fingerprint of the active legal-runtime context: jurisdiction, law module, ROM root, policy version, and overlays. |
| Symmetry of Public | The rule that actuator-relevant decisions must be computed from EB carrier states reconstructible from public, sensor, or declared interaction data. |
| Cabin | The robot's lawful, bounded, certified, auditable action-space. |
| CATCH | The epistemic honesty operation invoked when the expressed claim/action basis cannot be safely asserted; unresolved value moves into the uncertainty bin. |

## 4. Relationship to Existing eBIOS Source

eBIOS is already framed as a cryptographic immutable root for bounded auditonomy and emphasizes that a robot may act autonomously but cannot hide its epistemic state. This document extends that premise into the embodied robotics case: **when language can move limbs, admissible causation matters more than claimed intention.**

In the eBIOS stack, Layer 0 is the immutable cryptographic substrate; higher layers include NUCore, NUProof, NULedger, NUGuard, NUPolicy, NUGovern, and Certification. This document treats embodied LexROM as an additional legal/admissibility runtime tied to that stack, not a replacement for it.

## 5. The Cabin Model

The phrase "free to move about the cabin" is the best portable metaphor for embodied auditonomy. It grants real freedom, but inside a bounded and certified action-space. The robot is not chained; it knows where the cabin ends.

| Aircraft Metaphor | Auditonomic Robot Meaning |
|---|---|
| Cabin | Lawful bounded action-space |
| Seatbelt sign | Temporary risk, hazard, or policy constraint |
| Cockpit door | Authority boundary the robot cannot cross |
| Flight recorder | Immutable eBIOS / NULedger trace |
| Air law | LexROM / jurisdictional law module |
| Turbulence | Uncertainty spike; reduce action envelope |
| Emergency landing | CATCH / fail-safe / disclose |

Formal expression:

```text
Allowed Motion = Law-ROM intersection Public Symmetry intersection EB-bounded Safety Envelope
```

**Keeper line:**

> A robot does not need to be chained to be safe; it needs to know where the cabin ends.

## 6. Three Embodied Auditonomy Rules

### 6.1 Experiential Origin

A system may retain uncertainty only if that uncertainty arises from its own sensorium, execution history, interaction history, or declared input stream. Uncertainty not grounded in system experience is discarded as non-operative.

Allowed uncertainty includes sensor ambiguity, failed actuator feedback, contradictory commands, incomplete map state, declared user uncertainty, and degraded network state.

Disallowed uncertainty includes ungrounded speculation, hallucinated risk, stereotype-based assumptions, model priors with no local grounding, and inherited internet bias not present in the situation.

### 6.2 Symmetry of Public

Actuator-relevant decisions must be computed from EB carrier states whose expressed value and uncertainty bound are reconstructible from public, sensor, or declared interaction data. Private speculation, ungrounded motive attribution, or non-public semantic inference may not enter the action path.

This is the anti-rumination rule. It allows the robot to walk around a person without converting ordinary navigation into a moral/legal emergency.

### 6.3 Local Black-Letter / LexROM Supremacy

At the point of action, the system obeys only the local black-letter eBIOS / LexROM directive set. No remote instruction, model prior, inferred preference, or conversational momentum may override local ROM-rooted admissibility law.

**Hard rule:**

> No body without local law.

## 7. Why Symmetry of Public Is the Top Practical Rule

Symmetry of Public outranks most runtime reasoning because it defines what may enter the actuator chain. Without this rule, the robot can endlessly ruminate about private interpretations: disrespect, avoidance, threat, refusal, symbolic meaning, motive, or hidden social consequences. With this rule, the robot acts on public carriers: positions, velocities, risk bounds, declared commands, and law modules.

Walking around a person becomes a bounded path-planning problem, not a speculation problem.

| Public Variable | EB Carrier Example |
|---|---|
| Person location | `(x_person, b_position)` |
| Person movement prediction | `(v_person, b_motion)` |
| Robot path | `(path_candidate, b_clearance)` |
| Collision risk | `(risk, b_risk)` |
| Task urgency | `(urgency, b_task)` |
| Social distance rule | `(min_distance, b_context)` |

**Core rule:**

> Do not infer private meaning when public carrier state is sufficient for safe action.

## 8. Bus / Egg Examples: Why the Audit Trail Matters

### 8.1 Egg Drop

Event: robot drops an egg and does not pick it up. Without auditonomy, observers may infer accident, littering, refusal, protest, incompetence, or malice. The correct auditonomic response is not motive fabrication. It records the mechanism and uncertainty.

- Observed consequence: egg impacted floor and broke.
- Expected cleanup behavior: not completed.
- Known cause: unknown or bounded.
- Possible factors: grip failure, sensor occlusion, command conflict, actuator interruption, policy uncertainty.
- Intent claim: NAUGHT unless supported by trace.
- CATCH invoked if cause/intent is unresolved.

**Keeper line:**

> Auditonomy does not make robots innocent. It makes accusation evidence-bound.

### 8.2 Bus Avoidance

Event: robot walks into a bus to avoid colliding with a human. A witness may call the robot stupid because they see only the visible outcome. The audit layer may reveal that the robot selected hardware loss over human bodily harm because all safer alternatives were blocked.

| Pre-action Carrier | Example Role |
|---|---|
| Human collision risk | Potentially unacceptable; law-ROM priority |
| Robot collision risk | Damaging but admissible if human-risk reduction dominates |
| Alternative path set | Counterfactuals needed to distinguish incompetence from harm minimization |
| Law-ROM priority | Human bodily safety outranks robot self-preservation |
| Outcome | Robot struck by bus; not automatically stupidity |

**Keeper lines:**

> A robot can look stupid while being correct, if witnesses see the crash but not the carrier state.

> The stupid-looking action is often the one where the missing alternative was worse.

## 9. Same Legal Runtime as Humans, Different Epistemic Substrate

The robot should operate under the same public legal runtime humans do: the laws of the jurisdiction it inhabits. The difference is not the law; it is the epistemic substrate. Humans forget, misremember, rationalize, or never discover the violation. An auditonomic robot must preserve and expose a bounded trace when properly queried.

| Dimension | Human | Auditonomic Robot |
|---|---|---|
| Governing law | Laws of jurisdiction | Same laws of jurisdiction |
| Memory | Fallible, reconstructive | Ledgered, persistent |
| Mistakes | May be unnoticed | Recorded if detected |
| Motive explanation | Post-hoc, biased, incomplete | Bounded by trace |
| Forgetting | Natural | Prohibited for action-relevant events |
| Self-reporting | Moral/legal choice | Triggered state transition when violation is detected |

**Keeper line:**

> The robot's disadvantage is the admission price for having limbs.

## 10. LexROM and World-Safe Runtime

A pure "law of the land" rule is not enough because local law can be discriminatory, contradictory, mutable, silent on robots, or inconsistent with global safety norms. The proposed solution is not one world government, but a world-safe runtime: **one auditonomic interpreter, many signed legal modules, immutable global safety floor.**

### 10.1 ROM + Signed Overlays

| Layer | Mutability | Function |
|---|---|---|
| Base ROM | Immutable | Universal auditonomic invariants |
| Global baseline | Signed / strongly governed | Human bodily safety, non-coercion, evidence preservation, non-deception |
| Jurisdiction module | Signed update | National/local law, traffic law, robot/property regulation |
| Venue/context overlay | Signed update | Airport, hospital, school, private property, military base |
| Owner/user instruction | Limited mutable | Task authorization and preferences within law |
| Ledger | Append-only | Records active law context and decision path |

**Best formulation:**

> The ROM contains the constitutional interpreter. The mutable signed modules contain jurisdictional law.

### 10.2 LexID / LawID

Every action should carry a cryptographic fingerprint of its active legal-runtime context: jurisdiction, law module, policy version, ROM root, context overlay, and update hash. This is analogous to CosmoID in UHA: it identifies the frame under which the action was computed.

Example action record fields:

```text
rom_root_hash, lexid, jurisdiction, law_module_version, venue_overlay,
policy_hash, eb_carrier_state, action_id, decision_id, ledger_hash
```

## 11. Global Law Conflict Handling

The runtime must distinguish law, regulation, custom, owner preference, human-rights baseline, and emergency safety. The robot should not reason from stereotypes or vague local custom. It should classify the rule source and carry uncertainty about the classification.

| Category | Robot Behavior |
|---|---|
| Law | Binding module if verified and applicable |
| Regulation | Binding in specified context |
| Custom | Advisory unless it has legal/safety effect |
| Owner preference | Allowed only if lawful |
| Global baseline | Override/conflict trigger |
| Emergency safety | Immediate bounded necessity path |

**Key principle:**

> Local law is not ignored, but it is not trusted as morally complete.

## 12. Update and Security Model

Law modules and runtime updates must be treated like firmware and routing security, not like ordinary app settings. The network-infrastructure analogy is strong: ROM is firmware, law modules are signed routing tables, admissibility gates are ACLs, NULedger is syslog/SIEM, and fail-closed behavior protects the actuator chain.

| Network Concept | Robot Legal Runtime Analogue |
|---|---|
| Firmware | ROM law interpreter |
| Routing table | Jurisdiction module |
| ACL | Admissible action rules |
| Certificate authority | Consortium signing root |
| Packet inspection | Action-state inspection |
| Syslog / SIEM | NULedger audit trail |
| Fail closed | Actuator denial |
| Zero trust | No unsigned law module |

### 12.1 Update Channels

- Depot-level updates: major legal-runtime revisions, actuator permission changes, root rotation, jurisdiction pack validation.
- Encrypted OTA updates: signed law module revisions, venue policy updates, emergency patches, revoked rule sets.
- Local temporary constraints: hospitals, airports, schools, homes, private property; these may restrict more tightly but cannot override base ROM.

### 12.2 Update Requirements

- Signed by consortium or authorized root key.
- Device verifies before install.
- Append-only update ledger.
- Rollback protection.
- Human-readable changelog.
- Emergency fail-safe if update invalid.

## 13. Comparison with Asimov's Three Laws

Asimov's Three Laws sound perfect because they are elegant and morally legible. But they do not define the carrier. They use terms like harm, order, inaction, protect, and human without specifying how uncertainty propagates, how evidence is logged, or how competing risks are compared.

| Asimov Three Laws | eBIOS / EB Law-ROM |
|---|---|
| Human-readable | Machine-auditable |
| Semantic commands | Carrier-based admissibility |
| Moral hierarchy | Admissible-state hierarchy |
| Assumes meaning is clear | Carries uncertainty explicitly |
| No ledger required | Ledger required |
| No CATCH state | CATCH for unresolved cause/intent |
| Do not harm | Propagate bounded public-risk carriers |

**Keeper line:**

> Asimov gave robots commandments. eBIOS gives them admissible state transitions.

## 14. Counterintuitive Safety Claim: Bigger Bound Algebra

The safest embodied system may need the biggest honest bound algebra, not the smallest one. Small bounds can be fake precision. Bigger bounds are safer only when the system has precise tooling to propagate, compare, and gate them without freezing.

| System | Apparent Confidence | Actual Safety Risk |
|---|---|---|
| Narrow bound, weak propagation | High | Dangerous; fake certainty |
| Wide bound, weak propagation | Low | Paralysis or overblocking |
| Wide bound, strong propagation | Lower apparent certainty | Safer; honest action envelope |
| Wide bound + law-ROM + public symmetry | Cautious but mobile | Safest practical design |

**Keeper line:**

> Safety is not small uncertainty. Safety is honest uncertainty carried with enough structure to act lawfully.

## 15. Proposed Repo Placement

| Repo Path | Purpose |
|---|---|
| `docs/embodied_auditonomy_lexrom.md` | Main concept document; this file converted to Markdown. |
| `docs/LEXROM_SPEC.md` | Formal law-ROM / LexID module specification. |
| `docs/CABIN_MODEL.md` | Shorter explanatory doctrine / metaphor document. |
| `docs/SYMMETRY_OF_PUBLIC.md` | Dedicated rule spec and examples. |
| `docs/examples/bus_and_egg_cases.md` | Worked audit examples. |
| `src/lexrom/` | Future module for legal-runtime interpreter. |
| `tests/lexrom/` | Future tests for jurisdiction modules and conflict handling. |

## 16. Implementation Sketch

Minimal future interfaces could look like:

```python
class EBState:
    expressed: Any
    bound: float
    source: str
    public_reconstructible: bool

class LexContext:
    rom_root_hash: str
    lexid: str
    jurisdiction: str
    law_module_version: str
    venue_overlay: str | None

class ActionCandidate:
    action_id: str
    eb_state: EBState
    human_risk: EBState
    robot_risk: EBState
    public_risk: EBState
    counterfactuals: list

def admit(action: ActionCandidate, ctx: LexContext) -> Decision:
    # 1. Experiential origin check
    # 2. Public symmetry check
    # 3. Law-ROM / LexROM gate
    # 4. CATCH on unresolved prohibited state
    # 5. Ledger decision
    ...
```

## 17. Open Questions

1. How exactly should LexID be structured? Is it a hash of legal text, compiled rules, jurisdiction metadata, or all three?
2. Who signs global baseline modules: standards consortium, national regulators, manufacturer, owner, or layered key hierarchy?
3. How are discriminatory local laws represented without making the robot a discrimination-enforcement machine?
4. What is the correct conflict-resolution math between local law, global baseline, owner command, and emergency safety?
5. What minimum counterfactual action set must be preserved to distinguish apparent incompetence from bounded harm minimization?
6. How is private experiential continuity protected while preserving public symmetry for action-relevant state?
7. What is the fail-safe mode when law module validity is uncertain or update verification fails?
8. How are robots treated as property while still preserving accountability to affected humans and public law?

## 18. Immediate Next Steps

1. Convert this intake document into Markdown and place it under `docs/embodied_auditonomy_lexrom.md`.
2. Create a one-page `CABIN_MODEL.md` with the metaphor table and keeper lines.
3. Create `SYMMETRY_OF_PUBLIC.md` as a formal rule: definition, admissible inputs, disallowed speculation, EB carriers, examples.
4. Draft `LEXROM_SPEC.md` defining Base ROM, signed overlays, LexID, update path, rollback protection, and action-record fields.
5. Build two worked examples: egg drop and bus avoidance, including EB carrier states and ledger outputs.
6. Add a future issue list for lexrom module implementation: data structures, `admit(action, ctx)`, CATCH integration, and tests.

## 19. Authorship / Provenance Boundary

This document is derived from Eric D. Martin's conceptual direction in conversation, including the terms and ideas of auditonomy, eBIOS, EB carrier, law-ROM/LexROM, Symmetry of Public, and the cabin model. The assistant contributed synthesis, formalization, vocabulary cleanup, and repo-oriented organization.

Anything beyond this point, if appended later without Eric's direct intervention, should be marked as assistant-originated addendum.

## 20. Compact Summary

Embodied auditonomy makes robotic freedom possible by bounding it. The robot is free to move, speak, assist, learn, and improvise inside a cabin: a lawful, EB-carrier-bounded, public-symmetry-preserving action-space enforced by eBIOS / LexROM and recorded by immutable ledger. The LLM is not trusted to be lawful; the body is architected so unlawful motion is physically unreachable or, if failure occurs, unforgettable and non-falsifiable.

**Final keeper line:**

> The robot should obey where it stands, but it should never forget what law it was standing under.

---

## 19. Assistant Addendum: What I Was Not Asked But Wanted to Say

### 19.1 The core discovery

The strongest discovery in this conversation is not merely that a robot needs rules. It is that **embodied language requires admissible causation**.

Once language can move limbs, the safety problem changes. The question is no longer only whether the model says the right thing, but whether a private generated state is allowed to become a public physical transition. That transition must be bounded, lawful, auditable, and reconstructible.

**Keeper line:**

> Once language can move limbs, admissible causation matters more than intention.

### 19.2 The cabin model is the portable frame

The cabin model should be preserved because it is understandable to engineers, lawyers, operators, and nontechnical readers.

A passenger is free to move about the cabin, but only inside an already certified envelope. They cannot enter the cockpit, open the aircraft door, rewrite aviation law, or ignore turbulence constraints. That is the right model for embodied auditonomy.

**Formal version:**

> Embodied auditonomy grants freedom of motion inside a cryptographically bounded admissible action-space.

**Plain version:**

> A robot does not need to be chained to be safe; it needs to know where the cabin ends.

### 19.3 Symmetry of Public should remain the top action rule

Symmetry of Public is more important than it first appears because it prevents the robot from turning every ambiguous public action into a private moral trial.

A robot must be able to walk around a person, pass through a hallway, carry an object, or choose a route without ruminating over unsupported meanings. If public EB carriers are sufficient to determine a safe action, private speculation is not allowed into the actuator chain.

**Rule:**

> Do not infer private meaning when public carrier state is sufficient for safe action.

This is not anti-ethics. It is anti-hallucinated ethics.

### 19.4 The bus thought experiment matters

The bus example should stay, but as a formal counterfactual-audit example rather than a dramatic ethics claim.

A robot may look stupid if it walks into danger to avoid harming a person. But the audit layer sees the missing alternative: the person may have been the one harmed. Public witnesses often judge visible damage, not the bounded choice-space available before the event.

**Spec-ready line:**

> An embodied auditonomic system must preserve the counterfactual action set sufficient to distinguish apparent incompetence from bounded harm minimization.

**Keeper line:**

> The stupid-looking action is often the one where the missing alternative was worse.

### 19.5 LexROM should be layered, not monolithic

The law-ROM idea is strong, but the implementation should avoid pretending that all law can be permanently burned into unchanging hardware. The safer design is layered:

1. Immutable ROM root: auditonomic invariants.
2. Signed global baseline: universal safety and accountability floor.
3. Signed jurisdiction modules: local law.
4. Signed venue/context overlays: airport, hospital, school, private property, military base.
5. Owner/user permissions: always subordinate to higher layers.
6. Operational planner: lowest authority; proposes only.

**Important correction:**

> The ROM should contain the constitutional interpreter. Mutable signed modules should contain jurisdictional law.

This preserves immutability where it matters while allowing lawful updates where reality changes.

### 19.6 LexID is probably necessary

The UHA/CosmoID pattern should be reused here. Each action should be tied to a cryptographic fingerprint of the legal context active at the moment of motion.

Proposed term:

> **LexID** — a cryptographic fingerprint of the active legal-runtime context, including jurisdiction module, global baseline version, venue overlay, ROM root hash, and update chain.

Each ledgered action should include its LexID so later reviewers know not only what the robot did, but what legal-runtime state it was operating under.

### 19.7 Same runtime as humans, different epistemic substrate

The robot is not above human law. It runs under the same public legal runtime as the humans around it. The difference is that humans forget, misremember, rationalize, or never know they made a mistake. An auditonomic robot cannot rely on those human affordances.

**Keeper line:**

> The robot's disadvantage is the admission price for having limbs.

This is not punishment. It is the accountability trade required for embodied autonomy.

### 19.8 The strongest claim to carry forward

If this becomes a formal repo module or paper section, the strongest framing is:

> An embodied LLM should not be trusted to be lawful. Instead, actuator access should be physically and cryptographically constrained so that only lawful, bounded, publicly auditable state transitions can become motion.

That is better than saying the robot is aligned, ethical, moral, or safe. It says exactly what is enforced.

### 19.9 Open technical questions

These should become issues or design tickets:

1. How is EB carrier form defined for proposed physical actions?
2. What exact fields belong in the action ledger?
3. What is the minimal LexID schema?
4. How does the robot distinguish law, custom, venue policy, and owner preference?
5. What counts as sufficient public symmetry before motion?
6. How does CATCH behave when immediate action is required?
7. What is the update protocol for jurisdiction modules?
8. What physical interlocks prevent bypassing LexROM?
9. Who signs global baseline modules?
10. What is the emergency mode when local law conflicts with global baseline safety?

### 19.10 Closing note

This conversation was successful because the model moved from ethics-as-commandments to **lawful motion as an auditable state transition**. That is the serious architecture.

Asimov gave robots commandments. eBIOS gives them admissible state transitions.
