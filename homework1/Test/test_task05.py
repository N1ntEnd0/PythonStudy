import pytest
from Task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["data", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 7, -5, 4, 3, -8, 2, 3, 4, 9, -2, -4, 9, 8], 5, 20),
        ([-1, -2, -3], 3, -1),
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-5, 10, 2, -3, 100], 3, 100),
        ([-5, 10, 2, -3, 100], 0, 0)
    ],
)
def test_function(data, k, expected_result):
    assert find_maximal_subarray_sum(data, k) == expected_result

