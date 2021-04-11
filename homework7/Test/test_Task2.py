import Task2
from Task2 import backspace_compare


def test():
    assert backspace_compare("ab#c", "ad#c")
    assert backspace_compare("a##c", "#a#c")


def test_with_different_words():
    assert backspace_compare("a#c", "b") is False


def test_str_starts_with_bs():
    assert backspace_compare("##b", "#b")
