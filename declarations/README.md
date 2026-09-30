# Origination declarations

> **Rough drafts, 2026-09-24.** Every file here was drafted by an AI assistant
> working for Tyler (TimeLordRaps), and none has been read by him yet. Treat
> them as first passes to argue with, not as findings.

Each declaration tells the origin story of one emotion, idea, belief, piece
of knowledge or thought: **when** it most likely appeared in people, **how**
(if a new tool or change made it possible), **why** (what problem it solved),
**where** (first, and most prominently, and why there), and **who** (only if
someone can honestly be named). Then it follows how the thing changed shape
over time, and where it lives today in the world's traditions.

The numbers are the order the files were written in. **They are not a
ranking,** and neither is the order of anything else in this folder.

| File | Kind | Subject | When | Confidence in the dating |
|---|---|---|---|---|
| [01-grief-and-burial](01-grief-and-burial.yaml) | emotion | Grief that keeps the dead close, shown by burial | Burials from about 120,000 years ago; the emotion, probably much earlier | medium |
| [02-care-for-the-vulnerable](02-care-for-the-vulnerable.yaml) | emotion | Compassion that keeps alive someone who cannot keep up | Possibly 1.77 million years ago; more securely by 273,000 to 146,000 years ago | low |
| [03-the-mark-that-means](03-the-mark-that-means.yaml) | idea | The idea that a mark or an ornament can stand for something | Possibly half a million years ago; clearly by about 142,000 years ago | medium |
| [04-law-written-down](04-law-written-down.yaml) | idea | The idea that rules can be written down, made public, and applied to everyone | Writing about 5,300 years ago; published laws by about 4,100 years ago | high |
| [05-trust-between-strangers](05-trust-between-strangers.yaml) | belief | The belief that a stranger can be dealt with fairly, if the terms are honest and witnessed | Exchange between groups perhaps 320,000 years ago; written, witnessed trust by about 4,000 years ago | low |
| [06-the-gathering-place](06-the-gathering-place.yaml) | belief | The belief that some places are set apart, worth travelling to and gathering at | Built from about 11,500 years ago; out of use by about 10,000 years ago | high |
| [07-sky-calendars](07-sky-calendars.yaml) | knowledge | Knowing that the sky keeps time, and building to keep time with it | Claimed from about 20,000 years ago; Stonehenge about 4,500 years ago | medium |
| [08-fire-kept](08-fire-kept.yaml) | knowledge | Knowing how to keep fire, and later how to make it | Used about a million years ago; made at will by about 400,000 | medium |
| [09-the-fireside-story](09-the-fireside-story.yaml) | thought | The thought that what happened can be told, and told again | Surely as old as language; written down by about 4,100 years ago | low |

"Confidence in the dating" is copied from each file's `when.confidence`. A
"high" there means the dates of the evidence are secure; it does not mean the
story told about that evidence is settled. Each file separates what is
**consensus** from what is **speculation**, and marks every source that is
**contested**.

## How to read one

Start with `summary` and `restory` (a retelling in a few sentences; the word
is Tyler's, see the [glossary](../GLOSSARY.md)). Then read `consensus` and
`speculation` side by side. The `evidence` list says what each source
supports and how firmly. `tenet_links` shows where the same thing lives in
living traditions, listed alphabetically; `paradox_held` keeps the tensions
that people hold together rather than resolve.

## How to add one

1. Copy [TEMPLATE.yaml](TEMPLATE.yaml) to `NN-your-id.yaml`, where `NN` is
   the next free number and `your-id` matches the file's `id`.
2. Fill it in. The template's comments give the rules. The most important
   is: **never invent a source.** If the evidence is thin, say so.
3. Check it:

   ```
   python -m pip install pyyaml jsonschema
   python tools/validate_declarations.py
   ```

   The check runs against [the schema](../schema/origination-declaration.schema.json),
   and also makes sure the file name matches the id, no id is used twice,
   the dates run oldest first, and traditions are listed alphabetically.
4. Add a row to the table above.
