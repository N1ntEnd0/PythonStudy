"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from contextlib import ExitStack
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:

    count = 0
    all_files = os.listdir(dir_path)
    files = filter(lambda x: x.endswith(file_extension), all_files)

    with ExitStack() as stack:
        for file in files:
            for line in stack.enter_context(open(file)):
                if tokenizer is None:
                    count += 1
                else:
                    count += len(tokenizer(line))
        return count
