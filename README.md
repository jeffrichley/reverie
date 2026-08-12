# Reverie

**A world that keeps living when you are not there, made of beings who know only what
reached them.**

*Reverie* — the state of being pleasantly lost in an imagined place.

> ⚠️ **There is no engine yet.** This repository currently holds a design and a project
> skeleton. If you are looking for something to run today, there is nothing here.

---

## What it is

A simulation engine for persistent worlds you can drop into. Three properties, in the order
they matter:

**The world does not need to run continuously — it needs to have *run* when you arrive.**
A cheap deterministic tick advances it while nobody is watching, with no language model
involved.

**Every being knows only what reached it.** Not instructed to withhold — structurally unable
to know. Knowledge moves through discrete interactions and nowhere else.

**You can talk to one being and durably change them**, in a way that ripples to beings who
were not present.

The full architecture, the evidence behind each choice, and the prior art it descends from
are in **[docs/design.md](docs/design.md)**.

## Engine, not world

**This repository is the engine. Worlds live elsewhere.**

That is a correctness boundary rather than packaging: the engine owns the *meta*-schema —
what shape a fact must have, how changes propagate, how conflicts resolve — and a world owns
its own schema, its vocabulary, and its content. The engine's job is enforcing declarations
it did not author.

A consequence worth stating up front, because it constrains every contribution:
**the engine's test suite may not contain a domain noun.** Tests run against synthetic
worlds — fact types `t1`, `t2`, beings `a`, `b`. If an engine test needs a real-world word to
make sense, the boundary has leaked.

## Status

**Design complete enough to build against. No engine.**

The first commit of code will be the smallest thing that exercises the boundary: one engine,
two world files differing only in a declaration, producing opposite behaviour, with the same
engine bytes for both. If making the second one work requires touching engine code, the
design is wrong — and better to learn that against forty lines than four hundred.

There is also **one genuinely open question** that no published work answers, and it decides
whether the rest matters. It is stated as open in
[the design](docs/design.md#-the-open-question).

## Development

Requires [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
uv sync --all-packages     # create the environment
just check                 # lint + typecheck + tests, the same gate CI runs
```

`just` on its own lists the available recipes. A `pre-push` hook runs the same gate before
anything leaves your machine; it is wired automatically via `core.hooksPath`.

## Layout

```
packages/reverie/     the engine
docs/design.md        the architecture and its sources
docs/superpowers/     specs and implementation plans
```

## Contributing

Conventional commit subjects (`feat:`, `fix:`, `chore:`) — the release tooling reads them,
and PR titles are linted. Run `just check` before pushing.

## License

MIT — see [LICENSE](LICENSE).
