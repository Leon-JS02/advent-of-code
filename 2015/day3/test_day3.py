"""Tests for day3."""

# pylint: skip-file

import pytest

from day3 import process_direction, process_direction_string


@pytest.mark.parametrize("direction, current_loc, expected", [
    ("^", (0, 0), (0, 1)),
    (">", (0, 0), (1, 0)),
    ("v", (0, 0), (0, -1)),
    ("<", (0, 0), (-1, 0)),
    ("^", (2, 3), (2, 4)),
    (">", (-1, -1), (0, -1)),
    ("v", (1, 2), (1, 1)),
    ("<", (3, 3), (2, 3)),
])
def test_process_direction(direction, current_loc, expected):
    assert process_direction(direction, current_loc) == expected


@pytest.mark.parametrize("directions, expected", [
    (["^"], {(0, 0): 1, (0, 1): 1}),
    (["^", "v"], {(0, 0): 2, (0, 1): 1}),
    (["^", "^", "^"], {(0, 0): 1, (0, 1): 1, (0, 2): 1, (0, 3): 1}),
    ([], {(0, 0): 1}),
    (["<", "<", "<", "<"], {(0, 0): 1, (-1, 0)
     : 1, (-2, 0): 1, (-3, 0): 1, (-4, 0): 1}),
])
def test_process_direction_string(directions, expected):
    assert process_direction_string(directions) == expected
