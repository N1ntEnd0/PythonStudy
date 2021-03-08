import pytest
from Task03 import find_maximum_and_minimum


def write_file(data):
    with open("test_data/test_file", 'w') as fi:
        for i in data:
            fi.write(str(i) + '\n')


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1, 2, 3, 4, 5], (1, 5)),
        ([0, 100, -20, 8, 0, 11, 32], (-20, 100)),
        ([-6, -12, -5, -3], (-12, -3)),
        ([0], (0, 0)),
    ],
)
def test_function(value, expected_result):
    write_file(value)
    assert find_maximum_and_minimum("test_data/test_file") == expected_result


