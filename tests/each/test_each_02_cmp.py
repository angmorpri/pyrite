# 2025/07/01
"""
test_each_02_cmp.py - Comparision
"""

import pytest

from pyrite.each import each


@pytest.fixture
def base():
    return each([1, 2, 3])


def test_eq_operand(base):
    assert (base == 2).list == [False, True, False]


def test_eq_each_ok(base):
    assert (base == each([1, 2, 3])).list == [True, True, True]


def test_eq_each_bad_length(base):
    with pytest.raises(ValueError):
        base == each([1, 2])


def test_ne(base):
    assert (base != 2).list == [True, False, True]


def test_lt(base):
    assert (base < 2).list == [True, False, False]


def test_le(base):
    assert (base <= 2).list == [True, True, False]


def test_gt(base):
    assert (base > 2).list == [False, False, True]


def test_ge(base):
    assert (base >= 2).list == [False, True, True]


def test_hash(base):
    assert hash(base) == hash((base.__class__.__name__, tuple(base.list)))


def test_bool(base):
    assert bool(base) is True
    assert bool(base > 2) is False
    assert bool(each([])) is False  # Empty list should be False
    assert bool(each([0])) is False  # Not all elements are truthy should be False
