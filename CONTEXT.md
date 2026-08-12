# Context — Reverie

The language Reverie is described in. **A glossary and nothing else** — no implementation, no
decisions, no scratch notes. Terms land here the moment they are settled, not in a batch at
the end.

**Reverie is a platform.** It runs worlds it did not author. So every term below is either
something the platform owns, or something it explicitly leaves to a world — and which one is
part of the definition.

---

## Platform

**What keeps a world running when nobody is watching, and keeps every being's knowledge honest
while it does.** It holds what actually happened, decides who could have learned it, advances
time, refuses worlds that would break those guarantees, and loads plugins that extend all of
it.

**It never knows what anything means.** It can enforce that a change is irreversible; it cannot
know what that change *is*.

🔑 **Checkable form, for settling arguments about where a thing belongs: the platform is
everything that would be byte-identical if you deleted all world data and invented a completely
different world.**

⇒ **The platform owns the shape of things. A world owns what things there are.**

## World

**One setting and everything in it** — who is there, what has happened, what is true. A season
on an island, a ship's crew on a long voyage, a street of houses.

**A world is itself a plugin**, so it is shareable, forkable and installable like any other.

⚠️ **A world's cast, its places and its things are the world's business.** The platform never
names them, and a term that only makes sense inside one world does not belong in this glossary.

## Plugin

**Something that extends Reverie without changing it** — installed, not merged; used without
asking anyone's permission.

**Three kinds are known:** a new way to **see** a world · a new **kind of thing that can
happen** · **a whole world**. *Relationships and places are both plugins, having been ruled out
of the platform.*

🔑 **The line the platform holds: a plugin may add anything, and may never break a guarantee.**
⚠️ *What the platform requires of a plugin's behaviour — and how it knows when one broke a
promise — is not settled yet. **Replay is the known case where the platform promises something
it cannot enforce**, so what it guarantees there is detection rather than prevention.*

📌 **The model is Eclipse and VSCode**, deliberately: a thin core, an ecosystem, and no
central permission to build on it.

## Being

Anyone who could hold a belief. **"Could" is the whole test** — a being who is currently
scenery is still a being, because they can wake. A thing that could never hold a belief is not
a being, no matter how much it is acted upon.

## Belief

What a being holds true, together with **how it came to them** — observed, told, inferred,
confabulated — and from whom.

**Beliefs are the only social state the platform provides.** There is no relationship
primitive: *"they are married"* is not stored, it is what you get when you read two beings'
beliefs together.

⇒ **Asymmetry is therefore free and normal.** He loves her, she tolerates him — both true, no
special case. *A stored relationship would drift from the beliefs under it, and the world would
end up insisting on a marriage neither party believes in.*

📌 **Relationships are a plugin.** A world that wants them builds them on top of beliefs.

## Happening

Something that occurred in a world. **The world's own record of it** — as distinct from what
anyone believes about it.

## Ground truth

**What actually happened, held apart from what anyone thinks happened.**

🔑 **The platform carries it, and no being can ever reach it.** *The world knows; nobody in it
does.*

⇒ Three things depend on it: **a run can be checked against reality** · **information spread
can be measured** — tell one being something, count who knows a week later · and **a lie is
only a lie if there is a fact for it to contradict.**

## Witness list

**Who saw a happening.** Every happening has one, and **only witnesses can come to know it.**

🔑 **The platform requires the witness list. It does NOT require space.** *How the list gets
computed is the world's business* — a room, a guest list, a chat thread, a phone line, a letter
that arrives three days later.

⇒ **The phone call is why.** Two beings exchange something with no shared location at all. If
geography were the platform's primitive, that call would have to be faked into a room that does
not exist — and a letter would be worse.

📌 **Places are a plugin**, exactly like relationships. A world that wants geography brings it.

## Liveness

Whether a being is **alive** (an inner life, running) or **scenery** (a name, a job and a
clock; a life happening with nobody home).

🔑 **Liveness is a MODE a being is in, not a status they acquire.** The same being is alive on
Tuesday and scenery on Wednesday. ⇒ *If it were acquired, worlds would ratchet — met once,
alive forever — and every world would eventually be expensive everywhere.*

⚠️ *What wakes a being, what puts them back to sleep, and what is true of a sleeping one are
not yet settled — see the map.*

## Author

Whoever owns a world. **The author outranks the simulation always**, regardless of who wrote
last.

⇒ **Generation may fill anything the author did not pin, and may never overturn anything they
did.** Generation is a default, never an override.

## Refusal

Something a world must supply, which the platform **will not start without and will not
default**.

🔑 **The test for one — and it is a test, not a list: a default would fail SILENTLY.** *A
missing witness rule does not crash. It produces a world where everyone is omniscient and
nothing looks wrong.*

**Three are known: how witnesses are computed · the floor · what the simulation may write as
against the author.** ⚠️ **"These three, and probably others"** — three were found by looking,
and an enumeration presented as complete gets believed.

## Floor

**How empty a world may get.** Beings can leave and can die; **a world cannot end, and cannot
empty below the floor its author set.**

⇒ *Without it, the interesting thing about a world that runs unattended is also the thing that
destroys it.*

## Ordering

**What came before what.** The platform owns this and requires it — provenance is worthless
without it, and *"she already knew by Tuesday"* is unanswerable.

⚠️ **The platform does not know what a tick MEANS.** A day, a turn, an hour — that is the
world's. *Same shape as the witness list: require the structure, leave the meaning.*

## Append-only

**The simulation may only ever add to ground truth.** It can never change what already
happened.

**The author may rewind — and the rewind is itself recorded.** ⇒ *A truth layer that can be
silently edited is not a truth layer.* ⚠️ **The cost, stated rather than buried: worlds carry
scars.** Every rewind is visible to the author forever, and to nobody inside.

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
