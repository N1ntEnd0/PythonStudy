"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from contextlib import ExitStack
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    with ExitStack() as stack:
        files = (stack.enter_context(open(file)) for file in file_list)
        numbers = ([num.strip("\n") for num in line] for line in files)
        yield from merge(*numbers)
