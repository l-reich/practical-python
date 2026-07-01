# pcost.py
#
# Exercise 1.27

import report


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio_obj = report.read_portfolio(filename=filename)
    return portfolio_obj.totalcost


def main(args):
    print(portfolio_cost(args[1]))


if __name__ == "__main__":
    import sys

    main(sys.argv)
