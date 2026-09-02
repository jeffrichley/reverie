# Context — Reverie

The language Reverie is described in. **A glossary and nothing else** — no implementation, no
decisions, no scratch notes. Terms land here the moment they are settled, not in a batch at
the end.

**Reverie is a platform.** It runs worlds it did not author, and it comes in **three layers**:
the **core**, the **core plugins** installed on top of it, and the **seams** anyone else builds
into.

🔑 **Every term below says which layer it lives on, and that is part of its definition.** *A term
filed in the wrong layer reads as true and quietly is not — which is the whole reason the file is
split this way rather than alphabetically.*

⚠️ **Terms that only make sense inside one particular world do not belong here at all.** A world
declares its own nouns.

---

# The platform

**What is here no matter what is installed.**

## Platform

**What keeps a world running when nobody is watching, and keeps the record of it honest while it
does.** It holds what actually happened, advances time, and loads plugins that extend all of it.

**It never knows what anything means.** It can enforce that a change is irreversible; it cannot
know what that change *is*.

⇒ **The platform owns the shape of things. A world owns what things there are.**

⚠️ **The old checkable form — *"everything that would be byte-identical if you deleted all world
data and invented a completely different world"* — is retired as a test.** *It cannot tell the
core from a plugin everybody happens to install: belief machinery in a traffic simulation is
**unused**, not different, so it passes.* 🔑 **The test that works: delete the thing and see
whether the rest still means anything.** It terminates — take ordering out and ground truth is
meaningless; take ground truth out and belief is meaningless; take belief out and happenings,
branching and replay all still work — **so the core stops shrinking on its own.**

## Core

**The innermost layer — the shared machinery every plugin is built on.** Ground truth, ordering,
the fact that the record only grows. **Nobody uses it directly.** It is what lets two plugins
written by strangers talk about the same thing.

🔑 **The core is the vocabulary, not the story.**

⚠️ **"Engine" is retired as a name for anything.** *Reverie is a platform, and the platform is the
whole delivered thing. The core is only its innermost layer.*

## Core plugin

**A plugin that ships in the box and is installed for you.** It occupies the same seam anyone
else's plugin occupies, and can be replaced by one. **The being plugin is the flagship.**

🔑 **The test that separates it from the core: could you take it out and still have Reverie?**
**The slot can never be removed. The filler can always be replaced.** ⇒ *A core plugin is a
default answer to a required question, never a mandatory component.*

**Every default is the one that makes the platform do nothing, rather than the one that makes it
do everything.** ⇒ *A wrong default produces a world that visibly does not work, never one that
works and is lying.*

**What is installed for you is disclosed to you** — *these are the defaults you are running on
and you chose none of them.* **Visible, never blocking.**

**Out of the box, every seam is filled and there is nobody in the world.** *A cast is a world's
business, so anything arriving with people in it is a world, not the platform.*

## Seam

**A place where the platform requires a shape and refuses to supply the meaning.** Anyone may
build into one without touching the core and without asking permission.

**Four at the platform:** a **kind of thing a world can be made of** · a **kind of thing that can
happen** · a **way to see** · a **whole world**.

🔑 **Seams nest. A plugin opens seams of its own.** *Eclipse's Java tooling is itself a plugin,
and other plugins plug into it.* ⇒ **So most of what looks like a missing platform seam turns out
to be one plugin's internals** — the being plugin's three are below.

## Plugin

**Something that extends Reverie without changing it** — installed, not merged; used without
asking anyone's permission.

🔑 **The line the platform holds: a plugin may add anything, and may never break a guarantee.**
**Every guarantee is held one of two ways — impossible by design, or always caught
afterwards — and anything held by neither is a request, and says so.** *A guarantee that
depends on a plugin behaving is not a guarantee.* **Impossible:** editing the past · forging
order or origin · undoing a scar · reading what another plugin did not expose ·
writing except by causing a happening · granting anything below you that you do not hold
yourself — *seams nest, and nothing plugged into a plugin reaches more than the plugin
itself.* **Caught:** breaking replay. **Asked:** keeping the
vocabulary you exposed stable and honest for the strangers reading it — and honoring what the
author stated, which the generation that ships in the box does.

**A plugin's facts are sealed by default and exposed by its choice — the core withholds
nothing; it simply holds.**

📌 **The model is Eclipse and VSCode**, deliberately: a thin core, an ecosystem, and no central
permission to build on it. *Eclipse's own core is a workspace and a plugin loader; the IDE is
plugins. **Reverie's core being small and dull is the model working**, not a warning sign.*

## World

**One setting and everything in it** — what is there, what has happened, what is true. A season
on an island, a ship's crew on a long voyage, a street of houses.

**A world is itself a plugin**, so it is shareable, forkable and installable like any other.

⚠️ **A world's cast, its places and its things are the world's business.** The platform never
names them.

## Author

Whoever owns a world. **The author outranks the simulation always**, regardless of who wrote
last.

⇒ **Generation may fill anything the author did not state, and the generation that ships in
the box honors what they did.** Generation is a default, never an override. ⚠️ *That is
conduct, not machinery: an overturned authorial fact is **always visible to the author who
looks, never caught by the platform** — the author manages their own data, sees all of it, and
replaces a plugin that keeps drifting it. There is no pin* (see **Retired terms**).

🔑 **An author is either outside the world or someone in it. There is no third position.**
Outside, they act on the world — *cause a happening*, *change the rules going forward* — or on
its record — *branch* (see **Append-only**) — and nothing they do edits the past. **Inside
requires beings to exist** — see **Possession**, which arrives with the being plugin.

**Four verbs are the platform's: observe · cause a happening · author · control time.** *Become
someone* is a fifth that comes with beings.

**Observing leaves no trace** — no record of it, and nothing in the world can ever come to know
it happened.

⚠️ **Nothing an author does is reversible except by branching, and the branch is recorded.**
A branch sweeps everything after its point — the author's own acts included — *so no
authorial residue ever steers a regrown week.*

## Happening

Something that occurred in a world. **The world's own record of it** — as distinct from what
anyone makes of it.

**Some happenings have a doer and some do not.** It rains, the boat does not come, a tree falls
— nobody looks for a person behind those.

🔑 *(being plugin)* **A happening a being would attribute to a person requires a person inside the
world to have done it.** ⇒ *So there is no speaking from nowhere — and in a world where there
were, nobody could be lied to.*

## Ground truth

**What actually happened, held apart from what anything in the world makes of it.**

🔑 **The platform carries it, and nothing inside can reach it.** *The world knows; nobody in it
does.*

⇒ **A run can be checked against reality.** *(being plugin)* Two further consequences arrive with
beings: **information spread can be measured** — tell one being something, count who knows a week
later — and **a lie is only a lie if there is a fact for it to contradict.**

## Ordering

**What came before what.** The platform owns this and requires it — provenance is worthless
without it, and *"she already knew by Tuesday"* is unanswerable.

⚠️ **The platform does not know what a tick MEANS.** A day, a turn, an hour — that is the
world's. *Require the structure, leave the meaning.*

## Append-only

**The simulation may only ever add to ground truth.** It can never change what already
happened.

**The author may branch — there is no other way to touch the past, and "rewind" was always
this.** The author picks a moment; a new timeline grows fresh from there — fresh dice, no
promise the week comes back the same, *because the branch itself is a cause*. **No surgical
edit exists**: "remove the ravine, keep the vote" is not a thing anyone can say — beliefs are
world-state and revert with everything else, so nothing ever orphans.

⚠️ **Nothing is ever lost.** The old branch survives — frozen, it is the **scar**: the fork
point plus the abandoned timeline, visible to the author forever, invisible from inside; kept
running, it is a sibling world, which forkable worlds already allow. A frozen branch costs
nothing, because nothing happens in it. ⇒ *A truth layer that can be silently edited is not a
truth layer — and a branch is recorded, never silent.*

**A branch is never refused — an irrevocable happening included.** What escaped the world
stays escaped, the record never lies about it, and the new branch simply does not contain it.
**How many days and happenings a branch abandons is always knowable before branching**;
showing it is a view's business.

## Replay

**Same starting state, same inputs, same week.** How a run gets checked against reality more
than once, how *"what would have happened if I had not walked in"* is answerable, and the only
way to debug a world at all.

🔴 **Promised only as far as the plugin set allows.** *A plugin that ignores the seed voids it,
and the platform has no say* — it cannot promise determinism it does not control.

🔑 **So the guarantee the platform actually makes is detection: when a plugin breaks replay,
you find out.** ⚠️ *A silently non-replayable world looks fine and quietly is not.*

📌 Consequence: **anything genuinely random — a language model's output included — is captured
on the way past**, or the promise is a lie the first time you rerun.

## Cost

**A world costs what happened in it, never what it contains.** The quiet week is free: a week
where nothing expensive happened costs almost nothing to have run, and the size of the world
does not change that — *a million scenery beings passing a quiet Tuesday cost what one does.*

🔑 **A step takes what it takes.** There is no falling behind — *"behind" presumes a schedule
the world owes somebody, and it owes nobody anything.* An expensive week simply takes longer,
and costs more, to have run.

**The record never fills, and whatever is slow in a world, it is never the record** — the cost
of a tick is the cost of what happened in it.

⚠️ **No number appears anywhere in the promise.** The ceiling belongs to the installed plugin
set — a vectorized crowd sim holds millions, an LLM-backed conversation holds a dinner table,
and both are Reverie worlds. *Every published number in the field is a configuration somebody
chose.*

---

# The being plugin

**The flagship core plugin.** Installed for you, and removable. **Take it out and there is no
witness, no liveness, no being seen at all** — what remains is a world that runs unattended, only
ever adds, and can be rewound.

⚠️ **Everything in this section is therefore contingent.** A world of traffic, or weather, or a
factory floor has none of it, and is still a Reverie world.

**It opens three seams of its own:** a **mind** — what a being does with what she believes · a
**witness rule** — how the witness list gets computed, which is where geography lives · a
**liveness rule** — what moves a being between minds.

**Its flagship promise, made to its own mind seam: a mind is never handed more than what
reached its being.** The plugin's own code reads the public record — that is what a witness
rule is for — and a mind receives only the witnessed subset. 🔑 *This promise is the
being plugin's, not the platform's — beings do not exist at the platform level — and it
is the clause that makes lying possible.*

**However long a moment takes to compute, the world inside it stays whole.** A step that takes
fifteen minutes to make does not leave the world deaf for fifteen minutes: someone can arrive
mid-happening and be seen, and what happens bends around them — *three people talking privately
change the subject when the one on the outs walks up.*

## Being

Anyone who could hold a belief. **"Could" is the whole test** — a being running the cheapest
mind is still a being: hand her a deeper one and she was always there. A thing that could never
hold a belief is not a being, no matter how much it is acted upon.

⚠️ **Not everything that moves in a world is a being.** A crowd that could never believe —
townsfolk who are set dressing by construction — is another plugin's kind of thing, not a
cheap being.

## Belief

What a being holds true, together with **how it came to them** — observed, told, inferred,
confabulated — and from whom.

**That provenance is written true at formation, and it is the author's view** — what a
mind-swap hands over, what the chain view renders. **What *she* holds about where a belief
came from is another belief** — plantable, wrong, confabulated like any other. ⇒ *"Who told
you?" is always answered by her account, never by the record* — two of nine genuinely do not
remember being told, and the record still says *told, by Cass*.

🔑 **From inside, the most anyone can ever recover is the last hop.** A telling she witnessed
is a happening on her record forever — **fading is a mind's; the tape never fades** — while
the hop before her reached her nowhere, so it is sealed away by design: **a rumour launders
itself across hops structurally, one hop at a time, under any mind.** Whether the hop she
*did* witness stays reachable is the mind's business — permitted, never promised — so
traceable rumours and self-laundering ones are both an author's choice of minds. ⚠️ *A trace
never surfaces the author: a planted telling traces to the being who spoke, and an
outside-caused happening has no teller.*

**Beliefs are the only social state there is.** There is no relationship primitive: *"they are
married"* is not stored, it is what you get when you read two beings' beliefs together.

⇒ **Asymmetry is therefore free and normal.** He loves her, she tolerates him — both true, no
special case. *A stored relationship would drift from the beliefs under it, and the world would
end up insisting on a marriage neither party believes in.*

📌 **Relationships are a plugin built on this one.**

## Utterance

Something a being said. **A happening like any other** — ordered, witnessed, origin attached —
and **only the saying is ever recorded: what she held while saying it reached nobody.**

🔑 **Nothing anywhere requires an utterance to match a belief — there is no machinery that
could even check.** ⇒ *Most lying is not inventing facts. It is saying a true-shaped thing you
do not hold, to a chosen audience — she knows exactly how she feels, and says otherwise,
because of who is listening and what it is worth to her.*

**The same words from a different asker are a different happening.** Audience is who witnessed
the saying — so a different answer is always possible, and nothing more is promised. *What she
would say to you is not what she would say to Ben.*

**The author sees the gap live** — ground truth holds the saying, every belief holds the
holding — *visible to an author who looks, never caught by the platform.*

🔑 **Lying has no floor.** The cheapest mind can say what it does not hold — *the lie is
cheap, only the sentence is expensive.* ⚠️ *What shapes an utterance — audience, incentive,
fear, trust, personality — is the mind's business, not this glossary's.*

## Witness list

**Who saw a happening.** Every happening has one, and **only witnesses can come to know it.**

🔑 **The witness list is required. Space is not.** *How the list gets computed is the **witness
rule**, which is a seam* — a room, a guest list, a chat thread, a phone line, a letter that
arrives three days later.

⇒ **The phone call is why.** Two beings exchange something with no shared location at all. If
geography were a primitive, that call would have to be faked into a room that does not exist —
and a letter would be worse.

📌 **Places are a witness rule.** A world that wants geography installs one.

⚠️ **Its fail-closed default is the empty list — nobody learns anything.** *A world where nobody
knows anything is visibly broken inside a minute. A world where everyone knows everything looks
like a well-informed island and is silently wrong forever.*

## Liveness

**How alive a being is, is which mind she is running.** A name, a job and a clock · a tick that
gossips and holds grudges · a model that finds fresh words — all of them are minds, and a being
on the cheapest is exactly as *present* as one on the dearest: she witnesses what reaches her,
and makes of it what her mind can.

🔑 **"Is anyone home?" was the wrong question. Nobody is ever absent** — there is no scenery
mode, no waking, and no seam to keep shut: a being always witnessed what reached her and always
made exactly what her current mind could make of it. **"Scenery" survives only as the informal
word for a being running the cheapest mind.** ⇒ *Aliveness is not a yes/no — and it has no
top.*

**The liveness rule is what moves a being between minds when events warrant.** The author sets
the defaults and outranks it always. 🔴 **It moves beings when it matters, never to pay a
bill** — making a world cheaper is the author's act alone. ⚠️ *Its triggers — what earns a
deeper mind, what hands back a cheaper one — are the being plugin's own business, not this
glossary's.*

🔑 **A mind swap loses nothing.** What reached her being and what she believes are hers, not the
mind's — **the incoming mind is handed everything that reached her**, beliefs and witnessed
record both, so a deeper mind can infer late: *now that I think about it, his sleeves were
wet.*

**Cost tracks depth and events, never population** — the same beings cost several times more in
a busy hour than a quiet one. 🔑 **Scenery is free; depth is metered** — and the meter reads
what happened, never how many exist. ⇒ *The failure mode of an expensive world is time and
money, never fidelity.*

## Confabulation

**A belief a being formed to explain something they did not decide.**

🔑 **Anything done to a being from outside is remembered by them as their own, and they cannot
tell otherwise.** A forced act, a possessed hour, a possessed week — **one mechanism covers all
three.**

⚠️ **A world may choose the harsher version: a hole.** *She did it and does not know why.*
**Confabulation is the default because it is what people actually do.**

## Possession

**Being someone in a world.** You see only what she knows · **nobody can tell it is you** · and
**she keeps what you did as her own** (see **Confabulation**).

🔑 **A stranger and a lifelong resident are the same verb** — the only difference is how much
past the body has, and a walk-on may be created on arrival. ⇒ *You drift from one to the other
by turning up: a stranger seen five times is not a stranger.*

**One body at a time.** *Two at once is the union of two people's knowledge, which is not being
either of them.*

🔑 **Asking and compelling are two different verbs, never one verb with a strength dial.** *If
asking sometimes simply works, nobody can tell whether she agreed or obeyed — and that
difference is the whole reason to be there.* **Whether beings may refuse at all is a world's
setting.**

**The world never outruns you without consent.** While you are someone, your reply is the clock
by default; whether a silence can be an answer — a council that votes without you — is a
world's setting.

## Floor

**How empty a world may get.** Beings can leave and can die; **a world cannot empty below the
floor its author set.**

⇒ *Without it, the interesting thing about a world that runs unattended is also the thing that
destroys it.*

⚠️ **This term straddles the layers and is filed here provisionally.** *"A world cannot end" looks
like the core's; "how empty, of what" is whatever supplies a population. Its fail-closed default
is **one**, which is the core half restated.*

---

## Retired terms

Kept only so that a word appearing in an older ticket can be looked up.

- **Refusal** — *something a world had to supply that the platform would not start without and
  would not default.* **Retired**: it rested on a missing witness rule producing omniscience,
  and a missing one produces silence instead. What replaced it is the fail-closed default rule
  under **Core plugin**, plus disclosure.
- **Engine** — never meant anything distinct from **Platform** or **Core**, and meant both at
  different times. Use those.
- **Visitor** — an outside-but-present third position. **Retired while settling the author's
  verbs**: you are either outside the world or someone in it.
- **Scenery (as a mode)** — *a state a being was in — "a life happening with nobody home" —
  flipped by waking.* **Retired while resolving liveness**: there is no mode — a being is as
  alive as the mind she is running, and nobody is ever absent. The word survives only
  informally, for a being on the cheapest mind.
- **Pin** — *an author's mark on a fact that generation could never overturn, always caught.*
  **Retired while resolving what a branch reaches**: it existed to save the author from the
  plugins they chose, and the author manages their own data — ownership walls plugins off from
  each other, the author sees everything and outranks everything, and a plugin that drifts an
  authored fact is replaced, not refereed. A "lock this fact" feature is any plugin's to offer
  over its own data.
- **Rewind** — *going back.* **Retired as a name**: there was never a rewind, only a
  **branch** — a new timeline grown fresh from a chosen moment, with the old one kept as scar
  or sibling. "Undo" implied the past could be edited; nothing edits the past.
