import pytest

from Task1 import instances_counter


@instances_counter
class A:
    """some documentation"""

    def get_one(self) -> int:
        return 1


@instances_counter
class B:
    pass


@pytest.fixture
def create_class():
    a = A()
    yield a
    a.reset_instances_counter()


@pytest.fixture
def create_two_classes():
    a, _, _ = A(), A(), A()
    b = B()
    yield a, b
    a.reset_instances_counter()
    b.reset_instances_counter()


def test():
    a = A()
    assert a.__name__ == "A"
    assert a.__doc__ == "some documentation"


def test_metod_of_decorated_class(create_class):
    assert create_class.get_one() == 1


def test_reset_instances_counter(create_class):
    assert create_class.reset_instances_counter() == 1


def test_instance_counter_for_two_class(create_two_classes):
    a, b = create_two_classes
    assert a.get_created_instances() == 3
    assert b.get_created_instances() == 1
