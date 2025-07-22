# 2025/07/02
"""
test_each_04_container.py - Behavior as a container and iterable.
"""

import pytest

from pyrite.each import each


@pytest.fixture
def matrix():
    return each(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )


def test_len(matrix):
    assert len(matrix) == 3


def test_iter(matrix):
    assert list(matrix) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_reversed(matrix):
    assert list(reversed(matrix)) == [[7, 8, 9], [4, 5, 6], [1, 2, 3]]


def test_contains(matrix):
    alt = each([[1, 2], [1, 2], [1, 2]])
    assert 2 not in matrix  # Not in all objects in the matrix
    assert 2 in alt  # Yes in all objects in the alternative list


def test_contains_each(matrix):
    assert each([1, 2, 3]) not in matrix
    assert each([1, 5, 9]) in matrix


def test_getitem_standard(matrix):
    assert matrix[0].list == [1, 4, 7]
    assert matrix[1].list == [2, 5, 8]
    assert matrix[2].list == [3, 6, 9]


def test_getitem_slice(matrix):
    assert matrix[:2].list == [[1, 2], [4, 5], [7, 8]]


def test_getitem_each(matrix):
    assert matrix[each([0, 1, 2])].list == [1, 5, 9]


def test_getitem_boolean_each(matrix):
    assert matrix[each([True, False, True])].list == [[1, 2, 3], [7, 8, 9]]


def test_getitem_boolean_each_error(matrix):
    with pytest.raises(ValueError, match="must have the same length"):
        matrix[each([True, False])]


def test_setitem_standard(matrix):
    matrix[0] = -1
    assert matrix.list[0] == [-1, 2, 3]
    assert matrix.list[1] == [-1, 5, 6]
    assert matrix.list[2] == [-1, 8, 9]


def test_setitem_each_on_key(matrix):
    matrix[each([0, 1, 2])] = -1
    assert matrix.list[0] == [-1, 2, 3]
    assert matrix.list[1] == [4, -1, 6]
    assert matrix.list[2] == [7, 8, -1]


def test_setitem_each_on_value(matrix):
    matrix[0] = each([-1, -2, -3])
    assert matrix.list[0] == [-1, 2, 3]
    assert matrix.list[1] == [-2, 5, 6]
    assert matrix.list[2] == [-3, 8, 9]


def test_setitem_each_on_key_and_value(matrix):
    matrix[each([0, 1, 2])] = each([-1, -2, -3])
    assert matrix.list[0] == [-1, 2, 3]
    assert matrix.list[1] == [4, -2, 6]
    assert matrix.list[2] == [7, 8, -3]


def test_setitem_boolean_each_on_key_ok(matrix):
    matrix[each([True, False, True])] = -1
    assert matrix.list[0] == -1
    assert matrix.list[1] == [4, 5, 6]
    assert matrix.list[2] == -1


def test_setitem_boolean_each_on_key_and_value(matrix):
    matrix[each([True, False, True])] = each([-1, -2])
    assert matrix.list[0] == -1
    assert matrix.list[1] == [4, 5, 6]
    assert matrix.list[2] == -2


def test_setitem_boolean_each_on_key_and_value_error(matrix):
    with pytest.raises(ValueError, match="must match the number of True items"):
        matrix[each([True, False, True])] = each([-1, -2, -3])


def test_delitem_standard(matrix):
    del matrix[0]
    assert matrix.list == [[2, 3], [5, 6], [8, 9]]


def test_delitem_each_on_key(matrix):
    del matrix[each([0, 1, 2])]
    assert matrix.list == [[2, 3], [4, 6], [7, 8]]


def test_delitem_boolean_each_on_key(matrix):
    del matrix[each([False, True, False])]
    assert matrix.list == [[1, 2, 3], [7, 8, 9]]
