# 2025/07/02
"""
test_each_03_attrs.py - Attributes access and manipulation, also, behavior
as a function (`__call__()`).
"""

from datetime import datetime

import pytest

from pyrite.each import EachError, each


class Person:
    def __init__(self, name: str, age: int, birthday: datetime):
        self.name = name
        self.age = age
        self.birthday = birthday

    def __call__(self, target: str = "John") -> str:
        """Example of a callable method."""
        return f"{self.name} says hello to {target}!"


@pytest.fixture
def people():
    return each(
        [
            Person("Alice", 30, datetime(1993, 5, 17)),
            Person("Bob", 25, datetime(1998, 8, 22)),
            Person("Charlie", 35, datetime(1988, 12, 1)),
        ]
    )


# getattr


def test_getattr_ok(people):
    assert people.name.list == ["Alice", "Bob", "Charlie"]
    assert people.age.list == [30, 25, 35]


@pytest.mark.xfail(reason="`default` argument is not propagated in `getattr`")
def test_getattr_function(people):
    assert getattr(people, "name").list == ["Alice", "Bob", "Charlie"]
    assert getattr(people, "invalid", "default").list == [
        "default",
        "default",
        "default",
    ]


def test_getattr_deep(people):
    assert people.birthday.year.list == [1993, 1998, 1988]


def test_getattr_invalid(people):
    with pytest.raises(EachError):
        _ = people.invalid_attribute


@pytest.mark.skip(reason="`getattr` only allows string")
def test_getattr_each(people):
    keys = each(["name", "age", "birthday"])
    assert getattr(people, keys).list == ["Alice", 25, datetime(1988, 12, 1)]


# setattr


def test_setattr_ok(people):
    people.age = 100
    assert people.age.list == [100, 100, 100]


def test_setattr_create_attr(people):
    people.country = "Wonderland"
    assert people.country.list == ["Wonderland", "Wonderland", "Wonderland"]


def test_setattr_each(people):
    new_ages = each([40, 50, 60])
    people.age = new_ages
    assert people.age.list == [40, 50, 60]


def test_setattr_each_invalid_length(people):
    new_ages = each([40, 50])  # Shorter than original
    with pytest.raises(ValueError):
        people.age = new_ages  # Should raise ValueError due to length mismatch


# delattr


def test_delattr_ok(people):
    del people.age
    assert not hasattr(people.list[0], "age")
    assert not hasattr(people.list[1], "age")
    assert not hasattr(people.list[2], "age")


def test_delattr_invalid(people):
    with pytest.raises(EachError):
        del people.invalid_attr  # Should raise EachError


@pytest.mark.skip(reason="`delattr` only allows string")
def test_delattr_each(people):
    keys = each(["name", "age", "birthday"])
    delattr(people, keys)
    assert not hasattr(people.list[0], "name")
    assert not hasattr(people.list[1], "age")
    assert not hasattr(people.list[2], "birthday")


# dir


def test_dir(people):
    attrs = dir(people)
    assert "name" in attrs
    assert "age" in attrs
    assert "birthday" in attrs
    assert "country" not in attrs  # Not set yet
    assert "invalid_attr" not in attrs  # Should not exist


# call


def test_call_with_args(people):
    assert people("Lewis").list == [
        "Alice says hello to Lewis!",
        "Bob says hello to Lewis!",
        "Charlie says hello to Lewis!",
    ]


def test_call_without_args(people):
    assert people().list == [
        "Alice says hello to John!",
        "Bob says hello to John!",
        "Charlie says hello to John!",
    ]


def test_call_with_kwargs(people):
    assert people(target="Alice").list == [
        "Alice says hello to Alice!",
        "Bob says hello to Alice!",
        "Charlie says hello to Alice!",
    ]


def test_call_with_each(people):
    targets = each(["Alice", "Bob", "Charlie"])
    assert people(targets).list == [
        "Alice says hello to Alice!",
        "Bob says hello to Bob!",
        "Charlie says hello to Charlie!",
    ]


def test_call_invalid_args(people):
    with pytest.raises(EachError):
        people("Invalid", "Args")
