class Stock:
    __slots__ = ("name", "_shares", "price")

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = float(price)

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._shares = value

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, amount: int) -> None:
        self.shares -= amount

    def __repr__(self) -> str:
        return f'Stock("{self.name}", {self.shares}, {self.price})'
