from Task03 import combinations


def test_zero_list():
    assert combinations([]) == []


def test_different_size():
    assert combinations([1], [1, 2]) == [[1, 1], [1, 2]]


def test_example_value():
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]


def test_size_more_than_2():
    assert combinations([1, 2, 3], [4, 5, 6]) == [
        [1, 4],
        [1, 5],
        [1, 6],
        [2, 4],
        [2, 5],
        [2, 6],
        [3, 4],
        [3, 5],
        [3, 6],
    ]


def test_three_lists():
    assert combinations([1, 2], [3, 4], [5, 6]) == [
        [1, 3, 5],
        [1, 3, 6],
        [1, 4, 5],
        [1, 4, 6],
        [2, 3, 5],
        [2, 3, 6],
        [2, 4, 5],
        [2, 4, 6],
    ]
