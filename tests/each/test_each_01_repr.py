# 2025/06/10
"""
test_each_01_repr.py - Initialization and representation
"""

import pytest

from pyrite.each import each, EachError


def test_init_with_list():
    x = each([1, 2, 3])
    assert x.list == [1, 2, 3]


def test_init_with_iterable():
    x = each(range(3))
    assert x.list == [0, 1, 2]


def test_repr():
    x = each([1, 2])
    assert repr(x) == "each([1, 2])"


def test_str():
    x = each(["a", "b"])
    assert str(x) == "[a, b]"


def test_bytes():
    x = each([b"a", b"b"])
    assert bytes(x) == b"ab"


def test_bytes_error():
    x = each([1j, 2j])
    with pytest.raises(EachError):
        bytes(x)


def test_format():
    x = each([1.2345, 2.3456])
    assert f"{x:.1f}" == "[1.2, 2.3]"


def test_format_error():
    x = each([1, "two"])
    with pytest.raises(EachError):
        f"{x:.1f}"
