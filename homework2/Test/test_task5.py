import string

from Task05 import custom_range


def test_without_letter_argument():
    assert custom_range(string.ascii_lowercase) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]


def test_with_one_letter_argument():
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_with_two_letter_arguments():
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_with_three_letters_arguments():
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_without_number_argument():
    assert custom_range([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_with_one_number_argument():
    assert custom_range([1, 2, 3, 4], 3) == [1, 2]


def test_with_two_numbers_arguments():
    assert custom_range([1, 2, 3, 4, 5], 2, 4) == [2, 3]


def test_with_three_numbers_arguments():
    assert custom_range([1, 2, 3, 4, 5], 5, 2, -2) == [5, 3]
