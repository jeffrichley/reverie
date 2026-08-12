# Reverie

**A world that keeps living when you are not there, made of beings who know only what
reached them.**

*Reverie* — the state of being pleasantly lost in an imagined place.

> ⚠️ **Very early.** This repository currently holds a design, not a working engine. The
> design is grounded in a literature review rather than invented from taste, and the parts
> that are unproven say so. **If you are looking for something to run today, there is
> nothing here yet.**

---

## What it is meant to be

Three properties, in the order they matter:

**1. The world does not need to run continuously. It needs to HAVE RUN when you arrive.**
A tick advances it while nobody is watching, cheaply, with no language model involved. A
day that produces *"she said the wrong thing to the wrong person on Tuesday"* is
indistinguishable from a world that simulated all night, and costs a rounding error.

**2. Every being knows only what reached it.** Not *instructed* to withhold — structurally
unable to know. Knowledge moves through discrete interactions and nowhere else. A being
cannot reveal what no conversation ever carried to it.

**3. You can drop in, talk to one being, and it changes them.** Durably, and in a way that
ripples to beings who were not present.

⇒ **Property 3 is the hard one, and as far as we can tell nobody has published a measured
result on it.** See *The open question* below.

---

## The design, and where it comes from

### Two tiers, split on write versus read

**The expensive tier sits on the mutation path. The cheap deterministic tier sits on the
read path.** Reads stay free; the cost lands where state changes.

*This was measured twice, independently, sixteen years apart — once in agent-memory
research (arXiv 2606.15903) and once in game AI, where the same codebase read a
steady-state fact in under 0.1 ms and paid ~9 ms to materialise a new one
(Sunshine-Hill & Badler, AIIDE 2010).*

### Beliefs, with provenance

A fact a being holds carries **who told it, when, how strongly, and how it was acquired** —
observed, told, inferred, or confabulated.

**Provenance is not flavour. It is a correctness requirement.** You cannot compute which
claim defeats which without knowing which were uttered and which were inferred. It is also
what makes isolation structural: scoping by belief means a being has no path to information
nobody gave it.

*Descended from James Ryan's Talk of the Town. ⚠️ Note for anyone following that trail: the
belief system is **not** in its public repository. The dissertation —* Curating Simulated
Storyworlds*, UC Santa Cruz 2018, §9.2.12 — is the only complete specification.*

### Bounded changes, and warrants

The simulation may only emit a change it can bound: **is it reversible, whose state does it
touch, and when does it expire.** A change it cannot bound is not forbidden — it is
**unrepresentable**, and goes to the author's desk instead.

**Where the author wants the simulation to do something otherwise out of bounds, they issue
a warrant**: an authored procedure granting that class of change.

🔑 **The author delegates the MECHANISM, never the OUTCOME.** *"Whoever takes the most votes
leaves"* is a delegation. Naming who leaves is not.

⚠️ **Bounds must compose.** A change with a two-day expiry that triggers a rule whose effect
has no expiry has laundered itself into a permanent one. Bounds travel as labels; a derived
fact inherits the most restrictive of its antecedents.

### Arbitration: authority before recency

**Author's reservations outrank warrants. Warrants outrank the simulation's defaults.**
Within a single level of authority, later supersedes earlier.

🔴 **Never recency across levels.** *Recency favours whoever writes most, and the simulation
writes constantly while the author writes rarely. Under a recency rule the simulation beats
the author by default, forever.*

### No projection step

**The representation does not change granularity between tiers.** A fact is the same shape
whether the cheap tier is ticking it or a language model is rendering it. Rendering is a
**read**, not a lossy transform.

⇒ *This dissolves the worst failure available to a system like this: a being who remembers
something during a conversation and has forgotten it by morning. If the conversation writes
facts, there is nothing to lose.*

---

## 🔑 The engine/world boundary

**This repository is the engine. Worlds live elsewhere and are nobody's business but their
author's.** That split is not packaging — it is the correctness property, enforced
structurally:

- **The engine owns the META-schema:** what shape a fact must have, how changes propagate,
  how bounds compose, how conflicts resolve.
- **The world owns the schema:** which fact types exist, what they mean, what values they
  take, what is salient.

🔑 **Criterion, stated so it is checkable rather than arguable: the engine is every part that
would be byte-identical if you deleted all world data and invented a completely different
world.**

⇒ **The engine's entire job is enforcing declarations it did not author.** *It may know that
a change is irreversible. It may not know what that change means.*

### The lint that keeps it honest

**The engine's test suite may not contain a domain noun.** Tests run against synthetic
worlds — fact types `t1`, `t2`, beings `a`, `b`. **If an engine test needs a real-world word
to make sense, the boundary has already leaked**, and unlike a repository split you can grep
for it in CI on the first commit.

⚠️ **A repository split stops world DATA crossing. It does nothing about a world-shaped
ASSUMPTION** — a hardcoded arity, an implicit ordering, a default that only makes sense in
one domain. Those cross cleanly. **The synthetic test suite is what catches them.**

---

## 🔴 The open question

**Nobody has published a measured result on a human's conversational input reaching beings
who were not present.** Three systems each have half of it:

| System | Human can write in | Reaches absent beings |
|---|---|---|
| Talk of the Town | ❌ | ✅ designed in full — never built |
| Mismanor | ✅ | ❌ stops at the first character |
| Generative Agents | ✅ | ⚠️ one anecdote, never measured |

⇒ **The first experiment is: talk to one being, then count how many others know a week
later.** Cheap to run, and it decides whether any of the above matters.

📌 **And the lesson from Mismanor is the design constraint:** a player-writable belief store
with no being-to-being channel is worth nothing. **What a human says must enter the world as
ordinary evidence with the human as its source** — same weight, same decay, same chance of
being disbelieved. **The moment it is a special case, it stops travelling.**

---

## Prior art worth reading

**James Ryan**, *Curating Simulated Storyworlds*, UC Santa Cruz 2018 — belief, gossip, and
fallible memory, at 300–500 characters. **Richard Evans & Emily Short**, *The AI Architecture
of Versu*, IEEE TCIAIG 6(2) 2014 — social practices as constitutive rather than regulative
rules. **Ensemble / Comme il Faut** — social exchange as the unit of action. **Park et al.**,
*Generative Agents*, UIST 2023 — memory streams and measured information diffusion.
**Sunshine-Hill & Badler**, *Perceptually Realistic Behavior through Alibi Generation*, AIIDE
2010 — materialising detail on demand without contradicting what was already observed.

---

## Status

**Design. No engine yet.** The first commit of code will be the smallest thing that
exercises the boundary: one engine, two world files differing only in a declaration,
producing opposite behaviour, with the same engine bytes for both.

*If making the second one work requires touching engine code, the design is wrong — and
better to find that out against forty lines than four hundred.*

## License

MIT.
