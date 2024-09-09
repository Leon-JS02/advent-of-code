"""Test functions for day 1."""

# pylint: skip-file
import pytest

from day1 import building_floor


@pytest.mark.parametrize("floors, expected", [
    (['(', '(', ')', ')'], 0),
    (['(', ')', '(', ')'], 0),
    (['(', '(', '('], 3),
    ([')', ')', '(', '(', '(', '(', '('], 3)

])
def test_building_floor(floors, expected):
    assert building_floor(floors) == expected
