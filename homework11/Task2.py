"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""


class Order:
    def __init__(self, price, discount):
        self.price = price
        self._discount = discount._discount

    def final_price(self, price=None):
        if price is None:
            price = self.price
        return price - price * self._discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount._discount


class Discount:

    _discount = 0.0

    def __init_subclass__(cls):
        if not hasattr(cls, "_discount"):
            raise NotImplementedError(
                f"Class {cls} lacks required _discount class attribute"
            )


class MorningDiscount(Discount):
    _discount = 0.5


class ElderDiscount(Discount):
    _discount = 0.9
