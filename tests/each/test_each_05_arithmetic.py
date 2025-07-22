# 2025/06/10
"""
test_each_05_arithmetic.py - Arithmetic and logical operations
"""

import pytest

from pyrite.each import each


@pytest.fixture
def base():
    return each([1, 2, 3])


def test_add(base):
    assert (base + 1).list == [2, 3, 4]


def test_radd(base):
    assert (1 + base).list == [2, 3, 4]


def test_iadd(base):
    base += 1
    assert base.list == [2, 3, 4]


def test_add_each(base):
    assert (base + each([1, 2, 3])).list == [2, 4, 6]


def test_sub(base):
    assert (base - 1).list == [0, 1, 2]


def test_rsub(base):
    assert (10 - base).list == [9, 8, 7]


def test_isub(base):
    base -= 1
    assert base.list == [0, 1, 2]


def test_mul(base):
    assert (base * 2).list == [2, 4, 6]


def test_rmul(base):
    assert (2 * base).list == [2, 4, 6]


def test_imul(base):
    base *= 2
    assert base.list == [2, 4, 6]


def test_truediv(base):
    assert (base / 2).list == [0.5, 1.0, 1.5]


def test_rtruediv(base):
    assert (6 / base).list == [6.0, 3.0, 2.0]


def test_itruediv(base):
    base /= 2
    assert base.list == [0.5, 1.0, 1.5]


def test_floordiv(base):
    assert (base // 2).list == [0, 1, 1]


def test_rfloordiv(base):
    assert (7 // base).list == [7, 3, 2]


def test_ifloordiv(base):
    base //= 2
    assert base.list == [0, 1, 1]


def test_mod(base):
    assert (base % 2).list == [1, 0, 1]


def test_rmod(base):
    assert (5 % base).list == [0, 1, 2]


def test_imod(base):
    base %= 2
    assert base.list == [1, 0, 1]


def test_divmod(base):
    assert divmod(base, 2).list == [(0, 1), (1, 0), (1, 1)]


def test_pow(base):
    assert (base**2).list == [1, 4, 9]


def test_pow_modulo(base):
    assert pow(base, 2, 10).list == [1, 4, 9]


def test_rpow(base):
    assert (2**base).list == [2, 4, 8]


def test_ipow(base):
    base **= 2
    assert base.list == [1, 4, 9]


def test_lshift(base):
    assert (base << 1).list == [2, 4, 6]


def test_rlshift(base):
    assert (2 << base).list == [4, 8, 16]


def test_ilshift(base):
    base <<= 1
    assert base.list == [2, 4, 6]


def test_rshift(base):
    assert (8 >> base).list == [4, 2, 1]


def test_rrshift(base):
    assert (base >> 1).list == [0, 1, 1]


def test_irshift(base):
    base >>= 1
    assert base.list == [0, 1, 1]


def test_bitwise_and():
    x = each([0b1100, 0b1010])
    assert (x & 0b1111).list == [0b1100, 0b1010]


def test_bitwise_or():
    x = each([0b1100, 0b1010])
    assert (x | 0b0001).list == [0b1101, 0b1011]


def test_bitwise_xor():
    x = each([0b1100, 0b1010])
    assert (x ^ 0b1111).list == [0b0011, 0b0101]


def test_bitwise_each():
    x = each([True, False, True])
    y = each([False, True, True])
    assert (x & y).list == [False, False, True]
    assert (x | y).list == [True, True, True]
    assert (x ^ y).list == [True, True, False]


def test_neg(base):
    assert (-base).list == [-1, -2, -3]


def test_pos(base):
    assert (+base).list == [1, 2, 3]
