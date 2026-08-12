# Agent guidelines for reverie

This file documents conventions for AI agents (Claude Code, Codex, etc.)
working in this repo.

## Required reads before substantial changes

- `README.md` — project overview
- `CLAUDE.md` — repo-specific working conventions
- `docs/superpowers/specs/` — design specs for any in-flight feature work

## Conventions

- **Conventional commits** — PR titles enforced by CI (`pr-title-lint`).
- **Pre-push gate** — `.githooks/pre-push` runs `just check`. Don't skip.
- **Specs before code** — non-trivial features land a design doc in
  `docs/superpowers/specs/` before the implementation PR.
- **Squash-merge only** — repo is configured for squash-merge; the PR
  description becomes the commit body.

## Customize this file

Add project-specific agent guidance here. Examples:
- Forbidden imports / unsafe patterns
- Specific test discipline (TDD requirements, golden-path tests, etc.)
- Branch naming convention (e.g., `feat/<short-name>`)
- Release-validation runbook (qa-runner pattern; see scaffold-agent-core-project
  references for the pattern)
