# Placement, and what an anchor point is

Written 2026-09-21. Companion to `SCOPE.md`, which states the specification, the
directed goal, and the open questions. This file answers the two questions
`SCOPE.md` posed and does not restate them.

Nothing here is theory. Two decisions and their arguments, plus a vocabulary
finding that arrived unasked and is load-bearing. The ordering constraint
(*"probably comes after metamathethicology honestly"*) is respected: no layer,
no axiom, no operator is defined below.

---

## 1. Placement: this repository gets content. Confirmed, on a different reason.

`SCOPE.md` answers this from the directed goal — `metamathethicology` derives
*why religion is necessary*, this repository asks what religions *share*, so the
subjects differ and the placement rule is satisfied. That argument holds. It is
also weaker than the one available, and the stronger one should be on record
because it survives changes to the directed goal.

### The rule, in its sharpest form

`SCOPE.md` paraphrased the test as: does stating this require naming two foreign
subjects? That test is wrong, and it is wrong in a way that would have given the
wrong answer. It sends `grounded-hypercalculi` to `metamathethicology`, and
`grounded-hypercalculi` did not go there — it is a public repository of its own,
cited by `hyperethics/L3_consciousness.hm` and not reproduced in it.

The rule as `metamathethicology/README.md` actually states it:

> A **combination field** is a submodule that combines two fields this package
> does not depend on.

And the worked case, `will_electrophysics`, in Tyler's own words:

> Electricity hyperphysics should go in hyperphysics, underlying will
> foundations in hyperethics, and then their combination field of will
> electrophysics is in metamathethicology.

Read against its contrasting precedent, the rule has two limbs, not one:

| | material | destination |
|---|---|---|
| `will_electrophysics` | a **transport between two subjects each already stated in full** by its own field | `metamathethicology` |
| `grounded-hypercalculi` | a **new subject** standing on a foundation another field supplies | **its own repository**, citing not reproducing |

`hyperethics/L3_consciousness.hm:989` states the second limb outright: L3
supplies "a TYPE of languages and a SOURCE for them" and builds no calculus,
because "a field states its own subject once."

So the test is not *how many fields does this touch*. It is: **are there two
parents, each of which has already stated its half?**

### Applying it: there is no second parent

One parent exists. `hyperethics` states creation, immanence, and — at
`L0_creation.hm:213`, `d-no-exterior` — the absence of an exterior vantage.

The other half, the memetic carrier, is **stated by nothing in the corpus.**

`SCOPE.md` names `taxonomy-of-deception` as "adjacent prior art on memetic
narrative." **That characterisation is wrong, and correcting it is not a
quibble — the placement turns on it.** Measured 2026-09-21 against the local
checkout, re-runnable:

| term | occurrences in `TAXONOMY.md` + `README.md` |
|---|---|
| `meme` / `memetic` | **0** |
| `transmission` | **0** |
| `replicat*` | **0** |
| `population` | **0** |
| `narrative` | **1**, and it is a negation: *"a plausible narrative does not by [itself]…"* |
| `propagat*`, `iterat*`, `chain` | 1 each, all incidental |

`taxonomy-of-deception` is **single-hop**: `representation -> reception ->
operative state -> material divergence -> representation contribution ->
deceptive bridge`. One representation, one receiver, one judgement. It has no
iteration, no retelling, no population, no time axis. It is the *single step
that memetics iterates* — which makes it a foundation to cite, exactly as L3
cites `grounded-hypercalculi`, and **not** a parent to combine with.

**A combination field is a transport between two stated subjects. You cannot
transport to a subject nobody has stated.** The combination slot is therefore
not merely unattractive here; it is structurally unavailable. This repository
gets content because there is nowhere else the material can go, and that reason
does not depend on the directed goal being worded as it currently is.

### The condition, which is not scheduling

The ordering constraint binds for a reason sharper than queue position, and
`metamathethicology` supplied the reason itself.

`p0_barrier.hm` Section IV concludes **the P0 barrier is field-local**, and
Section V gives the consequence: *"a barrier imported from a sibling field is
not a weaker argument but a category error."* A field must build its own barrier
from its own clauses, because — by `d-no-exterior` — there is no exterior
position to build one from.

If this repository is a field, it owes its own barrier argument. It may not
borrow `hyperethics`' displacement barrier (UNRUN — `GC-P0X-2`) or `hyperlogic`'s
Section VI close. **That is the admission requirement for this name becoming a
field, and `metamathethicology` is where it was established.** The dependency
runs through a result, not a calendar.

---

## 2. Anchor point: reading (c), the bottleneck. Formally, a **dominator**.

`SCOPE.md` offers four readings and says the live argument is **(b')** against
**(c)**. The choice is **(c)** — and the argument is not that (b') is wrong
about *what anchor points are made of*. It is right about that. (b') is wrong
about the *structure*, and (c) supplies the structure that rescues (b') from
both objections `SCOPE.md` raises against it.

### The commitment

> An **anchor point** is a **dominator**: given a source, a node `n` such that
> every path from the source to anything downstream of `n` passes through `n`.

Standard graph theory (Prosser 1959; Lengauer–Tarjan 1979). **Nothing is
coined.** See §3.

The nodes are **coalitions** — sets of religions together with the tenets they
share. A religion "passes through" an anchor when it enters a coalition, and
what it must hold to enter is what the anchor consists of. So the tenets are
(b')'s tenets. They sit at the nodes instead of being the nodes.

### Why (b') fails, and it fails on the constraint `SCOPE.md` calls hardest

Three arguments, in increasing order of severity.

**(i) It fails the static/trajectory test, which `SCOPE.md` already names.** An
intersection is everywhere in the family by construction; nothing passes through
it. `SCOPE.md` offers two escapes — the passage is epistemic, or the passage is
real. Neither is needed once the motion is put in the right object: **the
tenets are static and the admissions move.** A gate does not travel; things
travel through it. (b') put motion in the tenet, which has none to give.

**(ii) `SCOPE.md`'s reading 2 conflates two opposite monotonicities.** It
proposes "a sequence of progressively larger common grounds — partial
intersections, each admitting more religions than the last." For `T(R) =`
the tenets shared by every religion in `R`, `T` is **monotone decreasing**: more
religions, *fewer* shared tenets. "Larger common ground" and "admitting more
religions" pull in opposite directions, and reading 2 as written asks for both
at once. Under (c) the tension disappears, because the chain is ordered by
*reachability*, not by the size of anything.

**(iii) It is not discoverable from limited cognition. This is decisive.**
`SCOPE.md` identifies the constraint as "the hard part and it is easy to read
past," and `d-no-exterior` is its formal version. Computing an intersection over
*all* religions requires **enumerating all religions**. That is the exterior
vantage, and it is the thing the constraint forbids. (b') as literally stated
cannot be executed by any bounded observer. It answers a different question —
the one asked from outside.

### Why (a) and (b) are not anchors either — and what they are instead

**(a) fixed point of the morph, `morph(s) == s`.** Wrong dynamics. A fixed point
is where morphing *stops*; "pass through" is motion that continues. If anchors
were fixed points there would be one per basin and no sequence leading anywhere.

This matters for how the period-1 finding should be read. `SCOPE.md` records,
correctly and re-usably, that **period 1 is not barred** — `hypermath` admits it
(`trace-levels` case (a), `apply(x) == x`), `hyperlogic` inhabits it by axiom
(`ax-closure-self`), `hyperethics` has never been asked (`GC-P0X-4`), and the
arithmetic barrier is broken. **That finding bears on the limit object, not on
the anchors.** The single memetically supported narrative is the plausible
fixed point. The waypoints en route are not. (a) is promoted, not rejected.

Secondary: in `hypermath`'s filtration `==` is the *top* of three levels
(`trace-levels`, `L1_relations.hm:362`). Requiring anchors at `==` demands the
strongest available relation for what the specification describes as a transit
point. The middle level `=~` — "substance kept, path discarded" — is what a
tradition passing through a common tenet actually looks like.

**(b) invariant over the morph orbit.** Type-wrong as an anchor, and doubly so.
First, in `hypermath`'s own filtration the orbit-universal relation is the
**floor**: `apply(x) ~~ x` holds for every `x` by `ax-sim`, guaranteed
(`trace-levels` case (c)). A property satisfied by everything in the orbit
**identifies nothing**, and the specification demands a frame that *identifies*
anchor points. By this family's governing standard — *a constraint that cannot
fail is not being checked* — (b) is not being checked. Second, an invariant has
no position, and "pass through" needs a locus.

(b) is demoted from anchor to **certificate**, and in that role it is essential.
See below.

### Why (c) survives the constraint that killed (b')

(c) has one serious problem and it must be met head-on: **a dominator is a
global property.** Establishing that every path passes through `n` quantifies
over all paths — the exterior vantage `d-no-exterior` denies.

The resolution is in the specification's own quantifier placement:

> what **frame** is discoverable from limited cognition **that identifies**
> anchor points

Discoverability attaches to the **frame**, not to each anchor's verification.
The frame must be findable from inside; the anchors are what it then identifies.
So the question is whether a bounded observer has a **local certificate** for a
global dominator. It does, and this is (b)'s proper job:

> A tenet that holds throughout an observer's own reachable cone, and that
> entered at an identifiable point, **dominates that cone.**

Forward-only. It needs the observer's own reach and the point where a property
became true — never a survey of the family. An observer inside one tradition can
ask *which of my tenets must I retain to remain in coalition with the traditions
I can actually reach?* and compute an answer locally.

**Sound, not complete.** Every anchor certified this way is genuinely one; an
observer will miss anchors gating coalitions it cannot see. The frame
**under-reports**. That is the correct failure direction for a bounded observer,
and — again by the family's own standard — it means the test *can* fail, which
is what makes it a test.

### What (c) gets for free that the others must assume

**The ordering.** In a rooted directed graph, the dominators of any node are
**totally ordered** — they are the path from the root to that node in the
dominator tree. So "anchor points … **towards** a single narrative" is not an
extra assumption under (c); it is a consequence of anchors being dominators.
Under (a), (b) and (b') the directedness has to be asserted separately.

**The setting is already present, not assumed.** `hypermath` supplies both
conditions the dominator construction needs: a single source, at
`D-spans-ground` (`L1_relations.hm:418`) — *"D[ground][y] holds for all y:
ground derives every form"* — and finiteness, at `ax-box` (`L0_ground.hm:117`),
which bounds the `~~`-orbit so that *"the index space is finite."* Finite and
rooted is exactly where dominators exist and are computable.

### The four readings, in four roles

| reading | role | status |
|---|---|---|
| **(c) bottleneck** | **the anchor point** | **chosen** |
| (b') family invariant | supplies the *material* — anchors are made of tenets | right content, wrong structure |
| (b) orbit invariant | the **local certificate** that makes a dominator discoverable from inside | demoted, and essential |
| (a) fixed point | the **limit** — the single memetically supported narrative | promoted, not rejected |

All four survive. The commitment is that **(c) names the anchor**, and it is a
commitment: it makes anchors observer-relative, tenets structural rather than
terminal, and convergence a separate question rather than a built-in.

### One thing this buys immediately: two of `SCOPE.md`'s unknowns are one unknown

`SCOPE.md` lists separately (i) whether convergence to a single narrative is
asserted, predicted, or directional, and (ii) whether "common tenets" is a
strict intersection that **may well be empty**, which it calls the sharpest risk
in the directed goal.

Under (c) these are **the same question**. The single narrative is the top of
the anchor chain. The chain has a top exactly when the tenets shared across the
whole family are non-empty. So:

> **convergence holds if and only if the global intersection is non-empty.**

And the programme does **not** collapse if it is empty — which is the practical
payoff. Under (b'), an empty intersection is fatal: the anchors *are* the
intersection, so there are none. Under (c) the anchors are gates along the way,
and an empty global intersection means only that the chain has no maximum. The
anchor points still exist and are still identifiable. **(c) makes the sharpest
risk in the directed goal survivable.**

The threshold variant maps cleanly too. Replacing strict intersection with
"held by all but `k`" yields a family of graphs indexed by `k`, and the anchors
become `k`-relative. The parameter `SCOPE.md` worries is unchosen becomes an
explicit index rather than a hidden assumption.

---

## 3. Vocabulary: the collision check was run on every term, and it found two

`metamathethicology/VOCABULARY_BOUNDARY.md` records six words this corpus
already disagrees about, and gives a generally applicable rule: **run the
collision check on every coinage or on none** — running it on one term produces
false confidence about the rest.

It was run on every term, 2026-09-21, across `hypermath`, `hyperlogic`,
`hyperethics`, `hyperphysics`, `metamathethicology` and `taxonomy-of-deception`,
excluding vendored trees. Re-runnable.

**Clear, zero occurrences corpus-wide:** `scripture`, `origination`, `meme` /
`memetic`, `tenet`, `coalition`, `cut vertex`, `cone`, `fixpoint`.

**Two hard collisions, and both are in the specification's own sentence.**

### `frame` — the seventh word

`VOCABULARY_BOUNDARY.md` is explicit: FRAME in this family is *"a closure-status
label: an articulated derivation block with a named forward dependency and a
discharge layer. It is **not an aperture, an opening, or a point of view.**"*

Measured: **55 files across 5 repositories** use it in the closure sense
(`hypermath` 44, `hyperethics` 5, `metamathethicology` 3, `hyperlogic` 2,
`hyperphysics` 1).

The specification asks *"what **frame** is discoverable from limited cognition"*
— the aperture sense, which is the sense ruled out by name. This is the seventh
word, and unlike the first six it was found **inside the specification** rather
than in a proposed vocabulary. It cannot be fixed by declining to coin; the
collision is already written.

**Recommendation:** treat the specification's "frame" as prose. Do not let it
become a defined term here, and never write it capitalised. What the
specification calls a frame is, formally, the local-certificate procedure of §2.

### `anchor` — the eighth word

`hypermath` uses `anchor` **16 times, load-bearing**, and it means
*name-binding to ground*:

- `docs/terms/definition.md:7` — *"`definition` is the anchoring act that makes
  a form derivable by name."*
- `L1_relations.hm:236` — *"syntax is the relation-level anchor: x has a
  derivation chain reachable [from ground]."*
- `ground anchoring` is a closure predicate in four research documents.

The specification's "anchor point" means a **waypoint on a path**. hypermath's
anchor means **a name bound to the source**. The senses are close enough to be
confused and different enough to be wrong, which `VOCABULARY_BOUNDARY.md`
identifies as the worst case.

**Recommendation:** `anchor point` stays as the display name, because it is
Tyler's phrase and it is in the repository's specification. The **formal** name
is `dominator`, which is standard, has published mathematics behind it, and
collides with nothing here.

### One soft collision and one near-miss, disclosed

- **`morph`** — bare `morph` is clear (`hyperethics` has only `amorphous`,
  `taxonomy-of-deception` only `anthropomorphic`). But `hypermath` uses
  `-morphism` throughout in the structure-preserving-map sense — *"behavioral
  simulation isomorphism across the orbit"*, *"Retrace is a homomorphism for
  composition."* A `morph` operator that does **not** preserve structure would
  read there as a false cognate. Disclosed, not fatal.
- **`dominated`** — `taxonomy-of-deception` uses it in the **game-theoretic**
  sense (*"cheap deception is strictly dominated"*, `TAXONOMY.md:713`). Distinct
  from graph-theoretic `dominator`, and the standard terms differ ("strictly
  dominated strategy" vs "dominator node"), but a reader could trip. Disclosed.

### Terms rejected before use, on the check

`admission` (35 files in `hypermath`, where it names the sorry classification),
`gate` (45 files), `reach` (52 files) are all heavily loaded. **"Admission
graph" and "gate" were candidate names for the §2 construction and were dropped
on the check.** Recorded because `VOCABULARY_BOUNDARY.md`'s lesson is that the
check is worthless if its negative results go unreported.

### hyperstratum

Assessed, zero of ~24 terms clear the bar, **adopt none**. Nothing above adopts
anything from it.

---

## 4. What remains unknown

Including what the decisions above do **not** settle. `SCOPE.md`'s list stands
except where noted.

**Reduced to one question** (§2): convergence to a single narrative, and whether
the common-tenet intersection is empty. These were two entries; they are one.
Convergence holds iff the global intersection is non-empty.

**Changed status — now a precondition, not a background question:** whether the
morph operator is **deterministic**. Dominators are defined over a fixed edge
set. A nondeterministic morph gives a different graph per run, and "every path"
loses its referent. Under (a), (b) or (b') this was one open question among
several. Under (c) it is **required before the anchor notion is well-defined.**
Choosing (c) is what raised it.

**Still open, untouched by anything above:**

- What makes a narrative "memetically supported." No criterion is given, and
  without one the limit object is a named slot, not an object. §2 does not
  supply it, and (a)-as-limit does not need it to be stated — but the programme
  does.
- Whether "religions" is the subject or an instance.
- Whether the hierarchy in `SCOPE.md`'s reading 2 is the same hierarchy
  `metamathethicology` will use to derive the necessity of religion.
- The reality taxonomy (areality, surreality, preality, N-d universal base
  reality) is formalised nowhere. `SCOPE.md` calls it a dependency, not a
  resource. Unchanged.

**Opened by the decision in §2:**

- **Observer-relativity of the anchor set.** The local certificate is sound but
  not complete, so two observers with different reach may certify different
  anchors. Whether their dominator chains are comparable is now a question with
  a yes/no shape — and it is the sharpened form of `SCOPE.md`'s open question
  about whether "limited cognition" is one bound or a family of bounds
  parameterised by observer. **Sharpened, not closed.**
- **The graph does not exist.** There is no narrative graph, no morph operator,
  no scripture type, and no religion type anywhere in the corpus. §2 says what
  an anchor *would be* given the graph. It constructs nothing, by the ordering
  constraint, and that is the largest single gap between this file and a theory.
- **This repository's own barrier is unwritten** (§1). Required before it is a
  field rather than a name.

**Not re-derived, and not to be re-derived:** period 1 is not barred. Two fields
have answered, one has never been asked (`GC-P0X-4`). It bears on the limit
object, not on the anchors (§2).

---

## Provenance

Every count in this file was measured against local checkouts on 2026-09-21 and
is re-runnable. `hypermath`, `hyperlogic`, `taxonomy-of-deception` and
`grounded-hypercalculi` are PUBLIC; `hyperethics`, `hyperphysics`,
`metamathethicology` and this repository are PRIVATE, verified by `gh repo view`
before any path or repository name was written here. This file is private and
may name them.

The artefacts cited in `metamathethicology` and `hyperethics` are **uncommitted**
in their own working trees, per `p0_barrier.hm`'s `nd-p0-is-committed`. Anyone
treating this file's citations as repository state is reading a plan as a fact.
