"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence

# from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) >= 3:
        for i in range(len(data) - 2):
            if data[i + 2] != data[i] + data[i + 1]:
                return False
        return True
    return False


print(check_fibonacci([0, 1, 1]))
