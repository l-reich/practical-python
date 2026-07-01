# report.py
#
# Exercise 2.4

from . import fileparse
from . import stock
from . import tableformat
from . import portfolio
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    with open(filename, "rt") as f:
        return Portfolio.from_csv(filename, **opts)


def read_prices(filename):
    with open(filename, "rt") as f:
        price_list = fileparse.parse_csv(f=f, has_headers=False)
    price_dict = {}

    for entry_tuple in price_list:
        price_dict[entry_tuple[0]] = float(entry_tuple[1])

    return price_dict


def make_report_data(portfolio, prices):
    result_list = []
    for stock_object in portfolio:
        stock_name, nshares, buy_price = (
            stock_object.name,
            stock_object.shares,
            stock_object.price,
        )
        price_increase = round(-(buy_price - prices[stock_name]), 2)
        result_list.append(
            (
                stock_name,
                nshares,
                round(prices[stock_name], 2),
                price_increase,
            )
        )

    return result_list


def print_report(reportdata, formatter: tableformat.TableFormatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) < 3:
        portfolio_report(
            portfoliofile="Data/portfoliodate.csv",
            pricefile="Data/prices.csv",
        )
    elif len(args) == 4:
        portfolio_report(portfoliofile=args[1], pricefile=args[2], fmt=args[3])
    else:
        portfolio_report(portfoliofile=args[1], pricefile=args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
