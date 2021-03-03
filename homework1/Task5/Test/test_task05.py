import pytest
from Task5.Task5.Task05 import find_maximal_subarray_sum


def test_function():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_function2():
    assert (
        find_maximal_subarray_sum([1, 7, -5, 4, 3, -8, 2, 3, 4, 9, -2, -4, 9, 8], 5)
        == 20
    )
