"""General tests."""

import curses
from functools import reduce

from a8c_cusser import __version__
from a8c_cusser._misc import _SUPPORTED_ATTRIBUTE_TAGS, _SUPPORTED_COLOR_TAGS, _app


def test_version():
    """Ensure the version is correct."""
    assert __version__ == "0.2.0"


def test_styles():
    """Ensure styles don't break."""
    message = "The quick brown fox jumps over the lazy dog"
    text = reduce(
        lambda acc, style: acc + style(message) + "\n", _SUPPORTED_ATTRIBUTE_TAGS, ""
    )
    _app(curses.initscr(), text)


def test_colors():
    """Ensure colors don't break."""
    message = "The quick brown fox jumps over the lazy dog"
    text = reduce(
        lambda acc, color: acc + color(message) + "\n", _SUPPORTED_COLOR_TAGS, ""
    )
    _app(curses.initscr(), text)
