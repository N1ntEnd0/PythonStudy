import pytest
from Task2.Task2.Task02 import check_fibonacci


def test_function():
    assert check_fibonacci([0, 1, 1])


def test_function2():
    assert not check_fibonacci([0, 1])


def test_function3():
    assert not check_fibonacci([0, 1, 2])
