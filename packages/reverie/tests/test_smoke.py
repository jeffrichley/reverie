"""Smoke test: the package imports and the workspace is wired.

Uses no domain vocabulary, per the boundary lint described in the README.
"""

import reverie


def test_package_imports() -> None:
    """The package imports and carries its module docstring."""
    assert reverie.__doc__
