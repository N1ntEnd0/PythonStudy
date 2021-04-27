"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from collections import deque


def count_letters(word):
    que = deque()
    for i in word:
        if i == "#" and len(que) != 0:
            que.pop()
        if i != "#":
            que.append(i)
    return que


def backspace_compare(first: str, second: str):
    return count_letters(first) == count_letters(second)
