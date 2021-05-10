from Task2 import ElderDiscount, MorningDiscount, Order


def test_order_1():
    order = Order(100, MorningDiscount)
    assert order.final_price() == 50


def test_change_discount():
    order = Order(100, MorningDiscount)

    order.discount = ElderDiscount
    assert order.final_price() == 10


def test_order_price():
    order = Order(100, MorningDiscount)
    assert order.final_price(50) == 25
