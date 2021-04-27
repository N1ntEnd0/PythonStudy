import pytest
from Task2 import custom_sum


def test_stdout_of_print_result(capsys):
    custom_sum([1, 2, 3], [4, 5])
    captured = capsys.readouterr()
    assert captured.out == "[1, 2, 3] [4, 5]\n[1, 2, 3, 4, 5]\n"


def test_doc():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_name():
    assert custom_sum.__name__ == "custom_sum"


def test_original_func():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
