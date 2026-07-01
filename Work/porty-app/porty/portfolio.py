from . import stock
from . import fileparse


class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError()
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, filename, **opts):
        self = cls()
        with open(filename, "rt") as f:
            portfolio_list = fileparse.parse_csv(
                f=f, types=[str, int, float], select=["name", "shares", "price"], **opts
            )

        for stock_dict in portfolio_list:
            self.append(stock.Stock(**stock_dict))

        return self

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    @property
    def total_cost(self):
        return sum(s.cost for s in self._holdings)

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
