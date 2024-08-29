# pylint: skip-file

"""Tests for day 2 of 2015's advent of code."""

from day2 import get_dimensions_from_string, calculate_area_of_smallest_side, \
    calculate_surface_area, calculate_paper_needed


def test_get_dimensions_from_string():
    assert get_dimensions_from_string("2x3x4") == [2, 3, 4]
    assert get_dimensions_from_string("3x4x5") == [3, 4, 5]
    assert get_dimensions_from_string("4x5x6") == [4, 5, 6]


def test_calculate_area_of_smallest_side():
    assert calculate_area_of_smallest_side([2, 3, 4]) == 6
    assert calculate_area_of_smallest_side([3, 4, 5]) == 12
    assert calculate_area_of_smallest_side([4, 5, 6]) == 20


def test_calculate_surface_area():
    assert calculate_surface_area([2, 3, 4]) == 52
    assert calculate_surface_area([1, 1, 10]) == 42


def test_calculate_paper_needed():
    assert calculate_paper_needed("2x3x4") == 58
    assert calculate_paper_needed("1x1x10") == 43
