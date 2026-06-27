# report.py
#
# Exercise 2.4

import fileparse


def read_portfolio(filename):
    with open(filename, 'rt') as f:
        portfolio_list = fileparse.parse_csv(
            f=f, types=[str, int, float], select=["name", "shares", "price"]
        )
    return portfolio_list


def read_prices(filename):
    with open(filename, 'rt') as f:
        price_list = fileparse.parse_csv(f=f, has_headers=False)
    price_dict = {}

    for entry_tuple in price_list:
        price_dict[entry_tuple[0]] = float(entry_tuple[1])

    return price_dict


def make_report(portfolio_file, prices_file):
    portfolio_list = read_portfolio(filename=portfolio_file)
    price_dict = read_prices(filename=prices_file)

    result_list = []
    for stock_entry in portfolio_list:
        stock_name, nshares, buy_price = (
            stock_entry["name"],
            stock_entry["shares"],
            stock_entry["price"],
        )
        price_increase = round(-(buy_price - price_dict[stock_name]), 2)
        result_list.append(
            {
                "name": stock_name,
                "shares": nshares,
                "price": round(price_dict[stock_name], 2),
                "change": price_increase,
            }
        )

    return result_list


def print_report(report_list):
    print(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    dash_bar_string = "-" * 10
    print(dash_bar_string, dash_bar_string, dash_bar_string, dash_bar_string)
    for stock_dict in report_list:
        name, shares, price, change = (
            stock_dict["name"],
            stock_dict["shares"],
            stock_dict["price"],
            stock_dict["change"],
        )
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    print_report(
        make_report(portfolio_file=portfolio_filename, prices_file=prices_filename)
    )


def main(args):
    if len(args) < 3:
        portfolio_report(
            portfolio_filename="Data/portfoliodate.csv",
            prices_filename="Data/prices.csv",
        )
    else:
        portfolio_report(portfolio_filename=args[1], prices_filename=args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
