from typedproperty import String, Integer, Float


class Stock:
    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, amount: int) -> None:
        self.shares -= amount

    def __repr__(self) -> str:
        return f'Stock("{self.name}", {self.shares}, {self.price})'
