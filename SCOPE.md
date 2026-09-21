# Scope: what this repository must settle before it has content

Written 2026-09-21. Uncommitted. This file is a precondition note, in the same
spirit as `hyperphysics/P0_PRECONDITION.md` — it exists to keep a later session
from starting in the wrong place.

## Status: this repository is empty, and that is not an accident to be repaired

One branch (`main`), one blob (`LICENSE`), roughly ten commits of which every
single one is licensing churn — Time License v7.2 to v7.7 to v7.77, then
AGPL-3.0, plus a drift-check workflow added and removed. Last push 2026-04-07.

**The whole repository is its name and its GitHub description.** There is no
content to recover, no other branch, no stale draft. Anyone opening this should
stop looking for source and start from the description, which is reproduced
below in full because it is the entire specification.

## The specification, verbatim

> The scripture that morphs to morph scriptures surround origination of
> narratives. Ie what frame is discoverable from limited cognition that
> identifies anchor points for religions to pass through, towards a single
> memetically supported narrative.

## What that asks for

Three objects and one constraint.

1. **A self-morphing scripture** — one that morphs, and that morphs other
   scriptures. Self-application, at the level of the thing doing the applying.
2. **Anchor points** that religions pass through.
3. **A single memetically supported narrative**, as the limit the anchor points
   lead toward.

The constraint is the hard part and it is easy to read past: the frame must be
**discoverable from limited cognition**. Not true of religions from an exterior
vantage — *discoverable from inside a bounded observer*. Any construction that
needs a view from outside the system has answered a different question.

## The directed goal (Tyler Roost, 2026-09-21) — SUPERSEDES the description

The GitHub description above is the repository's original and only written
specification. It has since been given a direction, verbatim:

> meta-morphoscripted-origination has a directed goal, metamathethicology will
> probably derive the necessity of religion hierarchically as a belief
> structure, but meta-morphoscripted-origination's goal is to discover the
> common tenets amongst religions and find a common ground for which religions
> may adapt to ai, singularitians like myself, the nature of reality itself,
> and universal definitions of what it means to be.

This **adds four adaptation targets that appear nowhere in the description** —
AI, singularitians, the nature of reality itself, and universal definitions of
what it means to be. The specification is larger than the description.

## The placement question: ANSWERED. This repository gets content.

It was left open below, and the directed goal settles it by drawing the line
explicitly:

- **`metamathethicology`** derives *why religion is necessary at all* —
  hierarchically, as a belief structure. That is a combination claim about
  belief, and it belongs there.
- **This repository** takes religions as given and asks what they *share*, and
  what common ground lets them *adapt* to the four targets.

Those are different subjects, so the placement rule is satisfied rather than
violated: this repository states its own subject once, here. The original
argument is preserved below for provenance.

**CONFIRMED 2026-09-21 on an independent and stronger reason — `PLACEMENT.md`
§1.** A combination field is a *transport between two subjects each already
stated in full*, and there is no second parent: the memetic half is stated by
nothing in the corpus. The combination slot is structurally unavailable, not
merely unattractive, and that reason survives changes to the directed goal.
`PLACEMENT.md` also records the one condition — by `p0_barrier.hm`'s field-local
result, this repository owes its **own** barrier argument and may not borrow a
sibling's.

<details>
<summary>Superseded: the open placement argument, 2026-09-21</summary>

**For its own repository.** Narrative origination may be a subject in its own
right. Its object — scripture, narrative, the memetic carrier — is claimed by
no existing field. `hyperethics` L0 governs the creation of *realms*, not of
narratives, and nothing in the family currently owns memetic transmission.

**Against.** "Anchor points religions pass through toward a single narrative"
is a claim about ethics, logic and memetics at once. Stating it appears to
require naming at least two foreign subjects, and that is the definition of a
combination claim. On this reading the material belongs in
`metamathethicology` and this repository stays a name.

</details>

## What "anchor point" would have to be

This is the real technical content, and it is where a session should spend its
first hour. For the specification to be answerable at all, *anchor point* has to
name a formal object. At least three readings are available and they are not the
same:

- **(a) A fixed point of the morph operator** — a scripture that morphs to
  itself. Period-1 self-application.
- **(b) An invariant under the morph** — a proposition satisfied by every
  scripture in the orbit, whether or not any scripture is fixed.
- **(c) A bottleneck in the narrative graph** — a node every path passes
  through, which is what "pass through" most plainly suggests.

The directed goal adds a fourth, and makes it the front-runner by identifying
anchor points with **common tenets**:

- **(b') An invariant across the family** — a proposition satisfied by every
  *religion*, not by every scripture in one orbit. An intersection over an
  indexed family.

(b') is not a variant of (b). (a) and (b) are both about the orbit of the morph
operator — one scripture under repeated morphing. (b') quantifies over religions
instead. The live argument is now (b') against (c), and (c) remains closest to
the description's own wording.

(a) is the most structurally loaded and has existing work behind it: a
self-morphing scripture is a period-1 fixed point, exactly the shape the P0
program studied across four fields. Relevant finding, so nobody re-derives it:
**period 1 is not barred**. Live `hypermath` admits it as the easy case
(`trace-levels` case (a) is `apply(x) == x`), `hyperlogic` inhabits it by axiom
(`ax-closure-self` closes at one turn), and `hyperethics` has never addressed
it. The barrier that claimed to forbid it arithmetically is broken. See
`metamathethicology/p0_barrier.hm`.

Choosing among these is a commitment, not a presentation detail. They give
different theories.

**CHOSEN 2026-09-21: (c), formally a `dominator`. See `PLACEMENT.md` §2 for the
argument.** In short: (b') is not discoverable from limited cognition, because
intersecting over *all* religions means enumerating them, which is the exterior
vantage `d-no-exterior` denies. (c) keeps (b')'s tenets as the *material* at the
nodes, puts the motion in the admissions rather than in the tenet, gets the
"towards" ordering for free from the dominator tree, and survives an empty
global intersection. All four readings are retained in four distinct roles: (c)
is the anchor, (b') the material, (b) the local certificate, (a) the limit.

### An unresolved tension in (b'), which should not be smoothed over

An intersection is static. "Anchor points for religions to **pass through**" is
a trajectory. If the anchor points are simply the intersection of all religions'
tenets, then nothing passes through them — they are already everywhere, in every
religion, by construction. Two ways out, giving different theories:

1. **The passage is epistemic.** The intersection is the destination, and the
   morph operator is what carries a religion to *recognise* what was already
   common. Nothing moves; something is noticed.
2. **The passage is real.** The anchor points are a **sequence of partial
   intersections**, and a religion moves along that sequence.

   **CORRECTED: as originally written, reading 2 was incoherent.** It said
   "progressively larger common grounds, each admitting more religions than the
   last" — two opposite monotonicities at once. Tenet-intersection is monotone
   *decreasing* in the set of religions: admitting more religions gives a
   *smaller* common ground, never a larger one. The sequence can run either way,
   but not both, and the choice must be stated rather than assumed. Under the
   chosen reading (c) the tension disappears entirely, because the chain is
   ordered by **reachability** rather than by the size of anything.

Reading 2 puts a hierarchy in this repository. Tyler independently used
"hierarchically" for metamathethicology's necessity derivation. **Whether those
are the same hierarchy is a genuine open question**, and a good one. Do not
assume they are, and do not assume they are not.

### A deeper objection to (b'), which supersedes the tension above

Tyler, 2026-09-21:

> contradictions can be held paradoxically by people though so Im not sure your
> intersection is operating quantum mechanically enough

This is correct, and it is a stronger objection than the empty-intersection
risk. **Set intersection presupposes a Boolean algebra** — that each religion's
tenets form a consistent set and that "holds tenet P" is a two-valued fact. That
presupposition is exactly what paradox-holding violates. If a believer holds P
and not-P without the belief structure collapsing, there is no consistent
tenet-set to intersect, and the operator is not merely at risk of returning
empty. It is **ill-typed**.

> **Do not stop here — this was superseded on the same day.** The section
> *"Tyler's declaration"* below revises **ill-typed** to **projected**: the
> classical intersection is well-typed, computes the `b3 = 0` slice, and
> silently discards `b3 = 1`. It returns an answer and the answer is a shadow of
> the question. The conclusion for the directed goal is unchanged — do not use a
> classical intersection — but the reason is different and the corrected reason
> is the one to quote.

**The corpus already contains the correct structure, and it was reached past.**
`[unpublished PPL package]/logic/ppl.py` defines an
eight-state verdict lattice in which two states carry the signature
**"base-frame UNSAT, joint SAT"**:

- `SHADOW_PARADOX (010)` — base-frame UNSAT, joint SAT, **no convergence**.
  "Individual parts fail, but something about their composition produces a
  temporarily satisfiable joint system... emergent coherence from individually
  broken pieces, without structural guarantee."
- `MIRROR_PARADOX (011)` — base-frame UNSAT, joint SAT, **convergence**. "Same
  structural signature... but the solver converges — the anti-paradox is
  stable."

Parts contradict; the whole holds. That is the formal signature of a
contradiction held paradoxically, and the lattice already distinguishes the
**stable** case from the **unstable** one. It is also a duality pair with
`BASE_FRAMES (100)`, annotated in the source as *parts vs emergent whole* —
which is precisely the failure of classical part/whole decomposition.

**Three consequences for this repository's programme, and they are not small:**

1. **Classical intersection would systematically miss the deep material.** A
   tenet holdable only in a base-frame-UNSAT/joint-SAT configuration is in *no*
   religion's classical tenet set, so it cannot appear in a classical
   intersection. The operator would return the shallow overlap — ethical maxims,
   golden-rule variants — and discard the paradox-held mysteries, which are
   arguably what "common tenets amongst religions" is actually after. This is a
   systematic bias, not a sampling problem.
2. **Stable versus unstable is doctrine versus live tension.** A contradiction
   held stably as mystery is `MIRROR_PARADOX`; one held unstably is
   `SHADOW_PARADOX` and is schism-prone. PPL's five meta-paradoxes are named as
   the *convergence mechanism* driving SHADOW to MIRROR — which makes them a
   candidate **mechanism for doctrine formation**, already written down.
   `FOUNDATION_BOOTSTRAP`'s pathway is "weak emergence requires no prior ground."
3. **The empty-intersection risk partly dissolves.** A classical intersection can
   be empty while the joint-SAT common ground is non-empty, because the
   paradox-held material was never in the classical sets. Emptiness of the
   classical intersection is therefore weak evidence about common ground, not
   strong evidence against it.

**This bears on the chosen reading (c).** `PLACEMENT.md` keeps (b')'s tenets as
the *material* at the dominator's nodes. The dominator structure survives intact
— but the node material is not a classical tenet-set, and a gate's admission
condition should be "can this tradition reach a **joint-SAT** holding of the
node's material", not "does it classically contain these tenets." That is a
richer and more defensible gate, so the objection strengthens (c) rather than
threatening it.

**SUPERSEDED 2026-09-21 by Tyler, and the replacement is better.** What stood
here recommended dropping **distributivity** (an orthomodular lattice); a peer
session corrected that to dropping **explosion** (paraconsistency, the right
name for holding contradictions). Both had the **wrong shape**. Tyler's
statement, verbatim:

> tHE 8 ARE CLASSICAL PARADOXES, THERE ARE 16 WHEN QUANTUM PARADOXES ARE
> INVOKED. 32 WITH POSSIBILITY PARADOXES AND MORE LATER, WE JUST NEED QUANTUM
> FOR COGNITION DOCTRINATION FORMATION OF RELIGIOUS CONVERGENCE STATES

The lattice is **graded**: Z2^3 = 8 classical, Z2^4 = 16 with quantum, Z2^5 = 32
with possibility, more later. You extend by **adding a coordinate**, not by
weakening the logic over a fixed state space. Both earlier proposals were
repairs; the real structure is an extension, and the classical eight survive
untouched as the `b3 = 0` slice.

This dissolves the ill-typing worry rather than repairing it. A classical
common-tenet intersection is **not ill-typed — it is projected.** It computes
the `b3 = 0` slice and silently discards everything at `b3 = 1`. It returns an
answer; the answer is a shadow of the question.

The open question that stood here — *whether PPL can express order effects* —
is now **answered structurally**: not at `n = 3`, and that is the point of the
fourth bit rather than a defect. Only `n = 4` is needed for this repo's work;
`n >= 5` is out of scope.

Full treatment, with the bit semantics measured from source and the fourth bit
proposed but **not** asserted, is in `metamathethicology/paradox_lattice_tower.hm`
(combination statement, so it lives there). Two findings from it bear directly
on the section above and qualify it:

- **The lattice is implemented**, but not in `ppl.py` — it is in
  `logic/cycle_detector.py`, with the bit codes and the transition table.
  The 1-hop/3-hop asymmetry is four dictionary entries.
- **The "five meta-paradoxes drive convergence" claim is docstring-only.** So
  point 2 above should read *the convergence transition is implemented; the
  mechanism attributed to it is not wired.* The candidate mechanism for doctrine
  formation is a **name**, not code.

  **The supporting evidence as first written was wrong, and the corrected
  evidence is stronger.** It said `class MetaParadox` "has exactly one source
  occurrence package-wide: its own definition. Nothing imports it." It is
  imported — `tests/test_ppl.py:19` — and there is a `TestMetaParadox` class at
  `:72`. But that test asserts only `len(MetaParadox) == 5` and that each of the
  five members `is not None`: **an existence check that cannot fail unless a
  member is deleted.** Nothing *consumes* it. So the finding stands and gains a
  sharper form — the mechanism is not merely unwired, it has a **passing test
  that cannot fail**, which is this corpus's own named anti-pattern applied to
  itself. Verify before quoting the "nothing imports it" line; it is false.

## The four adaptation targets, and the one that already has machinery

The directed goal names four things religions must find common ground to adapt
to: **AI**, **singularitians**, **the nature of reality itself**, and
**universal definitions of what it means to be**.

The fourth is not a loose phrase. It is the **entity class of hyperethics L1**,
which already exists and was built from Tyler's own definition, reproduced in
`hyperethics/L1_entity.hm` at lines 16-25:

> an entity is any decision making object which can be seen from first
> perspective from ... entities are objects that can be represented as having
> wills

Formally that is a conjunction of limbs — `norm-decides`,
`norm-subjectifiable`, `norm-will-representable` — and the crucial property for
this repository is that **it is substrate-neutral by construction**. It does not
privilege humans. Tyler's own framing text puts programs explicitly in scope:
*"If a program makes decisions but the thinking behind that program is theory of
mind representable..."*

**CORRECTED 2026-09-21: the class is neutral, but the only route into it is
not.** The paragraph above is right that `ax-entity-class:191` is silent on
substrate. It was wrong to conclude that entity-quantifying tenets transfer for
free. The *class* is substrate-neutral; the *membership certificate* is
language-bound, and the file says so about itself:

- `ax-subjectify-via-tom:202` gives decides + ToM-representable implies
  subjectifiable, and is marked "**SUFFICIENT, NOT NECESSARY, and the asymmetry
  is deliberate**."
- It runs through `ax-tom-via-language:218` — ToM-representable implies
  linguistic — which the file calls "**the layer's substantive assumption, and
  it is the one most worth attacking**."
- `nd-nonlinguistic-subjectification:455` is **OPEN**: is there a first
  perspective language does not carry? "The class does not exclude it," but the
  mechanization does not reach it.

So the abstract quantifier transfers; the certificate does not. The sorting test
needs **three** buckets, not two:

1. **Entity-quantifying, certifiable.** The tenet quantifies over entities *and*
   the target can be shown to be one. No adaptation required. **AI is the easy
   case here** — a decision-making system that is theory-of-mind representable
   in language sails straight through `ax-subjectify-via-tom`. Singularitians
   are human and never left the domain.
2. **Human-quantifying.** Adaptation is needed, and the question is whether the
   human-restriction is load-bearing or incidental.
3. **The certification gap.** The tenet quantifies over entities, but no route
   exists to show the target *is* one. This is not a gap in the tenet; it is the
   open non-derive above. **It bites hardest on the adaptation target with least
   purchase — "the nature of reality itself"** — which is neither obviously a
   decision-making object nor obviously subjectifiable through language. The
   hard target is hard for a reason that is already named and open in
   hyperethics, which is better than it being hard for no stated reason.

This partitions the common tenets into the ones that transfer for free, the ones
that require an argument, and the ones that require an *open problem* to be
closed first. Read `hyperethics/L1_entity.hm` before building anything here.

The third target, **the nature of reality itself**, connects to the reality
taxonomy Tyler has stated elsewhere (areality, surreality, preality, and N-d
universal base reality). That taxonomy is not yet formalised in any repository,
so it is a dependency, not a resource.

## What already exists and bears directly on this

- **`hyperethics/L0_creation.hm:213`, `d-no-exterior`.** Proves L0 has no
  vantage outside itself. This is already the formal version of "discoverable
  from limited cognition," and it is the most relevant existing result in the
  family. Read it before inventing a bounded-observer notion.
- **`hyperethics/L0_creation.hm`, `ax-immanence` and `ax-other`.** The creation
  layer: `norm-inhabits(archetype, create(x))` and
  `norm-other(create(x), archetype)`. Origination of narratives is structurally
  the same move, one level down.
- **`hyperethics/P0_shadow_ground.hm`, `ax-self-maintenance`.**
  `carries(SelfMaintenance, SelfMaintenance)` — a thing that maintains itself by
  applying to itself. The same thought appears in
  `[unpublished PPL package]/logic/ppl.py` as
  `MetaParadox.FOUNDATION_BOOTSTRAP`: "the ground cannot ground itself." A
  scripture that morphs scriptures, including itself, is a foundation-bootstrap
  object, and that machinery already exists.
- **`metamathethicology/VOCABULARY_BOUNDARY.md`.** **Read before coining a
  single term.** Six words in this corpus already carry conflicting senses
  across repositories. A repository about scripture, morphing and memetics is
  exactly where new coinages will multiply, and it is exactly where that hazard
  compounds fastest.
- **`taxonomy-of-deception`** — PUBLIC. ~~Adjacent prior art on memetic
  narrative.~~ **CORRECTED 2026-09-21, see `PLACEMENT.md` §1.** It contains
  *zero* occurrences of `meme`/`memetic`, `transmission`, `replicat*` or
  `population`, and one incidental `narrative` which is a negation. It is a
  **single-hop** receiver-first taxonomy — one representation, one receiver, one
  judgement — with no iteration and no population. It is the single step that
  memetics iterates: a foundation to cite, not prior art on memetic narrative,
  and **not** a second parent field. The placement argument turns on this.
  Nothing private may be written there.

## What is not known

Stated plainly so that a later session does not mistake framing for progress:

- Whether "religions" is the subject or an instance. The description says
  religions; the machinery would apply to any memetically transmitted narrative,
  and it is unclear whether narrowing is intended or incidental.
- What makes a narrative "memetically supported" — no criterion is given, and
  without one the limit object is undefined.
- Whether convergence to a *single* narrative is asserted, predicted, or merely
  the direction anchor points point. The three are different claims with
  different burdens.
- Whether the morph operator is deterministic.
- Whether "limited cognition" is one bound or a family of bounds parameterised
  by observer.
- **Whether "common tenets" is a strict intersection or a threshold.** This is
  the sharpest risk in the directed goal. A strict intersection over *all*
  religions may well be **empty** — one sufficiently divergent tradition
  collapses it — and an empty intersection makes reading (b') vacuous and the
  programme with it. If it is a threshold ("held by most", "held by all but a
  bounded set"), that threshold is a parameter nobody has chosen, and the
  results will depend on it. Establishing that the intersection is non-empty,
  or replacing it with a defensible threshold, is a precondition for the rest.
- Whether the hierarchy in reading 2 of the anchor-point tension is the **same
  hierarchy** as the one metamathethicology will use to derive the necessity of
  religion. Both are called hierarchical; nothing yet says they coincide.

## Ordering

Tyler, on this repository: *"Probably comes after metamathethicology honestly."*

Taken as binding. This file is scoping, not construction, and nothing here
should be promoted to theory before the metamathethicology work it depends on
is settled.

The dependency is no longer a placement question — that is answered, and this
repository has its own subject. It is now a **substantive** dependency, which is
the stronger kind: metamathethicology derives *whether religion is necessary at
all*, and this repository's programme assumes religions exist and asks what they
share. If the necessity derivation fails, or derives something other than a
belief structure, the common-tenet question does not become wrong — it becomes a
question about a contingent set of artefacts rather than about a necessary
structure, which changes what the answer is worth.
