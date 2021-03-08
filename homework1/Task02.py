"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    length = len(data)
    if length == 0:
        return True
    elif length == 1:
        if data[0] == 0 or data[0] == 1:
            return True
        return False
    elif length == 2:
        if data[1] == 1 and data[0] == 0 or data[0] == 1:
            return True
        return False
    else:
        for i in range(length - 2):
            if data[i + 2] != data[i] + data[i + 1]:
                return False
        return True

