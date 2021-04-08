import pytest
from Task1 import instances_counter


@instances_counter
class A:
    def get_one(self) -> int:
        return 1


@instances_counter
class B:
    pass


def test_metod_of_decorated_class():
    a = A()
    assert a.get_one() == 1
    a.reset_instances_counter()


def test_get_created_instances():
    assert B.get_created_instances() == 0
    b, _, _ = B(), B(), B()
    assert b.get_created_instances() == 3
    b.reset_instances_counter()


def test_reset_instances_counter():
    b = B()
    assert b.reset_instances_counter() == 1
    b.reset_instances_counter()


def test_instance_counter_for_two_class():
    a, _, _ = A(), A(), A()
    b = B()
    assert a.get_created_instances() == 3
    assert b.get_created_instances() == 1
    a.reset_instances_counter()
    b.reset_instances_counter()
