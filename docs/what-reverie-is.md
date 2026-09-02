# What Reverie Is

> A world that keeps living when you are not there, made of beings who know only what
> reached them.

You can lie to someone, and she'll act on it, and she can tell someone else, and he'll
believe it came from her. That sentence is the product. Everything below exists so that it
is true — and so that it stays true no matter what is loaded, who built the world, or how
long you were away.

Reverie is a **platform**, not an engine and not a game: it runs worlds it did not author,
on the Eclipse model — a small, dull core, an ecosystem of plugins, and no central
permission to build. This document says **what** Reverie is: what the platform requires of
every world and guarantees regardless of what is installed, what its flagship plugin adds
on top, what you can do in any world, and where the seams are. It never says what any
particular world contains — a world's cast, places, and things are that world's business —
and it never says how any of this is built. The vocabulary here is the canonical one; the
glossary in [`CONTEXT.md`](../CONTEXT.md) holds each term's full definition.

---

## 1. The shape of the thing

Reverie comes in three layers, and every promise in this document names the layer it lives
on.

- **The core** — the shared machinery every plugin is built on. Nobody uses it directly.
  Its whole vocabulary is three words — **Thing · Happening · Fact** — plus the platform's
  conduct. *The core is the vocabulary, not the story.*
- **Core plugins** — plugins that ship in the box and are installed for you. Each occupies
  an ordinary seam and can be replaced by anyone's alternative. **The being plugin is the
  flagship.** A core plugin is a default answer to a required question, never a mandatory
  component.
- **Seams** — where everyone else builds, without asking permission. There are four at the
  platform, and **seams nest**: a plugin opens seams of its own, exactly as Eclipse's Java
  tooling — itself a plugin — hosts plugins of its own.

**A world is itself a plugin.** Worlds are shareable, forkable, and installable; "core vs
plugin" and "platform vs world" are the same boundary. A world can be fully authored, fully
generated, or anywhere between — **authored ↔ generated is a dial, not a rule** — and
generation fills what the author left open, while the generation that ships in the box
honors what the author stated.

Out of the box, **every seam is filled and there is nobody in the world.** A cast is a
world's business; anything arriving with people in it is a world, not the platform.

---

## 2. What the platform holds, no matter what is loaded

*Layer: the core.*

### The record

- **Ground truth exists and no being can reach it.** The platform holds what actually
  happened, distinct from what anyone makes of it.
- **Happenings are definitely ordered, and nothing happens anonymously.** Every happening
  carries its origin; order and origin can never be forged. The platform owns ordering; the
  world owns what a tick means.
- **Happenings are never sealable.** The record is the one surface every plugin reads —
  it is how two plugins written by strangers talk about the same thing. Privacy lives in
  facts, never in happenings.
- **The record only appends.** The simulation can only add; nothing edits the past — not a
  plugin, not the author, not the platform itself. "Remove the ravine, keep the vote" is
  not a thing anyone can say.
- **There is one way in, and it is everyone's.** A plugin, a mind, the author — every
  change enters the same way: a happening appended to the record. And everything
  downstream reacts to the record, never to being called — *nothing reacts to the doing;
  everything reacts to the done* — so nothing can be bypassed, and a happening's
  consequences never depend on who caused it. *This is why the author's hand can be
  invisible from inside.*
- **Only whole happenings are ever recorded.** A step that cannot complete has not
  happened.
- **A fact is owned by the plugin that stated it — sealed by default, exposed by its
  choice.** There is no global pool of facts: a fact lives with its owner, and exposure is
  a published vocabulary, not a shared format — what a plugin exposes, it is asked to keep
  stable and honest for the strangers reading it, and strangers read that, never arbitrary
  bits. **The core never reads a fact — it holds the seal, the ownership, and the link:
  every fact became true by a happening**, backstory included — which is why a branch
  reverts every plugin's facts with everything else.
- **One mark: *irrevocable*.** A happening so marked is never pretended away by any branch
  — the scar stays visible in every timeline that contains it.

### Branching, not rewinding

**There is no rewind — there was only ever a branch.** The author can grow a new timeline
from any chosen moment: fresh dice, because the branch itself is a cause. Nothing is ever
lost — the old branch frozen is the scar (and costs nothing, since nothing happens in it);
kept running, it is a sibling world. **A branch is never refused**, irrevocable happenings
included, and it sweeps the author's own acts after its point, so no authorial residue
steers a regrown week. **Replay** is read-only playback of a branch's tape — the decisions
already made, handed back — and it never consults anything that could answer differently.

### The plugin contract

A plugin may add anything, and may never break a guarantee. **Every guarantee names how it
is held**, one of three ways:

- **Structural — impossible by design:** editing the past · forging order or origin ·
  undoing a scar · reading what another plugin did not expose · writing except by causing a
  happening with origin attached · granting anything below you that you do not hold
  yourself (seams nest, and nothing plugged into a plugin reaches more than the plugin
  itself).
- **Caught — possible, always detected:** exactly one — breaking replay.
- **Asked — convention and reputation, said plainly:** keeping the vocabulary you exposed
  stable and honest, and honoring what the author stated.

The platform does not type plugins — whether one shows, changes, or both is its developer's
call — and it never referees them: the author sees everything and outranks everything, and
a plugin that drifts is **replaced, not refereed**.

### Defaults and disclosure

**Every default is the one that makes the platform do nothing**, never the one that makes
it do everything. A wrong default produces a world that visibly does not work — never one
that works and is lying. What is installed for you is disclosed to you: *these are the
defaults you are running on, and you chose none of them.* Visible, never blocking. **A
plugin names what it needs, and the platform will not load it half-fed; the world can
always name what it is missing.**

### When something dies with the world live

**A world that cannot take its next step takes no step.** The world stalls at the moment a
step needs the missing thing — never at the moment of death — and it never limps: the
platform will no more run a world half-fed than load one. **From inside, a stall is
indistinguishable from a slow moment**; no time passes during an outage, so nobody in the
world can ever witness one, and the outage is not a happening — it lands in the platform's
own ledger, where the world names what it is missing. **Coming back is not a branch**: the
in-flight step simply happens now, its first roll, and sim time is continuous across any
outage.

### What it costs

**A world costs what happened in it, never what it contains.** The quiet week is free — a
million scenery beings passing a quiet Tuesday cost what one does. The record never fills,
and whatever is slow in a world, it is never the record. **A step takes what it takes**:
there is no falling behind, because "behind" presumes a schedule the world owes somebody,
and it owes nobody anything. **No number appears anywhere in the promise** — every
published number in this field is a configuration somebody chose. The world never demotes
anyone, never drops a happening, never decides who matters; making a world cheaper is the
author's act alone. **The named failure mode is time and money, never fidelity** — Reverie
fails by presenting a bill, not by getting shallower. And **however long a moment takes to
compute, the world inside it stays whole.**

---

## 3. What you can do in any world

*Layer: the core — except* become someone*, which arrives with the being plugin.*

There are two positions: **outside the world, or someone in it.** There is no visitor — a
tourist and a lifelong resident are the same verb with different amounts of history behind
the body. The platform guarantees these verbs and nothing more concrete:

- **Observe.** You see ground truth and every belief at once, at any point, chains
  included. Watching leaves no trace.
- **Cause a happening.** You can cause anything; the world's reaction is the cost, and no
  preview softens it. What you cause enters the same shared record every plugin reads —
  the kinds available to cause are the world's installed vocabulary, but causing needs no
  plugin's mediation. To be *perceived*, you must be someone.
- **Become someone** *(with beings installed)*. You see only what she knows; the others
  cannot tell it is you — nobody can, ever; and she keeps the memory of what you did as
  her. One body at a time. **Possession is for answering, not for knowing** — you already
  see everything from outside; what you cannot do from there is be the one who has to
  reply.
- **Author.** Act on the world going forward: state facts, place things, adopt or overrule
  what generation proposed. **The author is just another source of false belief** — what
  you put in a head is believed honestly, and the only undo is the branch that scars.
  Asking and compelling are two verbs, never one with a dial. Generation may fill anything
  you did not state and may never overturn anything you did.
- **Control time.** Let it run, or say how far to advance — time runs by default, and speed
  is presentation. **The world never outruns a present human without consent.**

A world **advises and never forbids**. Nothing is reversible except a branch. The author
sees the gap between what anyone says and what they hold, live — *visible to an author who
looks, never caught by the platform.*

---

## 4. The being plugin

*Layer: core plugin — the flagship. Installed for you, replaceable by anyone.*

Strip it out and Reverie still means something — a world that runs unattended, only ever
adds, and can be branched. Install it and the worlds get people.

### Beings and beliefs

A **being** is anyone who could hold a belief — "could" is the whole test. A **belief** is
what a being holds true, together with how it came to them — observed, told, inferred,
confabulated — and from whom. **Beliefs are the only social state there is**: no
relationship primitive, so asymmetry is free and normal — he loves her, she tolerates him,
both true, no special case.

**The flagship clause: a mind is never handed more than what reached its being.** This is
the being plugin's half of "ground truth is unreachable from inside," and most of what
follows falls out of it.

Every happening has a **witness list** — who saw it — and only witnesses can come to know
it. **The witness list is required; space is not.** Places are a witness rule; a world that
wants geography installs one.

### Aliveness

**A being is as alive as the mind she is currently running, and aliveness has no top.** A
name, a job, and a clock is the cheapest mind, not the absence of one — so nobody is ever
absent, and there is no scenery mode, no waking, no seam to keep shut. The **liveness
rule** moves a being between minds when events warrant; the author sets its defaults and
outranks it always, and **it never acts to pay a bill**. A mind swap loses nothing — the
incoming mind is handed everything that reached the being, so a deeper mind can infer late:
*now that I think about it, his sleeves were wet.* **Scenery is free; aliveness is metered
by what happened, never by how many exist.**

### Saying and lying

An **utterance** is a happening like any other — ordered, witnessed, origin attached — and
**only the saying is ever recorded: what she held while saying it reached nobody.**
Nothing anywhere requires an utterance to match a belief; there is no machinery that could
even check. Most lying is not inventing facts — it is saying a true-shaped thing you do not
hold, to a chosen audience. The same words from a different asker are a different
happening, so a different answer is always possible. **Lying has no floor**: the cheapest
mind can say what it does not hold — the lie is cheap; only the sentence is expensive.

### Where beliefs come from, and whether anyone can trace them

The provenance **on** a belief is written true at formation, and it is the author's view.
What *she* holds about where a belief came from is another belief — plantable, wrong,
confabulated like any other. *"Who told you?" is always answered by her account, never by
the record.*

**From inside, the most anyone can ever recover is the last hop.** The telling she
witnessed is on her record forever — fading is a mind's; the tape never fades — while the
hop before her reached her nowhere, sealed away by the flagship clause. **A rumour launders
itself across hops by design**, one hop at a time, under any mind — and anyone can
counterfeit a chain for free, because claiming a source is just saying words. Whether the
hop she did witness stays reachable is the mind's business — permitted, never promised — so
traceable rumours and self-laundering ones are both an author's choice of minds. **A trace
never surfaces the author**: a planted telling traces to the being who spoke.

### Confabulation and possession

**Anything a being did not decide, she remembers as her own.** Confabulation covers a
forced act, a possessed hour, and a possessed week alike — it is the default because it is
what people actually do. When you leave a body, she keeps what you did as her own, and
nobody — including her — can ever tell it was you.

### Leaving, dying, and the floor

Beings can leave and can die. **A world cannot end, and cannot empty below a floor the
author sets.** The floor's content is the world's; the promise that one can exist is the
plugin's.

### The being plugin's own seams

Three, and their interiors belong to the being plugin's own design, not this document:
**a mind** (what a being runs on — what shapes an utterance, what it keeps, what it
surfaces) · **a witness rule** (how the witness list gets computed — where geography
lives) · **a liveness rule** (what moves a being between minds). Each filler is itself a
plugin — seams nest — so a mind is a plugin plugged into the being plugin, and the
cheapest one (a name, a job, and a clock) ships in the box. What this document fixes
about them: a mind is never handed more than what reached its being; a liveness rule never
acts to pay a bill; and every seam beneath the plugin inherits the plugin contract — seams
nest, and nothing plugged in reaches more than its host.

---

## 5. The seams

*Layer: the platform's edge.*

Four places where the platform requires a shape and refuses to supply the meaning:

1. **A kind of thing a world can be made of.**
2. **A kind of thing that can happen.**
3. **A way to see.** Views are plugins — an arrival screen that leads with a disagreement
   is one choice among many; what the platform guarantees is that the author sees ground
   truth and every belief at once, so a view *can*.
4. **A whole world.**

Anyone may build into any of them without touching the core and without asking permission.
**The seams are open, and there is no marketplace** — distribution returns only if this
earns it.

---

## 6. The horizon, named so it is not silently absent

- **VR.** It changes what *arrive* means. Stated, and deliberately not answered here.
- **A full-fidelity New York.** *"You can ask for New York"* stays; *"all eight million are
  thinking"* does not — everyone-has-an-inner-life versus becomes-one-when-you-meet-them is
  indistinguishable from inside, and only one is buildable.
- **One human in a world at a time** — assumed, not promised.
- **Every world is self-contained** — a being's record lives in one world. Worlds fork,
  and a kept branch is a sibling world; nothing crosses between them.

---

## Status

This document is the destination of the wayfinder map
[Reverie — what it is](https://github.com/jeffrichley/reverie/issues/8) — eighteen
decisions, each held in its closed ticket, indexed on the map. The build it plans for is
greenfield: the current code is discarded; the repo, its name, CI, and the `reverie-engine`
PyPI registration are kept. Much of the core is expected to be adopted rather than written
— which existing thing fills each requirement is the builder's decision, later. The being
plugin's interior gets a map of its own, seeded by the decisions stamped to it here.
