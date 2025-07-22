# 2025/07/18
"""
test_each_99_mix.py - Mix of operations.
"""


from datetime import datetime

import pytest

from pyrite.each import each


class Address:
    def __init__(self, title: str, number: int):
        self.title = title
        self.number = number


class Person:
    def __init__(self, name: str, age: int, birthday: datetime, address: Address):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.address = address

    def __call__(self, target: str = "John") -> str:
        """Example of a callable method."""
        return f"{self.name} says hello to {target}!"


@pytest.fixture
def people():
    return each(
        [
            Person("Alice", 30, datetime(1993, 5, 17), Address("Main St", 123)),
            Person("Bob", 25, datetime(1998, 8, 22), Address("Second St", 456)),
            Person("Charlie", 35, datetime(1988, 12, 1), Address("Third St", 789)),
        ]
    )


def test_nested_mutation_by_method(people):
    people.birthday = people.birthday.replace(year=2000)
    assert people.birthday.year.list == [2000, 2000, 2000]


def test_nested_mutation_by_operation(people):
    people.address.number += 100
    assert people.address.number.list == [223, 556, 889]


def test_nested_bool_evaluation(people):
    subset = (people.age >= 30) & (people.address.title.startswith("T"))
    assert subset.list == [False, False, True]


def test_getitem_conditional(people):
    result = people[people.age >= 30]
    assert result.name.list == ["Alice", "Charlie"]


def test_setitem_conditional(people):
    people[people.age >= 30].name = "Senior"
    assert people.name.list == ["Senior", "Bob", "Senior"]
