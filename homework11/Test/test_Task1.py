import pytest
from Task1 import SimplifiedEnum


def test_get_attribute():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"


def test_set_attribute():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S")

    SizesEnum.XS = "XS"
    assert SizesEnum.XS == "XS"


def test_len():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("BLUE",)

    assert len(ColorsEnum) == 1
