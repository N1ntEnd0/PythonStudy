"""
We have a file that works as key-value storage, each line is represented as key and value separated by = symbol,
example name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string,
it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and values accessible as collection items
and as attributes. Example: storage['name'] # will be string 'kek' storage.song_name # will be 'shadilay' storage.power
# will be integer 9001

In case of attribute clash existing built-in attributes take precedence. In case when value cannot be assigned to an
attribute (for example when there's a line 1=something) ValueError should be raised. File size is expected to be small,
you are permitted to read it entirely into memory.
"""


class KeyValueStorage:
    _dct = {}

    def __init__(self, path):
        with open(path) as f:
            for line in f:
                name, value = line.strip("\n").split("=")
                try:
                    self._dct[name] = int(value) if value.isdigit() else value
                except Exception as e:
                    raise ValueError from e

    def __getattr__(self, item):
        return self._dct.get(item)

    def __getitem__(self, item):
        return self._dct.get(item)

    def __len__(self):
        return len(self._dct)

    def __iter__(self):
        yield from self._dct.items()

    def __contains__(self, item):
        return item in self._dct
