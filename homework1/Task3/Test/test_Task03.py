import pytest
from Task3.Task3.Task03 import find_maximum_and_minimum


def test_function():
    assert find_maximum_and_minimum("test") == (1, 5)
