**Slack as a Third Behavioral Class in Information-Manding Acquisition:**

**An EB-Carrier Reanalysis of Swensson et al. (2024)**

*Version 3 --- Corrected Figure Digitization and Slack-Centered Revision*

**Eric D. Martin**

Independent Researcher

ORCID: 0009-0006-5944-1742

**Abstract**

Single-case experimental design (SCED) data in applied behavior analysis routinely contain response relations that are visible in graphs but not extracted as formal variables. Swensson et al. (2024) provide a clean public case: caregivers coached via telehealth taught three children with autism spectrum disorder to mand for information using the phrase "I don't know, please tell me" (IDKPTM). The original article measured independent IDKPTM responses and independent correct answers across five-trial sessions and reported the expected inverse relation between IDKPTM responding and correct-answer acquisition. The present paper does not challenge that analysis. It applies the Expressed--Bound (EB) carrier to a corrected digitization of Figure 1 and extracts the residual term that conventional reporting leaves implicit. For each Set 1 intervention session, the response system satisfies \(I_t+K_t+S_t=5\), where \(I_t\) is independent IDKPTM responding, \(K_t\) is independent correct answering, and \(S_t\) is slack: trials with neither independent IDKPTM nor independent correct answering. The corrected digitization shows a sharp cross-child slack contrast: Aden averaged 0.11 slack trials per session with 25/28 zero-slack sessions, Alex averaged 0.84 with 25/50 zero-slack sessions, and Ida averaged 1.07 with 6/14 zero-slack sessions. EB therefore converts the original two-path visual relation into a conserved three-class response system: adaptive uncertainty-manding, expressed correct responding, and residual slack. Secondary demonstrations show how the same reconstruction supports EB-operationalized response-system stability, a qualified signed contrast around Aden's six-week break, and sensitivity-style mastery-time ratios. The contribution is a science-expansion claim: Swensson et al. produced a high-quality dataset; EB extracts an additional behavioral quantity that their original reporting convention was not designed to compute.

**Keywords:**
 applied behavior analysis, single-case experimental
design, mands for information, telehealth, measurement uncertainty,
Expressed--Bound carrier, N/U Algebra

**1. Introduction**

Applied behavior analysis (ABA) generates dense longitudinal data. A
single-case experimental design (SCED) study with three participants,
twenty to sixty sessions per participant, and five trials per session
produces between 300 and 900 trial-level observations per study. The
field\'s reporting conventions condense this density into per-cell
summary statistics --- typically a mean and a range, supplemented by
visual analysis of a multiple-baseline graph --- and these conventions
are accepted at the highest tier of the literature. Swensson et al.
(2024) is exemplary work within those conventions: a clean replication
and extension of Ingvarsson and Hollobaugh (2010) demonstrating that
caregivers, coached entirely via telehealth, can teach children with
autism spectrum disorder to mand for information using the phrase \"I
don\'t know, please tell me\" (IDKPTM). Their data quality is excellent,
their interobserver agreement exceeds 98% on aggregate, their procedural
fidelity is at or near ceiling, and their conclusions are well-supported
within the descriptive-statistics framework they use.

This paper does not propose to revisit those conclusions. It proposes to
extract four additional quantities from the same data --- quantities
that the descriptive-statistics framework cannot represent and that the
standard SCED reporting conventions therefore necessarily omit. The
instrument that makes the extraction possible is the Expressed--Bound
(EB) carrier, an axiomatically characterised algebra over the
ordered-pair carrier ℝ × ℝ≥0 whose first-order regime was previously
published as N/U Algebra (Martin, 2025) and whose full characterisation,
including the exact regime and the uniqueness theorem under axioms
A1--A6, appears in Martin (2026). The EB carrier is not a statistical
method. It does not produce p-values, does not test hypotheses, does not
detect change points, and does not model temporal trends. What it does
is propagate measurement bounds through arithmetic operations natively,
with a constant-time-per-operation complexity, no auxiliary state, and
no post-operation admissibility repair. That capability --- narrow on
its face --- turns out to make four classes of quantities legible in
SCED data that were not legible before.

The four findings reported here are: (i) the inverse relationship
between IDKPTM responses and correct answers, which Swensson et al. note
as a qualitative pattern in the prose, can be promoted to a
session-level conserved quantity whose residual slack measures a third
response class the original coding scheme did not separate; (ii) the
response-system stability can be operationalized to a specific session number for each child by tracking the conserved EB sum across the intervention phase; (iii) Aden\'s six-week between-session break, treated by the
original paper as a methodological complication, contains a six-week
maintenance-of-acquired-skill measurement with a quantified retention
bound, and the EB carrier\'s signed-residual reading extracts it; (iv)
cross-child time-to-mastery ratios computed under the EB division
operation algebraically cancel the shared experimental protocol from the
centre rail, leaving a child-specific intraverbal-acquisition-rate
residual that is interpretable as a clean cross-child comparison.

The paper proceeds as follows. Section 2 summarises the EB carrier\'s
structural commitments and operations as they bear on the present
application; readers familiar with Martin (2025, 2026) may skim. Section
3 specifies the encoding of Swensson et al.\'s Table 1 and Figure 1 into
EB pairs, including a per-phase summary of session-level values
extracted by digitization of Figure 1 (Section 3.4). Sections 4 through
7 develop the four findings in sequence, each with its computation
against the digitized data, its interpretation, and its placement
against the alternatives the standard SCED toolkit would supply. Section
8 documents the scope discipline that distinguishes measurement-layer
propagation from inference-layer statistics, including a note on how
that scope discipline was clarified through self-correction in October
2025 (Martin, 2025; Zenodo) and applied a second time in the
version-1-to-version-2 supersession of this paper. Section 9 discusses
implications for systematic reanalysis of the SCED literature. Section
10 records limitations.

**2. The Expressed--Bound Carrier**

This section gives the minimum exposition of the EB carrier required for
the present application. Full development is in Martin (2026).

**2.1 The Carrier and Its Operations**

The EB carrier is the set *A = ℝ × ℝ*≥0 of ordered pairs (e, b) where e
∈ ℝ is the expressed value (the asserted central magnitude) and b ∈ ℝ≥0
is the bound (a non-negative admissible deviation). Three operations are
defined on the carrier:

*Addition: (e₁, b₁) ⊕ (e₂, b₂) = (e₁ + e₂, b₁ + b₂)*

*Multiplication: (e₁, b₁) ⊗ (e₂, b₂) = (e₁e₂, \|e₁\|b₂ + \|e₂\|b₁ + λ
b₁b₂)*

*Scalar: a ⊙ (e, b) = (ae, \|a\|b), for a ∈ ℝ*

The parameter λ governs the tightness regime. The exact regime λ = 1
produces the bound formula whose symmetric hull *\[e − b, e + b\]*
contains exactly the set of products of values drawn from the input
hulls; the first-order regime λ = 0 truncates the quadratic cross-term
b₁b₂ and reproduces the operations of N/U Algebra (Martin, 2025). The
two regimes coincide whenever at least one input has bound zero. For the
present application both regimes are exercised: range-bounded
percentages from Table 1 are encoded with non-zero bounds, and the
multiplication-derived ratios in Sections 6 and 7 use the exact regime.

Three derived operators are used below. The hull evaluator *hull(e, b) =
\[e − b, e + b\]* maps a pair to the symmetric closed real interval it
represents; this is a downstream reading, not the definition of the
pair. The flip operator *B(e, b) = (b, \|e\|)* exchanges the two
coordinates with an absolute-value gate on the first, and is
non-involutive on the signed half (B² ≠ id when e \< 0); this property
is the operator-level diagnostic that distinguishes the EB carrier from
interlocked pair algebras (Boolean pairs, intervals, intuitionistic
fuzzy pairs, rough sets) and activates whenever signed residuals enter
the calculation. The reciprocal *(e, b)⁻¹ = (1/e, b/e²)* is well-defined
for e ≠ 0 and is the unique admissible first-order summary inverse
within the axiomatic class.

**2.2 Why the EB Carrier Is the Right Instrument for SCED Data**

Three properties of the carrier are decisive for this application.

**First,** *no distributional assumption.* The bound rail records
admissible deviation as a primitive; it does not require the deviation
to be Gaussian, symmetric, or independent across observations. SCED data
with five-trial sessions and percentage outcomes saturated at 100%
violate Gaussian assumptions structurally. The EB bound captures
range-bounded behaviour without distortion.

**Second,** constant-time propagation with no auxiliary state. Affine
arithmetic and Monte Carlo summary methods either carry growing
dependency state across operations or require sampling decisions that
compromise reproducibility. The EB carrier propagates bounds in O(1) per
operation. This matters less for a three-child analysis than for the
systematic reanalysis the paper points toward in Section 9; it matters
here as a proof of principle that the propagation is closed and
reproducible.

**Third,** shared-factor cancellation in the centre rail under ratio
operations. When two pairs depend on a common multiplicative factor at
the centre, that factor cancels exactly in the centre of their EB ratio
(Proposition 28.2.1, Martin 2026). The bound rail of the ratio depends
only on the input magnitudes and bounds, not on the shared factor. This
property --- invisible at the per-cell level --- is what makes Finding 4
below extractable.

**3. Encoding Swensson et al.\'s Data**

Two encoding conventions are admissible for percent-with-range data. The
choice between them depends on whether one wishes to preserve the data
range as a symmetric hull or the reported mean as the centre.

**3.1 Reading R1: Range-Faithful Symmetric Hull**

Under Reading R1, each reported \"value (min--max)\" is encoded as e =
(min + max)/2 and b = (max − min)/2. The symmetric hull *\[e − b, e +
b\]* then equals the data range exactly. The reported mean is discarded;
the bound rail records the observed extrema and nothing more.

**3.2 Reading R2: Mean-Centred Bound-Loosened Hull**

Under Reading R2, e = the reported mean and b = max(mean − min, max −
mean). The hull *\[e − b, e + b\]* then contains both the mean and the
data range, generally with bound-loosening on one side. This is the
preferred encoding for the present analysis because it preserves the
central-tendency information that the field reports as primary.

**3.3 Encoded Table 1**

Applying R2 to the interobserver agreement (IOA) and treatment fidelity
cells of Swensson et al.\'s Table 1 yields the following EB pairs.
Bounds report the worst-session deviation from the mean. Bounds of zero
indicate single-valued reports without a stated range.

  ------------------------------------------------------------------------------
  **Participant**   **Caregiver    **Researcher   **IOA**         **Social
                    fidelity**     fidelity**                     validity**
  ----------------- -------------- -------------- --------------- --------------
  Alex              (96.33, 7.33)  (100, 0)       (98.25, 18.25)  (69.17, 0)

  Aden              (100, 0)       (100, 0)       (99.33, 19.33)  (100, 0)

  Ida               (100, 0)       (100, 0)       (98.50, 18.50)  (69.17, 0)
  ------------------------------------------------------------------------------

**Table 1.** EB pair encoding of Swensson et al. (2024) Table 1 under
Reading R2. The bound on each IOA cell records the worst-session
deviation observed across sessions monitored for IOA, not measurement
noise estimated from the mean. The bound rail therefore exposes
structure (worst-session 80% IOA across all three children) that the
headline percentages alone do not surface.

**3.4 Digitized Figure 1 --- Corrected Per-Session Phase Summary**

All numerical findings in Sections 4 through 6 derive from a corrected session-level digitization of Swensson et al.'s Figure 1. Version 3 uses the corrected CSV archived with this manuscript. The digitization contains 127 row-level graph readings (62 Alex, 39 Aden, 26 Ida). Of these, 100 rows fall in intervention phases; the primary slack analysis uses the 92 Set 1 intervention rows for which IDKPTM Set 1 and correct-answer values can be read jointly. Eight intervention rows are Set 2 generalization probes and are retained for generalization-related checks but are not included in the primary Set 1 slack table.

The corrected digitization was produced by overlaying calibrated horizontal response guides at y = 0, 1, 2, 3, 4, 5 and vertical session guides along the x-axis, then snapping visible marks to integer response counts on the 0--5 trial scale. A targeted v3 correction rechecked Alex sessions 48--62 with an enlarged calibrated grid because the prior version under-detected late-phase gray correct-answer bars. The Alex correction used x0 = 113.5 px at session 0, x step = 21.42 px/session, y0 = 617.9 px at response 0, and y step = 100.2 px/response. Patched rows were assigned high or medium confidence depending on line/marker overlap. The digitized reconstruction should be read as a published-figure reconstruction, not as author-provided raw trial data.

The digitization was validated against independent prose claims in the source paper: Ida's two baseline sessions with correct responses were recovered at sessions 5 and 8; Aden's mastery at session 39 was recovered as correct = 5 and IDKPTM = 0; Ida's mastery at session 26 was recovered as correct = 5 and IDKPTM = 0. After the v3 Alex patch, the late Alex mastery sequence also aligns with the source report that Alex met mastery by session 60 with 80%--100% correct responses across three sessions.

The corrected per-phase Set 1 intervention summaries are:

| Child | Phase | N sessions | Mean (IDKPTM, correct) | Mean slack |
|---|---:|---:|---:|---:|
| Alex | Intervention Set 1 | 50 | (2.34, 1.82) | 0.84 trials/session |
| Aden | Intervention Set 1 | 28 | (3.25, 1.64) | 0.11 trials/session |
| Ida | Intervention Set 1 | 14 | (0.93, 3.00) | 1.07 trials/session |

**Table 2.** Corrected v3 per-child intervention-phase summary computed from session-level digitization of Figure 1. Means are taken across Set 1 intervention rows only. The primary structural quantity is slack, not the individual response means alone. The corrected data reduce Alex's slack estimate relative to version 2 because late correct-answer bars were recovered.

**4. Finding 1: The Inverse Relationship as a Conserved Quantity**

Swensson et al.\'s discussion paragraph notes a structural pattern
visible in Figure 1: \"The data paths reflect an inverse relationship of
the IDKPTM response and the acquisition of correct answers to
questions.\" The relationship is reported as a qualitative observation.
The EB carrier promotes it to a quantitative conserved quantity at the
session level, and the conservation defect --- the slack --- is itself a
measurement.

**4.1 The Conserved Quantity**

Each session in Swensson et al.\'s design comprises five trials. Per the
procedure, when the child emits the IDKPTM response (independently or
after the prompt), the caregiver provides the correct answer; the trial
is therefore recorded as IDKPTM = 1, correct answer = 0. When the child
answers correctly without the IDKPTM response, the trial is recorded as
IDKPTM = 0, correct = 1. When the child neither emits IDKPTM nor answers
correctly (an incorrect or no response), the trial is recorded as IDKPTM
= 0, correct = 0. The two binary outcomes are mutually exclusive at the
trial level. At the session level, the per-session counts therefore
satisfy:

*e_IDKPTM + e_correct + slack = 5*

where slack ≥ 0 records the trials in the third response class. Encoding
each per-session count as an EB pair and applying EB addition (Section
2.1):

*(e_IDKPTM, b_IDKPTM) ⊕ (e_correct, b_correct) = (e_IDKPTM + e_correct,
b_IDKPTM + b_correct)*

The centre of the sum is bounded above by 5, with equality precisely
when slack = 0. The bound of the sum records the combined
session-to-session variability across the two response classes.

**4.2 What the Slack Measures, with Real Numbers**

Slack at the session level is the count of trials per session that fell into neither the independent IDKPTM-response class nor the independent correct-answer class. In the safest operational wording, slack means: trials with neither independent IDKPTM nor independent correct answering. Under the procedures, these would include incorrect responses, no responses within the response window, or other non-target responses if present. The present digitization does not attempt to subclassify slack internally because the published figure does not separately encode those categories.

The original measurement system reports IDKPTM and correct-answer paths but does not extract the residual term as its own variable. The session-level digitization performed for this paper allows slack to be computed across all 92 Set 1 intervention rows. The corrected v3 per-child distribution is:

| Child | N | Mean slack | Zero-slack sessions | Max slack observed |
|---|---:|---:|---:|---:|
| Alex | 50 | 0.84 trials/session | 25/50 (50.0%) | 5 |
| Aden | 28 | 0.11 trials/session | 25/28 (89.3%) | 1 |
| Ida | 14 | 1.07 trials/session | 6/14 (42.9%) | 4 |

**Table 3.** Corrected v3 slack distribution across Set 1 intervention sessions. Aden produced essentially no slack (mean 0.11 per session, 89.3% zero-slack, maximum one slack trial). Alex's corrected late-phase bars reduce his mean slack to 0.84 and raise his zero-slack rate to 50.0%. Ida remains the faster-mastery but higher-slack case (mean 1.07, 42.9% zero-slack). Thus, the v3 pattern is not that Alex and Ida are equivalent; it is that Aden is the near-zero-slack case, while Alex and Ida retain substantially more residual response space.

The clinical reading is that Aden's transition from the trained mand to the correct intraverbal was nearly clean trial-by-trial throughout intervention. Alex and Ida showed more residual response space, but the v3 correction makes Alex less slack-heavy than the earlier digitization suggested. Two children can reach the same correct-answer mastery criterion while differing sharply in how much of the intervention path is carried by residual slack. That difference is the EB-visible quantity.

**4.3 Why the Slack Rate Is a Treatment Outcome**

From the perspective of stimulus control, slack rate distinguishes two
kinds of mastery. A child who reaches the mastery criterion on correct
answers with low slack throughout the intervention has demonstrated
clean transition: every trial elicited either the trained mand or the
correct intraverbal, and the inverse-relationship structure that
Swensson et al. describe holds tightly. A child who reaches the same
mastery criterion with high slack across intervention has demonstrated a
noisier acquisition: some proportion of trials elicited neither the mand
nor the correct answer, and the residual was absorbed into the third
class. All three children met the mastery criterion. Their
response-system profiles differ sharply on slack rate, with Aden carrying the cleanest near-zero-slack path.

The clinical implication is that the slack rate is a candidate fidelity
indicator for the IDKPTM-response acquisition itself. A
behavior-analytic researcher reading Swensson et al. with the EB-sum
reading available has access to an additional outcome measure ---
third-class response rate --- that the published analysis does not
separately report. Aden's mean slack (0.11) is approximately one-eighth of Alex's corrected mean slack (0.84) and approximately one-tenth of Ida's (1.07). That contrast is one of the clearest cross-child structural differences in the dataset,
and it is invisible at the level of mean correct-answer rate.

**4.4 What the Alternatives Cannot Do**

Standard descriptive-statistics reporting handles each response class
separately. The mean correct rate is reported; the mean IDKPTM rate is
reported; their relationship is described qualitatively. Gaussian
root-sum-square aggregation across sessions cannot represent the
conservation constraint because the constraint is structural, not
stochastic. Interval arithmetic can represent the per-session sum but
cannot maintain a centre under repeated propagation, and the constant ≤
5 constraint is not naturally a parity-1 interlocking. The EB carrier\'s
zero-parity admissibility (Martin 2026, Chapter 6) is what makes the
per-session sum a closed object that can be propagated and compared.

**5. Finding 2: EB-Operationalized Response-System Stability**

**5.1 Operationalisation**

Swensson et al. argue, in the discussion paragraph, that the IDKPTM
response \"came under appropriate stimulus control of not knowing the
answer.\" The evidentiary basis is the inverse relationship --- as
children mastered specific questions, they ceased to mand for the
answers to those questions. The argument is made at the level of the
dataset as a whole. It does not localise response-system stability to a session number for any child.

The EB carrier permits an operational stability reading. Define EB-operationalized response-system stability as
the first session s\* such that for all sessions s ≥ s\*, the bound on
the session-level sum (e_IDKPTM + e_correct, b_IDKPTM + b_correct) drops
below a threshold τ and stays below. Operationally, the threshold is set
so that the hull of the sum lies entirely above some value v_min ---
meaning that the child reliably produces either the trained mand or the
correct intraverbal (and not the third class) on most trials. The
session s\* is the earliest session from which this lower-bound
stability persists.

Concretely: with five trials per session, set τ = 1.0 (no more than one
third-class trial per session) and v_min = 4.0 (at least four of the
five trials produce a target response of either kind). The session at
which (e_IDKPTM + e_correct − b_IDKPTM − b_correct) first crosses 4.0
and stays above 4.0 for the remainder of intervention is the operational
response-system stability point for that child.

**5.2 Computed Stability Points from the Corrected Digitized Data**

Applying the operational criterion to the session-level digitized data
with τ = 1.0 (lower bound on the conserved sum at least 4 of 5 trials)
yields the following stability points:

- **Aden:** 39 total sessions; stability session **10**; stability coincides with intervention start.
- **Ida:** 26 total sessions; stability session **15**; stability occurs four sessions into intervention.
- **Alex:** 62 total sessions; stability session **53**; stability appears late, after the v3 correction recovered late correct-answer bars.

**Table 4 summary.** EB-operationalized response-system stability per child, computed against the
operational criterion on session-level digitized data. Aden's response system met the stability criterion immediately upon transition from teaching to intervention; the conserved sum stabilized at the first intervention session and never relaxed. Ida met the stability criterion four sessions later, at session 15, after a brief ramp during which she was producing some
baseline-residual responding. Alex satisfies the strict criterion only late, at session 53, after the v3 correction recovered late-phase gray correct-answer bars. Before session 53 his response system remains variable, including a notable slack spike at session 52.

The Alex-late-stability finding is itself a structural result. Alex did reach the
content-mastery criterion (60 sessions to mastery on Set 1 correct
answers), but he reached it after a more variable and later-stabilizing path than Aden and Ida achieved. His session-to-session variability
on the conserved sum stays high through the entire intervention; his
slack rate (Section 4) reflects the same underlying structure. The
standard SCED mastery-criterion lens does not surface this distinction
--- Alex looks like a third successful case, comparable to Aden and Ida.
The bound-rail reading exposes that his trajectory to mastery has a
different shape: more sessions, higher within-session variability, and
residual slack that persists longer before late stabilization.

**5.3 Why This Quantity Did Not Exist Before**

The descriptive-statistics framework cannot define this response-system stability point as a measurable session-level event because it has no algebra
under which IDKPTM rate and correct-answer rate are jointly propagated
against a per-session constraint. Visual analysis of multiple-baseline
graphs supplies the inverse-relationship pattern; it does not support
the claim \"the conserved IDKPTM/correct-answer response system stabilized by session 10 for Aden.\" That claim requires the EB-sum bound rail to be tracked
across sessions, and it requires the per-session conservation constraint
to be encoded as a structural fact. Both are EB-carrier-specific.

The clinical implication is direct. A field that can locate
response-system stability to a session can perform dose-response analysis
on ABA interventions in a way it cannot today. The number of sessions
required to establish response-system stability --- distinct from the number of sessions required to reach a content-level mastery criterion --- is a
measurable intervention parameter. Comparing it across protocols,
prompt-delay schedules, target-set sizes, and child-baseline
characteristics is a research programme the EB-carrier framework opens.

**6. Finding 3: Aden\'s Six-Week Break as a Quantified Maintenance
Probe**

**6.1 The Natural Experiment in the Methods, with a Caveat the
Digitization Forced**

Swensson et al. report that Aden\'s intervention paused for six weeks at
the caregiver\'s request. The paper marks the gap with an asterisk in
Figure 1 and treats it as a methodological complication: the gap
occurred within intervention, after the IDKPTM response had been
acquired but before mastery on correct answers was reached. The
discussion does not extract a maintenance result from the gap.

From the EB carrier\'s perspective, the six-week gap is a natural
maintenance-of-acquired-skill measurement embedded within a
multiple-baseline study. Pre-break, Aden had been responding with IDKPTM
at 80--100% across many consecutive sessions. Post-break, the first
sessions reveal whether the response has been maintained across a
six-week absence with no programmed maintenance contingencies.

The session-level digitization performed for this paper requires that
this finding be qualified more carefully than the figure-eyeballed v1 of
this paper acknowledged. Aden\'s IDKPTM rate was already declining in
the sessions immediately before the break --- sessions 30, 31, 32 give
IDKPTM counts of 2, 2, 4 (40%, 40%, 80%) --- as he transitioned from the
trained mand to correct answering on the items he had learned. The
pre-break window is therefore not a stable asymptote against which
post-break performance can be cleanly compared. It is a sample of an
actively declining trajectory.

With this caveat acknowledged, the EB difference is still computable and
still informative. It reads as the interruption of an active learning
curve rather than the interruption of a stable plateau.

**6.2 The EB Difference Calculation, with Digitized Values**

Encode pre-break performance from the three sessions immediately
preceding the break (sessions 30--32) under Reading R1:

*Pre = (60, 20) --- IDKPTM percentages 40%, 40%, 80%; midpoint 60,
half-range 20*

Encode post-break performance from the three sessions immediately
following the resumption (sessions 33--35):

*Post = (40, 0) --- IDKPTM percentages 40%, 40%, 40%; midpoint 40,
half-range 0*

The EB difference, computed via signed scalar multiplication and
addition:

*ΔAden = Post ⊕ ((−1) ⊙ Pre) = (40, 0) ⊕ (−60, 20) = (−20, 20)*

The hull of ΔAden is *\[−40, 0\]*, a signed interval whose right edge
sits at zero. The reading: Aden\'s post-break IDKPTM rate dropped by
approximately 20 percentage points relative to his pre-break window,
with a bound that does not admit any gain (the upper edge is exactly
zero) and admits up to a 40-point decline. Six weeks without programmed
maintenance produced measurable decrement; the response was not lost,
but it had clearly weakened. This is a six-week retention result with a
quantified bound --- qualified by the pre-break-already-declining
structure noted above.

**6.3 The Sign Rail Activates Here**

The difference calculation produces a negative centre (−20). All
percentages in Swensson et al.\'s data are non-negative, placing the raw
data on the U/N substrate-pair carrier ℝ≥0 × ℝ≥0. Differences between
two non-negative percentages are signed and live on the full EB carrier
ℝ × ℝ≥0. This is the structural location at which the EB carrier\'s
distinguishing property --- non-involution of the flip operator B
(Martin, 2026, Chapter 7) --- activates.

Interval arithmetic on Pre = \[40, 80\] and Post = \[40, 40\] gives the
difference interval \[40 − 80, 40 − 40\] = \[−40, 0\], which matches the
EB hull but loses the centre. Gaussian root-sum-square is structurally
inappropriate (the IDKPTM rate is a binomial proportion bounded in
\[0,1\] with five trials per session, and the Gaussian assumption fails
at the boundary). The EB pair (−20, 20) preserves both the centre
(interpretable as the maintenance decrement under the active-decline
qualification) and the bound (interpretable as the worst-case observed
deviation), without distributional assumption.

**6.4 What This Adds to the Field, Honestly Stated**

The maintenance-of-mand-for-information literature is sparse.
Maintenance probes after intervention discontinuation are typical
components of a maintenance-design study but rare as incidental
measurements within an acquisition study. Swensson et al.\'s Aden-break
is precisely such an incidental measurement, made interpretable by the
EB difference calculation. The field gains a published six-week
maintenance datapoint for caregiver-implemented telehealth-coached
IDKPTM training in a child with ASD aged 7 --- quantified, with bound
--- that previously sat in the figure as an unremarked phase change. The
active-decline qualification means this datapoint should be treated as a
lower bound on retention quality rather than as a clean maintenance
probe; a more conservative reading of the same data is possible (e.g.,
comparing post-break performance against a pre-break window further back
in the trajectory where IDKPTM was at full strength), and that reading
would yield a larger decrement with a wider bound.

The general method extends. Any incidental gap, missed-session sequence,
or scheduling break in a published SCED study contains a similar
embedded maintenance measurement. Systematic identification across the
SCED literature would yield maintenance datapoints at gap-length
variations from days to months, accumulated as a meta-analytic resource
without any new data collection. The qualification noted here --- that
pre-break performance must itself be checked for stability before the
difference is interpreted as maintenance --- is a methodological
discipline the EB framework requires but does not by itself enforce.

**7. Finding 4: Cross-Child Learning-Rate Ratios with Procedural
Cancellation**

**7.1 The Cancellation Theorem and Its Specialisation**

Proposition 28.2.1 of Martin (2026) establishes that under the
four-property intersection --- magnitude observable, shared latent
factor, ratio observable, intercept-type operationalisation --- the
centre of the EB ratio of two pairs that share a multiplicative latent
factor θ is independent of θ. Formally:

*If e_u = θ · f_u and e_v = θ · f_v, then e\_(u⊘v) = f_u / f_v, ∂e_ξ/∂θ
= 0.*

The bound of the ratio depends only on the input magnitudes and bounds:

*b\_(u⊘v) = \|e_u\| · b_v / e_v² + b_u / \|e_v\| + b_u · b_v / e_v²*

Applied to Swensson et al.\'s three-child design: each child\'s
time-to-mastery on Unknown Set 1 is a function of (a) the shared
procedural protocol --- prompt-delay schedule, trial structure, praise
contingency, screen-shared questions, researcher coaching fidelity
(which was 100% across all three children) --- and (b) child-specific
factors, including baseline intraverbal repertoire, age, and family
context. Denoting the shared procedural contribution as θ and the
child-specific contribution as f_child, each mastery time decomposes (in
the centre of the EB pair) as:

*e_mastery,child = θ · f_child*

The ratio of any two children\'s mastery times therefore cancels θ
exactly:

*e\_(mastery,A ⊘ mastery,B) = (θ · f_A) / (θ · f_B) = f_A / f_B*

The cancellation does not require θ to be actually constant across
children --- only that it enters numerator and denominator in the same
algebraic position. Caregivers who implement with different fidelity
profiles, sessions of different durations, prompt-delay timing
variations within the protocol --- these all enter as multiplicative
components of θ, and they all cancel.

**7.2 The Computed Ratios**

Encoding mastery sessions as EB pairs with bound b = 5 (covering
target-reduction-timing variation across the three children, plus the
six-week break for Aden):

  ------------------------------------------------------------------------
  **Ratio**    **Centre e_ξ**   **Bound b_ξ**       **Hull**
  ------------ ---------------- ------------------- ----------------------
  ξ_Aden /     39 / 60 = 0.65   0.054 + 0.083 +     \[0.51, 0.79\]
  Alex                          0.007 = 0.144       

  ξ_Ida / Alex 26 / 60 = 0.43   0.036 + 0.083 +     \[0.30, 0.56\]
                                0.007 = 0.126       

  ξ_Ida / Aden 26 / 39 = 0.67   0.085 + 0.128 +     \[0.44, 0.90\]
                                0.016 = 0.229       
  ------------------------------------------------------------------------

**Table 4.** Cross-child mastery-time ratios under EB division, exact
regime λ = 1. Bound calculations follow Proposition 28.2.1 (Martin,
2026). The bound terms break down as \|e_u\|·b_v/e_v²
(numerator-magnitude × denominator-bound, scaled by squared
denominator), b_u/\|e_v\| (numerator-bound × inverse denominator), and
b_u·b_v/e_v² (cross term). The hulls are the symmetric intervals \[e_ξ −
b_ξ, e_ξ + b_ξ\].

**7.3 What the Ratios Say**

Aden mastered Unknown Set 1 in 51% to 79% of Alex\'s session count. Ida
mastered in 30% to 56%. Ida mastered in 44% to 90% of Aden\'s session
count. These ranges describe child-specific intraverbal-acquisition
rates with the shared procedural protocol algebraically removed from the
centre of comparison.

The structural reading: child-specific learning-rate variation is
roughly a factor of 2 to 3 across these three cases. This magnitude is
comparable to the intervention effect itself (the difference between
mastery and baseline non-responding). The implication for ABA practice
is that for caregiver-implemented telehealth-coached IDKPTM training in
this age range, the variance attributable to child-side variables is
structurally co-equal with the variance attributable to the
intervention.

**7.4 Why the Cancellation Is Inaccessible to the Alternatives**

Gaussian root-sum-square for ratio uncertainty under the delta method
does not preserve the cancellation structure: it treats numerator and
denominator as independent random variables and accumulates a residual
contribution from the shared factor at order √2 · σ_θ / θ in the bound.
For Swensson et al.\'s data, the σ_θ contribution is unidentified ---
the Gaussian framework has no decomposition that separates the shared
procedural contribution from child-specific contributions. Interval
arithmetic preserves the cancellation in the centre (positive-interval
division is exact) but at the cost of post-operation admissibility
repair and the parity-1 interlocking, neither of which scales to longer
chains. Affine arithmetic preserves the cancellation explicitly through
dependency tracking but accumulates auxiliary state across operations,
failing the constant-time stateless propagation of axiom A6 in Martin
(2026).

The EB carrier\'s cancellation is structural rather than book-kept. The
shared factor cancels because the centre rail of the EB ratio depends
only on the centres of numerator and denominator (Proposition 28.2.1),
and the bound rail depends only on magnitudes --- not on covariance, not
on dependency history, not on auxiliary parameters. The cancellation is
what the algebra natively does.

**7.5 Generalisation to Meta-Analytic Reanalysis**

The method extends directly to multi-study meta-analytic settings. Apply
the EB division to mastery-time pairs across studies sharing a common
procedural protocol --- for example, all Ingvarsson-style
IDKPTM-training studies --- and the shared protocol cancels at every
pairwise ratio, leaving child-specific (or in cross-study comparisons,
sample-population-specific) acquisition rates. Aggregating these
residuals across the literature constructs an empirical distribution of
intraverbal-acquisition rates in children with ASD, indexed by age,
baseline verbal repertoire, and any other available covariates, with the
cross-study procedural variance algebraically backed out. This is a
meta-analytic capability the field does not currently possess.

**8. Methodological Note: The Measurement / Inference Boundary**

The four findings in Sections 4 through 7 are all measurement-layer
results. The EB carrier propagates measurement bounds through
arithmetic; it does not perform statistical inference. This boundary is
structural, not stylistic, and it warrants explicit statement.

**8.1 What the EB Carrier Does and Does Not Do**

The EB carrier does the following:

-   Propagates measurement bounds through addition, multiplication,
    scalar multiplication, division, and chained arithmetic, with
    constant-time complexity per operation and no auxiliary state.

-   Surfaces conserved quantities (such as the per-session response sum
    of Section 4) as algebraic objects with quantified bounds.

-   Cancels shared multiplicative factors in the centre rail under ratio
    operations (Section 7), without requiring those factors to be known
    or estimated.

-   Encodes signed residuals (such as the maintenance decrement of
    Section 6) on the full carrier ℝ × ℝ≥0 with the sign rail intact.

The EB carrier does not do the following:

-   Perform statistical inference or hypothesis testing. It produces no
    p-values, no confidence intervals (in the Neyman-Pearson sense), no
    effect size estimates, and no significance assessments.

-   Model temporal dynamics, autocorrelation, learning trajectories, or
    change points. The findings of Section 5 (response-system stability)
    describe what the bound rail shows at each session, not what
    time-series methods would infer about underlying state transitions.

-   Replace standard SCED analysis methods such as visual analysis,
    Tau-U, multilevel modeling, or piecewise regression. Those methods
    continue to operate on the centre values; the EB carrier supplies a
    measurement-bound layer beneath them.

-   Detect treatment effects. Effect detection is an inferential
    question; the EB carrier supports it by quantifying measurement
    uncertainty propagated to the comparison, but the inferential step
    itself remains within standard methodology.

**8.2 The Self-Correction Record, Now Including a Second Iteration**

This scope discipline was clarified through self-correction in October
2025 (Martin, 2025; Zenodo deposit 17222201). In an initial application
of the precursor framework (N/U Algebra) to Swensson et al.\'s data, I
attempted what I called a \"gap effect analysis\" producing reported
level and slope changes with associated p-values around Aden\'s six-week
break. The category error was direct: I had used a measurement-layer
propagation tool to perform inferential time-series analysis. The errors
specifically were (a) using N/U Algebra to detect temporal trends and
produce p-values, beyond its mathematical scope; (b) writing imprecise
language about session weighting that misrepresented how the algebra
operates; (c) attempting to use uncertainty bounds within a
permutation-based statistical framework, treating propagated bounds as
if they were regression weights.

The correction process took 48 hours, with deliberate temporal
separation between the initial conclusion and the re-examination, and
external computational review before submission of the corrected
analysis. The corrected paper restricted N/U Algebra to
measurement-level uncertainty quantification and eliminated all claims
about statistical inference, trend detection, or effect-size estimation.

The present paper continues that scope discipline and adds a second
instance of it. Version 1 of this paper, drafted from the prose
summaries of Swensson et al.\'s Figure 1 without per-session data
extraction, contained figure-derived estimates that were structurally
correct but quantitatively imprecise. The pre-break window for Aden was
characterised as (90, 10) --- IDKPTM at 80--100%, drawn from the
discussion paragraph\'s description of his early-intervention asymptote
rather than from the actual three-session window immediately before the
break. The session-level digitization performed for version 2 of this
paper (described in Section 3.4) revealed that Aden\'s IDKPTM rate was
already declining in the immediate pre-break window (40%, 40%, 80%
across sessions 30--32), making the v1 framing of the maintenance probe
overstated. Version 2 corrects the encoding and acknowledges the
pre-break-already-declining structure as a limitation of the
maintenance-probe interpretation. The same scope-discipline pattern as
October 2025 --- extract, examine, correct, document --- operates here,
applied to a more local methodological imprecision rather than a
category error.

The four findings reported in this version remain measurement-layer
results. Section 6 reports a quantified maintenance decrement (−20, 20)
for Aden\'s six-week break with the active-decline qualification; it
does not test whether the decrement is statistically distinguishable
from zero under any inferential framework. Section 7 reports cross-child
mastery-time ratios with their hulls; it does not perform a
null-hypothesis test on the differences between children. Section 5
reports response-system stability points computed from the digitized data against
an explicit operational criterion; it does not claim those onsets as
inferentially validated change points.

**8.3 The Two-Layer Architecture**

The proper relationship between the EB carrier and standard SCED
analysis is layered. The measurement layer (EB carrier) takes raw
observations with their explicit bounds and propagates those bounds
through whatever arithmetic the analysis requires --- sums, ratios,
differences, aggregates. The output is a set of EB pairs, each with a
centre and a bound, ready for inferential treatment. The inference layer
(standard SCED methodology) takes those EB pairs and applies the
appropriate analytical tools --- visual analysis for treatment effect,
Tau-U or piecewise regression for trend detection, multilevel modeling
for between-child variation. The two layers do not compete; they
compose.

Misapplying the measurement layer to inferential questions --- as I did
in October 2025 before correction --- produces results that look
statistical but are not. Misapplying the inference layer to
measurement-bound propagation --- for example, by running Gaussian
aggregation through an SE-of-the-mean calculation that assumes IID
independent measurement error across heterogeneous caregivers ---
produces bounds that are anti-conservatively narrow. Both errors are
common and both are avoidable when the layers are kept distinct.

**9. Discussion**

**9.1 What This Paper Demonstrates**

The four findings demonstrate that single-case experimental design data
routinely encode structure that the field\'s standard summary
conventions cannot extract. Each finding draws on the same dataset
Swensson et al. (2024) collected, published, and analysed; each finding
describes a quantity that is present in their data and absent from any
current report. The instrument for extraction is the EB carrier, an
algebra with closed operations, axiomatic uniqueness within a precisely
stated complexity class, and 70,054 trials of deterministic numerical
validation in its first-order regime (Martin, 2025) and full regime
(Martin, 2026).

The findings are not improvements on Swensson et al.\'s analysis. The
conclusions reached by Swensson et al. --- that caregivers can be
coached via telehealth to teach children with ASD to mand for
information, that the IDKPTM response generalised across children, that
the procedure was rated socially acceptable --- are well-supported by
the methods they used and remain unchanged after the present analysis.
What the present analysis adds is a set of additional outcome measures
and structural readings that the original methods could not have
produced even in principle, because the algebra required to produce them
did not exist in publishable form when the original paper was written.

**9.2 Implications for Systematic Reanalysis**

The dominant practical implication is that the published SCED literature
contains a substantial body of extractable but currently uncomputed
quantities. Each multiple-baseline study with sessions of fixed trial
count contains conserved-quantity readings of the kind in Section 4.
Each intervention with a clear acquisition phase contains
stimulus-control-onset estimates of the kind in Section 5. Each study
with incidental between-session gaps contains embedded maintenance
probes of the kind in Section 6. Each multi-participant study sharing a
procedural protocol contains shared-factor cancellations of the kind in
Section 7. None of these requires new data collection. All of them
require the EB-carrier framework or its first-order N/U Algebra
precursor to be applied to existing published figures and tables.

Systematic reanalysis at the literature scale would proceed by
digitising published SCED figures (a task with established methodology
and tools), applying the four extraction operations, and aggregating
across studies. The aggregated outputs would constitute a new tier of
meta-analytic resources for ABA: stimulus-control-onset distributions,
maintenance-decrement distributions across gap lengths, and
child-specific learning-rate distributions cleaned of
procedural-protocol contributions. None of these resources currently
exists in the field.

**9.3 What This Paper Does Not Claim**

The paper does not claim that the EB carrier is necessary for all SCED
analysis. The standard descriptive-statistics framework remains
appropriate for many research questions. The paper does not claim that
the four findings here are clinically more important than the
conclusions Swensson et al. reached; clinical importance is determined
by treatment outcomes, not by methodological extractability. The paper
does not claim that the EB carrier replaces inferential statistics; it
explicitly maintains the measurement / inference layer separation of
Section 8. The paper does not claim that the digitization-extracted
values of Sections 4 through 6 are quantitatively final; author-provided
trial-level data, if released, would refine the count-level extraction
by recovering within-session ordering and trial-by-trial set
attribution, and the present paper records the digitized integer counts
as the best available reconstruction at session resolution.

**9.4 Acknowledgement of the Source Study**

The four findings rest on the quality of Swensson et al.\'s underlying
data collection. Their interobserver agreement above 98% on aggregate,
their treatment fidelity at or near ceiling, their clear coding scheme,
and their transparent reporting of session structure made the present
extraction possible. A study with weaker measurement quality would not
support the per-session bound-rail readings that Sections 4 and 5
require, and a study with less clearly described procedural protocol
would obscure the shared-factor cancellation of Section 7. The present
analysis is enabled by the quality of the source study, not despite any
deficiency of it.

**10. Limitations**

Four limitations are explicit.

**First,** the session-level data used in this paper are extracted from
the published figure, not author-provided trial-level records. Version 2
of this paper digitized Swensson et al.\'s Figure 1 to integer trial
counts on the 0--5 scale, validated the extraction against three
independent prose claims in the source paper (Ida\'s two baseline
correct responses at sessions 5 and 8; Aden\'s mastery at session 39;
Ida\'s mastery at session 26), and confirmed that all 100 intervention
sessions satisfy the per-session sum constraint. The extraction is
reproducible from the published figure with the calibration parameters
reported in Section 3.4 and the digitization script archived alongside
this paper. Author-provided trial-level data, if released, would refine
the count-level extraction by recovering the within-session ordering of
trial outcomes and the trial-by-trial Set 1 vs. Set 2 attribution; the
structural findings of Sections 4 through 7 do not depend on that
refinement, but the slack-rate within-session distributions of Section 4
and the stimulus-control-onset criterion of Section 5 would gain
finer-grained variants under trial-level data.

**Second,** the four-property intersection\'s intercept-type clause is
satisfied softly, not formally. SCED is not a generalised-least-squares
regression; it does not return its estimates at a fitted intercept of a
regression chain, and it does not minimise a chi-squared functional. The
shared-factor cancellation of Section 7 operates on the algebraic shape
of the comparison (centre depends only on centres; bound depends only on
magnitudes) rather than on a formally instantiated GLS structure. The
cancellation is therefore qualitative in its bound consequences (the
centre cancellation is exact) rather than quantitative in the strong
sense developed in Martin (2026, Chapter 29) for the cosmological
application.

**Third,** N = 3 is a clinical replication, not a statistical sample.
The cross-child ratios of Section 7 describe pairwise comparisons among
the three children Swensson et al. studied; they do not estimate
population parameters, and they do not support inferential
generalisation to the broader population of children with ASD. Section
9.2 outlines the systematic-reanalysis programme that would aggregate
across studies to construct population-level distributions; that
programme is future work, not a claim of the present paper.

**Fourth,** the encoding choices in Section 3 are decisions, not
derivations. Reading R2 (mean-centred bound-loosened) preserves the
reported mean and absorbs asymmetry into the bound; Reading R1
(range-faithful) preserves the range exactly and discards the mean. Both
are admissible under the EB-carrier framework; the choice is a
methodological decision about which information to preserve. Different
downstream applications may favour different readings, and replication
of the findings under alternative encodings is straightforward but
unperformed in the present paper.

**References**

Ingvarsson, E. T., & Hollobaugh, T. (2010). Acquisition of intraverbal
behavior: Teaching children with autism to mand for answers to
questions. *Journal of Applied Behavior Analysis, 43*(1), 1--17.
https://doi.org/10.1901/jaba.2010.43-1

Martin, E. D. (2025). *The NASA Paper & Small Falcon Algebra.* Zenodo.
https://doi.org/10.5281/zenodo.17222201

Martin, E. D. (2025). *The NASA Paper & Small Falcon Algebra --
Numerical Validation Dataset* \[Dataset\]. Zenodo.
https://doi.org/10.5281/zenodo.17221863

Martin, E. D. (2025). *Quantifying Telehealth Behavioral Measurement
Reliability Using N/U Algebra: A Validation of Swensson et al. (2024).*
Zenodo. \[Predecessor methodological paper documenting the N/U → EB
transition and the October 2025 self-correction.\]

Martin, E. D. (2026). *The Expressed--Bound Carrier: Axiomatic
Uniqueness, Cayley--Dickson Lifts, and Categorical Universality.*
\[Manuscript in preparation.\] Memoirs-format monograph developing the
full axiomatic characterisation, the four-property intersection
cancellation theorem, and the structural validation harness.

Swensson, R. M., Akers, J. S., Austin, M., Liu, R., Swafford, L. B., &
Gerow, S. (2024). Teaching children with autism spectrum disorder to
mand for answers to questions via telehealth: A caregiver
implementation. *Behavioral Interventions, 39*(3), e2015.
https://doi.org/10.1002/bin.2015

**Acknowledgments and Disclosures**

I thank Dr. Remington Swensson for the original empirical work that made
this analysis possible, and for prior correspondence in October 2025
that contextualised the data. Dr. Lee William Daffin is acknowledged for
referral guidance during the development of the precursor framework. The
October 2025 self-correction process documented in Section 8.2 was
supported by external computational review; specific reviewers are not
named at their request.

The author has no financial conflicts to disclose. The EB carrier
framework and its precursor N/U Algebra are released under permissive
open-source licences with full validation harnesses publicly archived
(Zenodo deposits 17221863 and 17222201). No patents are sought or held
on the framework. The author is an independent researcher with no
institutional affiliation funding this work.

All numerical computations in Sections 3 through 7 of this version were
performed against the formulas of Section 2 and Proposition 28.2.1 of
Martin (2026), using session-level values extracted by digitization of
Swensson et al.\'s Figure 1. The digitized dataset is archived alongside
this paper as a supplementary CSV (127 rows, columns: child, session,
phase, idkptm_set1, idkptm_set2, correct, sum, slack). Author-provided
trial-level data, if released by the original investigators, would
refine the count-level extraction without altering the structural
findings.
