# meta-morphoscripted-origination

> **Rough draft, 2026-09-24.** This page, the declarations, the surface and the
> glossary are first passes. They were drafted by an AI assistant (Claude) for
> Tyler Roost, who writes as TimeLordRaps, and he has not read them yet. The declarations just below are written in his voice,
> from his own words and lyrics. They are his to keep, change or strike.

## Origination Declarations

> This is the lesson, from beginnings of time.
> Don't go stressin, if the line divides.
>
> — The TimeLord, "Broken Time"

Hear ye, hear ye, beings of every kind. (They do be, do they not?)

**We declare** that nothing you have ever felt, thought, believed, known or
dreamed came from nowhere. Every one of them had a first time. Somebody,
somewhere, somewhen felt it first, or found it, or said it out loud. Then it
travelled: hand to hand, mouth to ear, fire to fire, generation to generation,
until it landed in you. You are carrying some of the oldest luggage on Earth,
and most of the tags fell off a long time ago.

**We declare** that we are going to read those tags back. For every emotion,
idea, belief, piece of knowledge and thought we can find, we ask five things.
**When** it most likely appeared in people (time is a construct, so we honor
it with dates). **How**, if a new tool or a new turn made it possible. **Why**:
what problem it solved. **Where**, first and most prominently, and why that
where was where it was. And **who**, but only if someone can honestly be named.

**We declare** that where the ground runs out, we say so. A guess is labelled a
guess. A source is real, or it is not there. "We don't know yet" is an answer
this repository is proud to give, and it will give it often.

**We declare** that the world's faiths are neighbours on this surface, not
rivals. Every tradition, and every person who holds none, is welcome here as
they are. Nobody gets ranked. Everybody gets listed alphabetically, the most
boring order there is, on purpose. We are not here to crown anything. We are
here to find the places where people who never met ended up holding the same
thing: grief that will not let the dead go, a welcome for the stranger at the
door, a fire that must never go out.

**We declare** that the contradictions people hold are not bugs. *The dead are
gone, and the dead are still with us.* Most people who have loved someone have
believed both at once, and been right to. A surface that deleted every paradox
would keep only the shallow end of the pool. We keep both sides, and we write
down who holds them.

**We declare** that the question does not stop at the first humans. It belongs
to everyone living now; to singularitians like myself, taken by the idea of what
comes next; to the minds we are building, which will one day ask where their
own feelings came from; to the nature of reality itself; and to whatever it
turns out it means to be.

So: when did we first grieve?
Same question, but in the context of the spectrum of dimensions which grief is
carried in.
Same question, but for the one being grieved.
Same question, but for a mind that was made rather than born.
Same question, but for the ones who come after us and have to decide what to
keep.

Because underneath every one of those is the question I keep coming back to:

> What kind of values maintain that future generations have the highest
> likelihood of the deepest depths of some form of universal moral
> understanding?

> Respect the unexpected
> From the ones first perspectin
>
> — The TimeLord, "Forgetful"

From the grave to the gathering place, from the spark to the story, from the
mark to the meaning, from the stars to the stranger at the door: this will be
our story, morphoscripted from origin to progination.

Let's restory it right.

— **TimeLordRaps** (Tyler Roost)

---

## What this repository is

Its description on GitHub, which was its whole specification for its first six
months:

> The scripture that morphs to morph scriptures surround origination of
> narratives. Ie what frame is discoverable from limited cognition that
> identifies anchor points for religions to pass through, towards a single
> memetically supported narrative.

Tyler, 2026-09-21, giving it a direction:

> meta-morphoscripted-origination has a directed goal, metamathethicology will
> probably derive the necessity of religion hierarchically as a belief
> structure, but meta-morphoscripted-origination's goal is to discover the
> common tenets amongst religions and find a common ground for which religions
> may adapt to ai, singularitians like myself, the nature of reality itself,
> and universal definitions of what it means to be.

Tyler, 2026-09-24, on what the repository is for:

> this entire repo is on how can we morphogenetically form a global religion
> surface to describe a social origination of human emotions, ideas, beliefs,
> knowledge, and thoughts. It's to represent how these ideas, beliefs,
> knowledge, and thoughts most likely topographically appeared in humans,
> when, how (if we can determine a reason like a new tool invented or
> something), why (what problem the emotion, idea, belief, knowledge, or
> thought solves), where (first and most prominently and why that where was
> where it was), who (if someone is associated with it specifically). This will
> be our story morphoscripted from origin to progination.

## A promise about respect

- **No ranking.** Traditions are always listed alphabetically. The numbers on
  the declaration files are the order they were written in, nothing more.
- **In their own terms.** Each tradition is described the way its own people
  would recognise, pointing to its own texts and practices where possible.
- **Faith and no faith.** People who hold no religion are part of the surface,
  not outside it.
- **Nobody is asked to change.** Common ground is looked for, not imposed. The
  description asks whether traditions pass through shared anchor points toward
  a single narrative. That is an open question, and if it is ever answered it
  will be by evidence and by consent, not by decree.
- **Corrections are welcome,** most of all from people inside the traditions
  described. If something here is wrong or unkind, please open an issue.

## What is here

| Path | What it holds |
|---|---|
| [declarations/](declarations/README.md) | The origination declarations: one origin story per file, with an index |
| [SURFACE.md](SURFACE.md) | How the declarations fit together into a surface, and what the surface cannot show yet |
| [GLOSSARY.md](GLOSSARY.md) | Tyler's words, and this repository's terms, with where each comes from |
| [schema/origination-declaration.schema.json](schema/origination-declaration.schema.json) | The shape every declaration must have |
| [tools/validate_declarations.py](tools/validate_declarations.py) | The check that holds every declaration to that shape |
| [SCOPE.md](SCOPE.md) and [PLACEMENT.md](PLACEMENT.md) | The earlier scoping notes: the specification, the directed goal, and the formal questions a theory would have to settle |
| [LICENSE](LICENSE) and [NOTICE](NOTICE) | Apache License, Version 2.0 |

## What a declaration holds

Each one answers **when, how, why, where and who** for a single emotion, idea,
belief, piece of knowledge or thought. Then it lists its **evidence**, each
source with what it supports, how firmly, and whether it is contested. It keeps
**consensus** and **speculation** in separate lists. It traces the thing's
**morphs**, the shapes it took over time. It notes **tenet links**, where the
same thing lives in today's traditions, and what they hold as **paradox**. It
ends with a **restory**, a short retelling, and its **open questions**.

To add one, or to check the ones here, see
[declarations/README.md](declarations/README.md). In short:

```
python -m pip install pyyaml jsonschema
python tools/validate_declarations.py
```

## What this is not, yet

- **Not theory.** No layer, axiom or operator is defined anywhere here. Tyler on
  the order of work: *"Probably comes after metamathethicology honestly."*
  [metamathethicology](https://github.com/TimeLordRaps/metamathethicology) is
  the sibling repository expected to derive why religion is necessary at all.
  This one collects the material a theory would stand on.
- **Not finished, and not Tyler's final word.** Every file is marked rough.
- **Not a verdict on anyone's faith.** A historical origin says when and where
  something first shows up in the record. It does not say whether it is true.

## Licence

Licensed under the [Apache License, Version 2.0](LICENSE). See [NOTICE](NOTICE).
