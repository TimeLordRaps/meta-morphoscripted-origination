# The global religion surface

> **Rough draft, 2026-09-24.** Drafted by an AI assistant for Tyler
> (TimeLordRaps), not yet read by him. It describes what the declarations add
> up to so far, and what they cannot show yet. It defines no theory.

> Faces and places, all woven in time's seam
>
> — The TimeLord, from his collected raps (untitled)

## What the surface is

Tyler's phrase for this repository is a **global religion surface**, formed
*morphogenetically*: grown, the way a living thing takes its shape, rather than
designed all at once. It describes how human emotions, ideas, beliefs,
knowledge and thoughts *topographically appeared*: when, how, why, where, and
through whom.

In plain terms, the surface is a map. Every
[origination declaration](declarations/README.md) is one feature on it, placed
along four directions:

- **Time.** When it most likely appeared, as a window of years ago rather than
  a single date. Time is drawn on a logarithmic scale, where each step back
  goes ten times further, so that a million years ago and a few thousand years
  ago fit on the same page.
- **Place.** Where it shows up first in the evidence, and where it became most
  prominent, each with a reason why there.
- **Kind.** Emotion, idea, belief, knowledge or thought.
- **Depth.** What grew on top of the origin: how the thing changed shape over
  time (its `morphs`), where it lives in today's traditions (its
  `tenet_links`), and which tensions people hold about it without resolving
  them (its `paradox_held`).

Every placement carries its own confidence. A feature with thin evidence should
be read as a smudge, not a dot.

**Height means nothing.** No feature is higher because it is older, more
widespread, or held by more people. The surface has a shape, not a
leaderboard.

## The surface on 2026-09-24

This is the time direction only, drawn by `python tools/draw_surface.py` from
the declarations as they stood on 2026-09-24. Run it again for the current
picture; this copy will go stale as declarations are added.

```
                                    1,000,000      100,000        10,000         1,000   years ago
                                        |             |              |             |
care-for-the-vulnerable  emotion    =================                                 low
fire-kept                knowledge      ========                                      medium
the-mark-that-means      idea              ==============                             medium
trust-between-strangers  belief                =============================          low
grief-and-burial         emotion                     ====                             medium
sky-calendars            knowledge                              ===========           medium
the-gathering-place      belief                                     ==                high
the-fireside-story       thought                                       ====           low
law-written-down         idea                                             ==          high
```

Three things stand out, and each needs the caveat that follows it.

1. **The oldest features are feelings and know-how; the youngest are written
   ones.** Care, fire and marks come first; written law and the written story
   come last. *Caveat:* this is at least partly a fact about evidence. Bones,
   ash and ochre survive for a million years. A song, a gesture or a promise
   leaves nothing until someone writes it down.
2. **Whoever is named comes late.** Only the declarations inside the age of
   writing name anyone. Everything older is anonymous, not because no one did
   it first, but because no one could sign it.
3. **Every declaration so far found both common ground and paradox.** Each one
   has traditions that hold the same thing in their own words, and each one
   has at least one tension that people keep rather than resolve. That is an
   observation about nine drafts written in one sitting, not a law.

## What the surface cannot show yet

Stated plainly, so that nobody mistakes the map for the territory.

- **Preservation bias.** Caves, dry ground and fired clay keep evidence;
  forests, wetlands, wood and skin lose it. "First found" is not "first".
- **Research bias.** Firsts cluster where archaeologists have dug most:
  Europe, the Levant, and parts of eastern and southern Africa. Much of the
  world is under-studied, and that shows up here as blank space.
- **Writing bias.** Oral traditions carry deep memory (see
  [the-fireside-story](declarations/09-the-fireside-story.yaml)), but they reach
  this surface mostly through outsiders' published studies. That is a thin and
  second-hand view of them.
- **Coverage.** The traditions linked so far are mostly large world religions
  with written scriptures. Indigenous, African, and many other traditions are
  under-represented. Filling that gap needs care, and ideally people from
  those traditions.
- **Emotions leave no fossils.** A burial shows a behaviour, not a feeling.
  Every emotion declaration infers the feeling from what people did.
- **Who drafted it.** These drafts were written in English, by an AI, from
  mostly English-language scholarship, in one day. They should be read as a
  first pass by one bounded observer.

## How this relates to the scoping notes

[SCOPE.md](SCOPE.md) and [PLACEMENT.md](PLACEMENT.md) set out the formal
questions a theory of this repository would have to settle. The surface does
not answer them. It collects material in a shape that keeps those answers open.

- **Anchor points.** PLACEMENT.md §2 chose to read an "anchor point" as a
  bottleneck, a place every path passes through, formally a *dominator*. The
  `tenet_links` are the kind of material that would sit at such a place. No
  graph exists yet, so nothing here is, or claims to be, an anchor point.
- **Paradox is kept, on purpose.** SCOPE.md records Tyler's correction:
  *"contradictions can be held paradoxically by people"*. A plain overlap of
  what traditions hold keeps only what is consistent and silently drops the
  rest, so it returns a shadow of the question. Every declaration's
  `paradox_held` list is where that rest is written down, so that a later
  theory is not handed only the shallow end.
- **Limited cognition.** The specification asks for what is discoverable *from
  limited cognition*. Each declaration is written from a bounded vantage, one
  writer and the sources found, and is built to under-report rather than
  over-claim. PLACEMENT.md's phrase for that is *sound, not complete*.
- **No new formal terms.** Words here are used in their plain senses. The
  [glossary](GLOSSARY.md) records where any of them collide with terms in
  sibling repositories.

## The four adaptation targets, as questions

The directed goal asks for common ground from which religions may adapt to
**AI**, to **singularitians**, to **the nature of reality itself**, and to
**universal definitions of what it means to be**. The declarations cannot
answer that yet. They can each pose it:

- **AI.** Grief meets the digital remains of the dead
  ([grief-and-burial](declarations/01-grief-and-burial.yaml)). Care meets
  machines that look after people
  ([care-for-the-vulnerable](declarations/02-care-for-the-vulnerable.yaml)).
  Written law meets rules written for machines
  ([law-written-down](declarations/04-law-written-down.yaml)). Trust between
  strangers is more and more checked by machines
  ([trust-between-strangers](declarations/05-trust-between-strangers.yaml)).
  Stories are now told by machines, and to them
  ([the-fireside-story](declarations/09-the-fireside-story.yaml)).
- **Singularitians,** Tyler among them. His word for being "taken by the idea
  of the singularity" is *singularitaken*. Many traditions hold a hope about what
  comes at the end of time, or after it. What does that hope share with theirs,
  and where do they differ?
- **The nature of reality itself.** Calendars hold time as a circle and as a
  line at once ([sky-calendars](declarations/07-sky-calendars.yaml)). What does
  each tradition take reality to be, and where does that meet what physics now
  says?
- **What it means to be.** SCOPE.md sorts common tenets into three buckets:
  those that already apply to any being that can be shown to be one, those
  that are written for humans alone, and those that would apply if only there
  were a way to show that the being counts. "Welcome the stranger" is a good
  first test: which bucket is it in, when the stranger is a machine?

## The order of work

Tyler: *"Probably comes after metamathethicology honestly."* This surface is
material, not theory. The sibling repository
[metamathethicology](https://github.com/TimeLordRaps/metamathethicology) is
expected to derive why religion is necessary at all, and nothing here should be
promoted to theory before that work is settled.

## From origin to progination

The surface has an old edge, which the declarations reach toward, and a future
edge. Tyler's phrase for the whole span is *from origin to progination*. What
*progination* means precisely is his to say (see the
[glossary](GLOSSARY.md)), so the future edge of this map is left open for him.
