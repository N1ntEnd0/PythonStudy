import pytest
from Task2 import custom_sum


@pytest.fixture
def fixture():
    custom_sum([1, 2, 3], [4, 5])


def test_doc(fixture):
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_name():
    assert custom_sum.__name__ == "custom_sum"


def test_original_func():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
