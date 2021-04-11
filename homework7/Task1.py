"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {"simple_key": ["simple", "list", "of", "RED", "valued"],},
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_in_dict(tree, element):
    for k, v in tree.items():
        if isinstance(k, tuple):
            for i in k:
                if i == element:
                    yield i
        else:
            if k == element:
                yield k

        if isinstance(v, dict):
            for j in find_in_dict(v, element):
                yield j
        if isinstance(v, (list, tuple, set)):
            for g in v:
                if isinstance(g, dict):
                    for h in find_in_dict(g, element):
                        yield h

                if g == element:
                    yield g
        else:
            if v == element:
                yield v


def find_occurrences(tree: dict, element: Any) -> int:
    result = list(find_in_dict(tree, element))
    return len(result)


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
