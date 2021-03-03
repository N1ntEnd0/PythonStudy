import pytest
from Task4.Task4.Task04 import check_sum_of_four


def test_function():
    a = [2, 1, 0]
    b = [-1, -2, 3]
    c = [-4, 0, -3]
    d = [3, 0, -1]
    assert check_sum_of_four(a, b, c, d) == 10


def test_function2():
    a = [1, 4, 7, 3, 2]
    b = [-1, 9, 5, 4, 8]
    c = [-4, -5, -6, -7, -8]
    d = [-3, -2, -1, -1, 0]
    assert check_sum_of_four(a, b, c, d) == 50
