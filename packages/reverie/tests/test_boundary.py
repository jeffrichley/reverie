"""The boundary, exercised.

Two worlds differing only in a declaration, producing opposite behaviour, with
the same engine for both. If making the second one work ever requires changing
engine code, the design is wrong.

No domain vocabulary appears here. Fact types are `t1`/`t2` and that is
deliberate: the README makes "engine tests may not contain a domain noun" a
rule, and this file is where it either holds or starts eroding.
"""

import pytest

from reverie import NotActionable, UndeclaredFactType, World, Writer, may_write, write

# The ONLY difference between these two worlds.
OPEN_WORLD = World.from_mapping({"t1": {"actionable": True}})
RESERVED_WORLD = World.from_mapping({"t1": {"actionable": False}})


def test_same_write_is_permitted_in_one_world_and_refused_in_the_other() -> None:
    """The whole claim, in one assertion pair. Same call, same engine."""
    write(OPEN_WORLD, "t1", Writer.SIMULATION)

    with pytest.raises(NotActionable):
        write(RESERVED_WORLD, "t1", Writer.SIMULATION)


def test_the_author_is_not_bound_by_actionable() -> None:
    """`actionable` governs the simulation. It says nothing about the author."""
    write(RESERVED_WORLD, "t1", Writer.AUTHOR)
    assert may_write(RESERVED_WORLD, "t1", Writer.AUTHOR)


def test_an_undeclared_type_is_refused_rather_than_defaulted() -> None:
    """Absence of a declaration is not permission.

    A type nobody declared must not fall through to allowed -- that is the
    failure where a boundary quietly stops existing.
    """
    with pytest.raises(UndeclaredFactType):
        may_write(OPEN_WORLD, "t2", Writer.SIMULATION)


def test_a_declaration_missing_actionable_fails_at_load_not_at_write() -> None:
    """The error arrives while authoring, not deep in a simulation run."""
    with pytest.raises(UndeclaredFactType):
        World.from_mapping({"t1": {}})
