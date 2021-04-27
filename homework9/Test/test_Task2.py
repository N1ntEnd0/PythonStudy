import pytest
from Task2 import Supressor, supressor


def test_class_with_raise_exc():
    with pytest.raises(ZeroDivisionError):
        with Supressor(IndexError):
            1 / 0
            [][2]


def test_class_without_raise_exc():
    with Supressor(IndexError):
        [][2]


def test_func_with_raise_exc():
    with pytest.raises(ZeroDivisionError):
        with supressor(IndexError):
            1 / 0
            [][2]


def test_func_without_raise_exc():
    with supressor(IndexError):
        [][2]


def test_work_contextmanager():
    with supressor(IndexError):
        a = 0
        a += 1
    assert a == 1
