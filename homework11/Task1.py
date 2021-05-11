"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(cls, name, bases, dct):
        attrs = dct.get(f"_{name}__keys")
        if attrs:
            dct["attrs"] = {key: key for key in attrs}
            print(dct)
        else:
            dct["attrs"] = {}
        return super().__new__(cls, name, bases, dct)

    def __getattribute__(self, item):
        try:
            return type.__getattribute__(self, item)
        except AttributeError as err:
            return self.attrs.get(item)

    def __setattr__(self, key, value):
        self.attrs[key] = value

    def __len__(self):
        return len(self.attrs)
