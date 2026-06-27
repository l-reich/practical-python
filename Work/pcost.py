# pcost.py
#
# Exercise 1.27

import report


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio_list = report.read_portfolio(filename=filename)
    return sum(d["shares"] * d["price"] for d in portfolio_list)


def main(args):
    print(portfolio_cost(args[1]))


if __name__ == "__main__":
    import sys

    main(sys.argv)
